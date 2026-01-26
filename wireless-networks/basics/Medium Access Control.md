---
tags:
  - CSE_122
---
How does a network determine which transmitter gets to transmit? The wireless medium is inherently broadcast. 

# Contention-Based Protocols
-  **ALOHA**: The rule is that if you have data, send it. 
	- Two simultaneously transmissions can collide and be lost. So after waiting a duration of time, send it again.
- **Slotted ALOHA**: Split time into synchronized "slots". Any device can transmit whenever it has data, but it can only transmit at the start of a slot and its transmission cannot be longer than a slot. 
	- Low throughput.
- **CSMA/CA**: Carrier Sense Multiple Access with Collision Avoidance 
	- First listen for a duration and determine if anyone is transmitting. If idle, transmit. If busy, wait and try again. 
	- "Listen before send"
	- Can be combined with slotting.
	- There can be a hidden terminal so that both transmitters never detect each other's transmissions. A partial solution would be to send a *Request to Send (RTS)*. 
	- The receiver will send a *Clear to Send (CTS)* to only one node at a time. 
# Contention-Free Protocols
The goal is to split up communication such that devices will not conflict. We can predetermine this or have it be reservation-based. 
- Very efficient at creating a high-throughput network
- **FDMA**: Frequency Division Multiple Access
	- Split transmissions in frequency. 
	- Technically, each device uses a separate, fixed frequency. This is how RF channels works (in bands).
- **TDMA**: Time Division Multiple Access
	- Split transmissions in time such that devices share the same channel
	- Splits time into fixed-length windows
	- Requires synchronization between devices
- **CDMA**: Code Division Multiple Access
	- Split transmission in "codes"
	- Think of it as multiple speakers in the same room in different languages. Then a receiver can ignore the ones it does not understand
	- Requires everyone to speak the same volume 
# Capture Effect
Two packets at once is not always a loss. We can see the difference in amplitude and detect either. 