---
layout: post
title: "Understanding VLANs and PVID: A Practical Guide"
date: 2026-02-19
toc: true
tags: [networking, vlan, pvid, lab]
summary: >
  A practical breakdown of how VLANs and PVID actually work — covering 802.1Q tagging,
  tagged vs. untagged ports, and the PVID misconfiguration that silently drops traffic
  from wired devices while WiFi works fine.
---

## Background

When building my home IDS/IPS lab, I encountered a common networking challenge that many
beginners face: understanding how VLANs and PVID actually work in practice. This isn't
theory from a textbook — I learned this by breaking my network and fixing it. When my
wired ports stopped working while WiFi stayed up, I had to troubleshoot layer by layer to
understand *why*.

This post covers what I found.

---

## What Are VLANs?

**VLAN (Virtual Local Area Network)** allows you to segment a physical network into
multiple logical networks. Think of it as creating separate "virtual switches" within one
physical switch.

In my lab, I use VLANs to isolate different types of devices:

| VLAN | Name  | Purpose                        |
|------|-------|--------------------------------|
| 20   | User  | Laptops, phones, trusted devices |
| 30   | IoT   | Smart home devices, cameras    |
| 40   | Guest | Visitor devices                |

This isolation prevents an IoT device compromise from affecting trusted devices — and is
critical for meaningful security monitoring. An IDS only detects lateral movement if
segments that should never talk to each other are visible as separate traffic flows.

---

## 802.1Q VLAN Tagging

The 802.1Q standard adds a 4-byte VLAN tag to Ethernet frames:

```text
Normal Frame:
[Dest MAC][Src MAC][Type][Data][CRC]

802.1Q Tagged Frame:
[Dest MAC][Src MAC][802.1Q Tag][Type][Data][CRC]
                    └─ Contains VLAN ID
```

---

## Port Types: Tagged vs. Untagged

### Tagged Ports (Trunk Ports)

**Purpose:** Carry multiple VLANs between network devices — the VLAN tag stays in the frame.

**Use case:** Switch ↔ Router, Switch ↔ Wireless AP

```text
Example: Port 1 (to Router)
├── VLAN 20: Tagged
├── VLAN 30: Tagged
└── VLAN 40: Tagged

Frame flow: All frames carry their VLAN tags
```

### Untagged Ports (Access Ports)

**Purpose:** Connect end devices that don't understand VLANs — the tag is added on
ingress and stripped on egress, so the device never sees it.

**Use case:** Switch ↔ Laptop, Switch ↔ Desktop

```text
Example: Port 2 (to Laptop)
└── VLAN 20: Untagged

Frame flow: Tag added on ingress, removed on egress
```

---

## The PVID Mystery Solved

Here's where I hit my first major issue: WiFi worked perfectly, but wired devices on
ports 2–5 wouldn't get a DHCP address at all. The problem was **PVID configuration**.

### What is PVID?

**PVID (Port VLAN ID)** answers one question: *"When an untagged frame arrives at this
port, which VLAN does it belong to?"*

Regular devices (laptops, phones) don't send VLAN tags. The switch needs to know which
VLAN to assign their traffic to — that's what PVID does.

### The Broken Configuration

```text
Port 2 Configuration (BROKEN):
├── PVID: 1                    ← Assigns VLAN 1 to incoming traffic
├── VLAN 1: Not Member         ← But port isn't in VLAN 1!
└── VLAN 20: Untagged          ← Port is only in VLAN 20

Result: Traffic dropped ✗
```

What actually happens step by step:

1. Laptop sends untagged frame to Port 2
2. Switch checks PVID = 1
3. Switch assigns VLAN 1 internally
4. Switch looks for VLAN 1 membership on Port 2
5. Not found → frame dropped

WiFi worked because those devices connected via trunk ports — frames were already tagged,
so PVID was never consulted.

### The Fix

```text
Port 2 Configuration (WORKING):
├── PVID: 20                   ← Assigns VLAN 20 to incoming traffic
├── VLAN 1: Not Member
└── VLAN 20: Untagged          ← Port is in VLAN 20

Result: Traffic flows ✓
```

### The Golden Rule

**For access ports:** PVID must equal the VLAN where the port is an untagged member.

```text
Access Port Checklist:
✓ PVID = 20
✓ VLAN 20: Untagged
✓ All other VLANs: Not Member
```

---

## Practical Example: Complete Traffic Flow

