---
tags:
  - CSE_223B
---
# Background
In the 1980s, there was no Ethernet, no [[WiFi PHY|WiFi]], or LAN to talk to other machines. There were some parallel applications, but back then there were no multi-core machines, so all processors existed on multiple systems at once. 

Your (or a client machine) would want to work on data not present on the physical machine. 

**Ivy** broke this into two parts:
1. Figuring out where the memory is located (which processor). 
	1. **Manager**: figures out where the memory is right now. Once the memory is local to you, you can access it. (Took ownership of the page when local). 
	2. If Management was also there, then management node would keep on moving (not ideal). 
2. [[Memory Coherence#Definition (Locality of Reference)|Locality]]/Moving Memory to your processor

# Ivy Requirements
The Ivy system required a few invariants to be present during all operations at all times. 
1. At most only one one owner at a time per page. This is the source of truth.
2. The page owner is the only node that can write to the page.
3. Every node has potential access to every page in the global virtual address space. 

In an effort for [[Memory Coherence#Definition (Memory Consistency)|memory consistency]], Ivy tries to enforce this by creating a **total ordering** over owner periods by giving each ownership a sequence number. So, every write is done in order. Locks are needed for consistency. 

# Algorithm
In Ivy, one node is designated the **manager**. The manager is responsible for keeping track of the ownership of pages. Any page has an authoritative copy, which is always held by the owner of the lock for that page. If the owner dies (fails), and there is no existing copy, the writes are lost. The core of Ivy is the **fault handler**[^1], which is responsible for handling page faults by fetching the page from the current owner and transferring ownership to the requesting node over the network.

[^1]: Ivy lives in the kernel.

We have a few scenarios.
1. **Local Read**: If the processor requests a page that already exists in the cache, then it will copy it over. 
2. **Remote Read**: If the page does not exist locally (i.e. it is not the Owner of the page), we trap to the Page Fault Handler and ask the manager for read access of the page. The manager must receive confirmation of reception to maintain the ordering.
3. **Local Write**: Ivy does nothing. This is fast because of locality. 
4. **Remote Write**: We immediately fault because the page table entry says it is `readonly`. We ask to acquire the lock from the manager and use the copyset to invalidate the page on every other node (Broadcast Shootdown). Once all nodes have invalidated their cache, ownership is transferred to the requester. 

> [!info] Implementation Details
> - **Priority**: Handlers operate with high priority within the kernel.
> - **Latency**: IVY is a bare-bones, on-demand system. It does not move pages proactively or perform preprocessing to reduce latency.
> - **Serialization**: The Manager serializes all requests to maintain consistency.

# Improved Algorithms
To address the performance bottlenecks and network overhead of a centralized manager, Ivy introduced dynamic management schemes.

### Metadata Migration (Let Metadata Follow the Page)
Instead of a central manager keeping all metadata, the metadata (such as the `copyset`) travels with the page itself. The Page Table Entry (PTE) of the current owner holds the `copyset`.
- **Benefit**: This significantly reduces the total number of network messages required for synchronization.
- **Serialization**: The "goalpost" for serialization shifts from the central manager to the current owner. In a race condition between concurrent requests, the first request to reach the owner wins.

### Distributed Manager Schemes
A centralized manager can become a bottleneck and create high latency if it is physically distant from the nodes actively reading or writing the page. This can lead to a single point of congestion in the network. The solution is to distribute the management responsibility across the network. The current owner of the page acts as its manager.

However, because ownership changes dynamically, the manager for a given page is constantly moving. Any node could be the owner at any given time, making the page harder to track. Nodes can then have a "Probable Owner" hint to help route requests to the current owner. They point from one node to the next, creating a chain of probable owners (like [[Chord]]!). If this chain is broken, a broadcast is used to find the current owner.

---
Thank you to Samvrit for lending me his notes for Ivy.
