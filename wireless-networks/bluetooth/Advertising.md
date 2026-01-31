---
tags:
  - CSE_122
aliases:
  - Advertisement
---
# Purpose
BLE discovery mechanism
- Make nearby devices aware of advertiser’s existence
- Communicate some information from or about advertiser
- Traditional purpose is to enable connections, but this is also useful for general
communication
## Overview
- Periodic broadcast messages with data
- Scan Requests/Responses
	- Scanner sends responses after getting a request
	- Only occurs when scanner is listening
- Almost literally “bonus advertisement data”
# Advertisement Packet Layering 
Inside the [[Bluetooth Low Energy#Packet Structure|PDU]], the range of $2-257$ bytes, it has a specific structure 
```
Header   2 Bytes
Payload  0-37 Bytes
```

The header has the following possibilities 

| Header Type       | Bits | Description                                            |
| ----------------- | ---- | ------------------------------------------------------ |
| `ADV_IND`         | 0000 | Advertisement, Allows Connections/Scan Requests        |
| `ADV_NONCONN_IND` | 0010 | Advertisement, No Connections/Scan Requests            |
| `ADV_SCAN_IND`    | 0110 | Advertisement, No connections but allows Scan Requests |
| `SCAN_REQ`        | 0011 | Scan Request                                           |
| `SCAN_RSP`        | 0100 | Scan Response                                          |
The last $12$ bits are used for other things. There are $6$ bits dedicated to the length of the payload. There is also $1$ bit called `TxAdd` or *Transmitter Address*.  

The first $6$ octets are *address of the advertiser (AdvA)* and the remaining octets (up to $31$, if any) are for data. 

The AdvA has two types:
- **Public**: first $24$ bits of company ID (a company will purchase these rights from IEEE), last $24$ bits of company assigned number (specific to device or randomly generated via hash)
- **Private**: top two MSBs (remember it is little endian, so MSB is on the right) specify type. $46$ bits of random or hash of identity key 

A receiver will know the AdvA is public or private via the `TxAdd` bit flag in the advertisement header. 

When a device receives `ADV_IND` or `ADC_SCAN_IND`, it will send a `SCAN_REQ` to the peripheral. The payload is just $6$ octets for its address, and $6$ octets of the advertiser's address. 

The peripheral will send a `SCAN_RSP`. It is identical to an advertisement, but only occurs after a request. At this points, both devices will be "paired" or "connected". 

# Advertising Timing
Advertising events occur periodically, $20$ms to $10.24$s or longer (in increments of $0.625$ms). There is some *random delay* ($0$ to $10$ms) after each instance to ensure two separate devices do not sync up and destroy the signal quality. 

Transmissions always occur in channels $37, 38, 39$ in that order (so the scanner knows where to look if it misses one). But in between each transmission, there is a listening window on the same frequency. Once the receiver gets the advertisement, there is a $150 \mu\text{s}$ gap between the advertiser and the scanner, enough time for the hardware to switch from talk to listen. 

So, 
```
adv payload @37 -> listen -> payload @38 -> listen -> payload @39 -> listen
```
This is what makes bluetooth "low energy" since most energy is spent *listening*. 

# Payload Types
Payload data (*AdvData*) follow the TLV format:
$$
\text{Type}-\text{Length} - \text{Value}
$$
**For BLE specifically, it uses Length-Type-Value**. This allows the scanner to hop through length-type pairs to parse information it cares about. 
- Flags
	- One bit Boolean flags. It tells scanners if the advertiser is in *Limited Discovery* or *General Discovery* mode. 
- Name (name of device)
- Service UUID
- TX Power Level 
- Manufacturer-specific data
- And more!

# Scanning Pattern 
The scanner iterates through channels $37,38,39$ listening for advertisements. The $T_{\text{scan interval}}$ controls the rate the scanner switches channels. The $T_{\text{scan window}}$ controls the **duty cycle** or how long the scanner stays awake. 

A low duty cycle saves phone battery. In general, 
$$
T_{\text{scan interval}} \leq T_{\text{scan window}}
$$
inside the channels. 

## Scanning Expectations
Packets are lost due to (in roughly descending order):
- [[#Scanning Pattern|duty cycle]]
- sharing $2.4$ GHz antenna with WiFi 
- retune period after each scanning interval 
- dropped packets in the receive software
- packet collisions 

# Advertising Only Applications
There are some devices that only do advertisements. 
- Beacons: iBeacon, Eddystone (you have to run an application registered to listen to these devices to do something with them)
- Tracking: Tile, Apple AirTag
- Local communication: Apple Continuity 

# Energy Costs
Configuration 
- nrf51822
- Max Payload Size
- Max transmit power
- Connectable Advertisement
- Sleep power $11 \; \mu W$.
One packet per second will last $270$ days on a CR2032. One packet pet minute is $\approx 6$ years. 