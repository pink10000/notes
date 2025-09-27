---
tags:
  - CSE_127
---
- DNS
- Netowrk perimeter defenses
- DOS

# Domain Name System
- DNS names like `google.com` need to get mapped to IP addr
- i already know this from 224

# Bailiwick Checking
- response from server is cached if it is within the same domain as the query 


# DNS Cache Poisoning
- user wants `a.bank.com`
- user cannot find the IP, so it goes to `ns.bank.com` to find the name server
- attacker has already hijacked local DNS resolver, so it returns a bad website
- user downloads malicious code from the bad website

## Defenses:
- increase query ID size
	- randomize src port and make sure it matches additional 11 bits
	- attacks take hours instead of minutes
	- `0x20` encoding. randomly vary capitalization (DNS is case sensitive)
	- check that you get the same capitalization back
- detect poisoning
	- and refuse to cache targets
	- ignore responses not directly necessary query
	- detect failed query matching

# Network Perimeter Defense
- firewalls and application proxies 
- Network Address Translation
- Netowrk Intrust Detection System


## Firewalls
- isolate/protect network from other parts 
	- protect self from network or another part
	- protect Internet from self
- firewalls run at
	- end hosts (more application/user specific information)
	- network firewalls (intercept/evaluate communications from many hosts)
- filter on:
	- packet filters (filtering header content)
	- proxy-based (operates at the level of the application)
![[Pasted image 20241126103732.png]]

## Access Control Policies
- firewalls tries to enforce and access control policy
- distinguish between inbound/outbound connections
	- **Inbound**: attempts by external users to connect to internal
	- **Outbound**: attempts by internal users to connect to external
- conceptually simply ACP
	- permit internal to connect internal freely
	- restrict external users 
- **Default Allow**: permit all services and only specify the ones that you want to exclude
- **Dedault Deny**: deny all services and only specify the ones you want to allow
	- safer (reduces chances of false negatives, and hits all true positives)
	- flaws get noticed more quickly (cannot access `canvas.ucsd.edu` -> big issue)

## Proxy Based Firewalls
- proxy acts as both client and a server
- more semantics available
![[Pasted image 20241126105117.png]]
### Pros
- reduced attack surface, filter out a lot of noise
- reduced liability
### Cons
- cost in hardware, administration
- bottleneck + single point of failure
- false sense of security (limited language)

# Network Content Analysis
- many network devices want to look at traffic **content** for security. Does this with:
	- Network Intrusion Detection/Prevention Systems
	- Spam Filters
	- Data Leakage
	- Traffic Differentiation
- would want to do this since it is cost-effective and centralized

## Challenges
- each packet is expensive to look into 
- sessions may be encrypted
- reassembling packets into streams can be expensive (since malware may be split across many different packets)
- imperfect network vantage point 

## Network Evasion
- NIDS is typically deployed at the network boundary (like a firewall)
- assumes it sees the same traffic the host receives
- In reality,
	- **Fragmentation**: attackers can split malicious payloads across packets in ways NIDS cannot fully reassemble
	- **Obfuscation**: encoding data or altering packet structure to bypass signature detection
	- **Timing Gaps**: sending packets at irregular intervals to disrupt detection
### TTL Evasion
- Imagine this setup:
![[Pasted image 20241126113008.png]]
- **Hops**: is how many jumps left before the packet expires (jumping to computer counts as 1)
- Malicious payload goes undetected 
### Sequence Evasion
```
				[A] [D] 
[I] [A] [M] [B] [E] 
 1   2   3   4   5   6
```
What does the destination see? `IAMBED`, `IAMBAD`, `IAMBD`, depends on the host.

### Solution
- NIDS can fix this by rewriting all packets to remove ambiguity
	- rewrite all TTL
	- does not allow overlapping packets (reject immediately)
- tricky to get write + expensive 

# Denial-of-Service
- attack against [[Lecture 2 - Threat Models#Availability|availability]]
	- **Logic Vulnerability**: explot bugs in network code to cause crash
	- **Resource Consumption**: overwhelm with too many requests (harder to fix)
		- SYN flood
		- too much time to evaluate messages
		- can cause no connections to be dropped and existing connections to time out
		- some routers are packet/sec limited (FIFO)
- **Distributed DOS (DDOS)**: many hosts attack a victim at once

## Solutions
### Source Address Validation
- filter packets with clearly bad source addresses
- **Network Egress**: filter outbound packets on a link whose source addresses are not reached using the link as the next hop (prevent spoofed packets from leaving)
	- requires cooperation from the router (requires good deeds for others)
- **Network Ingress**: filter inbound packets whose source addresses are not in the routing table at all

### SYN Cookies
- allocation per TCP session is expensive
- assume spoofers cannot complete TCP handshake -> delay allocation of state until remote host commits threeway handshake
- send back SYN/ACK packet without allocting state on server 
- uses a special SYN cookie
	- derived from source IP, dest IP, src PORT, dest PRT, timestamp
- validates SYN cookie on act -> establishes connection + allocate state
- spoofed addresses cannot complete handshake as they cannot send back a valid ACK

### Packet Filtering
- if there is a common feature in the packets, drop them (blacklist)
- instead, try to find a good feature if this is not possible (whitelist)
- can rate-limit suspicious packets
- EXPENSIVE

### Buy More Resources
- large servers can handle these attackers
- attackers can get diverted to local CDN server
- EXPENSIVE

## Special Case: Reflection Attacks
- spoof source address of victim (pretend to be the victim)
- use the victim's server to send requests to 1000s of DNS servers
- Attacker stays anonymous
- Responses may be extremely large, and so it can DOS the victim's server

