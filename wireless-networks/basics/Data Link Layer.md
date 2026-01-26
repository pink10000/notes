---
tags:
  - CSE_122
---
# Framing
The typical packet structure is 
- **Preamble**: Existence of packet and synchronization of clocks
- **Header**: Addresses, Type, Length
- **Data**: Payload plus higher layer levels (e.g. IP Packet)
- **Trailer**: Padding CRC

# Error Control
We want to make sure we can detect errors in the packet and discard them. We have **Cyclical Redundancy Checks** which detects single bit errors. 

We also want to recover from small bit errors. 