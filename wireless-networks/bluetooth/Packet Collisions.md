---
tags:
  - CSE_122
---

# Collisions 
Collisions occur if any part of the two packets overlap. The probability of collision is 
$$
\frac{\text{vulnerable period}}{\text{transmission window}} 
= 
\frac{2 T_{\text{adv}}}{T_{\text{adv\_interval}} + \text{avg}(t_{\text{adv\_delay}})}
$$
# Definition (Packet Reception Rate)
The **Packet Reception Rate** is the odds that a transmitted [[Advertising#Advertisement Packet Layering|advertisement]] packet will be received. 
$$
\text{PRR} = 1 - (\text{probability of collisions})
$$
# Definition (Data Reception Rate)
The rate at which at least one packet is received in $M$ redundant advertisements are sent. 
$$
\text{DRR} = 1 - (\text{probability of collisions})^{N}
$$
where $N$ is the number of packets. In general, redundancy results in high DRR even with many devices. Send less packets/s to reduce congestion or send more to gain from redundancy? 

If many devices ($> 400$), send less. If less, redundancy is better.

# BLE Advertisement Frequency 
Advertisements occur periodically, $10-20ms$ or $T_{\text{adv\_interval}}$. There is a random delay before each transmission at $0-10ms$ or $T_{\text{adv\_delay}}$. The data [[Advertising#Payload Types|payload]] is up to $31$ bytes. 