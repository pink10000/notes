---
tags:
  - CSE_223B
---
# Consensus
Consensus is the fundamental problem of **agreement** in distributed systems. If a system can achieve consensus, it can build arbitrary coordinated structures (like replicated state machines). Conversely, without consensus, distributed coordination is impossible.

Consensus is also very expensive. We want to perform consensus as infrequently as possible.
# Consensus vs. Other Protocols
To understand consensus, it is helpful to compare it to other distributed paradigms:
- **Two-Phase Commit (2PC)**: In [[Two Phase Commit|2PC]], nodes are authoritative for their own sub-tasks (e.g., debit vs. deposit). Each node decides if its part succeeded, and the coordinator merely aggregates these votes. In contrast, in consensus, no single node is authoritative; the decision is entirely a collective group choice. Thus, 2PC is *strictly easier* than consensus.
- **Replicated State Machines (RSM)**: RSMs look like consensus because all nodes execute the same operations, but a naive primary-backup RSM is *not* consensus. 
	- The primary is the **sole authority**: clients propose actions and the primary decides their *ordering* (i.e., which value goes into which log slot), while backups are passive followers with no say in that decision. 
	- There is no agreement being made.
	- We can implement RSM *with* Consensus, (and this is what happens in the last part of [[Paxos Algorithm|Paxos]]). 
- **Primary-Backup Replication**: Standard primary-backup (such as in [[Replication]]) centralizes all decision-making. The primary serializes and orders client requests, while backups act as passive followers. Centralization is highly efficient for day-to-day operations. However, if the primary fails, selecting a new primary requires consensus.
- **View Change**: In systems like [[HarpFS]], the "view change" protocol is where consensus is required. The system must agree on the next view and its primary to prevent "split-brain" (where multiple nodes believe they are the primary and diverge).
	- The easiest way to do this, was in a group of potential leaders, we simply select the node with the lowest ID. 
	- We could also select the node that was the leader in the previous view.
- **[[Frangipani]]**: The magic of Frangipani is that the lock manager is how the system determines who gets the lock for a particular file. 
	- Why does the lock manager require conensus? Every node needs to agree that one particular server/agent/node/processor is acquiring a lock for a file, so that only that particular entity can read/write to that file.
	- At the end of the day, the set of nodes need to *agree* on some decision. 

# Why Consensus is Hard
Consensus must operate under realistic network and node assumptions:
- **Node Failures**: Nodes can crash at any time.
- **Asynchronous Networks**: Messages can be arbitrarily delayed, lost, or reordered. It is impossible to distinguish a crashed node from a slow node.
- **Split Brain**: If we design our algorithm poorly, we could have two indepdendent nodes who think they both are the leader. 
	- It is fine if any individual node does not know who the leader is. This is because it does not have a *wrong* answer, only that has *no* answer.
	- Additionally, if it does not know who, then the node itself cannot be a leader, and thus cannot serve client requests, keeping the system consistent. 
- **FLP Impossibility**: In a fully asynchronous network with even a single unannounced node failure, deterministic consensus is impossible to guarantee in bounded time.
	- [Paper](https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf). It says that a deterministic algorithm for achieving consensus is impossible. 
- **Roommate Dinner Analogy**: Similar to deciding on dinner via text messages in an asynchronous network: if a roommate is slow to respond, you must eventually decide without them. But you must ensure everyone eventually agrees on what was decided (avoiding different subsets of roommates having different dinners).

# Overcoming Partitioning: Quorums
To make progress despite node failures and delays without waiting indefinitely:
- The system makes decisions once it receives responses from a [[Quorum]] (typically a simple majority, e.g., $\lfloor N/2 \rfloor + 1$).
- Because any two majorities of a set must overlap by at least one node, the overlapping node acts as a bridge of information, preventing split-brain partitioning.

# Changing Minds vs. Equivocation
To handle failures, nodes must be allowed to change their mind (e.g., if a proposer crashes before finishing, a new proposer must take over). However, nodes cannot change their mind arbitrarily without risking split-brain.
- Suppose we said no nodes can change their mind. When a proposal is made, that proposal cannot be changed. But if the original proposer dies (or does not respond in bounded time), the system is stuck. 
- **The Rule**: A node can change which proposer (or "team") it follows, but it cannot change a *value* once it has accepted it.
- If a node has already accepted a value, it must report this to any new proposer. The new proposer is then forced to adopt that existing value rather than proposing its own.

