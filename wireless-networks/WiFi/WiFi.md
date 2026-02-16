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
| 4     | 802.11n      | 2009     | 2.4/5 GHz      | OFDM + MIMO                                                    | 600 Mbps      | 70 m      |
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
- 802.11ac was rebranded as WiFi 5 and was backported.

# Physical Layer (PHY)
The details are not as clear. Different countries/regions have different standards, WiFi has evolved a lot over the last 30 years, and WiFi is focused on improving throughput. Any solutions that were once too complicated no longer are. 

How does WiFi improve throughput?
- techniques like OFDM and MIMO
- increase channel width (now 5 GHz, 6 GHz)
- better spatial use

# Orthogonal Frequency Division Multiplexing (OFDM)
This method replaced [[802.15.4#Direct Sequence Spread Spectrum (DSSS)|DSSS]] since it has more bandwidth. The idea is to 
- split band into a number of narrow subcarriers
- subcarriers are spaced so that they don't interfere
- transmit on multiple subcarriers to increase throughput

Originally, DSSS spread a signal across a wide band, making it susceptible to narrowband interference (interference from high interference power concentrated at specific frequencies). Instead of one wide signal, OFDM splits the frequency band into many narrow subcarriers.  

# MIMO
TODO