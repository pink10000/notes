---
tags:
  - CSE_223B
---
Largely ripped from [paper](https://cseweb.ucsd.edu/classes/sp11/cse223b/papers/bft.pdf).

# Definition (Byzantine Faults)
A **Byzantine fault** is the most severe and general type of failure in a distributed system, where a node or component can behave arbitrarily. Unlike a "fail-stop" fault (where a node simply crashes and stops responding), a Byzantine node can exhibit unpredictable and malicious behavior. For example, it might:
- Send incorrect or conflicting data to different nodes in the system.
- Fail to send messages or selectively drop messages.
- Corrupt local state or respond with garbage data.

This type of fault gets its name from the "Byzantine Generals Problem," a logical dilemma where generals must coordinate an attack but some of them might be traitors trying to sabotage the plan by sending conflicting information.

This system has some assumptions:
1. nodes are connected by a network 
2. a network may fail to deliver messages, delay them, duplicate them, or deliver them out of order.
3. independent node failures
4. each node runs different implentations of the service code and OS
	1. each node should have a different root password and a different admin
5. cryptographic techniques to prevent spoofing and replays to detect corrupted messages
6. A strong adversary
    - can coordinate nodes
    - delay communication (but not indefinitely)
    - the nodes are computationally bound (unable to subvert cryptographic techniques above)

# Definition (Safety)
The algorithm provides **safety** if the replicated service satisfies linearizability: it behaves like a centralized implentation that executes operations atomically one at a time. Safety requires the bound on the number of faulty replicas because a faulty replica can behave arbitrarily (can destroy its state).

Safety is also provided regardless of how many faulty clients are using the service (even with collusion). Faulty clients cannot break invariants on the service state if the service operations are designed to preserve invariants.

Safety is not sufficient for guarding against faulty clients (imagine a faulty client that writes garbage data to a NFS). Access control limits the damage that a faulty client can do. 

# Definition (Liveness)
The algorithm provides **liveness** if it guarantees that clients eventually receive replies to their requests, provided that at most $f$ replicas are faulty. 

## Byzantine Liveness
Because of the FLP impossibility result, PBFT cannot guarantee liveness in a purely asynchronous system. Instead, it relies on a "partial synchrony" assumption: it ensures liveness assuming that message delays do not grow faster than time indefinitely (i.e., the network eventually delivers messages within some finite, but perhaps unknown, bound).

PBFT guarantees liveness as long as at most 
$$
\left\lfloor \frac{n-1}{3} \right\rfloor
$$
replicas are faulty and $\texttt{delay}(t)$ does not grow faster than $t$ indefinitely. Here, $\texttt{delay}(t)$ is the time between the moment $t$ when a message is sent for the first time and the moment when it is received by its destination (assuming the sender keeps retransmitting the message until it is received).

## Lemma (Minimum Number of Replicas)
To tolerate $f$ Byzantine faults, a distributed system must have at least $3f + 1$ replicas.

Suppose we have $n$ replicas. Since we tolerate up to $f$ faults, at most the remaining $n - f$ replicas must be able to advance.  

The worst case scenario for $n - f$ responses is that the $f$ nodes that failed to respond were actually honest nodes that were simply delayed by some network latency. That means that the pool of $N - f$ responses we did collect might include all $f$ of the malicious, lying nodes. Thus, $(N - f) - f$ must be from honest nodes. Therefore
$$
(n - f) - f > f
$$
since the honest nodes must outnumber the malicious nodes. So,
$$
\begin{aligned}
(n - f) - f &> f \\
n &> 3f \\
n &\geq 3f + 1
\end{aligned}
$$
requiring $3f + 1$ nodes. 

## Privacy
The algorithm does not address fault-tolerant privacy. A faulty replica can leak private information to the adversary. 

# PBFT (Practical Byzantine Fault Tolerance)
The algorithm is a form of **replicated state machine** (RSM).  The set of replicas is $\mathcal{R}$ and each replica is denoted by an integer from $0, \dots, |\mathcal{R}| - 1$. Assume $|\mathcal{R}| = 3f + 1$ where $f$ is the maximum number of faulty replicas. 

Replicas move through a succession of configurations called **views**. In a view, one replica is the **primary** and the others are **backups**. Views are numbered consecutively. The primary of a view is the replica $p$ such that $p = v \bmod |\mathcal{R}|$ where $v$ is the view number. 

The algorithm works roughly as follows:
1. A client sends a request to invoke a service operation to the primary.
2. The primary multicasts the request to the backups.
3. The replicas execute the request and send a reply to the client.
4. The client waits for $f + 1$ replies from different replicas with the same result. This is the result of the operation.

Like all RSMs, replicas must be *deterministic* and they must execute from *the same state*. Given these two properties, the algorithm ensures the [[#Definition (Safety)|safety property]] by guaranteeing all non-faulty replicas agree on a total order for the execution of requests despite failures.

## Client Operations
The client sends 
$$
\langle \texttt{REQUEST}, o, t, c \rangle_{\sigma_c}
$$
where 
- $o$ is the operation to be executed
- $t$ is a timestamp
  - used for "exactly-once" semantics (prevent replay)
- $c$ is the client ID
- $\sigma_c$ is the client's signature on the message

Each message sent by the replicas to the client includes the current view number $v$, allowing the client to track the view (and hence the current primary).

A client sends a request to "what it believes is the primary", which atomically multicasts the requests to all the backups. The replica will send a reply to the client of the form 
$$
\langle \texttt{REPLY}, v, t, c, i, r \rangle_{\sigma_i}
$$
where
- $v$ is the view number
- $t$ is the timestamp from the client's request
- $c$ is the client ID
- $i$ is the replica ID
- $r$ is the result of executing the operation

The client waits for $f + 1$ replies from different replicas with the same timestamp $t$ and the same result $r$ before accepting $r$ as the result of the operation (recall at most $f$ replicas can be faulty).

**Error Case**: What if the client does not receive the replies soon enough? It will broadcast the request to all replicas. 
- If it has already been processed, the replica will simply resend the reply. 
- Otherwise, if the replica is not the primary, it relays the request to the primary. If the primary does not multicast the request to the group, it will be suspected as faulty, and a view change will occur. 

The state of each replica includes
- state of service
- message log containing messages the replica has accepted
- integer denoting replica's current view

When the primary $p$, receives a client request, $m$, it starts a three-phase protocol to atomically multicast the request to the replicas. It starts this protocol immediately unless the number of messages for which the protocol is in progress exceeds some threshold (to prevent the primary from being overwhelmed by requests).

The three phases are
- **pre-prepare**: the primary multicasts a pre-prepare message to the backups
- **prepare**: the replicas multicast a prepare message to each other
- **commit**: the replicas multicast a commit message to each other

## Pre-Prepare Phase
The pre-prepare and prepare phase are almost exactly like [[Paxos Algorithm]] and how they choose a value. The difference is that **pre-prepare**
$$
\langle \langle \texttt{PRE-PREPARE}, v, n, d \rangle_{\sigma_p}, m \rangle
$$
where
- $v$ is the view number
- $n$ is a sequence number (used to order requests)
- $d$ is the digest of the client request (cryptographic hash of the request, aimed to reduce the size of messages sent between replicas)
- $m$ is the message. 

Since the primary itself can be malicious, the replica cannot blindly trust this message. It must independently verify:
- $v$ is the correct view number
- $h < n < H$ where $h, H$ are the low and high watermarks for sequence numbers ^7fbed1
  - a malicious primary could try to exhaust the sequence numbers by using very large $n$ values, preventing the replicas from accepting any more requests. 
  - it can also reuse old sequence numbers, causing the replicas to accept old requests as new ones.
- $d$ is the digest of the client request, using Message Authentication Codes (MACs)
	- Symmetric cryptography: Sender and receiver share some secret to sign their messages.
	- faster than signing with cryptographic key (like [[RSA]])
	- verifies $d$ 

## Prepare Phase
If backup $i$ accepts $\langle \langle \texttt{PRE-PREPARE}, v, n, d \rangle_{\sigma_p}, m \rangle$, it enters the **prepare** phase by multicasting a 
$$
\langle \texttt{PREPARE}, v, n, d, i \rangle_{\sigma_i} 
$$
message to all other replicas and adds both messages to its log, where
- $v$ is the view number
- $n$ is the sequence number
- $d$ is the digest of the client request
- $i$ is the replica ID

A replica (including the primary) accepts `prepare` messages and adds them to its log provided 
- the signatures are correct (was not forged)
- view numbers equal the replica's current view
- sequence number is between $h, H$. The time should be somewhat recent.

Let the predicate $\texttt{prepared}(m, v, n, i)$ resolve to a Boolean value. It is true iff replica $i$ has inserted in its log
- the request $m$
- a `pre-prepare` message for $m$ with view number $v$ and sequence number $n$
- $2f$ `prepare` messages from different backups that the `pre-prepare` message.

The $2f$ is very important. From [[#Lemma (Minimum Number of Replicas)]], we ensure that we have $2f + 1$ (including itself) [[Quorum]] that ensures that if one non-faulty replica achieves a true $\texttt{prepared}(m, v, n, i)$, it is impossible for any other non-faulty replica to achieve a true 
$\texttt{prepared}(m', v, n, j)$ for $m' \neq m$ (i.e., the replicas cannot be split on different values for the same sequence number) for a different request. 

Both phases guarantee that non-faulty replicas agree on a total order for the requests within a view.

## Commit Phase
Then, replica $i$ enters the **commit** phase by multicasting a
$$
\langle \texttt{COMMIT}, v, n, D(m), i \rangle_{\sigma_i}
$$
message to all other replicas when $\texttt{prepared}(m, v, n, i)$ is true. Replicas accept `commit` messages and add them to their logs provided they are properly signed, the view numbers match, and the sequence number is between $h, H$.

We define two more predicates:
- $\texttt{committed}(m, v, n)$. This is true iff $\texttt{prepared}(m, v, n, i)$ is true for all $i$ in some set of $f + 1$ non-faulty replicas.
	- think of this as a "global truth"
	- Although this may be true, since the network is asynchronous, an individual node cannot know about it unless it has proof. ^f86b44
- $\texttt{committed-local}(m, v, n, i)$. This is true iff $\texttt{prepared}(m, v, n, i)$ is true and replica $i$ has accepted $2f + 1$ commits (possibly including its own) from different replicas that match the pre-prepare for $m$.
	- think of this as a "local truth"
	- This is the "local [[#^f86b44|proof]]". 
	- When this local predicate is true, the replica is finally authorized to execute the requested operation.

In particular, 
$$
\texttt{committed-local}(m, v, n, i) \text{ for some non-faulty } i \implies \texttt{committed}(m, v, n) \text{ is true.}
$$
This ensures non-faulty replicas agree on the sequence numbers of requests that commit locally even if commit in different views at each replica.

```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}

\begin{document}
\begin{tikzpicture}[xscale=1, yscale=0.80]

% --- Color Theme ---
\definecolor{faultColor}{RGB}{255, 60, 60}
\definecolor{msgColor}{RGB}{60, 120, 255}

% --- Background Layer: Phase Dividers ---
\begin{scope}[thick, dashed]
    \draw (2.5, 1) -- (2.5, -6.8);
    \draw (5.5, 1) -- (5.5, -6.8);
    \draw (8.5, 1) -- (8.5, -6.8);
    \draw (11.5, 1) -- (11.5, -6.8);
\end{scope}

% --- Midground Layer: Horizontal Timelines ---
\begin{scope}[very thick]
    \draw (0, 0) -- (15, 0);
    \draw (0, -1.5) -- (15, -1.5);
    \draw (0, -3.0) -- (15, -3.0);
    \draw (0, -4.5) -- (15, -4.5);
    \draw (0, -6.0) -- (15, -6.0);
\end{scope}

% --- Node Labels ---
\begin{scope}[font=\Large\bfseries]
    \node[anchor=east] at (-0.2, 0) {C};
    \node[anchor=east] at (-0.2, -1.5) {0};
    \node[anchor=east] at (-0.2, -3.0) {1};
    \node[anchor=east] at (-0.2, -4.5) {2};
    \node[anchor=east] at (-0.2, -6.0) {3};
\end{scope}

% --- Phase Labels ---
\begin{scope}[font=\large\bfseries]
    \node at (1.25, 0.5) {request};
    \node at (4.0, 0.5) {pre-prepare};
    \node at (7.0, 0.5) {prepare};
    \node at (10.0, 0.5) {commit};
    \node at (13.25, 0.5) {reply};
\end{scope}

% --- Fault Indicator ('X' on Node 3) ---
\begin{scope}[very thick, faultColor]
    \draw (1.3, -5.7) -- (1.7, -6.3);
    \draw (1.3, -6.3) -- (1.7, -5.7);
\end{scope}

% --- Foreground Layer: Message Vectors ---
% Using arrows.meta to explicitly scale the Stealth arrowhead
\begin{scope}[every path/.style={-{Stealth[scale=1.5]}, very thick, msgColor}]
    
    % Phase 1: Request
    \draw (0.5, 0) -- (2.4, -1.5);

    % Phase 2: Pre-Prepare
    \draw (2.8, -1.5) -- (5.4, -3.0);
    \draw (2.8, -1.5) -- (5.4, -4.5);
    \draw (2.8, -1.5) -- (5.4, -6.0);

    % Phase 3: Prepare
    \draw (5.8, -3.0) -- (8.4, -1.5);
    \draw (5.8, -3.0) -- (8.4, -4.5);
    \draw (5.8, -3.0) -- (8.4, -6.0);
    \draw (5.8, -4.5) -- (8.4, -1.5);
    \draw (5.8, -4.5) -- (8.4, -3.0);
    \draw (5.8, -4.5) -- (8.4, -6.0);

    % Phase 4: Commit
    \draw (8.8, -1.5) -- (11.4, -3.0);
    \draw (8.8, -1.5) -- (11.4, -4.5);
    \draw (8.8, -1.5) -- (11.4, -6.0);
    \draw (8.8, -3.0) -- (11.4, -1.5);
    \draw (8.8, -3.0) -- (11.4, -4.5);
    \draw (8.8, -3.0) -- (11.4, -6.0);
    \draw (8.8, -4.5) -- (11.4, -1.5);
    \draw (8.8, -4.5) -- (11.4, -3.0);
    \draw (8.8, -4.5) -- (11.4, -6.0);

    % Phase 5: Reply
    \draw (12.0, -1.5) -- (14.0, 0);
    \draw (12.0, -3.0) -- (14.4, 0);
    \draw (12.0, -4.5) -- (14.8, 0);

\end{scope}

\end{tikzpicture}
\end{document}
```

Here, $0$ is primary, $1, 2$ are honest replicas, and $3$ is a faulty replica. The important distinction here (and why it's different from [[HarpFS#Normal Operation Flow]]) is that the replicas execute the operation, not the primary (alleviates malicious primary).

## Problem: Faulty Primary
This is *easy*. More generally, we can get a new primary. In [[HarpFS]], this is done via view change. However, running an election may not be sufficient, as the old leader can win. PBFT fixes this by giving a deterministic primary selection algorithm. This is the $p = v \bmod |\mathcal{R}|$, ensuring that the primary changes in a round-robin fashion.

You cannot continually rig the elections. In the worst case, we need $f$ view changes in a row. 

## Problem: Honest Primary + Skeptical Replicas
This is *hard*. How does the primary convince the replicas it is honest? We get a quorum of $2f + 1$ replicas to agree. 

# Garbage Collection
The logs of the replicas can grow indefinitely. To prevent this, the replicas periodically checkpoint their state and discard old log entries. We can discard requests after have been executed by at least $f + 1$ non-faulty replicas and it can prove this to others in view changes. 

If some replica misses messages that were discarded by all non-faulty replicas, it will need to be brought up to date by transferring all or a portion of the service state. Therefore, replicas also need some proof that the state is correct.

Proofs are expensive. To reduce the cost, replicas can produce a proof of their state when a sequence number is divisible by some constant (e.g. $100$) is executed. Let 
- a **checkpoint** be the state produced by this request and
- a **stable checkpoint** be a checkpoint with a proof. 

A replica maintains several logical copies of the service state:
- the last stable checkpoint
- zero or more checkpoints (that are not stable)
- a current state 

## Proof of Correctness
When replica $i$ produces a checkpoint, it multicasts a message
$$
\langle \texttt{CHECKPOINT}, n, d, i \rangle_{\sigma_i}
$$
to the other replicas, where
- $n$ is the sequence number of the last request whose execution is reflected in the state 
- $d$ is the digest of the state

Each replica collects `checkpoint` messages in its log until it has $2f + 1$ of them for sequence number $n$ with the same digest $d$ signed by different replicas (possibly including itself). These $2f + 1$ messages are proof.

A checkpoint with proof is a stable checkpoint and discards all [[#Pre-Prepare Phase]], [[#Prepare Phase]], and [[#Commit Phase]] messages with sequence number $\leq n$ from its log. We use this to advance the [[#^7fbed1|low and high watermarks]], where 
- $h$ is the sequence number of the last stable checkpoint
- $H = h + k$ where $k$ is big enough so that replicas do not stall waiting for a checkpoint. 
	- If we use $100$ as a checkpoint generator, then $k$ might be $200$. 

# View Changes
The view change protocol provides [[#Definition (Liveness)|liveness]] by allowing progress when the primary fails. A view change is triggered by timeouts that prevent backups from waiting indefinitely for requests to execute. A backup starts a timer when it receives a request and the timer is not already running.

If the timer of backup $i$ expires in view $v$, the backup starts a view change to move to the system to view $v + 1$. It stops accepting messages (other than [[#Garbage Collection|checkpoint]], $\texttt{view-change}$, and $\texttt{new-view}$ messages) and multicasts a 
$$
\langle \texttt{VIEW-CHANGE}, v + 1, n, \mathcal{C}, \mathcal{P}, i \rangle_{\sigma_i}
$$
message to all replicas, where
- $v + 1$ is the new view number
- $n$ is the sequence number of the last stable checkpoint $s$ known to $i$
- $\mathcal{C}$ is a set of $2f + 1$ `checkpoint` messages for the stable checkpoint with sequence number $n$ (proof of $s$)
- $\mathcal{P}$ is a set contain a set $\mathcal{P}_m$ for each request $m$ that prepared at $i$ with a sequence number higher than $n$. 
  - Each $\mathcal{P}_m$ contains a valid `pre-prepare` message (without the corresponding client message) and $2f$ matching, valid `prepare` messages signed by different backups with the same view, sequence number, and digest of $m$.

When the primary $p$ of view $v + 1$ receives $2f$ valid `view-change` messages for view $v + 1$ from different backups, it starts the view change by multicasting a
$$
\langle \texttt{NEW-VIEW}, v + 1, \mathcal{V}, \mathcal{O} \rangle_{\sigma_p}
$$
message to all other replicas, where
- $v + 1$ is the new view number
- $\mathcal{V}$ is the set of $2f$ valid `view-change` messages that the primary received
- $\mathcal{O}$ is a set of `pre-prepare` messages. It is computed as follows:
  - Think of it as the "carry-over" to-do list for the new primary. When the old primary failed, the network was likely in the middle of processing several client requests (local commits, still in prepare phase, some sequence slots might be empty). The new primary cannot ignore these in-flight requests otherwise it may lost data and diverge. 
  - The primary determines the sequence number $\texttt{min-s}$ of the latest stable checkpoint in $\mathcal{V}$ and the highest sequence number $\texttt{max-s}$ in a `prepare` message in $\mathcal{V}$.
    - Set up the boundaries for the sequence numbers that the new primary needs to worry about.
  - The primary creates a new `pre-prepare` message for view $v + 1$ for each sequence number $n$ between $\texttt{min-s}$ and $\texttt{max-s}$. There are two cases:
    1. There is at least one set in the $\mathcal{P}$ componentof some `view-change` message in $\mathcal{V}$ with sequence number $n$.
      - The primary creates a new message:
      $$
      \langle \texttt{PRE-PREPARE}, v + 1, n, d \rangle_{\sigma_p}, m \rangle
      $$
      where $d$ is the request digest in the `pre-prepare` message for sequence number $n$ with the highest view number in $\mathcal{V}$.
    2. There is no such set.
      - It creates a new message with a null request:
      $$
      \langle \texttt{PRE-PREPARE}, v + 1, n, d^\texttt{null} \rangle_{\sigma_p}
      $$
      where $d^\texttt{null}$ is the digest of a null request. This is similar to `no-op` in [[Paxos Algorithm]].

The primary then appends the messages in $\mathcal{O}$ to its log. If $\texttt{min-s}$ is greater than the sequence number of its own latest stable checkpoint, the primary also inserts the proof stability for the checkpoint with sequence number $\texttt{min-s}$ in its log. Then **the primary enters view** $v + 1$ and can accept messages for view $v + 1$.

A backup accepts a `new-view` message for view $v + 1$ if 
- it is properly signed
- the view change messages it contains are valid for view $v + 1$
- if the set $\mathcal{O}$ is correct
  - It verifies the correctness by performing a similar computation to the used by the primary to create $\mathcal{O}$.

Then it adds the new information to its log as described for the primary, multicasts a `prepare` for each message in $\mathcal{O}$, and enters view $v + 1$.