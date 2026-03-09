---
layout: post
title: "Sensor NIC, Port Mirroring and MikroTik ether3"
date: 2026-03-06
toc: true
tags: [lab, sensor, mikrotik, tp-link, port-mirroring, networking]
summary: >
  Configuring the Shuttle DL30N dual-NIC architecture for passive traffic capture.
  enp2s0 set to promiscuous with no IP, MikroTik ether3 added as VLAN 20 access
  port, TP-Link port mirroring verified via tcpdump.
---

## Why This Post Exists

The Shuttle DL30N has two Intel i226-LM 2.5GbE NICs. The dual-NIC architecture is
central to the sensor design:

| Interface | Role | Config |
|-----------|------|--------|
| `enp1s0` | Management | Static IP `10.0.20.5`, SSH, Grafana access |
| `enp2s0` | Monitoring | No IP, promiscuous mode, receives mirrored traffic |

This separation means management traffic never interferes with packet capture, and the
monitoring interface has no IP — reducing attack surface and keeping capture clean.

This post covers configuring `enp2s0`, adding `ether3` on MikroTik as a VLAN 20 access
port for the Shuttle's management NIC, and setting up port mirroring on the TP-Link switch
to feed traffic to the sensor.

---

## Design

```
Internet
    │
[MikroTik E50UG]
    │ ether2 (trunk: VLANs 20,30,40 tagged)
[TP-Link TL-SG108E]
    ├─ Port 1  ← uplink to MikroTik (mirror source)
    ├─ Port 6  ← EAP225 AP #1
    ├─ Port 7  ← EAP225 AP #2
    └─ Port 8  ← mirror destination → Shuttle enp2s0

[MikroTik ether3] ──── Shuttle enp1s0 (management, VLAN 20 untagged)
```

**Mirror strategy:** Port 1 (uplink to MikroTik) only — both directions. This captures
all internet-bound and inter-VLAN traffic without duplicates. Device-to-device traffic
on the same switch and same VLAN is the only blind spot, which is an acceptable tradeoff
for a home lab — threats like C2 callbacks and exfiltration always cross the router.

---

## Configuring enp2s0 as Monitoring Interface

`enp2s0` was DOWN with no configuration after install:

```
ip a show enp2s0
```

```
3: enp2s0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
    link/ether 80:ee:73:xx:xx:xx brd ff:ff:ff:ff:ff:ff
```

Bring it up in promiscuous mode with no IP:

```
sudo ip link set enp2s0 up
sudo ip link set enp2s0 promisc on
ip a show enp2s0
```

```
3: enp2s0: <NO-CARRIER,BROADCAST,MULTICAST,PROMISC,UP> mtu 1500 qdisc mq state DOWN group default qlen 1000
    link/ether 80:ee:73:xx:xx:xx brd ff:ff:ff:ff:ff:ff
```

`PROMISC` flag confirmed. `NO-CARRIER` is expected — no cable connected yet.

### Making it Persistent via Netplan

Already declared in `/etc/netplan/50-cloud-init.yaml` from the previous post:

```
    enp2s0:
      dhcp4: false
      match:
        macaddress: 80:ee:73:xx:xx:xx
      set-name: enp2s0
```

After `sudo netplan apply`, verified:

```
ip a show enp2s0
```

```
3: enp2s0: <BROADCAST,MULTICAST,PROMISC,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 80:ee:73:ff:0e:98 brd ff:ff:ff:ff:ff:ff
    inet6 fe80::82ee:73ff:feff:e98/64 scope link
```

`UP`, `PROMISC`, no IPv4 address. Exactly correct.

---

## MikroTik ether3 — VLAN 20 Access Port

The Shuttle's management NIC (`enp1s0`) connects to `ether3` on the MikroTik. `ether3`
needs to be an untagged access port on VLAN 20 — the Shuttle sends plain (untagged) traffic
and the router handles VLAN assignment at the port level.

### Checking Existing Config

```
/interface bridge port print
/interface bridge vlan print detail
```

VLAN 20 already existed (tagged on `bridge` and `ether2`) but `ether3` was not in the
bridge at all.

### Adding ether3

```
/interface bridge port add bridge=bridge interface=ether3 pvid=20 frame-types=admit-only-untagged-and-priority-tagged
```

This adds `ether3` to the bridge with PVID 20 — untagged frames arriving on this port
get assigned to VLAN 20.

Then add `ether3` as untagged member of VLAN 20:

```
/interface bridge vlan set [find vlan-ids=20] untagged=ether3
```

Note: the first attempt tried `untagged=ether2,ether3` which failed — `ether2` is already
tagged in VLAN 20 and cannot be both. Setting `untagged=ether3` alone was correct.

### Verification

```
/interface bridge vlan print detail
```

```
 0   bridge=bridge vlan-ids=20 tagged=bridge,ether2 untagged=ether3 mvrp-forbidden=""
     current-tagged=bridge,ether2 current-untagged=""
```

`tagged=bridge,ether2` — router routes VLAN 20, ether2 trunks it to the switch.
`untagged=ether3` — Shuttle gets VLAN 20 traffic untagged. Correct.

After connecting the cable, `ether3` transitioned from `INACTIVE` to `ACTIVE`.

---

## TP-Link Port Mirroring

Configured via the TL-SG108E web interface under **Switching → Port Mirror**:

| Setting | Value |
|---------|-------|
| Mirroring Port (destination) | Port 8 |
| Mirrored Port (source) | Port 1 |
| Mode | Ingress and Egress |

Port 8 is dedicated as the mirror destination — nothing else is connected to it.
Port 1 is the uplink to MikroTik — mirroring both directions captures all traffic
crossing the router in either direction.

Connected a cable from Port 8 to `enp2s0` on the Shuttle.

---

## Verification — Traffic on enp2s0

```
sudo tcpdump -i enp2s0 -c 20
```

```
15:15:31.673654 IP shuttle.ssh > 10.0.20.227.50300: Flags [P.], seq ..., length 196
15:15:31.674162 IP 10.0.20.227.50300 > shuttle.ssh: Flags [.], ack 196, ...
15:15:31.770498 IP shuttle.44021 > pi.hole.domain: 673+ [1au] PTR? 227.20.0.10.in-addr.arpa. (53)
15:15:31.771721 IP pi.hole.domain > shuttle.44021: 673 NXDomain* 0/0/1 (53)
20 packets captured
36 packets received by filter
0 packets dropped by kernel
```

Traffic is visible — including the active SSH session and DNS queries to Pi-hole.
Zero packet drops. Mirror is working correctly.

---

## What Failed and Why

| Attempt | What I tried | What happened | Root cause |
|---------|-------------|---------------|------------|
| 1 | /interface bridge vlan set [find vlan-ids=20] untagged=ether2,ether3 | failure: interface cannot be in tagged and untagged at the same time | `ether2` is already tagged in VLAN 20 — cannot also be untagged |
| 2 | /interface bridge vlan add bridge=bridge vlan-ids=20 untagged=ether3 | failure: vlan already added | VLAN 20 entry already existed, needed `set` not `add` |

---

## Current State and Next Steps

**Status:** Operational. Both NICs configured correctly. Port mirroring verified via
tcpdump. MikroTik ether3 active as VLAN 20 access port. Shuttle reachable at `10.0.20.5`.

1. **Install and configure Zeek** on `enp2s0`
2. **Install and configure Suricata** on `enp2s0`
3. **Set up Grafana + Loki** for log visualization
