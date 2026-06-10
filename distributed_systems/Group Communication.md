---
tags:
  - CSE_223B
---
# Group Communication
This note summarizes group communication protocols, focusing on the design, trade-offs, and mechanics of the ISIS Group Communication System developed at Cornell University in the 1980s.

Largely ripped from [paper](https://dl.acm.org/doi/pdf/10.1145/7351.7478). ^ee2684
# Introduction & Motivation: The ISIS System
The ISIS Group Communication System provides reliable, ordered message delivery services for distributed applications. Historically, ISIS has been used in critical, real-world systems such as NASDAQ and the Boeing 777 software control system.

## The Replicated State Machine (RSM) Dilemma
To build a [[Replication|Replicated State Machine (RSM)]] that does not diverge, a system needs a single total ordering on all events (the gold standard of [[Memory Coherence#Definition (Strict Consistency Model)|strict consistency]]). However, enforcing a total order is:
- **Expensive & Poorly Scalable**: Ordering everything requires coordination across all nodes.
- **Speed-of-Light Bound**: The latency of coordination is ultimately limited by the physical speed of light over distances.

## The Solution: Relaxed Consistency
Instead of forcing every part of a distributed system to be a strict RSM:
1. Identify the small subsets of the system that absolutely require strict RSM semantics.
2. Allow the rest of the system to operate under weaker/relaxed ordering semantics to maximize performance by reducing coordination and message serialization.

# The Communication & Semantics Spectrum
Group communication protocols trade off ordering guarantees against reliability and performance costs.

```tikz
\begin{document}
\begin{tikzpicture}[>=stealth, scale=1.4]
% Axis line drawing
\draw[->, thick] (0,0) -- (6.5,0);
\draw[->, thick] (0,0) -- (0,6.5);

% Axis labels inside the chart
\node[above left] at (6.5, 0.15) {\small \underline{Reliability (Atomicity)}};
\node[below right] at (0.15, 6.3) {\small \underline{Ordering Guarantees}};

% X-axis Ticks
\draw (1, 0.1) -- (1, -0.1) node[below=4pt] {\small Best Effort};
\draw (3.5, 0.1) -- (3.5, -0.1) node[below=4pt] {\small Reliable Channel};
\draw (5.5, 0.1) -- (5.5, -0.1) node[below=4pt] {\small Atomic / Agreement};

% Y-axis Ticks
\draw (0.1, 1) -- (-0.1, 1) node[left=5pt] {\small None};
\draw (0.1, 2) -- (-0.1, 2) node[left=5pt] {\small FIFO};
\draw (0.1, 3) -- (-0.1, 3) node[left=5pt] {\small Causal};
\draw (0.1, 4) -- (-0.1, 4) node[left=5pt] {\small Causal Total};
\draw (0.1, 5) -- (-0.1, 5) node[left=5pt] {\small Total Order};
\draw (0.1, 6) -- (-0.1, 6) node[left=5pt] {\small Total Wall Clock};

% Draw nodes (transparent background to allow text to adapt to light/dark themes natively)
\node[draw, rectangle, rounded corners, inner sep=4pt] (udp) at (1, 1) {\small\textbf{UDP}};
\node[draw, rectangle, rounded corners, inner sep=4pt] (tcp) at (3.5, 2) {\small\textbf{TCP}};
\node[draw, rectangle, rounded corners, inner sep=4pt] (cbcast) at (5, 3) {\small\textbf{CBCAST}};
\node[draw, rectangle, rounded corners, inner sep=4pt] (abcast) at (5.5, 5) {\small\textbf{ABCAST}};

% Projection lines
\draw[dashed, gray!60] (udp) -- (1, 0);
\draw[dashed, gray!60] (udp) -- (0, 1);

\draw[dashed, gray!60] (tcp) -- (3.5, 0);
\draw[dashed, gray!60] (tcp) -- (0, 2);

\draw[dashed, gray!60] (cbcast) -- (5, 0);
\draw[dashed, gray!60] (cbcast) -- (0, 3);

\draw[dashed, gray!60] (abcast) -- (5.5, 0);
\draw[dashed, gray!60] (abcast) -- (0, 5);
\end{tikzpicture}
\end{document}
```

- [[computer_security/lectures/Lecture 13 - Network Security I|UDP]]: Best effort, unreliable transport.
- [[computer_security/lectures/Lecture 13 - Network Security I#TCP|TCP]]: Guarantees FIFO delivery per channel. Cannot guarantee 100% reliability if endpoints fail (due to the impossibility of acknowledging ACKs infinitely).
- **CBCAST**: *Relaxed* causal ordering where messages respect the happens-before relationship, allowing high concurrency.
- **ABCAST**: *Strict* total ordering where every node delivers messages in the exact same order, which can clog queues during coordination.

# Types of Ordering Semantics
- **Total Wall Clock Ordering**: All messages are ordered strictly by the physical time they were sent. (Extremely difficult to achieve precisely in distributed systems due to clock drift; see [[Google Spanner#TrueTime]]).
- **[[Memory Coherence#Definition (Sequential Consistency)|Sequential Consistency]] (Total Order)**: All nodes deliver all messages in the *same* sequence, but this sequence does not necessarily correspond to physical wall-clock time.
	- It is important to note that total ordering does not care *what* the order is, only that the order is mutually consistent across all nodes. 
	- Doing this inherently requires synchronization with a leader, enforcing a performance penalty and limits concurrency.
- **Causal Ordering**: Respects the "happens-before" ($\to$) relationship. If message $m_1$ causally influenced[^1] the sending of $m_2$, then $m_1$ must be delivered before $m_2$ at all destinations. Unrelated (concurrent) messages do not have a defined order, which allows for parallel processing.
  
  [^1]: Message $m_1$ causally influences $m_2$ if the sender of $m_2$ had already sent or received $m_1$ (directly or transitively) before generating $m_2$ (i.e., $m_1 \to m_2$ via Lamport's happens-before relation).
- **Causal Total Ordering**: Combines both causal and total ordering guarantees. This can be achieved by layering ABCAST on top of CBCAST. Uses [[Vector Timestamps]] to track causality.

# CBCAST (Causal Broadcast)
CBCAST guarantees that messages are delivered respecting causal relationships. 

## Mechanics & Rules
Every node maintains a local message buffer (FIFO queue). To satisfy causal consistency:

1. **FIFO Sender Order**: Messages sent by a specific node must be delivered in the order they were sent.
   - *Implementation*: A node maintains a FIFO queue of outgoing messages. When connecting to another node via TCP, it sends the entire queue from the beginning. If the connection drops, it restarts transmission from the beginning of the queue, discarding duplicates at the receiver (idempotency).
2. **Transitive Causality**: If a node receives a message $m$ and subsequently sends message $m'$, then any node receiving $m'$ must deliver $m$ before $m'$.
   - *Implementation*: When a node receives a message, it appends it to its local queue. Thus, when it talks to another node, it transmits not only its own messages but all messages it has "heard" so far. The "so far" is explicitly the "happens-before" relation, giving us the causal ordering.

```
Example Buffer Queue 
containing locally generated and transitively heard messages:
 --+----+----+----+----+----+----+----+
   | B1 | A4 | C1 | A3 | A2 | A1 | ...| <-- Front of Queue (sent first)
 --+----+----+----+----+----+----+----+
```

## Optimization via [[Vector Timestamps|Vector Timestamps (VTS)]]
To avoid sending the entire history and to detect duplicate messages:
- Each queue state/message is labeled with a Vector Timestamp (VTS) summarizing the highest sequence number seen from each node.
- If node $C$ sends a message with VTS entry $C: 7$, the receiver checks its own VTS. If the receiver's VTS for $C \ge 7$, it discards the message as a duplicate (because it only updates its own VTS if it had seen the $C:7$ before). If it is exactly $6$, it accepts it. If it is $< 6$, it buffers the message and waits for the missing causal history to arrive.

## Trace Example 1
Suppose we have three nodes $A$, $B$, and $C$, all starting with VTS initialized to `[0, 0, 0]`.

### Initial VTS State
```
A: [0, 0, 0]
B: [0, 0, 0]
C: [0, 0, 0]
```

### Event 1: Transmission
Node $A$ broadcasts message $a_1$, incrementing its own index in its VTS. The message is sent with metadata $V(a_1) = \texttt{[1, 0, 0]}$.
```
A: [1, 0, 0]
B: [0, 0, 0]
C: [0, 0, 0]
```

### Event 2: Causal Dependency
Node $B$ receives and delivers $a_1$ (updating its VTS to `[1, 0, 0]`), and subsequently broadcasts message $b_1$, incrementing its VTS. The message is sent with metadata $V(b_1) = \texttt{[1, 1, 0]}$.
Because $B$ delivered $a_1$ before sending $b_1$, a causal dependency is established: $a_1 \to b_1$.
```
A: [1, 0, 0]
B: [1, 1, 0]
C: [0, 0, 0]
```

### Event 3: Out-of-Order Arrival & Buffering
Due to network latency, Node $C$ receives $b_1$ (with VTS `[1, 1, 0]`) first, before $a_1$ has arrived.
Node $C$ checks the causal delivery rules:
- $V(b_1)[B] = 1 \le V_C[B] + 1$ (expected next message from $B$, holds).
- $V(b_1)[A] = 1 \le V_C[A]$ (failed: $1 > 0$, since $C$ has not yet delivered $a_1$).
Since the causal constraint is not satisfied, Node $C$ buffers $b_1$.
```
A: [1, 0, 0]
B: [1, 1, 0]
C: [0, 0, 0]  |  Buffered: [b_1 (VTS: [1, 1, 0])]
```

### Event 4: Delivery and Resolution
Node $C$ finally receives $a_1$ (with VTS `[1, 0, 0]`).
1. Node $C$ delivers $a_1$ immediately, since its causal dependency is met: $V(a_1)[A] = 1 \le V_C[A] + 1$ and $V(a_1)[B] = 0 \le V_C[B] = 0$. Node $C$'s VTS updates to `[1, 0, 0]`.
```
C: [1, 0, 0]  |  Buffered: [b_1 (VTS: [1, 1, 0])]
```
2. Node $C$ checks its buffered messages. Since $V_C$ is now `[1, 0, 0]`, the causal constraint for $b_1$ is satisfied ($V(b_1)[A] = 1 \le V_C[A] = 1$). $C$ delivers $b_1$, and updates its VTS.
```
A: [1, 0, 0]
B: [1, 1, 0]
C: [1, 1, 0]  |  Buffered: []
```

## Trace Example 2: Concurrent Messages
When messages are concurrent ($a_1 \parallel b_1$), CBCAST does not enforce any ordering between them, allowing different nodes to deliver them in different orders without blocking.

Suppose we have three nodes $A$, $B$, and $C$, all starting with VTS `[0, 0, 0]`.
```
A: [0, 0, 0]
B: [0, 0, 0]
C: [0, 0, 0]
```

### Event 1: Concurrent Transmission
Node $A$ and Node $B$ broadcast messages $a_1$ and $b_1$ at the same time.
- $a_1$ is sent with $V(a_1) = \texttt{[1, 0, 0]}$.
- $b_1$ is sent with $V(b_1) = \texttt{[0, 1, 0]}$.
```
A: [1, 0, 0]
B: [0, 1, 0]
C: [0, 0, 0]
```

### Event 2: Deliveries at Node C
Node $C$ receives $a_1$ first, then $b_1$.
1. Node $C$ receives and delivers $a_1$ immediately (VTS becomes `[1, 0, 0]`).
2. Node $C$ receives and delivers $b_1$ immediately, since 
   $$
   V(b_1)[A] = 0 \le V_C[A] = 1
   $$
   is satisfied (VTS of $C$ becomes `[1, 1, 0]`).
*Delivery Order at C*: $a_1 \to b_1$.
```
C: [1, 1, 0]
```

### Event 3: Delivery at Node B
Node $B$ (having delivered its own message $b_1$ locally) receives $a_1$. Since 
$$
V(a_1)[A] = 1 \le V_B[A] + 1 
\quad\text{and}\quad
V(a_1)[B] = 0 \le V_B[B] = 1
$$
Node $B$ delivers $a_1$ immediately (VTS becomes `[1, 1, 0]`).
*Delivery Order at B*: $b_1 \to a_1$.
```
B: [1, 1, 0]
```

### Event 4: Delivery at Node A
Node $A$ (having delivered its own message $a_1$ locally) receives $b_1$. Since 
$$
V(b_1)[B] = 1 \le V_A[B] + 1
\quad\text{and}\quad
V(b_1)[A] = 0 \le V_A[A] = 1
$$
Node $A$ delivers $b_1$ immediately (VTS becomes `[1, 1, 0]`).
*Delivery Order at A*: $a_1 \to b_1$.
```
A: [1, 1, 0]
```

*Summary*: Because $a_1$ and $b_1$ are causally independent, CBCAST delivers them without any coordination, resulting in Node $B$ delivering $b_1 \to a_1$ while Nodes $A$ and $C$ deliver $a_1 \to b_1$.

## Atomicity & Garbage Collection
- **Atomic Propagation**: If a message reaches at least one alive node before the sender dies, it will eventually propagate to all other alive nodes through transitive gossip, ensuring atomicity.
- **Garbage Collection (`REM_DST`)**: To prevent the queue from growing indefinitely, each message tracks a remaining destination set (`REM_DST`). 
  - As nodes acknowledge receipt, they are removed from `REM_DST`.
  - Once `REM_DST` is empty, the message is garbage collected from the queue.
  - **Optimization**: Senders can include metadata indicating which nodes have already received the message to prevent redundant transmissions (similar to [[TreadMarks#Lazy Release Consistency (LRC)|Lazy Release Consistency]] / [[TreadMarks|TreadMarks]] diff propagation using lock acquisition).

# ABCAST (Atomic Broadcast)
ABCAST guarantees total ordering of messages across all group members. Unlike CBCAST, nodes cannot immediately process messages; they must wait for the group to agree on a final sequence number.

## The Challenge: Queue Clogging
Every node maintains a local queue. Since messages must be delivered in the exact same total order, if the message at the front of the queue is waiting for order agreement (i.e., is not yet marked `deliverable`), the entire queue is clogged. No messages behind it can be delivered to the application, even if their ordering is already decided.

## Protocol Steps
1. **Initiation**: The sender broadcasts a message to all nodes.
2. **Temporary Sequence**: Each node places the message in its local queue, marks it as undeliverable (temporary), and assigns it a temporary sequence number (usually the local counter). It sends this number as an `ACK` proposal back to the sender.
3. **Agreement**: The sender collects all proposals, selects the maximum sequence number, and broadcasts this final sequence number.
4. **Commit & Sort**: Each node updates the message's sequence number to the final maximum, marks it as deliverable, and re-sorts its queue based on the final sequence numbers (breaking ties using node IDs).
5. **Delivery**: A message is delivered to the application only when it is at the front of the queue and marked deliverable.

## Trace Example 3
Suppose node $A$ sends message $a$ and node $B$ sends message $b$ *concurrently*. Node $C$ is a receiver.

### Initial Queue State (Proposed Sequences)
Messages are placed in the queues with temporary proposed sequences. Sequence number tuples are in the format `<seq,node_id>` (e.g., `2a` represents sequence number 2 proposed by node A).

```
[Queue End]                                          [Queue Front]
    v                                                      v
A:  b(2a) [Undeliverable]    |   a(1a) [Undeliverable]
B:  a(2b) [Undeliverable]    |   b(1b) [Undeliverable]
C:  b(2c) [Undeliverable]    |   a(1c) [Undeliverable]
```
This is the state of the queues after $A,B,C$ have received the messages. Note that in $B$, it received message $a$ after $b$ (because it sent out $b$, so we can very quickly add it to its queue).

### Step 1: Proposal Collection
- **For message $a$**: Proposals collected by $A$ are `1.A` (from $A$), `2.B` (from $B$), and `1.C` (from $C$). Max sequence = `2.B`.
- **For message $b$**: Proposals collected by $B$ are `2.A` (from $A$), `1.B` (from $B$), and `2.C` (from $C$). Max sequence = `2.C`.

### Step 2: Final Sequence Broadcast & Re-sorting
The senders broadcast the chosen final sequence numbers (`2.B` for message $a$, `2.C` for message $b$). Nodes update the sequence numbers, mark them as deliverable, and re-sort their queues. Since `2.B` < `2.C` (by alphabetical tie-breaker), $a$ sorts before $b$.

```
[Queue End]                                    [Queue Front]
    v                                                v
A:  a(2b) [Deliverable]     |   b(2a) [Undeliverable]  <-- a is Clogged by b
B:  a(2b) [Deliverable]     |   b(1b) [Undeliverable]  <-- a is Clogged by b
C:  b(2c) [Undeliverable]   |   a(2b) [Deliverable]    <-- a is deliverable
```

### Step 3: Delivery and Resolution
- **Node C**: Message $a$ (final sequence `2.B`) is at the front of the queue and marked deliverable. Node $C$ delivers $a$ immediately.
- **Nodes A and B**: Message $a$ is deliverable but is blocked because the messages at the front of their queues (`b(2a)` and `b(1b)`) are still undeliverable. The queues are clogged.
- **Resolution**: In the fullness of time, node $B$ decides the final sequence number for $b$ (`2.C`) and broadcasts it. Nodes A and B update $b$ to `2.C` (deliverable) and re-sort their queues:

```
A:  b(2c) [Deliverable]  |  a(2b) [Deliverable]    <-- a can be delivered
B:  b(2c) [Deliverable]  |  a(2b) [Deliverable]    <-- a can be delivered
C:                       |  b(2c) [Undeliverable]  <-- waiting for b's decision
```
*(Once $b$ is updated to `2.C` on all nodes, both $a$ and $b$ are delivered sequentially across all nodes).*

## Trace Example 4
What happens if during [[#Step 2 Final Sequence Broadcast & Re-sorting]], $A$ is unable to broadcast its final order? I.e. it crashed or network partition before sending. 

Sometime immediately after sending the messages, this is the queue state.
```
[Queue End]                                    [Queue Front]
    v                                                v
A:  DEAD!                   |   DEAD!
B:  a(2b) [Undeliverable]   |   b(1b) [Undeliverable]
C:  b(2c) [Undeliverable]   |   a(1c) [Undeliverable]
```

Nodes $B$ and $C$ detect that Node $A$ has failed.
- This can be done via heartbeats.
- $B$ and $C$ can interrogate other participants about the status of the message. A participant being interrogated responds with `no msg received` or `<seq,node_id>` of the sender. The new coordinator collects responses. 
- The [[#^ee2684|paper]] doesn't explain who gets picked as the new cooridnator, but you can imagine the next node (like in [[Chord]]) or the node with the lowest ID is the new coordinator. For our purposes, we can assume $B$ is the leader.
- What about concurrent takeovers? If both $B,C$ interrogate the network, both will collect `1c` and `2b`. The maximum is `2b`, and will broadcast `2b`. In particular, it is **idempotent**, such that the same operation can be applied multiples without changing the result. 

At this point, $B$ "owns" message $a$ and we proceed with the above example normally. 

What if $B$ was the one that failed? Same thing, except $C$ won't need to reoreder anything.

# GBCAST (Group Broadcast)
Processes frequently need to monitor one another to react to failures, recoveries, or dynamic changes in group membership (like a new node joining). If every node independently updated its local view of the group membership whenever it noticed a failure, massive inconsistencies would arise. A system might try to route a request to a node that half the network thinks is dead, or two nodes might both think they are the designated "coordinator".

GBCAST solves this by ensuring that changes to the group's global properties are treated as atomic broadcast events. Every alive member maintains a local, identical copy of the process group view, updating it in perfect synchronization relative to other events. 

GBCAST is much like [[#ABCAST (Atomic Broadcast)|ABCAST]], in the sense that the value/messages are just the group metadata. However, it is different where:
- GBCAST messages live in the same ABCAST queue. When normal ABCAST messages reach the front and are deliverable, they will be immediately delivered. When GBCAST reaches the front, delivery complete stops, freezing the queue.
- All GBCAST messages at this point are tagged as `undeliverable`. The protocol waits until the GBCAST message is the head of ALL ABCAST queues across the system. 
- All [[#CBCAST (Causal Broadcast)|CBCAST]] messages arrive concurrently and unpredictable, so we cannot easily freeze them. We establish a FIFO wait queue for the CBCAST messages. The node initating the GBCAST asks all group members for a list of the CBCAST message IDs they have already placed on their local delivery queues (not the wait queue), merging the lists for a system-wide "before list". 
- If a trapped message is on the before list (or causally precedes one on the list), it is released from the wait queue to the delivery queue. 
- The GBCAST message is then officially `delivered`, shifting the system to the new group state. 
- The wait queue are extended to the delivery queue, GBCAST is removed, and standard delivery assumes

This for standard and **failure** GBCAST. When a node randomly dies, it is a **failure GBCAST** message. Before standard ordering, the system must search for and schedule the transmission of any buffered messages sent by the failed process. Once all pending messages from the failed process are `deliverable`, does the protocol proceed. Think of this like a "forced flush".

## Trace Example: Failure GBCAST for Process F
Setup: Nodes $A$, $B$, $C$, and $F$ are in Process Group $G$. Node $F$ experiences a halting failure.
Node $A$ detects the failure via the monitoring mechanism and initiates the protocol.

### Initial State (Pre-GBCAST)
Before crashing, Node $F$ sent two messages that are still propagating through the network:
- ABCAST message `f1`
- CBCAST message `f2`

Node $B$ holds a copy of `f2` in its buffer en route to its destination. Node $C$ holds `f1` in its ABCAST priority queue, currently tagged `[Undeliverable]`.

### Phase 1: The Pre-Emptive Failure Flush
- **Step 1.1**: Node $A$ acquires a read-lock on its site view and sends a preliminary alert to $B$ and $C$: "Starting failure GBCAST for $F$."
- **Step 1.2**: Node $B$ searches its internal buffers, finds `f2` (sent by $F$), and immediately schedules it for transmission to its remaining destinations. Node $B$ pauses until `f2`'s status turns to 'sent'.
- **Step 1.3**: Node $C$ pauses and waits until the pending ABCAST `f1` becomes `[Deliverable]` (e.g., another node takes over the ABCAST protocol for `f1` and finalizes its sequence).
- **Step 1.4**: Once `f1` is deliverable and `f2` is sent, $B$ and $C$ send an acknowledgment back to $A$.

The network is drained of $F$'s remaining messages.

### Phase 2: The ABCAST Queue Freeze
- **Step 2.1**: Node $A$ distributes the formal GBCAST("$F$ has failed") message to $B$ and $C$.
- **Step 2.2**: Nodes $B$ and $C$ place the GBCAST in their ABCAST queues, tag it `[Undeliverable]`, assign a proposed priority, and send the priority back to $A$.
- **Step 2.3**: Node $A$ calculates the maximum priority and broadcasts the final sequence. Nodes $B$ and $C$ update the priority and re-sort their queues.
  - Unlike a standard ABCAST, the GBCAST is NOT marked deliverable yet.

**Queue State at Node $C$**
```text
[Queue End]                                                       [Queue Front]
    v                                                                   v
X(3c) [Undeliverable]  |  GBCAST(2a) [Undeliverable]  |  f1(1c) [Deliverable]
```

- **Step 2.4**: Node $C$ delivers `f1`. The GBCAST now reaches the head of the queue. Delivery on this ABCAST queue is SUSPENDED. Message `X` is blocked from delivery.

### Phase 3: CBCAST Wait Queue & Before List
- **Step 3.1**: Node $A$ contacts $B$ and $C$ to resolve asynchronous CBCAST boundaries.
- **Step 3.2**: Nodes $B$ and $C$ establish a temporary FIFO "Wait Queue". Any incoming CBCASTs (like `f2` finally arriving at $C$) are placed here instead of the standard delivery queue.
- **Step 3.3**: Nodes $B$ and $C$ send their `IDlist` (a list of all CBCAST IDs they have already placed on their delivery queues) to Node $A$.
- **Step 3.4**: Node $A$ merges all received `IDlists` into a definitive "Before List" and broadcasts it back to $B$ and $C$.

### Phase 4: Resolution & Resumption
- **Step 4.1**: Nodes $B$ and $C$ examine the messages trapped in their Wait Queues.
  - If a message is explicitly on the "Before List" (or precedes one on the list), it is flagged.
  - Because this is a failure GBCAST for $F$, any message originally sent by $F$ (like `f2`) found in the Wait Queue is forcefully added to the "Before List".
- **Step 4.2**: Flagged CBCASTs (including `f2`) are transferred from the Wait Queue to the standard Delivery Queue and processed.
- **Step 4.3**: The GBCAST("$F$ has failed") is officially delivered to the application. The Process Group View is updated. $F$ is formally removed.
- **Step 4.4**: The GBCAST is removed from the head of the ABCAST queues.
  *Result*: The queues unfreeze. Normal delivery resumes (`X` can now become deliverable and process). Node $F$ is never heard from again.