---
tags:
  - CSE_122
---
# Wide Area Networks
The goal of this technology is for communication at the region/city scale rather than the building/residence scale. For example,
- throughout cities
	- air quality monitoring in a city
- agricultural deployments
- industrial facilities
How do we collect data from many sensors?
1. Manually collect measurements
	1. too much work 
2. Connect it to WiFi or Ethernet
	1. too many separate networks
3. Pay for cellular access
	1. too expensive for many devices

Such a technology needs
- wide area of coverage (deploy fewer gateways)
- low power (deploy on batteries)
- does not need high throughput (sensor data is relatively small)

Another way to get wide-area coverage is [[Satellite Communication]], though with very different cost, latency, and deployment tradeoffs.

# Low Power WANs (LPWANs)
- Uses unlicensed 900 MHz
- Higher power transmissions ($\sim 20$ dBm or $100$ mW)
- Low data rate < 100 kbps
- Range is on multiple kilometers
- Simple [[Medium Access Control#Contention-Based Protocols|ALOHA]] access control

# Bit Flux 
**Bit Flux** is a metric for wide-area communication. 
$$
\text{BitFlux} = \frac{\text{network throughput}}{\text{coverage area}}
$$
Units are in bit per hour per square meter. For an application, 
$$
\text{BitFlux} = \frac{
	\sum \text{each device's uplink}
}{
\text{deployment area}
}
$$
This assumes a relatively homogeneous distribution. I.e. you cannot measure a room but all the devices are in one corner. For a network, bit flux can measure its capability:
$$
\text{BitFlux} = \frac{\text{gatway goodput}}{\text{gateway coverage area}}
$$
This assumes non-overlapping deployment of gateways. Note that bit flux **ignores** the total number of gateways required. It can also account for spatial reuse. Intuitively, reducing coverage area and deploying additional gateways improves capacity. So, if coverage area decreases, the bit flux increases. 

## Example 1 
We can show bit flux for [[LoRaWAN]]:
$$
\frac{
    5\frac{\text{kbps}}{\text{channel}}\cdot 64\text{ channels}\cdot \overbrace{18\%}^{\text{ALOHA access control}}
}{
    \pi\cdot (\underbrace{5\text{ km}}_{\text{Hata model}})^2
}
\approx \frac{58000\text{ bps}}{79\text{ km}^2}
\approx 2.6\frac{\text{bph}}{\text{m}^2}
$$
We can show this for other networks. See [image](https://www.researchgate.net/figure/Throughput-per-unit-area-bit-flux-as-range-is-varied-through-power-control-Plotted-are_fig2_336453523).

## Example 2 
We can show this for a smart household electric meter:
$$
\frac{\frac{250\text{ bytes}}{4\text{ hours}}\cdot 370000\text{ devices}}{120\text{ km}^2}\approx \frac{51000\text{ bps}}{120\text{ km}^2}\approx 1.5\frac{\text{bph}}{\text{m}^2}
$$
---
## Bit Flux Conclusions
- [[Sigfox]] has poor bit flux at longer ranges, so it became less used. Additionally, it suffers from poor throughput capacity. It cannot meet application needs like [[#Example 2]].
- LTE and 2G dominates bit flux charts
- [[LoRaWAN]] in the middle. It can meet application needs (it's bit flux is higher than the electric meter), but only by using 50% of the 915 MHz unlicensed band spectrum.
- Satellite systems trade even larger coverage areas for higher latency and tighter shared-capacity constraints; see [[Satellite Communication|Satellite Communication]].

# Coexistence
In general, **coexistence** defines the requirement for multiple independent wireless networks to operate simultaneously within the same physical space and frequency spectrum.  

In urban environments, the long range leads to many overlapping deployed networks. Devoting excessive bandwidth to a single application creates capacity deficits that severely degrade the operational coexistence of all networks utilizing that shared medium (noisy neighbor!). 

No methods work for inter-network negotiation so far. Without buy-in from most (if not all) deployments, all access control becomes uncoordinated. However, cellular IoT does not have this problem. 
