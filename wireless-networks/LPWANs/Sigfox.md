---
tags:
  - CSE_122
---
# Overview 
- 600 bps data rate, DBPSK
	- allows greatly increased link budget (150-160 dBm, 10-15 km range in urban)
- Very long range, 10+km communication
- [[Network Topologies#Star and Tree Topologies|Star-topology networks]] with always-listening gateways (any number of low-power end devices)
- Uplink focused communication
- Very low-rate metering
- Unlicensed-band communication (902-928 MHz in US)
- Ultra-narrowband 600 Hz channel bandwidth
	- Improves signal-to-noise ratio
	- Detection only needs to occur at very specific frequency 
- Downlink: 1.5 kHz bandwidth, 600 bps, [[Bluetooth Low Energy#BLE Modulation|GFSK]]

# MAC
- [[Medium Access Control#Contention-Based Protocols|ALOHA]] style access control (send whenever, no Acks)
- messages can be sent three times for increased reliability 
```
+---------+---------+--------+---------+-------------+-----+
|Preamble |Frame    | Dev ID | Payload |Msg Auth Code| FCS |
|  (19)   |Sync (29)|  (32)  | (0-96)  |   (16-40)   | (16)|
+---------+---------+--------+---------+-------------+-----+
                  Uplink Frame Format
```
- Up to 29 bytes per packet, payload up to 12 bytes
- Preamble + Frame Sync are really a 6 byte field for radio sync 
- Auth: 2-5 bytes
- Frame Check Sequence (FCS): 16-bit [[Data Link Layer#Error Control|CRC]] 
We get faster bitrate in the US, since 600 bps $\implies$ 0.387 seconds in the air. The maximum dwell time for 915 MHz is 400 ms.
```
+---------+---------+-------+---------+-------------+-----+
|Preamble |Frame    |  ECC  | Payload |Msg Auth Code| FCS |
|  (91)   |Sync (13)| (32)  | (0-64)  |   (16)      | (8) |
+---------+---------+-------+---------+-------------+-----+
                Downlink Frame Format
```
- Similar structure, 28 bytes total, payload up to 8 bytes 
- Larger preamble + frame sync of 13 bytes 
- Error Correcting Code (ECC) for increased reliability

# Sigfox Status
Mostly abandoned the US. Filed for bankruptcy and purchased by another company.