A laptop on Port 2 requesting a webpage:

```text
1. Laptop sends frame (no VLAN tag)
   [Dst: Gateway][Src: Laptop][HTTP Request]

2. Arrives at Switch Port 2
   PVID check: 20
   Internally tagged: VLAN 20

3. Switch forwards to Port 1 (trunk to router)
   VLAN 20: Tagged
   [Dst: Gateway][Src: Laptop][VLAN:20][HTTP Request]

4. Router receives, processes VLAN 20 traffic
   Routes to vlan20-user interface (10.0.20.1)

5. Router responds back through Port 1
   [Dst: Laptop][Src: Gateway][VLAN:20][HTTP Response]

6. Switch receives on Port 1, checks destination
   Laptop is on Port 2 (VLAN 20 untagged)

7. Switch removes VLAN tag, sends to Port 2
   [Dst: Laptop][Src: Gateway][HTTP Response]

8. Laptop receives (no VLAN tag visible to it)
```

---

## Why Trunks Don't Need PVID

Trunk ports carry tagged traffic — frames already have VLAN IDs. PVID only matters for
**untagged** incoming frames, so on a pure trunk port it's effectively ignored.

```text
Port 1 (Trunk):
├── PVID: 1                ← Ignored (all traffic is tagged)
├── VLAN 20: Tagged        ← Frame has VLAN 20 tag
├── VLAN 30: Tagged        ← Frame has VLAN 30 tag
└── VLAN 40: Tagged        ← Frame has VLAN 40 tag
```

---

## Common Mistakes to Avoid

### Mistake 1: Port in Multiple VLANs as Untagged

A port cannot be untagged in two VLANs simultaneously.

```text
Wrong:
Port 2:
├── VLAN 1: Untagged
└── VLAN 20: Untagged   ← CONFLICT
```

### Mistake 2: PVID Mismatch

PVID must match the untagged VLAN membership.

```text
Wrong:
Port 2:
├── PVID: 1
└── VLAN 20: Untagged   ← PVID doesn't match
```

### Mistake 3: Forgetting to Remove from Default VLAN

Explicitly set ports to "Not Member" of VLAN 1 when dedicating them to another VLAN.

```text
Wrong:
Port 2:
├── PVID: 20
├── VLAN 1: Untagged    ← Still in default VLAN
└── VLAN 20: Untagged
```

---

## My Lab Configuration

Final switch configuration on the TP-Link TL-SG108E:

| Port | Type  | Connected To        | VLANs          | PVID |
|------|-------|---------------------|----------------|------|
| 1    | Trunk | MikroTik Router     | 20, 30, 40 (T) | 1    |
| 2–5  | Access| Wired Devices       | 20 (U)         | 20   |
| 6–7  | Trunk | WiFi Access Points  | 20, 30, 40 (T) | 1    |
| 8    | Monitor| IDS Sensor (future)| —              | 1    |

*T = Tagged, U = Untagged*

---

## Verification

After configuration, these are the checks that confirmed everything was working:

**1. Check IP assignment** — device on Port 2 should receive a `10.0.20.x` address:

```text
ip addr show eth0
# Expected: inet 10.0.20.xxx/24
```

**2. Test gateway reachability:**

```text
ping 10.0.20.1      # VLAN 20 gateway
ping 8.8.8.8        # Internet
```

**3. Verify from router:**

```text
/ip dhcp-server lease print
# Shows device in correct VLAN pool
```

---

## Why This Matters for Security

Network segmentation through VLANs is foundational to security monitoring:

- **Isolation:** Compromise in the IoT VLAN doesn't reach trusted devices by default
- **Monitoring:** IDS sensor sees inter-VLAN traffic routed through the firewall
- **Detection:** Unusual cross-VLAN access attempts indicate lateral movement
- **Control:** Firewall rules between VLANs enforce security policy

In my IDS lab, port mirroring captures all inter-VLAN traffic to the sensor for analysis
with Zeek and Suricata — but none of that works without the VLAN plumbing being correct
first.

---

## Key Takeaways

1. **VLANs create logical network separation** on physical infrastructure
2. **Tagged ports (trunks)** carry multiple VLANs with tags intact
3. **Untagged ports (access)** serve devices unaware of VLANs
4. **PVID assigns a VLAN to untagged incoming traffic**
5. **Critical rule:** PVID must match the untagged VLAN membership
6. **For access ports:** Remove from VLAN 1, set PVID to target VLAN
