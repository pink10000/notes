---
tags:
  - CSE_223B
---
# Replicated State Machines and Distributed Transactions

In distributed systems, we want multiple nodes to maintain the same state, providing the same robustness and atomicity as a single system (like a [[Quorum]]). For any event across the system, we must be able to definitively answer:
* Did it happen or not? (Purely yes or no)
* When did it happen?
* Where did it happen?

## Example 1: Roommates and Rent
Consider transferring money to pay rent. You want to ensure:
1. You transfer the money exactly once.
2. Your roommate actually transfers the money to the landlord.
3. The amount is correct.
4. The roommate successfully receives the money (it is not lost in transit).

In a distributed system, there can be an arbitrary number of "roommates" (nodes). Actions should only be executed if the entire system can execute its respective part.

# Definition (Transactions) 
A **transaction** is a sequence of operations that must be executed atomically. Either all operations in a transaction occur, or none of them do. 

# Definition (Coordinators)
To decide on transaction states and enforce total ordering, the system requires a **Coordinator**. The coordinator is a third party whose job is to arbitrate and ensure all participants in the system are on the same page.

## Example 2: The Banking System and The Halfway State
Suppose we have two banks, Bank A and Bank B, coordinated by Coordinator C. A client requests to transfer $5 from Bank A to Bank B. 

If C simply orders A to withdraw $5 and orders B to deposit $5, network failures create inconsistent states:
* **Money in Limbo:** C tells A to withdraw, A does it, but C crashes before telling B to deposit. 
* **Printed Money:** C tells B to deposit, B does it, but A crashes before withdrawing.

Even if A and B send an `ack` (acknowledgement) upon completion, problems persist. If C receives an `ack` from A but not B, the system is still broken. We must solve for correctness first, then optimize for performance.

## The Solution: Promises and Two-Phase Commit
Instead of immediately ordering the transaction, the coordinator must verify that all conditions are met across all nodes. This is done by extracting a "promise" in two distinct phases.
### Phase 1: The Prepare Message
Coordinator C sends an advance warning (a `prepare` message) to A and B. This is not an order, but a request: 

> I am getting ready to execute a transaction. If I decide to ask you to execute, will you be able to?

* A and B check their local state (e.g., A checks if the account actually has $5).
* If a node says **YES**, it is making a *binding promise*. It locks the required resources and guarantees it can execute the transaction if requested.
* If any node says **NO**, C cancels the proposed transaction.

### Phase 2: The Commit Message
Because C is the only node that knows the state of all peripherals, it makes the final decision.
* If both A and B reply **YES**, C decides the transaction will proceed and sends a `commit` message.
* A and B execute the transaction and release their locks.

## Example 3: Bank Failures and Logs
Nodes can disconnect or fail at any point, leading to ambiguity. For example, Bank A might crash after making its promise in Phase 1, but before receiving the final `commit` or `abort` decision from C in Phase 2.

Because there is no evidence A actually executed the transaction yet, an "undo" operation is unnecessary. Instead, when A comes back online, it must ask C if the transaction was ultimately committed. This implies both parties must keep **logs**.

### Managing the Logs
* **The Participant's Log:** A and B must keep track of their pending promises. When they reboot, they check their log for these pending promises and ask C for the final verdict.
* **The Coordinator's Log:** C only needs to keep a log of **committed** transactions. 
    
If C is waiting on a disconnected node (Bank B), it will hold the transaction pending. If the client tries a new, conflicting transaction (like withdrawing money from Bank A again), C must decide whether to abort the new transaction or the pending one. C does not need to store pending or aborted transactions in its permanent log; if a recovering node asks about a transaction that is not in C's log, C knows it was never finalized and simply tells the node to ignore/abort it.