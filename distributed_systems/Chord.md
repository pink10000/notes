---
tags:
  - CSE_223B
---
Based off of this [paper](https://dl.acm.org/doi/pdf/10.1109/TNET.2002.808407). 

# Chord Overview
The question on peer-to-peer (different machines talking to each other) is how to find something after we stored it. The goal is to efficiently find the location of the node that stores a desired data item. **Chord** is a protocol to map keys to nodes in a peer-to-peer network and also handles network changes (nodes joining and leaving).

> Effectively a distributed `HashMap<Key, Node>`, but with nodes instead of buckets. This is hard because the set of things to be stored and the number of nodes is unknown and can change at all times.

# Consistent Hashing
Consistent hashing is a technique to assign keys to nodes in a distributed system such that the assignment is resilient to changes in the system (e.g., nodes joining or leaving). The main idea is to hash both the keys and the nodes into the same identifier space, and then assign each key to the node that is closest to it in the identifier space. This way, when a node joins or leaves, only a small number of keys need to be reassigned.

Consider a $2^m$ id space, giving us $[0, 2^m - 1]$ range of integer identifiers. We have a hash function $H(x) \to [0, 2^m - 1]$ that takes in any string and maps it to an integer in this range. A good hash function should be evenly distributed and should not be easily reversible (i.e., it should be a cryptographic hash function). 

Imagine a large circle with $2^m$ nodes on it labeled from $0$ to $2^m - 1$. Each node is responsible for the keys that hash to a value between itself and the next node in the circle. For example, if we have nodes at positions $u$ and $v$ (where $u < v$), then the node at position $v$ is responsible for all keys that hash to values in the range $(u, v]$, i.e. 
$$
\forall x \in \text{Keys}, \text{ if } H(x) \in (u, v] \text{ then } x \text{ is stored at node } v
$$ 

<!-- When a new node joins the system, it takes over responsibility for some of the keys from its successor node. When a node leaves the system, its successor node takes over responsibility for its keys. This way, only a small number of keys need to be reassigned when nodes join or leave, making the system scalable and efficient. -->

> If we picked two nodes uniformly at random, the [[Expectation|expectation]] is that they are "half way" across the circle, meaning their distance is $2^m / 2$. This is because the nodes are evenly distributed around the circle, so on average, any two nodes will be about half the circle apart.

# Mechanics

Chord implements [[#Consistent Hashing|consistent hashing]] to efficiently manage the mapping of keys to nodes in a distributed system. What happens when a node leaves the system? The node's successor takes over responsibility for the keys that the leaving node was responsible for. 

Since on average, nodes are evenly distributed around the circle, each node is responsible for approximately $1/2^m$ of the keys. This means that when a node leaves, only $1/2^m$ of the keys need to be reassigned (this is negligible when $m$ is large).

## Storage and Message Complexity
If every node knew about every other node in the system, then the storage complexity would be $O(n)$, where $n$ is the number of nodes. At minimum, every node must know itself, so $O(1)$. 

In the first case, every node having knowledge of every other node allows for efficient routing, as each node only needs $1$ message to find the node responsible for a key, giving a message complexity of $O(1)$. In the second case, where each node only knows about one other node, the message complexity can be as bad as $O(n)$ in the worst case, but on average, it would be $O(n/2)$ due to the random distribution of nodes.

**Chord** optimizes both storage and message complexity to be sublinear, specifically $O(\log(n))$. Each node maintains a "finger table" that allows it to efficiently route messages to the correct node responsible for a key. In particular, each node only knows about nodes that are a power of 2 away from it in the identifier space. For example, node $k$ would know about the nodes 1,2,4,8, etc. positions away from it, which allows it to quickly narrow down the search for the node responsible for a key.

## Finger Table
Each node maintains a finger table that allows it to efficiently route messages to the correct node responsible for a key. The finger table is a data structure that contains information about other nodes in the system, specifically those that are a power of 2 away from the current node in the identifier space, with exactly $m$ entries. 

# Join Algorithm
When a new node joins the system, it needs to find its successor node and update the finger tables of existing nodes to reflect the new node's presence. The join algorithm is designed to be efficient and minimize the number of messages required to integrate the new node into the system. The new node will first contact an existing node in the system to find its successor. It will then update its own finger table and notify other nodes to update their finger tables as well. This process ensures that the new node is properly integrated into the system and that the routing of messages remains efficient.

How do we know when a node has joined the system? The exact moment a node joins a Chord ring is when a new node decides that another node is part of its successor.