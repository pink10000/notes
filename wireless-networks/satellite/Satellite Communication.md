---
tags:
  - CSE_122
---
# Satellite Communication (SATCOM)
- True global connectivity 
- [[Cellular]] is dependent on someone building a cell tower near the area you want to communicate on
	- Remote areas are out of luck!
- Satellites are like moving cell towers

# SATCOM Challenges
- Longer distances lead to path loss, and thus extra latency (LEO is 160-2000km from ground)
- Large deployment areas, means we share a lot of bandwidth. There are many handoffs.
- Deployment is expensive and coordination is difficult. 
- Making a satellite is difficult!
	- Radiation in space is a lot higher (no ozone to protect it).
	- Need to use older technology

# Orbits
## Low Earth Orbit (LEO)
- 160-2000km
- Includes all current human spaceflight. ISS is at 400 km.
- Roughly 90 min for complete orbit
- Last about 5 years (fuel limitations)
## Geostationary Orbit (GEO)
- 35768 km
	- bandwidth is lower than LEO, also larger service area = more shared bandwidth
- Exactly 24 hours per complete orbit 
- Result: fixed location in the sky over a portion on Earth
	- very few satellites can cover all of earth
	- operator can choose to only service a specific region
- Last about 20 years
## Medium-Earth Orbit (MEO)
- roughly between LEO and GEO
- roughly 12 hours per complete orbit 
- GNSS satellites are here (GPS, Galileo, etc.)
	- smaller constellation, longer lifetime, signal is a little stronger
- radiation belts make this area more difficult to use

# Path Loss and Latency to Orbit
- Distance contributes significantly to signal strength loss
- Need higher frequency. But higher frequency $\implies$ smaller antenna $\implies$ less energy connected $\implies$ weaker signal. This is part of the same signal-budget story discussed in [[Signal Qualities]].
- Being at an angle on the horizon increases total distance and path loss.
- Speed of light gives
	- LEO: $\approx 30\!-\!50$ ms
	- MEO: $\approx 125\!-\!325$ ms
	- GEO: $\approx 600\!-\!800$ ms
- Huge coverage areas share bandwidth among many users
	- [[Cellular]] ideas can apply here by providing "cells of coverage" on the ground.
- Moving satellites lead to many handoffs. They move at around $7$ km/s.

Compared with [[Wide Area Networks]], satellite systems push coverage much farther but pay for it with more latency, more shared bandwidth, and higher deployment complexity.

# Cost Considerations
- Costs have dropped a lot in the last few years
- It is about $1000 per kg. 
- Starlink v1.0: 260 kg, Starlink v2.0: 1250 kg, GPS: 1000-2000 kg
