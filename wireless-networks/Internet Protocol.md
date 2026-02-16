---
tags:
  - CSE_122
---
# IPv6
Replacement to [[#IPv4]]. 128-bits for addresses. Supports multiple transmit models:
- Broadcast: one-to-all
- Multicast: one-to-many
- Unicast: one-to-one

Example:
```
a39b:239e:ffff:29a2:0021:20f1:aaa2:2112
```
Groups of zeros can be replaced with `::`. For example,
```
0000:0000:0000:0000:0000:0000:0000:0001 → ::1
2345:1001:0023:1003:0000:0000:0000:0000 → 2345:1001:23:1003::
aecb:0222:0000:0000:0000:0000:0000:0010 → aecb:222::10
```
There are some *special addresses*:
- Localhost, `::1` 
- Link-Local Network, `fe80::` 
- Local Network, `fc00::` and `fd00::`
- Global Addresses, `2000::` 