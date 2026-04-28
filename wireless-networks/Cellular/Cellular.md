---
tags:
  - CSE_122
---
Cellular provides the only reliable global coverage available today. For truly remote regions without terrestrial tower deployment, compare with [[Satellite Communication]].

# Evolution of Cellular Network Technologies
- 1948: First commercial phone 
	- cell phones, 5,000 users, 30,000 calls weekly
	- everyone shares the same signal 
- 1965: improved mobile telephone service
	- more spectrum
	- full duplex (receive and transmit)

Early mobile networks were *inefficient*. There were a lot of overlap, and an active user could be anywhere in a 40-60 mile range of the transmit tower (giving exclusive access). 

Each tower's range is called a **cell**. In the early days, each tower had 12 frequencies at the same time. 
# Definition (Cell)
A **cell** is *spatial* division of coverage via cell towers.
- requires more infrastructure/towers
- needs logic to support handoff of a user between towers (harder for operators)
	- there will be some overlap... so who gets the user?
- How often does handoff happen? Depends on the size of the cells. 

This same idea reappears in [[Satellite Communication]], where satellites effectively act like moving cells covering portions of the Earth.
# 1G
- AMPS - Advanced Mobile Phone Service (circa 1983)
- 1G is defined by analog voice channels and established digital control channel (handles the handoffs)
- single-user analog is not very efficient 
- spectrum allocation is extremely scarce resource, therefore want to maximize efficiency of its use
- Deprecated 
	- killed off OnStar (used for emergency calls during car crashes)
	- ADT home alarms
	- AMPS died in early 2000s

## Dual Tone Multi Frequency (DTMF) Signaling
- Switchboard operators used to physically plug wires to make connections 
- Pulse dialing was used to make a phone number by sending specific pulses.

## Handoff
- Base station detects weak signal 
- Base station tells mobile about new, better tower
- Base station sends cutover trigger
- Cons:
	- No "make before break" $\implies$ many drops
	- Mobile has better estimates than base station 
- Towers are in between hexagonal ranges, not in the center. Each antenna gets a beam formation to cover some pattern in a cell/hexagon. 
- Overtime AMPS received more frequencies.
	- divided bands into more blocks. 
	- 850 MHz

# 2G 
- Deployed 1933
- Used [[Medium Access Control#Contention-Based Protocols|TDMA]] to share AMPS channels
	- each channel analog pair was 30 kHz
	- digital compression gave 3 time slots per channel
- encrypted 
> AKA as TDMA, D-AMPS (Digital AMPS)

2G is a collection of second generation protocols. This is also true for later generations.

First sunset happened in 2008. 

## Global System for Mobile Communications (GSM)
- standard for 2G
- GSM meant phone for a while in parts of Europe
- GSMA is GSM Association
- 1987: 13 European countries sign accord to use one wireless standard
	- GSM standard ratified 
	- Not much new in GSM, but many arbitrary design decisions 
- Real innovation was *indirection* and *interoperability*. 
	- Indirection to talk to different towers by giving identity. 
	- Therefore needs to be interoperable between different towers.
