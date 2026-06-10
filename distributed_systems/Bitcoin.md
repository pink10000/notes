---
tags:
  - CSE_223B
---
# Overview
**Bitcoin** is a purely peer-to-peer version of electronic cash that allows online payments to be sent directly from one party to another without going through a financial institution. It solves the inherent weaknesses of the trust-based model and the **double-spending problem** by relying on cryptographic proof rather than trusted third parties. 

# Transactions
An electronic coin is defined as a **chain of digital signatures**. Each owner transfers the coin to the next by digitally signing a hash of the previous transaction and the public key of the next owner. A payee can verify the signatures to verify the chain of ownership. 

The idea is that 
- public keys are used to receive bitcoins
- private keys are used to sign and spend bitcoins

To prevent double-spending without a centralized mint, transactions must be publicly announced, so that all transactions are aware. Participants need a system to agree on a single history of the order in which they were received.
# Timestamp Server
A distributed timestamp server works by taking a hash of a block of items to be timestamped and widely publishing the hash. Each timestamp includes the previous timestamp in its hash, forming a chain, with each additional timestamp reinforcing the ones before it.

# Proof-of-Work
To implement a distributed timestamp server on a peer-to-peer basis, Bitcoin uses a **Proof-of-Work (PoW)** system similar to Adam Back's Hashcash.
- PoW involves scanning for a value (a **nonce**) that, when hashed with SHA-256, begins with a certain number of zero bits.
- The average work required is exponential in the number of zero bits, but can be verified by executing a single hash.
	- Once the CPU effort has been expended to satisfy the PoW, the block cannot be changed without redoing the work (and the work of all blocawq`s chained after it).

**One-CPU-One-Vote**: Proof-of-work solves the problem of determining representation in majority decision making. The majority decision is represented by the **longest chain**, which has the greatest proof-of-work effort invested in it. As long as honest nodes control a majority of CPU power, the honest chain will grow the fastest and outpace competing chains.
- Difficulty is adjusted automatically using a moving average targeting an average number of blocks per hour.

# Network
The steps to run the network are:
1. New transactions are broadcast to all nodes.
2. Each node collects new transactions into a block.
3. Each node works on finding a difficult proof-of-work for its block.
4. When a node finds a proof-of-work, it broadcasts the block to all nodes.
5. Nodes accept the block only if all transactions in it are valid and not already spent.
6. Nodes express their acceptance of the block by working on creating the next block in the chain, using the hash of the accepted block as the previous hash.

# Incentives
By convention, the first transaction in a block is a special transaction that starts a new coin owned by the creator of the block. 
- This adds an **incentive** for nodes to support the network and provides a way to initially distribute coins into circulation (analogous to gold miners adding gold to circulation).
- The incentive can also be funded with **transaction fees** (the difference between the output value and input value of a transaction).
- Incentives encourage nodes to stay honest, as an attacker would find it more profitable to play by the rules and generate new coins than to undermine the system.

# Reclaiming Disk Space and SPV
- **Merkle Trees**: Once the latest transaction in a coin is buried under enough blocks, spent transactions can be discarded to save disk space. Transactions are hashed in a Merkle Tree, with only the root included in the block's hash. Old blocks can be compacted by stubbing off branches.
- **Simplified Payment Verification (SPV)**: A user can verify payments without running a full network node. They only need to keep a copy of the block headers of the longest PoW chain and obtain the Merkle branch linking the transaction to the block it was timestamped in.

# Combining and Splitting Value
To allow value to be split and combined, transactions contain multiple inputs and outputs. Normally there will be either a single input from a larger previous transaction or multiple inputs combining smaller amounts, and at most two outputs: one for the payment, and one returning the change back to the sender.

# Privacy
Privacy is maintained by breaking the flow of information: **public keys are kept anonymous**. The public can see that someone is sending an amount to someone else, but without information linking the transaction to a specific real-world identity. A new key pair should be used for each transaction to keep them from being linked to a common owner.

# Security
The race between the honest chain and an attacker chain is characterized as a **Binomial Random Walk**. The probability of a slower attacker catching up from a given deficit is analogous to a Gambler's Ruin problem. 
- The probability of an attacker catching up drops exponentially as the number of blocks the attacker has to catch up with increases.
- Because the sender cannot prepare a chain of blocks ahead of time, the recipient simply waits until the transaction has been added to a block and $z$ blocks have been linked after it. The attacker's potential progress follows a Poisson distribution, and the odds of them catching up diminish rapidly as $z$ increases.
