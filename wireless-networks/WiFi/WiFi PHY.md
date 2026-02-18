---
tags:
  - CSE_122
---
# Overview
WiFi, or IEEE 802.11.x

| **-** | **Protocol** | **Year** | **Frequency**  | **PHY**                                                        | **Max Rate**  | **Range** |
| :---- | :----------- | :------- | :------------- | :------------------------------------------------------------- | :------------ | :-------- |
| -     | 802.11       | 1997     | 2.4 GHz        | [[802.15.4#Direct Sequence Spread Spectrum (DSSS)\|DSSS]]/FHSS | 2 Mbps        | 20 m      |
| 1     | 802.11b      | 1999     | 2.4 GHz        | DSSS                                                           | 11 Mbps       | 35 m      |
| 2     | 802.11a      | 1999     | 5 GHz          | OFDM                                                           | 54 Mbps       | 35 m      |
| 3     | 802.11g      | 2003     | 2.4 GHz        | OFDM                                                           | 54 Mbps       | 38 m      |
| 4     | 802.11n      | 2009     | 2.4/5 GHz      | OFDM + [[#Multiple In Multiple Out (MIMO)\|MIMO]]              | 600 Mbps      | 70 m      |
| 5     | 802.11ac     | 2013     | 5 GHz          | OFDM + MU-MIMO [downlink only]                                 | 3400 Mbps     | 35 m      |
| 6     | 802.11.ax    | 2021     | 2.5/5 [/6] GHz | OFDMA + MU-MIMO                                                | 9600 Mbps     | 35 m      |
| 7     | 802.11.be    | 2024     | 2.4/5/6        | OFDMA + MU-MIMO                                                | 23000 Mbps    | 35 m      |
| 8     | 802.11.bn    | *TBA*    | 2.4/5/6        |                                                                | *100000?Mbps* |           |
- The original specification used Frequency Hopping Spread Spectrum ([[BLE Connections#Frequency Hopping Spread Spectrum (FHSS)|FHSS]]), and [[Bluetooth Low Energy#BLE Modulation|GFSK]], hopping over 80 channels.
- 802.11b was very popular but is now usually unsupported. 
	- Uses [[802.15.4#Direct Sequence Spread Spectrum (DSSS)|DSSS]]. 
	- Data gets translated into chips.
	- 14 channels, 1-11 for US
- 802.11g still uses the same channels as 802.11b, but now with 20 MHz bandwidth.
	- uses OFDM, but backwards compatible with 802.11b/DSSS
- 802.11n supports 20 MHz and 40 MHz due to [[#Orthogonal Frequency Division Multiplexing (OFDM)|OFDM]]. Extremely successful.
- 802.11ac was rebranded as WiFi 5 and was backported.
	- supports 5 GHz
	- widely used (as of 2025)
	- there are a lot of ways you can modulate/code the signal
- 802.11ax is relatively new (WiFi 6)
	- around this time, WiFi was mostly focused on aggregating throughput across all devices since so many devices can be in a single place
	- was the first to use [[#Orthogonal Frequency Division Multiple Access (OFDMA)|OFDMA]] and 6 GHz (a lot of bandwidth)
	- [[#MU-MIMO]] used for uplink
- 802.11be would be WiFi 7

# Physical Layer (PHY)
The details are not as clear. Different countries/regions have different standards, WiFi has evolved a lot over the last 30 years, and WiFi is focused on improving throughput. Any solutions that were once too complicated no longer are. 

How does WiFi improve throughput?
- techniques like OFDM and MIMO
- increase channel width (now 5 GHz, 6 GHz)
- better spatial use

# Orthogonal Frequency Division Multiplexing (OFDM)
This method replaced [[802.15.4#Direct Sequence Spread Spectrum (DSSS)|DSSS]] since it has more bandwidth. The idea is to 
- split band into a number of narrow subcarriers (subsets of the channel's bandwidth)
- subcarriers are spaced so that they don't interfere
- transmit on multiple subcarriers to increase throughput

Originally, DSSS spread a signal across a wide band, making it susceptible to narrowband interference (interference from high interference power concentrated at specific frequencies). Instead of one wide signal, OFDM splits the frequency band into many narrow subcarriers.  

OFDM allows many subcarriers within a channel to be used at once. So, throughput can scale with the amount of bandwidth available (40 MHz channels can be used, which is larger).
```
Frequency
     ^
  -- | +----+----+----+----+----+----+----+----+----+
   ^ | | U1 | U2 | U3 | U4 | U1 | U2 | U3 | U4 | U5 |
 C | | | U1 | U2 | U3 | U4 | U1 | U2 | U3 | U4 | U5 |
 h W | | U1 | U2 | U3 | U4 | U1 | U2 | U3 | U4 | U5 |
 a i | | U1 | U2 | U3 | U4 | U1 | U2 | U3 | U4 | U5 |
 n d | | U1 | U2 | U3 | U4 | U1 | U2 | U3 | U4 | U5 |
 n t | | U1 | U2 | U3 | U4 | U1 | U2 | U3 | U4 | U5 |
 e h | | U1 | U2 | U3 | U4 | U1 | U2 | U3 | U4 | U5 |
 l | | | U1 | U2 | U3 | U4 | U1 | U2 | U3 | U4 | U5 |
   v | +----+----+----+----+----+----+----+----+----+
  -- | 
     +------------------------------------------------> Time
Legend:
U1 = User 1 | U2 = User 2 | U3 = User 3 | U4 = User 4 | U5 = User 5
```
## # Orthogonal Frequency Division Multiple Access (OFDMA)
We can allocate subcarriers to a device for an amount of time. This turns OFDM into an access control mechanism.

```
Frequency
     ^
     | 
  -- | +----+----+----+----+----+----+----+----+----+
   v | | U5 | U2 | U5 | U3 | U5 | U2 | U4 | U5 | U1 | --- RU of user1
 Sub-| +----+----+----+----+----+----+----+----+----+
 car.| | U3 | U4 | U1 | U2 | U3 | U1 | U5 | U4 | U3 | --- RU of user3
   ^ | +----+----+----+----+----+----+----+----+----+
  -- | | U1 | U5 | U3 | U1 | U2 | U4 | U1 | U3 | U2 | --- RU of user2
(78. | +----+----+----+----+----+----+----+----+----+
 125 | | U4 | U1 | U2 | U4 | U1 | U3 | U2 | U1 | U4 | --- RU of user4
 kHz)| +----+----+----+----+----+----+----+----+----+
     |  
     +------------------------------------------------> Time

----------------------------------------------------------------------
Legend:
U1 = User 1 | U2 = User 2 | U3 = User 3 | U4 = User 4 | U5 = User 5
```
It's not clear in this diagram, but the blocks are not the same size. I.e. at time $=2$, User 1 may use more bandwidth.
- The net spectrum usage is *about* the same
- Each user will get less bandwidth in OFDMA, but more users can exist at once.
- This is the same strategy cellular "resource blocks" use. 

# Multiple In Multiple Out (MIMO)
**Multiple In Multiple Out** (MIMO) is a method to increase throughput on a router. The idea is that you can use $N \times M$ subchannels, to send data simultaneously. 
- $N$ transmit antennas
- $M$ receive antennas

The signals may interfere, but receiving all of them allows data to be recovered. 
```tikz
\begin{document}
\begin{tikzpicture}[
    antenna/.style={circle, draw=black, thick, minimum size=8mm},
    connection/.style={->, >=stealth, gray!50, thin}
]

% Transmitter Nodes (Left)
\node[antenna] (T1) at (0, 0) {$T_1$};
\node[antenna] (T2) at (0, -1.5) {$T_2$};
\node[antenna] (T3) at (0, -3.0) {$T_3$};

% Receiver Nodes (Right)
\node[antenna] (R1) at (4, 0) {$R_1$};
\node[antenna] (R2) at (4, -1.5) {$R_2$};
\node[antenna] (R3) at (4, -3.0) {$R_3$};

% Connection Logic (Manual loop for maximum compatibility)
\foreach \i in {1,2,3} {
    \foreach \j in {1,2,3} {
        \draw[connection] (T\i) -- (R\j);
    }
}

% Labels
\node at (0, 0.8) {\textbf{TX}};
\node at (4, 0.8) {\textbf{RX}};

\end{tikzpicture}
\end{document}
```


MIMO has been expanded to support multiple simultaneously. 
## MU-MIMO
**Multi-user MIMO** or MU-MIMO allows for multiple devices to stream without worrying about *Time Division Multiplexing* since you can have multiple receivers by parallelizing messaging. In general, it improves average performance across a network as a whole, but not for a particular machine. 

# WiFi 6/7 Hardware (802.11ax, 802.11bx)
There are two varieties of 6:
- WiFi 6: Most of the features, but NOT the new frequencies
- WiFi 6E: includes the extra 6 GHz channels, basically entirely unused as of 2023
In WiFi 7:
- extremely high performance 
- 4096-QAM
- 16-stream MIMO
- new features

# Bit Rate Adaptation 
All modern WiFi standards support multiple bit rates, or "Modulation and Coding Scheme (MCS)". Many factors influence the choice of bit rate.
- Capability of device (not all devices support all bit rates)
- Range and packet reliability (interference)

Essentially the router will change the throughput depending on the signal. Selecting the right rate at the right time is a complex problem and needs to be decided per-device. (Trial and Error)

# Real-World Channel Use
- For 2.4 GHz, most networks use 20 MHz channels 1,6, or 11. Several networks create 40 MHz
- For 5 GHz, devices use 80 MHz almost entirely. 
- A new expensive router can have a single 160 MHz bandwidth channel. 
