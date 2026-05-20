---
tags:
  - CSE_223B
---
# Group Communication
This note summarizes group communication protocols, focusing on the design, trade-offs, and mechanics of the ISIS Group Communication System developed at Cornell University in the 1980s.

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
- **Total Wall Clock Ordering**: All messages are ordered strictly by the physical time they were sent. (Extremely difficult to achieve precisely in distributed systems due to clock drift).
- **[[Memory Coherence#Definition (Sequential Consistency)|Sequential Consistency]] (Total Order)**: All nodes deliver all messages in the *same* sequence, but this sequence does not necessarily correspond to physical wall-clock time.
- **Causal Ordering**: Respects the "happens-before" ($\to$) relationship. If message $m_1$ causally influenced[^1] the sending of $m_2$, then $m_1$ must be delivered before $m_2$ at all destinations. Unrelated (concurrent) messages do not have a defined order, which allows for parallel processing.
  
  [^1]: Message $m_1$ causally influences $m_2$ if the sender of $m_2$ had already sent or received $m_1$ (directly or transitively) before generating $m_2$ (i.e., $m_1 \to m_2$ via Lamport's happens-before relation).
- **Causal Total Ordering**: Combines both causal and total ordering guarantees. This can be achieved by layering ABCAST on top of CBCAST. Uses [[Vector Timestamps]] to track causality.

# CBCAST (Causal Broadcast)
CBCAST guarantees that messages are delivered respecting causal relationships. 

## Mechanics & Rules
Every node maintains a local message buffer (FIFO queue). To satisfy causal consistency:

1. **FIFO Sender Order**: Messages sent by a specific node must be delivered in the order they were sent.
   - *Implementation*: A node maintains a FIFO queue of outgoing messages. When connecting to another node via TCP, it sends the entire queue from the beginning. If the connection drops, it restarts transmission from the beginning of the queue, discarding duplicates at the receiver (idempotency).
1. **Transitive Causality**: If a node receives a message $m$ and subsequently sends message $m'$, then any node receiving $m'$ must deliver $m$ before $m'$.
   - *Implementation*: When a node receives a message, it appends it to its local queue. Thus, when it talks to another node, it transmits not only its own messages but all messages it has "heard" so far. The "so far" is explicitly the "happens-before" relation. 

```
Example Buffer Queue containing locally generated and transitively heard messages:
+----+----+----+----+----+----+----+
| B1 | A4 | C1 | A3 | A2 | A1 | ...| <-- Front of Queue (sent first)
+----+----+----+----+----+----+----+
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
Messages are placed in the queues with temporary proposed sequences. Sequence number tuples are in the format `seq.node_id` (e.g., `2a` represents sequence number 2 proposed by node A).

```
[Queue End]                                          [Queue Front]
    v                                                      v
A:  b(2a) [Undeliverable]    |   a(1a) [Undeliverable]
B:  a(2b) [Undeliverable]    |   b(1b) [Undeliverable]
C:  b(2c) [Undeliverable]    |   a(1c) [Undeliverable]
```

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