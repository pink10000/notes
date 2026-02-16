---
tags:
  - CSE_122
aliases:
  - Thread
---
# Overview
**Thread** is built off of [[802.15.4]]. It reuses most of PHY and MAC with IPv6 communication. These networks use a mix of [[Network Topologies#Star and Tree Topologies|star]] and [[Network Topologies#Break and Mesh Networks|mesh]] topologies. 

Each router (parent) communicates with other routers. Their radio is always on so they can forward packets for network devices. Up to 32 *routers per network*. 

Each end device (child) communicates with one parent. They cannot forward packets, and disable transceiver to save power. Up to 511 *end devices per router*.

Thread leaders are devices in charge of making decisions. This is automatically selected from routers. 

Border routers are routers with connectivity to another network (WiFi, Ethernet). Multiple borders may exist at once. 

# Changes to 802.15.4
Physical Layer
- removes all non-2.4 GHz PHY options
- reuses [[802.15.4#O-QPSK|O-QPSK]]
- same 16 channels, with 5 MHz spacing

Link Layer and MAC
- non-beacon enabled PAN only
- no superframe, no periodic beacons, no Guaranteed Time Slots (GTS)
- most MAC Commands removed 
- keep unslotted [[Medium Access Control#Contention-Based Protocols|CSMA/CA]] algorithm
- keep [[Packet Format|packet structure]] and frame types

# Addressing
Thread uses [[Internet Protocol#IPv6|IPv6]] for communication. 
- address structure is easier to support sensor networks
- addresses are more compressible
- interopable with normal computers and networks 
- reuse developed standards
- packet overhead can be high (40 bytes of header for 127 byte payload!)

One benefit is that each Thread device can multiple IPv6 addresses on how to contact it.
- Global IP address
	- all interfaces reachable form outside a thread network
	- `2000::/3`
- Mesh-local IP
	- all devices reachable within the same Thread network
	- `fd00::/8`
	- remaining bits are randomly chosen as part of joining the network
	- permanent while connection is maintained 
	- used for application-layer interactions
- Link-local-IP
	- all devices reachable by a single radio transmission
	- `fe80::/16` 
	- The bottom most 64-bits are EUI-64, MAC address with `0xFFFE` in the middle
	- Permanent for a given device, no matter the network 
	- used for low-layer interactions with neighbors
- Topology-based IP
	- RLOC: Routing Locator plus Child ID
	- `ROUTER ID` (5 bits) + `R` (1 bit) + `Child ID` (9 bits)
	- changes with network topology, used for routing packets
	- All devices using the same router will have the same RLOC16. See [here](https://openthread.io/guides/thread-primer/ipv6-addressing#how_a_routing_locator_is_generated) for more information.
- Role-based IP
	- Multicast can be:
		- `ff02::1`- link-local, all listening devices
		- `ff02::2`- link-local, all routers/router elligible
		- `ff03::1`- mesh-local, all listening devices
		- `ff03::2`- mesh-local, all routers/router-elligible
	- Anycast
		- `fd00::00ff:fe00:fcXX`
		- where `XX` is `00`:thread leader, `01`-`06`: DHCPv6 agent, `30`-`37`: commissioner, etc
![scopes](https://openthread.io/guides/images/ot-primer-scopes_2x.png)
![rloc](https://openthread.io/guides/images/ot-primer-rloc-topology_2x.png)

Consider 
```
fe80::54db:881c:3845:57f4
```
This is a link-local address, as shown by `fe80`. It cannot be routed, only to discover neighbors, configure links, and exchange routing information.

Consider 
```
fde5:8dba:82e1:1:4160:993c:8399:35ab
```
This is a mesh-local address, chosen after commissioning is complete. It does not change as topology changes, and *should be used by applications*. 

## 6LoWPAN
The IPv**6** over **Lo**w-Power **W**ireless **P**ersonal **A**rea **N**etworks (6LoWPAN) is an IETF standard for running IPv6 over 802.15.4 links. 

Goals:
- compress IPv6 headers
- handle fragmentation of packets
- enable sending packets through mesh 
- communication inside 15.4 network should be low-overhead
- communication outside should minimize overhead where possible

They figured a lot of common parameters can be assumed or set to default values. The payload length can be redetermined from packet length. The source/destination can often be reassembled from link layer data. 

For example, the source/destination addresses can be derived from the 802.15.4 header. 

# Device Types
**Full Thread Devices**
- MAC: always-on, and participates in routing
- Examples are: routers, thread leaders, border routers, and Router-Eligible End Device (REED)

**Minimal Thread Device**
- MAC: Can be low power
- Only send/receive to/from parent
- Examples are: Minimal End Device (MED), Sleepy End Device (SED)

A **Router-Eligible End Device** (REED) is a router with no children. It can operate as an end device with one connection. When a joining end device relies on it, it can promote to a router. 

A **Sleepy End Device** (SED) are lower devices that periodically exchange messages with router. It can send whenever, as needed, but will periodically check with with the router if it has data pending (think of a mailbox)

A **Synchronized Sleepy End Device** (SSED) is the same, but it can listen only during preconfigured windows.

# Discovering Thread Networks
Any device can beacon request MAC command. Any routers are router-eligible device can respond, and the payload will contain information about the network. 

Joining a network is done by becoming a child of an existing router.
1. Sent a parent request, multicast
2. Receive a parent response (from all routers/router-eligible)
3. Send a Child ID Request to the router with the best link
4. Receive a Child ID Response from that router. 

A Thread device may become a commissioner to allow it to join and encrypt communications. 

Becoming a router is done by sending a link request. Each router stores 
- Router ID Set: set of current valid router IDs
- Link Set: information about routers that are/were recently neighbors
- Route Set: records route cost and next hop about other routers that are/recently were reachable from this router
The link cost is computed via quality of link by threshold. 

# Communication With IP
Any communication with IP is now possible (if there is a library to support it). For example,
- UDP
- DNS
- SNTP
- CoAP
	- HTTP but over UDP targeting less-capable devices. 
	- Uses the same REST architecture
	- Has a URL

TCP is uncommon (too large and slow).