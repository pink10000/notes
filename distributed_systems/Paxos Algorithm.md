---
tags:
  - CSE_223B
aliases:
  - Paxos
---
Largely ripped from [paper](https://cseweb.ucsd.edu/classes/sp11/cse223b/papers/paxos-simple.pdf).

# The Consensus Algorithm
Assume a collection of processes that can propose values. A **consensus algorithm** ensures that a single proposed value is chosen. If no value is proposed, then no value should be chosen. The safety requirements for consensus are:
1. Only a value that has been proposed may be chosen.
2. Only a single value is chosen. ^6bf8d1
3. A process never learns that a value has been chosen unless it actually has been.

The goal is to ensure that some proposed value is *eventually* chosen and, if a value has been chosen, then a process can eventually learn the value. 

The above three roles are performed by the following three classes of processes/agents: ^9a3922
- **Proposers**: they propose values
	- Nodes that advocate for client values by proposing them to the system.
- **Acceptors**: they accept values 
	-  The core consensus engine. They receive, vote on, and store proposals to form [[Quorum|quorums]].
	- They do not know what (or when) a system has decided on something. Otherwise, they are next the kind of agent.
- **Learners**: Nodes that discover which value was ultimately chosen by the `acceptors`.

All agents can send messages to one another via messages. We assume these messages are asynchronous in which  ^1e859d
- Agents operate at arbitrary speed. 
- Agents may fail by: stopping, restart
- Since all agents can fail after a value is chosen and then restart, a solution is impossible unless some information can be remembered by an agent that has failed and restarted.
- Messages can take arbitrarily long to be delivered. ^6a9267
- Messages can be duplicated.
- Messages can be lost. ^199cfe
- Messages *cannot* be corrupted.

## Choosing a Value
In the most simplest case, to choose a value we must have a single `acceptor` agent. A `proposer` sends a proposal to acceptor, who chooses the first proposed value it receives.

If the `acceptor` dies, the whole system stops. We must have multiple `acceptors`. A `proposer` will send a message to a set of `acceptors`. A majority of `acceptors` agreeing on a value is sufficient to establish a [[Quorum]]. 

Assuming no failure or message loss, a value *must* be accepted even if only one value was proposed. Therefore
> [!idea] Proposition 1
> An acceptor must accept the first proposal that it receives.

What happens when several values are proposed by different `proposers` at the same time, such that no value has a majority accept?

We must change `Prop 1`. Suppose each proposal now has a natural number. So a proposal is $(n, v)$ of proposal number $n$ and value $v$. Different proposals must have different numbers (implementation dependent)[^2]. 

[^2]: We can use [[Group|Group Theory]] where nodes have a set of generating primes to ensure a collision never occurs. 

A proposal is **chosen** (and thus its value) when a single proposal with that value has been accepted by a majority of `acceptors`. All chosen proposals must have the same value. By induction on the proposal number $n$, it suffices to guarantee
>[!idea] Proposition 2
>If a proposal with value $v$ is chosen, then every higher-numbered proposal that is chosen has value $v$.

Since numbers are totally ordered, `Prop 2` guarantees the [[#^6bf8d1|Property 2]]. To be chosen, a proposal must be accepted by at least one `acceptor`. We can satisfy `Prop 2` by 
>[!idea] Proposition 2a
>If a proposal with value $v$ is chosen, then every higher-numbered proposal accepted by **any** `acceptor` has value $v$. 

Here, `Prop 1` must still hold. 

**Error Case**: Because of message property [[#^1e859d|x]] and [[#^6a9267|y]], a particular `acceptor` $c$ may never receive any proposals. Suppose a new `proposer` wakes up and issues proposal $(n', v')$ where $n' > n$ and $v' \neq v$. By `Prop 1`, $c$ must accept, violating `Prop 2a`. 

Therefore we must make `Prop 2a` stronger. Consider
>[!idea] Proposition 2b
>If a proposal with value $v$ is chosen, then every higher-numbered proposal issued by **any** `proposer` has value $v$. 

which supercedes `Prop 2a`. Since a proposal must be isued by a `proposer` before it can be accepted by an `acceptor`, `Prop 2b` $\implies$ `Prop 2a` $\implies$ `Prop 2`. Now we need to satisfy `Prop 2b`. 

Assume proposal $(m, v)$ is chosen. WTS that any proposal with number $n > m$ also has value $v$. We do this by inducting on $n$, and that every proposal with number $i \in [m, n-1]$ must also have the same value, i.e. $(i, v)$. 

If proposal $(m, v)$ was chosen, there must be some set $C$ containing a **majority** of `acceptors` such that every `acceptor` in $C$ accepted $(m, v)$. By induction, 
- *every* `acceptor` in $C$ has accepted a proposal $(i, v)$ with $i \in [m, n-1]$, and 
- *every* proposal with number $i \in [m, n-1]$ was accepted by *any* `acceptor` has value $v$.

Suppose we have another set $S$ of "another majority" of `acceptors`. Since $S \cap C \neq \varnothing$, a proposal numbered $n$ has value $v$ by ensuring the following invariant:
>[!idea] Proposition 2c
>For any $v,n$, if a proposal with $(n, v)$ is issued, there $\exists S$ consisting of a majority of `acceptors` such that either
>
>1. no `acceptor` in $S$ has accepted any proposal numbered less than $n$
>2. $v$ is the value of the highest-numbered proposal among all proposals numbered less than $n$ accepted by the `acceptors` in $S$.

^370cc8

The above is an example of [[CAP Theorem#ACID|atomicity]]. By maintaining `Prop 2c`, we imply `Prop 2b`. To maintain `Prop 2c`, a `proposer` who wishes to issue a proposal $(n, -)$ must learn of the highest-numbered proposal with number $< n$, if any, that has been accepted by each `acceptor` in some majority of `acceptors`. 

Instead of learning of future proposals, the `proposer` will extract a promise that the `acceptors` do not accept any more proposals $(<n, -)$. 

We get the following algorithm.
1. A `proposer` chooses proposal $(n, -)$ and sends a request to each member of some set of `acceptors`, asking it to respond with the following. This request is the **prepare** request with number $n$. Denote $\texttt{prepare}(n)$. ^7cd75f
	1. A promise to never accept a proposal $(<n, -)$, and 
	2. The proposal with the highest number less than $n$ that it has accepted (if any). Denote the set of these reponses as $H_{<n}$.  ^ed7f9a
2. If the `proposer` receives the requested responses from a majority of the `acceptors`, then it can issue a proposal $(n, v)$ where $v = \max_{(-, v)}H_{<n}$, or any arbitrary value if $H_{<n} = \varnothing$. 

A `proposer` issues a proposal by sending to some set of `acceptors` a request that its proposal $(n, v)$ be accepted. Let this be called an **accept** request and denote it as $\texttt{accept}(n, v)$.

`Acceptors` receive two kinds of requests from `proposers`. 
1. $\texttt{prepare}(n)$ request 
2. $\texttt{accept}$ request

Since `acceptors` can ignore any request, we must determine when it should respond to a request. It can always respond to a $\texttt{prepare}(-)$ request. But,
>[!idea] Proposition 1a
>An `acceptor` can accept a proposal $(n, -)$ $\iff$ it has not responded to a $\texttt{prepare}(a)$ where $a > n$. 
>

`Prop 1a` is stronger than `Prop 1`. 

### Optimization 
Suppose an `acceptor` receives a $\texttt{prepare}(n)$ request, but it has already responded to a $\texttt{prepare}(a)$ request where $a > n$. There is no reason for the `acceptor` to respond to the $\texttt{prepare}(n)$ request, since the `acceptor` will never accept that proposal anyway. Therefore, an `acceptor` can ignore a $\texttt{prepare}(n)$ request if it has already responded to a $\texttt{prepare}(a)$ request where $a > n$.

Thus, the `acceptor` only needs to store the highest proposal $(a, -)$ it has ever accepted and the highest $\texttt{prepare}(b)$ request it has ever responded to. To ensure `Prop 2c`, $a,b$ must be stored, even during failure and restart.

### In Total
**Phase 1**: 
1. A `proposer` selects proposal $(n, -)$ and sends $\texttt{prepare}(n)$ to a majority of `acceptors`.
2. If an `acceptor` receives $\texttt{prepare}(n)$ and $n > a$ where $a$ is the highest $\texttt{prepare}$ it has already responded so far, it responds with [[#^7cd75f|a promise to never accept any more proposals]] $(n', -)$ where $n' < n$ AND [[#^370cc8|with]] $a$ (if it exists). 

**Phase 2**: 
1. If the `proposer` receives a reponse to its $\texttt{prepare}(n)$ request from a majority of `acceptors`, then it sends $\texttt{accept}(n, v)$ where 
   $$
   \begin{aligned}
   H &:=  \{(n_{i}, v_{i}) : \text{response to } \texttt{prepare}(n) \} \\
   v &= \max_{v} \max_{(n_{i}, -)} H \\
   \end{aligned}
   $$
   the highest-numbered proposal among all the responses (or any value if $H = \varnothing$). 
2. If an `acceptor` receives $\texttt{accept}(n, v)$, it accepts the proposal $(n, v)$ unless it has already responded to a $\texttt{prepare}(b)$ request where $b > n$.

For implementation, if an `acceptor` decides to ignore a request, it should tell the sender that it is ignoring the request, so that the sender can retry with a higher proposal number. This is a performance optimization and does not affect correctness.

## Learning a Chosen Value
To learn that a value $v$ has been chosen, a `learner` must find out a proposal $(n, v)$ has been accepted by a majority of `acceptors`. An obvious algorithm is to have each `acceptor` respond to all `learners` whenever it accepts a proposal, sending them the proposal. However, this is inefficient. Each `acceptor` must respond to each `learner`, with $l$ `learners` and $a$ `acceptors`, this results in $O(al)$ messages.

We can have the `acceptors` respond with their acceptances to a **distinguished learner**, (denote this as `^learner`)  which in turn informs the other `learners` when a value is chosen; this results in $O(a + l)$ messages. However, this creates a single point of failure. If the distinguished `learner` fails, no `learner` can learn the chosen value.

Instead, the `acceptors` can respond to some set of `^learners`each of which can inform the other `learners` when a value is chosen. This results in $O(a + k + l)$ messages where $k$ is the number of `^learners`. More `^learners` $\implies$ more reliability, but more messages. 

Because of [[#^199cfe|message loss]], a value could be chosen with no `learner` ever finding out. In this case, `learners` will only know what value is chosen only when a new proposal is chosen. Thus, we can repeat the [[#In Total|algorithm]]. 

## Progress
The above algorithm is not guaranteed to make progress. Two `proposers` can keep issuing proposals with higher and higher numbers, none of which are ever chosen. 

**Error Case**: `Proposer` $p$ can complete Phase 1 for proposal $(n_1, -)$. Another `proposer` $q$ then completes Phase 1 for proposal $(n_2, -)$ where $n_2 > n_1$. $p$'s $\texttt{accept}(n_1, -)$ will be ignored because the `acceptors` have already promised $q$ to ignore any proposal with number less than $n_2$. Thus, $p$ must begin issuing proposals $(n_3, -)$ where $n_3 > n_2$, causing $q$ to have its $\texttt{accept}(n_2, -)$ ignored, and so on.

To ensure progress, we need a **distinguished proposer** (denoted as `^proposer`) that is the only one allowed to issue proposals. If the `^proposer` can communicate successfully with a majority of `acceptors`, then it can ensure that some proposal is eventually chosen.

If enough of the system (`proposer`, `acceptors`, communication network) is working properly, liveness can therefore be achieved by electing a single `^proposer`. Now, we need an election to determine the `^proposer`.

## Implementation
All processes will play the above three roles. 
- The algorithm needs to choose a leader such that it is the `^proposer` and the `^learner`. 
- We need stable, persistent storage to store the highest proposal number an `acceptor` has accepted and the highest `prepare` request it has responded to, so that this information is not lost during failure and restart.
- An `acceptor` must store its data before responding to a `proposer`'s request.
- Now, we need to ensure that no two proposals are ever issued with the same proposal number. We can do this by having each `proposer` select proposal numbers from a disjoint set of natural numbers. 

# Implementing a State Machine
A simple way to implement a distributed system is as a collection of clients that issue commands to a central server. The server can be described as a **deterministic state machine** that takes a command as input and produces an output and a new state. 

> [!faq] Example
> The clients of a distributed banking system might be the tellers, and the state-machine state might consist of all the account balances of all users. A $\texttt{withdrawal}$ would be performed by executing a state machine command that decreases the account's balance iff the balance is greater than the withdrawal amount. The output is the new balance.

A single server is a single point of failure. We must use a collection of servers, each independently executing the same state machine. Because the state machine is deterministic, if all servers execute the same sequence of commands, they will all be in the same state and produce the same output. A client can then use any server to execute a command and get the output.

- We split up the Paxos algorithm into a sequence of separate instances. The value chosen in the $i^{th}$ instance is the $i^{th}$ state machine command in a sequence. 
- Each server plays all [[#^9a3922|three roles]] in each instance of the algorithm. 
- Assume the set of servers is fixed. 

In normal operation, a single server is elected to be the leader and acts as `^proposer` in all instances. 
- Given a client command $c$, the leader executes the Paxos algorithm to try and choose value $c$ in this instance. 
- Usually succeeds. 
- Failure can happen from a server failure.
- Failure can happen from another false leader.
- Failure can happen from a network partition.

Suppose the leader fails. The new leader, which is also the `^learner`, should know "most" (if not all) of the commands that have already been chosen. Suppose it knows ^1e38f0
$$
1, 2, 3, \ldots, 133, 134, \quad 138, 139
$$
That is, it knows what values were chosen in those instances and is missing the values chosen in instances $135, 136, 137$ and instances greater than $139$ (if any). 

Upon becoming the new leader, it must determine that the values it proposes does not violate `Prop 2b`. It will do this by executing **Phase 1** of the Paxos algorithm for instances $135, 136, 137$ and instances greater than $139$ (if any). The purpose of this is to check if the previous leader already accepted these values for these slots before it crashed.

Suppose that instances $135, 140$ had already been chosen and the rest (i.e. $136, 137, 138, 139$) had not (unconstrained). The values chosen in instances $135, 140$ CANNOT be changed. Since the new leader is free to propose any value in instances $136, 137$, in **Phase 2**, it will run $\texttt{accept}(136, \varnothing)$ and $\texttt{accept}(137, \varnothing)$ to indicate a special `no-op` command. 

Once these `no-op` commands are chosen, the new leader can execute commands $138, 139, 140$. At this point, commands $1-140$ have been chosen. It is now free to propose any value in **Phase 2** for all instances greater than $140$.

**Error Case**: The leader can propose command $142$ before it learns its proposed command $141$ has been chosen. It's possible all messages it sent in proposing $141$ were lost and $142$ is chosen before any server has learned about $141$. When the leader fails to receive a response, it will retransmit $141$. 

Suppose the leader could not get responses back for $141$, but is able to learn that proposals after $142$ are chosen. This creates a gap. In general, suppose we have $i$ chosen proposals, and the leader is allowed to be up to $\alpha$ commands ahead. I.e.
$$
\underbrace{
  1, 2, 3, \ldots, i-1, i
}_{i \text{ chosen instances}}
,
\underbrace{
  \underbrace{
    i+1, i+2, \ldots, i+j-1, i+j
  }_{j \text{ lost instances}}
  ,
  \underbrace{
    i+j+1, \ldots, i+\alpha
  }_{\text{chosen instances}}
}_{\alpha \text{ instances}}
$$
So, $j \leq \alpha - 1$, where $j$ is the gap of commands that are known to be not chosen. If the leader is alive, it will retransmit until it learns that $i+j+1$ is chosen.

Suppose this leader fails before it learns that $i+j+1$ is chosen. The new leader will be elected and will a very similar gap of commands as in [[#^1e38f0|this example]], and execute **Phase 1** for the empty slot (and then later **Phase 2**). 

Allowing gaps is a performance optimization. It allows the leader to continue proposing commands without waiting for the previous command to be chosen, which can be slow. 

The only time the system can move forward is if there is a leader. If there is no leader, the system cannot make progress and thus cannot become inconsistent. 

**Error Case**: Suppose the set of servers can change. We need to determine what servers implement what instances of the consensus algorithm. We solve this by making the servers part of the state machine itself. 

# HarpFS View Change via Paxos
In [[HarpFS]], the view change algorithm is left ignored. It requires some consensus of nodes to determine who is the leader. Although the original paper never explicitly mentions how they do this (or if they ever implementation leader election at all), we can implement it ourselves here. 

Each node must have some permanent storage where they persistent some data for Paxos.
- $n_{a}$: the highest proposal number this node has ever accepted.
- $v_{a}$: the value associated with the highest proposal number this node has accepted (initially $\varnothing$).
	- This is the proposal $(n_{a}, v_{a})$.
- $n_{\max}$: The highest proposal number this node has ever *seen* in a prepare request.
	- It is natural to say $n_{\max} \geq n_{a}$.
- $n_{\text{mine}}$: The highest proposal number this node has ever *issued* as a `proposer`.

We will also store some information relevant to HarpFS.
- $\texttt{VID\_max}$: The highest "view ID" this node has ever heard of.
- $\texttt{Views[]}$ array: An array indexed by View ID containing the set of member nodes in that view.
	- Doing this removes the need for the `learner`. 
	- The goal is to have this array grow monotonically, where each element is filled one by one with the members of that view. 
	- In any practical implementation, we need to perform garbage collection on this.
	- If a node crashes and comes back, then it will store know the highest view its ever seen.
- $\texttt{done}$: A Boolean indicating whether the node believes Paxos has decided on the current view (i.e., whether the `learner` role has finished).
	- If it is true, then we come to consensus and need to perform duties.
	- If it is false, it is not in a quorum (and does not imply there is not a quorum happening in the system). This node should then try to force a view change. 

## View Change
### Initialization
When a node decides to start a view change (e.g., because the primary is dead or it just joined), it must initialize a new instance of Paxos to become a proposer.
- Set $n_a = 0$, $n_{\text{mine}} = 0$, $n_{\max} = 0$.
	- We have not accepted any proposals yet.
	- We have not proposed anything yet.
	- We have seen no proposals yet.
- Set $v_{a} = \varnothing$ or $\bot$. 
	- We have not accepted and values. 
- The node decides it wants to lead Paxos and amasses a team.

### Phase 1: Prepare
The node acts as a `proposer` to prepare a proposal[^1]. In Harp, this means some node decided it wants to be the primary. It must choose a proposal number that is strictly greater than any it has seen or issued before.
- The `proposer` chooses $n_{\text{mine}} \leftarrow \max(n_{\text{mine}}, n_{\max}) + 1$.
- It updates $n_{\text{mine}} \leftarrow n$.
- It assumes the view is not chosen yet, so it sets $\texttt{done} \leftarrow \text{false}$.
- It broadcasts a $\texttt{prepare}(n_\text{mine}, \texttt{VID\_{max}} + 1)$ message to a quorum of nodes (e.g., the members of the last known view).
	- (Paxos number, reason to create new view)
	- We sent the max plus 1 to check if a view change has already happened. If it has happened, we can quit Paxos (because it is expensive) and they just need to be caught up. A leader has already been chosen. 
	- The $n$ ensures if anotheer node is running Paxos, we can compete with them (and so only one can win).

[^1]: Otherwise, no node is a `proposer` and the system does not move.

When an `acceptor` receives a $\texttt{prepare}(n, \texttt{VID})$ message, it performs the following checks:
1. **View ID Check**: If $\texttt{VID} \le \texttt{VID\_max}$, the `acceptor` short-circuits Paxos entirely. It replies with an $\texttt{oldView}(\texttt{VID}, \texttt{Views}[\texttt{VID}])$ message. This informs the `proposer` that the view has already been decided and Paxos is unnecessary. Otherwise, we begin Paxos.
2. **Fresh Proposal Check**: If $n > n_{\max}$, this is the highest proposal the `acceptor` has seen. 
   - It updates $n_{\max} \leftarrow n$.
   - It sets $\texttt{done} \leftarrow \text{false}$ (pausing its normal operations to participate in the view change).
   - It replies with $\texttt{prepare\_response}(n, n_a, v_a)$, indicating it joins the proposer's team and informs the proposer of the highest value it has already accepted (if any).
3. **Obsolete Proposal**: If $n \le n_{\max}$, the acceptor ignores the proposal or replies with a negative acknowledgment ($\texttt{reject}$/`NACK`). This serves as a performance optimization to let the proposer know it is behind.

As pseudocode,
```rust
// self := acceptor node
if let recv_prepare(n, VID) = self.recv():
	if VID <= self.VID_max:
		return oldView(VID, self.Views[VID])
	else if n > n_max:
		self.n_max = n
		self.done = False
		return prepare_response(n, n_a, v_a)
	else
		return reject()
```

This like the first round of [[Two Phase Commit|2PC]].
### Handling Prepare Responses
The `proposer` collects responses from the `acceptors`. (Recall from [[#^ed7f9a|this]]).
- **Receives $\texttt{oldView}(\texttt{VID})$**: The proposer learns that the view was already decided. It updates its history. If it is not part of this view, it must start a new view change for $\texttt{VID}$.
- **Receives $\texttt{reject}$/$\texttt{NACK}$**: This indicates a race condition where another proposer has a higher proposal number. 
	- To avoid increasing entropy and thrashing, the proposer "folds" and delays for some time to allow the other leader to finish. 
	- If the other leader fails to drive consensus to completion, the proposer will retry with a higher proposal number.
- **Receives $\texttt{prepare\_response}(n, v)$ from a majority**: The proposer successfully completes Phase 1. It must now pick the value $V$ to propose in Phase 2.
	- It is important we have a majority. Otherwise, another node who is preparing to be a leader may also think they will be a leader.
		- This node votes for itself.
	- It looks at all the returned $v_a$ values. 
	- If **any** $v_a \neq \varnothing$, the proposer **must** find the highest $n_a$ among all responses and choose the corresponding $v_a$. It has no free choice and is fated to drive the previous consensus attempt to conclusion (even if that view is obsolete or does not include this proposer).
		- This is just finding $\max_{v_{i}} \max_{(n_{i}, -)} H$ where $H$ is the set of proposals from the responders.
		- Otherwise, if $H = \varnothing$, then we can respond with whatever (from Paxos).
	- If **all** $v_a = \varnothing$, the `proposer` is the first to amass a quorum. It has free choice and can pick $V$ to be the new view (typically the majority of nodes that responded). 
		- For Harp, we must let $v_{a} = V := \text{everybody we heard from}$. This is useful 
		- Note: The `proposer` should delay slightly before choosing $V$ to ensure it doesn't leave out nodes whose responses arrive a fraction of a second later, which would immediately trigger another view change.
	- We need to ensure the $n$ it receives is not an old $n$, Indeed, it could be from the second branch here. If it's anything less than $n$, ignore it.
- We may not receive a majority of responses. We would just delay and restart Paxos.

In pseudocode, 
```rust
// self := leader node, the proposer that triggered a view change
if let recv_oldView(VID, vs) = self.recv():
	self.Views = vs
	self.VID_max = VID
	// from a harp perspective, we need to do a view change
	self.new_change()
	
	// this instance of Paxos failed, start a NEW paxos
	self.restart_paxos() 
	
else if recv_reject() = self.recv():
	// since we only want leader, if this node is "losing"
	// then it should immediately give up
	delay(?)
	// eventually we will receive a response from a "winner"
	// i.e. a new leader was chosen and join them 
	// we do the SAME paxos
	self.restart_paxos()

else if majority_prepare_responses():
    let (max_na, chosen_va) = find_max_na(responses)
    let V = if chosen_va != empty {
        chosen_va
    } else {
        delay_slightly_for_more_responses()
        form_view_from_responders()
    }
    broadcast(accept(self.VID_max + 1, n_mine, V))
```

> Cursed syntax `:(`

Importantly, at the end of this phase, only this node knows it is the leader. If it dies before sending `broadcast(accept())`, it's as if nothing has happened (since no evidence exists). At this point, another Paxos will start.

### Phase 2: Accept
The `proposer` (now leader) broadcasts an $\texttt{accept}(n, \texttt{VID}, V)$ message to everyone.

When an `acceptor` receives an $\texttt{accept}(n, \texttt{VID}, V)$ message:
1. **View ID Check**: If $\texttt{VID} < \texttt{VID\_max}$, the view has already been decided. The acceptor replies with an $\texttt{oldView}$.
2. **Stale Proposal Check**: If $n < n_{\max}$, the proposer is stale (another leader with a higher proposal number has emerged). The acceptor replies with a $\texttt{reject}$/$\texttt{NACK}$.
3. **Accept**: If $\texttt{VID} = \texttt{VID\_max}$ and $n \ge n_{\max}$, the acceptor officially accepts the value! It writes $n_a = n$ and $v_a = V$ to durable storage. It then replies to the proposer with an $\texttt{accept\_response}$.

### Phase 3: Decide
The `proposer` collects the $\texttt{accept\_response}$ messages.
- If it receives $\texttt{oldView}$ or $\texttt{reject}$/$\texttt{NACK}$, it handles them similarly to Phase 1 (updates state and steps down).
- If it receives $\texttt{accept\_response}$ from a **majority** of nodes: The value is officially chosen, because it has been written to durable storage on a quorum.
- The proposer broadcasts a $\texttt{decide}(\texttt{VID}, V)$ message to everyone to inform them the view is finalized.

When any node (acting as a `learner` for Harp) receives a $\texttt{decide}(\texttt{VID}, V)$ message:
1. It knows the view is finalized and sets $\texttt{done} = \text{true}$.
2. It updates its $\texttt{Views}$ array with the new view $V$ at index $\texttt{VID}$.
3. It exits Paxos and returns to running Harp with the new view.

## Generalizing to Other Systems
The idea is that whenever we have some system that uses a primary, or some coordinator, we want to store the epoch/age/era/"what node is alive, and when" in a Paxos value. Then, we'll need to store the history to ensure that **really old** proposers/nodes/participants who think the leader is someone else can be corrected. 