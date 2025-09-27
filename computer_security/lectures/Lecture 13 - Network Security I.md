---
tags:
  - CSE_127
---

- communication on the internet is constructed of discrete, self-addressed, chunks of data called **packets**
- networking is done in layers
	- Application layer (SMTP, FTP, HTTP)
	- Transport Layer (port-addressed communications, TCP, UDP)
	- Internet Layer (IP)
	- Link Layer (Transformation of data within local network, Ethernet)
	- Physical Layer (Traansmission of raw bits vover physical data link, WIFI)

# TCP
- breaks messages into segments
- delivers packets reliably and in order
- routers forward packets towards destination
- ports identify connection along with IP addresses

# IP Packet Fragmentation
- sender writes unique value in identification field of packet
- if router fragments packet, then it copies the `id` into each fragment
- eaach fragment retains the same `id` field value from the original packet
- `offset` field indicates position of frgment in bytes
- `MoreFragments` flag to tell that the fragment is not the last one
- `DontFragment` tells gateway not to fragment
![[Pasted image 20241126090440.png]]
### Example:
Given fragment
```python
S [ len=4000 | id=x | MF=0 | offset=0 ] ->

A [ len=1500 | id=x | MF=1 | offset=0 ] + 
B [ len=1500 | id=x | MF=1 | offset=1480 ] +
C [ len=1040 | id=x | MF=0 | offset=2960 ] +
```
Where the offset of the first fragment is decremented by 20 bytes, for the header part of the IP packet (see above)

## TTL (Time-To-Live)
- designed to limit packet looping around in a network forever
- each router decrements the TTL field
- if `TTL == 0`, then router discards packet

## TCP Primer
- stateful bidrectional session between two `IP:port` endpoints
- each side maintains:
	- **Sequence Number**: sequence base (start from here) + count of bytes sent
	- **Acknowledgement Number**: ack base + count of bytes received
- Special packet flags:
	- **SYN**: I want to start a connection
	- **FIN**: I want to shut down a connection
	- **RST**: We are killing this connection
- The flags do this:
![[Pasted image 20241126091728.png]]
# TCP/IP Security
## 1970s
- End-to-End Principle (focuses on transmission of data between *end*points)
	- network is simple, efficient, scalable
- Robustness: when sending, the system should strictly follow protocol for data, but when recieving data, should tolerate minor errors

## Built-in Assumptions
- TCP/IP should only be ued an intended
	- correct packet headers
	- consideration of others' resources
- hosts controlled by trusted administrators
	- random people cannot get on the nwtwork 
	- correct information needs to be reported by hosts
	- protocols should be implemented correctly
	
## 1980s
- not everyone can be trusted
- threat model changed to :
	- cannot trust everyone (some hosts are compromised)
	- untrusted insiders on internal networks
	- anyone can connect to a public network
- networks generally still trusted

## Today
- these no longer work today
- the network is very open, where anyone can get on it (including bad people)
- attackers can immediately and intentionally misuse protocols/resources 
- not all devices are trustworthy 

# Attacker Models
- person in the middle, eavesdropping, off-path (inject traffic into network)
- many layers to view your own packets
	- network (routers, switches, access points)
	- unprotected WIFI network
	- non-switched Ethernet: everyone on same network
	- switched Ethernet: everyone gets their own link, but sometimes someoen can intercept your traffic
- No authentication in TCP/IP
	- attacker can spoof your IP
- Attackers can **blast packets at a target** with a **spoofed address** and make it look like someone else is attacking them. 

# IP Routing

Given IP `8.8.8.8`
1. Check if host is on local -> send directly
2. If not, -> default gateway
3. Create IP packet
4. Create and send link layer (i.e. Ethernet) frame
	1. 48 bit source addr, 48 bit destination addr
```
[ dest MAC addr | src MAC addr | ethertype | <-- data --> | crc checksum ]
```

## Address Resolution Protocol
- maps IP to MAC within a LAN (local area network)
- used to find the MAC corresponding with the IP addr

1. ARP Request (Broadcast)
	1. *A* wants to send to *B*, where *B* has addr `141.23.56.23`
	2. *A* does not know *B*'s address 
	3. *A* sends request, asking, who is `141.23.56.23`
	4. ARP request is broadcasted across all devices on network with MAC addr  `0xFFFFFFFFFF`
2. ARP Reply (Unicast)
	1. Each device on LAN checks if the IP addr matches its own
	2. Only *B* responds, sending an ARP reply back to *A* with its MAC addr 
	3. This is **unicast**, sent by **one** person directly to *A*

### ARP Spoofing
- ARP is broadcast on a local subnet, so anyone can pretend to be someone else
- Attacker can impersonate any other host 
- mitigate with **static ARP tables** (impractical, but better for small, fixed networks)
- **Port Binding**: restrict MAC/IP on single port at a time
- depend on higher level host auth to save you (SSH/TLS)

## IP Spoofing Attacks
- no auth in Link or Internet layers
- even if routing is correct, Eve can still spoof Alice's IP adr
	- recall Eve is enemy
- UDP is trivial, each data is independent of others
- TCP: complicated, but possible
	- need to guess Bob's SYN-ACK number 
### Blind Port Scanning
![[Pasted image 20241126100402.png]]
- used to determine if a specific port on a target system denoted as *V* is open or closed without recieving direct responses from the target 
- can by pass firewalls and what not using an intermediate *S* that interacts with both attacker *A* and victim *V*

1. *A* sends SYN to *S*
2. *S* sends RST to *A*, with `id=x`
3. *A* sends SYN to *V* with `id=x`, pretending to be *S*
4. *V* processes SYN and has two options:
	1. Open: *V* sends SYN-ACK to *S*
	2. Closed: *V* sends RST to *S*
5. *V* will:
	1. If *V* sends SYN-ACK, *S* responds with RST to terminate
	2. If *V* sends RST, *S* does nothing
6. *S* responds with RST, revealing value of `x`
	1. If `id=x+2`, then *S* sent an RST to *V*, meaning the port was open
	2. If `id=x+1`, then the port was closed
