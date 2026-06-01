---
tags:
  - CSE_291G
  - CSE_127
---
# CAP Theorem
The **CAP Theorem**, also known as **Brewer's theorem**, **Brewer's law**, or **Brewer's conjecture**, states that it is impossible for a distributed system to simultaneously provide more than two out of the following three guarantees:

- **C**onsistency: Every read receives the most recent write or an error. (Often managed via [[Consensus]] algorithms or [[Quorum]] reads).
- **A**vailability: Every request receives a (non-error) response, without the guarantee that it contains the most recent write.
- **P**artition tolerance: The system continues to operate despite an arbitrary number of messages being dropped (or delayed) by the network between nodes.

In the presence of a network partition (which is practically inevitable in distributed systems), you must choose between Consistency (CP) and Availability (AP).

# ACID
ACID represents a pessimistic approach to data consistency. It prioritizes data integrity and correctness above all else, ensuring that an operation is an all-or-nothing event that leaves the system in a valid state.

- **A**tomicity: Operations are "all or nothing." If any part of the operation fails, the entire operation is rolled back, leaving the system unchanged. (In distributed systems, this is often implemented via [[Two Phase Commit]] or similar protocols).
- **C**onsistency: Any operation will bring the system from one valid state to another. It must adhere to all defined invariant rules.
- **I**solation: Concurrent execution of operations leaves the system in the same state that would have been obtained if the operations were executed sequentially.
- **D**urability: Once an operation has successfully completed, its effects will remain, even in the event of power loss, crashes, or errors.

**Use Cases:** Financial systems, banking, inventory management, or anywhere you absolutely cannot afford data anomalies or partial transactions.

# BASE
BASE represents an optimistic approach. It relaxes the strict consistency of ACID in favor of high availability and scalability, which are critical in large distributed systems.

- **B**asically **A**vailable: The system guarantees availability. There will be a response to any request (success or failure), even if there is a partial system failure.
- **S**oft State: The state of the system could change over time, even without input. This is because updates might still be propagating through the network.
- **E**ventually Consistent: The system will eventually become consistent once it stops receiving input. Given enough time, all nodes will receive the latest updates. (Systems often use structures like [[CRDT]]s or [[Vector Timestamps]] to resolve conflicts).

**Use Cases:** Social media feeds, analytics, content delivery networks, or situations where it's acceptable if users see slightly stale data as long as the system remains fast and responsive.
