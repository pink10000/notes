---
tags:
  - CSE_122
---
# Base Packet Format
| **Section**         | **Field Name**               | **Size**         | **Purpose**                                                                  |
| ------------------- | ---------------------------- | ---------------- | ---------------------------------------------------------------------------- |
| **Synchronization** | Preamble                     | 4 bytes          | Composed of zeros to help the receiver synchronize with the signal.          |
| **Synchronization** | Start-of-Packet Delimiter    | 1 byte           | A specific value (**0xA7**) that signals the actual beginning of the packet. |
| **PHY Header**      | PHR (PHY Header)             | 1 byte (8 bits)  | Contains a single field indicating the length of the payload (0–127).        |
| **Payload**         | PSDU (PHY Service Data Unit) | $\leq 127$ bytes | The actual data content being transmitted.                                   |
Inside the payload, we have the [[#Mac Frame]]. 

# Mac Frame
|**Section**|**Field Name**|**Size (Octets)**|
|---|---|---|
|**MAC Header**|Frame control|2|
|**MAC Header**|Sequence number|1|
|**MAC Header (Addressing)**|Destination PAN identifier|0 or 2|
|**MAC Header (Addressing)**|Destination address|0, 2, or 8|
|**MAC Header (Addressing)**|Source PAN identifier|0 or 2|
|**MAC Header (Addressing)**|Source address|0, 2, or 8|
|**MAC Payload**|Frame payload|Variable|
|**MAC Footer**|Frame check sequence|2|
- The sequence number is an 8-bit monotonically incrasing number. 
- The frame check sequence is a 16-bit [[Data Link Layer#Error Control|CRC]]. 

There are a couple different frame types:
- Beacon
- Data
- MAC Command
- Acknowledgement

# Throughput
If we assume the best possible case for data transmission, 
- 122 Bytes per packet, 250 kbps $\to$ 3.904 ms
- inter-frame spacing of 40 symbols, 62.5 kBaud $\to$ 0.640 ms
- So,
  $$
  \frac{122 \text{ bytes}}{4.544 \text{ ms}} = 214 \text{ kbps}
  $$
Compared to BLE [[Advertising|Advertisements]] at 9.92 kbps, this is better. But compared to BLE [[BLE Connections|connections]] at 520 kbps, it is worse. 