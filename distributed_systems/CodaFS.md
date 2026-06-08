---
tags:
  - CSE_223B
---
# Overview
The primary contribution of **CodaFS** was that *caching of data* (primarily used for performance), can be exploited to improve [[Networked File Systems#Definition (High Availability)|availability]]. It builds on top of [[Networked File Systems|NFS]], mitigating file system failures. 

CodaFS wanted to allow access to an NFS while disconnected. Actions made during this state are called **disconnected operations**, a temporary deviation from normal operation as a client of a shared repository. 
- 1-2 days of disconnect
- optimized for access and sharing, not for highly concurrent, fine granularity data access
- clients say Coda as a single, location transparent shared Unix file system 
- The entire namespace is mapped to to individual file servers at the granularity of subtrees called **volumes**.
- At each client, a **cache manager** (Venus) dynmically obtains caches volume mappings. 
- **Server replication** is used for better access.
	- **Volume Storage Group (VSG)**: set of replicated sites
	- **Accessible VSG (AVSG)**: subset of what the client can access
	- When a cached copy is no longer valid, the notification to do so is called a **callback break**. ^3ce6c6
- Cache [[Memory Coherence#Definition (Memory Coherence)|coherence]] protocol based on *callbacks*, ensuring an open file is the latest copy in the AVSG.
	- Modifications propagate through all AVSG sites, then VSG sites. 
- Involuntary disconnects are functionally the same as voluntary disconnects.

When AVSG is empty, disconnected operation begins working. Venus services file system requests via its cache. Cache misses cannot be serviced nor masked, so to the user, they are reported as failures. When disconnection ends, Venus propagates modifications and reverts to server replication. 

# Replication Hierarchy
First Class:
- more persistent
- widely known
- secure
- available
Think of them as good public utilities

Second Class:
- cache copies on clients
- inferior among all above
- periodic revalidation to 1st class makes 2nd class useful

cache coherence combines performance and scalability advantages of a 2nd class with the quality of a 1st class. 

[[Replication]] 
- preserves quality of data. 
- expensive hardware wise

Disconnected operation 
- forsakes quality for availability.
- cheap
- can be exclusively relied on 

## Replica Control
Pessimistic
- avoids conflicting operations by disallowing all partitioned writes or by restricting reads/writes to a single partition.
- client needs to acquire exclusive control
	- allwos reading at other clients, but writes forbidden everywhere
	- voluntary = easy, involuntary = hard
- retaining control is acceptable on brief disconnects, but on extended periods, the entire user community as at the mercy of a single errant client for an unboudned amount of time
- Use **leases** for a time bound for exclusive/shared control.
	- but defeats the purpose of disconnected operation
	- updates during disconnect would need to be discarded


Optimisitc
- higher availability by allowing reads/writes everywhere
- conflicts will happen, either disconnect-server, disconnect-disconnect
- deals with conflicts by detecting and resolving them after their occurrence
	- manual resolution violates transparency (seamless integration of high availability to a normal Unix environment)
	- annoying, reduces usability

CodaFS chose optimistic because ^0d7f29
- they belived writes were rare
- uniform model of the system from the user perspective.
### Whole-File Caching
A cache miss can only occur on an `open`, never on a `read`, `write`, `seek`, or `close`. This substantially simplifies the implementation of disconnected operation. 

# Client Strucutre
Venus is a user-level process because of its complexity. Venus intercepts Unix calls via the Sun Vnode interface. Since this interface is slow, it talks to the **MiniCache** which filters out many kernel-Venus interactions. This services the syscall (if possible). Otherwise, it delegates it to Venus and control is returned to the application (which may contact other Coda servers).
```tikz
\usepackage{tikz}

\begin{document}
\begin{tikzpicture}[>=stealth, font=\sffamily, thick]

% --- 1. Background/Kernel Box ---
\draw (0.5, 0.5) rectangle (9.5, 5.0);
\draw (0.5, 4.4) -- (9.5, 4.4);
\node at (5, 4.7) {System Call Interface};

% --- 2. Application and Venus Boxes (Top Level) ---
\node[draw, fill=white, rounded corners=12pt, minimum width=2.4cm, minimum height=4.0cm, align=center] (app) at (1.8, 7.0) {Application};
\node[draw, fill=white, rounded corners=12pt, minimum width=3.6cm, minimum height=3.0cm, align=center] (venus) at (7.0, 6.5) {Venus};

% --- 3. Kernel Nodes ---
\node[draw, fill=white, minimum width=3.2cm, minimum height=0.6cm, inner sep=3pt] (vnode) at (2.5, 3.2) {Vnode Interface};
\node[draw, fill=white, minimum width=3.5cm, minimum height=0.8cm, inner sep=3pt] (minicache) at (6.5, 1.5) {Coda MiniCache};

% --- 4. Left Side Arrows (Application -> Vnode -> MiniCache) ---
% Downward arrow (App -> Vnode)
\draw[->] ([xshift=0.3cm]app.south) -- ([xshift=-0.4cm]vnode.north);

% Downward arrow (Vnode -> MiniCache)
\draw[->] ([xshift=0.5cm]vnode.south) -- ([xshift=-1.2cm]minicache.north);

% --- 5. Right Side Arrows (Venus <-> MiniCache) ---
% Downward arrow (left side, bulging left)
\draw[->] ([xshift=-0.5cm]venus.south) to[bend right=15] ([xshift=-0.5cm]minicache.north);
% Upward arrow (right side, bulging right)
\draw[->] ([xshift=0.5cm]minicache.north) to[bend right=15] ([xshift=0.5cm]venus.south);

% --- 6. External Network Arrow ---
\draw[->] (venus.east) -- ++(1.5,0) node[right, align=center, font=\sffamily\itshape] {to Coda\\servers};

\end{tikzpicture}
\end{document}
```

Venus operates in three states:
- hoarding
- emulation
- reintegration
```mermaid
graph TD;
	h[[Hoarding]] --Disconnection--> e[[Emulation]]
	e --Physical Reconnection--> r[[Reintegration]]
	r --Logical Reconnection--> h
```
Venus is normally in the hoarding state, relying on [[#Replication Hierarchy|replication]] but always on alert for possible disconnection. Upon reconnection, it reintegrates, updating the AVSG, then reverts to hoarding when done. 

## Hoarding
The key responsibility of Venus is to hoard usefaul data in anticipation of disconnection. It needs to also manage its cache that balances the needs of connected and disconnected operation. Many factors complicate implementation
- file reference behavior
- disconnections and reconnections are unpredictable
- trust cost of a cache miss while disconnected is highly variable 
- activity at other clients must be accounted for
- cache space is finite, so may have to sacrifice less critical objects

Per-workstation **hoard database (HDB)** is used to identify files of interest. A **hoard profile** is used to determine which files are stored. **Hoard priority** is used to determine the priority of certain objects. All ancestors of an object will also be cached (like a directory).

We say a cache is in **equilibrium** when the user can expect its cache to be available, and non uncached object has a higher priority than a cached object (may be disturbed as a result of normal activity). Venus periodically restores equilibrium via an operation known as **hoard walking**. 
- portable machines means the user is better at augmenting cache management for disconnected operation.
- occurs every 10 minutes
- can be required on voluntary disconnection
- Phase 1: name bindings of HDB entries are reevaluated to reflect update activity at other clients
	- New children may have been created in a directory whose pathname is specified with the `+` option in the HDB. 
- Phase 2: Priorities of all entrie in the cahce and HDB are reevaluated, and objects are fetched/evicted to store equilibrium.
- Hoard walks address [[#^3ce6c6|callback breaks]].
	- In traditional callback-based caching, data is refetched on demand after a callback break. 
	- In Coda, this may result in a critical object being unavailable should disconnection occur before the next reference to it.
	- Refetching immediately solves this problem, but ignores how modified things are typically modified many more times in a short interval. 
	- Thus, this would increase traffic, reducing scalability. 
	- Balance on availability, consistency, and scalability by purging and refecting it {on demand, during next hoard walk} whichever occurs earlier.
	- Directories are not purged, but *marked suspicious*. 

## Emulation
This occurs on disconnect. Venus performs many actions normally handled by servers. Generates temporary **file identifiers (fids)** for new objects, pending assignment fids on reintegration. Cache managemtn is done with the same priority algorithm during [[#Hoarding]]. Cache entries of deleted objects are freed immediately, but modified objects get infinite priority to ensure deletion does not happen.  ^b0fc4c

Venus keeps a **replay log** to replay update activity on reintegration. During a `write` and `close`, since Venus uses [[#Whole-File Caching]], it installs a completely new copy of a file, storing a single record in the log, `store`. Venus discards previous `store` records when a new one is appended because all previous versions of a file are "superflous" (what does this mean?). It merely points to the copy in the cache. 

On disconnect, the user must be able to restart (clearing RAM) without losing data, so the data must persist to disk. Venus stores metadata 
- cached objects of all types, logs, HDB is stored to **recoverable virtual memory (RVM)**
- The actual content is stored in disk, only metadata is in RVM.
Transactions are used to manipulate metadata (operations have a clear defined start and end, so we never leave the system in an incoherent state). 

## Reintegration
This is when the client reconnects. Venus needs to replay the log and the server log to catch up its AVSG. 

First, the systems propgates changes by
1. Venus obtains permanent fids for new objects and uses them to replace temporary fids in the replay log. 
	1. Typically avoided in many cases since Venus obtains a small set of permanent fids in advance during [[#Hoarding]].
2. The replay log shipped in parallel to the AVSG, and executed independently of each member. Each server peforms the replay within a single transaction (to ensure coherence) and aborts if any error is detected. 

Then, it executes the replay algorithm by:
1. The log is parsed, a transaction is begun, and all objects referenced in the log are locked. ^2470da
2. Each operation in the log is validated and then executed. ^335b24
	1. Validation consists of conflict [[#Replica Control|detection]], integrity protection, and disk space checks. Except in `store` operations, execution during replay is identical to execution in connected mode. 
	2. For a `store`, the an empty *shadow file* is created, and metadata is updated to reference it, but transfer is deferred. 
3. Data transfer is done for `store`. Known as **back-fetching**. 
4. The transaction commits, and the [[#^2470da|locks]] are released.

If reintegration succeeds, the replay log is freed and the [[#^b0fc4c|priority of cached objects]] are reset.

### Conflict Handling
Use of [[#^0d7f29|optimistic]] replica contorl means that we can have conflicts with other disconnected clients. In particular, more care needs to be had for `write`/`write` conflicts. Each replica of an object is tagged with a **storeid** that uniquely identifies the last update to it. During [[#^335b24|phase two]] of replay, a server compres the storeid of every object mentioned in a log entry with the storeid of its own replica of the object. 

If comparison indicates equality for all objects, the operation is performed and the mutated objects are tagged with a new storeid specified in the log entry. 

If the storeid comparison fails, the action taken depends on the operation being validated. 
- In the case of `store` of a file, the entire reintegration is aborted. 
- For directories, a conflict is declared only if a newly created name collides with an existing name.
	- If an object updates at the client or the server has been deleted by the other, or
	- if directory attirubtes have been modified at the server and the client

# Avoidance of System-Wide Rapid Change
They rejected strategies that require election or [[Consensus|agreement]] by large numbers of nodes. 

