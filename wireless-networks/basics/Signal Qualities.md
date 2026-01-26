---
tags:
  - CSE_122
---
# Signal Strength 
Signal strength is measured in decibels
* Power is measured in Watts or dBw or dBm
$$
\begin{aligned}
Power_{\text{dBw}} &= 10 * \log_{10}(Power_{\text{Watts}}) \\ 
Power_{\text{dBm}} &= 10 * \log_{10}(Power_{\text{milliwatts}}) \\
\end{aligned}
$$
* dBm is most relevant to the IoT domain
    * 0 dBm equals 1 mW transmit power
    * Example
        * Max BLE transmit power for nRF52840: 8 dBm (6.31 mW)
        * Min BLE receive sensitivity for nRF52840: -95 dBm (316.2 fW)
* Rules of thumb: +3 dB is double the power, 10 dB is 10x power

* Bluetooth Low Energy (local area)
    * nRF52840 transmit power:          8 dBm (6.31 mW)
    * nRF52840 receive sensitivity:   -95 dBm (316.2 fW)

* LoRa (wide area)
    * SX127X LoRa transmit power:      20 dBm (100 mW)
    * SX127X LoRa receive sensitivity: -148 dBm (1.6 attoWatt)

## Degradation
- Propagation degrades RF signals (logarithmic)
- Physical obstacles, interference, reflections 

# Signal Frequency and Analysis
- Which channel the signal is sent on
- sum of sinusoids can be reversed
- frequency separation is how different technologies can operate simultaneously 
- higher frequency $\implies$ shorter ranger, higher speed
- IoT thrives on unlicensed bands
- Bluetooth operates on sequence of transmit channels. 

# Signal Modulation (Data Encoding)
- encoding signal data in an analog "carrier signal"
- modulation scheme + data defines the bandwidth

## On-Off Keyring
When the carrier is present, send 1. Otherwise there will be no signal. 
- Simple
- Spectrum Frugal
- Susceptible to noise 

## Amplitude-shift Keyring (ASK)
- Modify amplitude of carrier signal
- This is an extreme example of [[#On-Off Keyring]]. 
- Extremely susceptible to noise.

## Frequency-shift Keyring (FSK)
This modifies the frequency of the carrier signal. The bandwidth is limited, but still commonly used. This is relatively simple and robust to noise.

## Phase-shift Keyring (PSK)
This modifies the phase of the carrier signal. It is energy efficient and robust, but requires more expensive hardware.

---
There are other more complicated ones like Quadrature Amplitude Modulation.