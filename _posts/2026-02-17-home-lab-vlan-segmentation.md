---
layout: post
title: "Home IDS Lab — VLAN Segmentation on MikroTik E50UG and TP-Link TL-SG108E"
date: 2026-02-17
tags: [lab, vlan, mikrotik, tp-link, networking, segmentation]
summary: >
  Building the network visibility foundation for a home IDS/IPS lab.
  Three-VLAN design (User, IoT, Guest) across a MikroTik E50UG router and
  TP-Link TL-SG108E switch, with port mirroring to a Zeek/Suricata sensor.
---

## Why This Post Exists

Before deploying Zeek or Suricata, the sensor needs to see all the traffic worth monitoring.
That requires proper segmentation — not just creating VLANs, but making sure devices end up
in the right VLAN, that inter-VLAN traffic is routed through the MikroTik (so it can be
mirrored), and that the mirror port actually delivers frames to the sensor interface.

This post documents the full configuration from router to switch, the problems I ran into,
and the evidence I used to verify each stage actually worked.

---

## Design

Three VLANs on a flat `10.0.x.0/24` scheme:

| VLAN | Name  | Subnet        | Purpose                    |
|------|-------|---------------|----------------------------|
| 20   | User  | 10.0.20.0/24  | Trusted wired + WiFi Home  |
| 30   | IoT   | 10.0.30.0/24  | Smart home devices         |
| 40   | Guest | 10.0.40.0/24  | Visitor WiFi               |

Management is on `ether5` at `192.168.88.1/24`, isolated from the bridge entirely — this
turned out to be a critical design decision, explained below.

```
Internet
    │
[ISP Router] 192.168.1.x
    │
 [ether1] MikroTik E50UG [ether5]─── Management PC (192.168.88.10)
    │
 [ether2] trunk: VLANs 20,30,40 tagged
    │
[Port 1] TP-Link TL-SG108E
    ├─[Port 2]───── Wired devices    (VLAN 20 access, PVID 20)
    ├─[Port 3]───── Wired IoT        (VLAN 30 access, PVID 30)
    ├─[Port 4]───── Wired devices    (VLAN 20 access, PVID 20)
    ├─[Port 5]───── Wired devices    (VLAN 20 access, PVID 20)
    ├─[Port 6]───── EAP225 AP #1     (trunk: VLANs 20,30,40 tagged)
    ├─[Port 7]───── EAP225 AP #2     (trunk: VLANs 20,30,40 tagged)
    └─[Port 8]───── Shuttle eth1     (mirror destination, VLAN 1 untagged)

Port mirror source: Ports 1, 6, 7 → Port 8 (both directions)
```

**Success criteria (defined before starting):**

1. Wired device on Port 2, 4, 5 receives `10.0.20.x` via DHCP
2. Wired device on Port 3 receives `10.0.30.x` via DHCP
3. WiFi "Home" SSID receives `10.0.20.x`, "IoT" receives `10.0.30.x`, "Guest" receives `10.0.40.x`
4. Inter-VLAN pings to gateway addresses succeed
5. Internet access works from all VLANs
6. Management at `192.168.88.1` always reachable

---

## Phase 1 — MikroTik Router

### The Management Lockout Problem

Enabling bridge VLAN filtering on  creates an immediate conflict: the bridge
needs to be tagged in the VLAN table for inter-VLAN routing, but you cannot simultaneously
manage the router through an interface that only accepts tagged frames. Attempting to do
this locks you out entirely.

The fix is to separate management **before** touching VLAN filtering. `ether5` was given
a static IP and removed from the bridge first:

```text
/ip address add address=192.168.88.1/24 interface=ether5
/interface bridge port remove [find interface=ether5]
/ip address remove [find interface=bridge]
```

**Evidence of success:** Connection by Winbox to `192.168.88.1` remained live throughout all subsequent
configuration phases, including when VLAN filtering was enabled. No safe-mode revert
was triggered.

### Building the VLANs

After cleaning up a previous misconfiguration, the new VLAN interfaces were created on the bridge:

```text
# VLAN interfaces
/interface vlan add interface=bridge name=vlan20-user vlan-id=20
/interface vlan add interface=bridge name=vlan30-iot vlan-id=30
/interface vlan add interface=bridge name=vlan40-guest vlan-id=40

# bridge VLAN table (bridge and ether2 carry all three tagged)
/interface bridge vlan add bridge=bridge tagged=bridge,ether2 vlan-ids=20
/interface bridge vlan add bridge=bridge tagged=bridge,ether2 vlan-ids=30
/interface bridge vlan add bridge=bridge tagged=bridge,ether2 vlan-ids=40

# gateway IPs
/ip address add address=10.0.20.1/24 interface=vlan20-user network=10.0.20.0
/ip address add address=10.0.30.1/24 interface=vlan30-iot network=10.0.30.0
/ip address add address=10.0.40.1/24 interface=vlan40-guest network=10.0.40.0
```

DHCP servers were created for each VLAN with pools in the `.100–.254` range. VLAN
filtering was enabled in safe mode last:

```text
/interface bridge set bridge vlan-filtering=yes
/system backup save name=vlan-config-working
```

### MikroTik Evidence Checklist

**Interface state:**

```text
/interface print
```

Expected: `vlan20-user`, `vlan30-iot`, `vlan40-guest` all show as running on bridge.

```text
[admin@MikroTik] > /interface print
Flags: R - RUNNING; S - SLAVE
Columns: NAME, TYPE, ACTUAL-MTU, L2MTU, MAX-L2MTU, MAC-ADDRESS
#    NAME          TYPE      ACTUAL-MTU  L2MTU  MAX-L2MTU  MAC-ADDRESS
0 R  ether1        ether           1500   1600       2048  F4:1E:57:xx:xx:xx
1 RS ether2        ether           1500   1596       2026  F4:1E:57:xx:xx:xx
2    ether3        ether           1500   1596       2026  F4:1E:57:xx:xx:xx
3    ether4        ether           1500   1596       2026  F4:1E:57:xx:xx:xx
4    ether5        ether           1500   1596       2026  F4:1E:57:xx:xx:xx
;;; defconf
5 R  bridge        bridge          1500   1596             F4:1E:57:xx:xx:xx
6 R  lo            loopback       65536                    00:00:00:00:00:00
7 R  vlan20-user   vlan            1500   1592             F4:1E:57:xx:xx:xx
8 R  vlan30-iot    vlan            1500   1592             F4:1E:57:xx:xx:xx
9 R  vlan40-guest  vlan            1500   1592             F4:1E:57:xx:xx:xx
```

---

**Bridge VLAN table:**

```text
/interface bridge vlan print
```

Expected: VLANs 20, 30, 40 each list `bridge` and `ether2` as tagged members.

```text
[admin@MikroTik] > /interface bridge vlan print
Flags: D - DYNAMIC
Columns: BRIDGE, VLAN-IDS, CURRENT-TAGGED, CURRENT-UNTAGGED
#   BRIDGE  VLAN-IDS  CURRENT-TAGGED  CURRENT-UNTAGGED
0   bridge        20  bridge
                      ether2
1   bridge        30  bridge
                      ether2
2   bridge        40  bridge
                      ether2
;;; added by pvid
3 D bridge         1                  bridge
```

---

**DHCP leases** (after connecting test devices):

```text
/ip dhcp-server lease print
```

Expected: Leases from `dhcp20-user`, `dhcp30-iot`, `dhcp40-guest` pools visible.
A device on VLAN 20 shows address `10.0.20.x`; VLAN 30 shows `10.0.30.x`.

```text
[admin@MikroTik] > /ip dhcp-server lease print
Flags: D - DYNAMIC
Columns: ADDRESS, MAC-ADDRESS, HOST-NAME, SERVER, STATUS, LAST-SEEN
 #   ADDRESS      MAC-ADDRESS        HOST-NAME  SERVER        STATUS  LAST-SEEN
 0 D 10.0.20.250  F4:34:F0:xx:xx:xx             dhcp20-user   bound   5m38s
 1 D 10.0.20.246  CC:5E:F8:xx:xx:xx             dhcp20-user   bound   5m34s
 2 D 10.0.20.245  8C:86:DD:xx:xx:xx             dhcp20-user   bound   11m15s
 3 D 10.0.20.244  70:F1:1C:xx:xx:xx             dhcp20-user   bound   6m33s
 4 D 10.0.20.243  58:D3:49:xx:xx:xx             dhcp20-user   bound   38s
 5 D 10.0.20.241  60:DC:81:xx:xx:xx             dhcp20-user   bound   10m
 6 D 10.0.20.248  4C:60:BA:xx:xx:xx             dhcp20-user   bound   4m42s
 7 D 10.0.20.233  48:E1:5C:xx:xx:xx             dhcp20-user   bound   3m17s
 8 D 10.0.30.253  F8:81:1A:xx:xx:xx             dhcp30-iot    bound   1m47s
 9 D 10.0.20.229  90:9A:4A:xx:xx:xx             dhcp20-user   bound   2m29s
10 D 10.0.20.228  90:9A:4A:xx:xx:xx             dhcp20-user   bound   2m16s
11 D 10.0.30.252  D8:3A:DD:xx:xx:xx             dhcp30-iot    bound   7m1s
12 D 10.0.20.254  AA:04:14:xx:xx:xx             dhcp20-user   bound   4m49s
13 D 10.0.20.251  70:EE:50:xx:xx:xx             dhcp20-user   bound   6m6s
14 D 10.0.20.238  74:DF:BF:xx:xx:xx             dhcp20-user   bound   12m56s
15 D 10.0.20.235  5C:80:B6:xx:xx:xx             dhcp20-user   bound   3m44s
16 D 10.0.20.227  D0:17:C2:xx:xx:xx             dhcp20-user   bound   11m26s
17 D 10.0.20.226  D0:17:C2:xx:xx:xx             dhcp20-user   bound   6m51s
18 D 10.0.40.254  12:AB:66:xx:xx:xx             dhcp40-guest  bound   59s
```

---

**Routing table:**

```text
/ip route print
```

Expected: Connected routes for `10.0.20.0/24`, `10.0.30.0/24`, `10.0.40.0/24` present.

```text
[admin@MikroTik] > /ip route print
Flags: D - DYNAMIC; I - INACTIVE, A - ACTIVE; c - CONNECT, d - DHCP
Columns: DST-ADDRESS, GATEWAY, ROUTING-TABLE, DISTANCE
    DST-ADDRESS      GATEWAY       ROUTING-TABLE  DISTANCE
DAd 0.0.0.0/0        192.168.1.1   main                  1
DAc 10.0.20.0/24     vlan20-user   main                  0
DAc 10.0.30.0/24     vlan30-iot    main                  0
DAc 10.0.40.0/24     vlan40-guest  main                  0
DAc 192.168.1.0/24   ether1        main                  0
DIc 192.168.88.0/24  ether5        main                  0
```

---

## Phase 2 — TP-Link Switch

### The PVID Problem

Configuring the switch proved to be the difficult task as well. The symptom was specific:
WiFi devices (connected via the APs on the trunk ports) received correct IPs, but wired
devices on ports 2–5 did not get any IP at all.

The root cause was PVID misconfiguration. PVID determines which VLAN the switch assigns
to an untagged incoming frame. The ports had been added to VLAN 20 as untagged members,
but their PVID was still set to 1 (the default), and they were still listed as members
of VLAN 1.

| State          | PVID | VLAN 1 membership | VLAN 20 membership | Result              |
|----------------|------|-------------------|--------------------|---------------------|
| **Broken**     | 1    | Untagged          | Untagged           | Conflict / dropped  |
| **Broken**     | 1    | Not Member        | Untagged           | PVID points nowhere |
| **Correct**    | 20   | Not Member        | Untagged           | Traffic reaches VLAN 20 |

The fix for ports 2–5:

1. Set PVID to `20` in `VLAN → 802.1Q VLAN → Port Config` for ports 2, 4, 5
1. Set PVID to `30` in `VLAN → 802.1Q VLAN → Port Config` for port 3
2. Set VLAN 1 membership to `Not Member` for ports 2–5
3. Set VLAN 20 membership to `Untagged` for ports 2, 4, 5;
3. Set VLAN 30 membership to `Untagged` for port 3

### Final Port Configuration

| Port  | Type   | Connected To           | VLANs              | PVID |
|-------|--------|------------------------|--------------------|------|
| 1     | Trunk  | MikroTik ether2        | 20, 30, 40 tagged  | 1    |
| 2     | Access | Wired devices          | 20 untagged        | 20   |
| 3     | Access | Wired devices          | 30 untagged        | 30   |
| 4     | Access | Wired devices          | 20 untagged        | 20   |
| 5     | Access | Wired devices          | 20 untagged        | 20   |
| 6     | Trunk  | EAP225 AP #1           | 20, 30, 40 tagged  | 1    |
| 7     | Trunk  | EAP225 AP #2           | 20, 30, 40 tagged  | 1    |
| 8     | Future | Shuttle eth1 (pending) | —                  | 1    |

Port 8 is reserved as the mirror destination for the Shuttle IDS sensor. Port mirroring
configuration will be covered in the next post once the Shuttle is physically connected.

---

## Verification — Evidence of Completion

The following are the actual verification steps run after configuration. Each one maps
to a success criterion defined at the start.

### 1. DHCP Assignment per VLAN

On a wired device connected to port 2:

```text
ip addr show eth0
```

Expected: `inet 10.0.20.xxx/24 brd 10.0.20.255 scope global dynamic eth0`

```text
ondrej@kali:~$ ip addr show eth0
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether d0:17:c2:xx:xx:xx brd ff:ff:ff:ff:ff:ff
    inet 10.0.20.227/24 brd 10.0.20.255 scope global dynamic noprefixroute eth0
       valid_lft 1293sec preferred_lft 1293sec
    inet 10.0.20.226/24 brd 10.0.20.255 scope global secondary dynamic eth0
       valid_lft 1368sec preferred_lft 1368sec
    inet6 fdaf:cde6:48f8:46ef:f541:f563:5bce:2975/64 scope global dynamic noprefixroute
       valid_lft 1730sec preferred_lft 1730sec
    inet6 fe80::2ec1:1405:4e8b:a28d/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
```

---

### 2. Gateway Reachability

```text
ping -c 4 10.0.20.1   # VLAN 20 gateway
```

Expected: 0% packet loss, rtt < 5ms.

```text
ondrej@kali:~$ ping -c 4 10.0.20.1
PING 10.0.20.1 (10.0.20.1) 56(84) bytes of data.
64 bytes from 10.0.20.1: icmp_seq=1 ttl=64 time=0.364 ms
64 bytes from 10.0.20.1: icmp_seq=2 ttl=64 time=0.320 ms
64 bytes from 10.0.20.1: icmp_seq=3 ttl=64 time=0.333 ms
64 bytes from 10.0.20.1: icmp_seq=4 ttl=64 time=0.353 ms

--- 10.0.20.1 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3050ms
rtt min/avg/max/mdev = 0.320/0.342/0.364/0.017 ms
```

```text
ping -c 4 10.0.30.1   # IoT gateway — inter-VLAN
ping -c 4 10.0.40.1   # Guest gateway — inter-VLAN
```

Expected: Both succeed. Success here confirms inter-VLAN routing is active — traffic
is crossing VLAN boundaries through the MikroTik, not just reaching a local gateway.

```text
ondrej@kali:~$ ping -c 4 10.0.30.1
PING 10.0.30.1 (10.0.30.1) 56(84) bytes of data.
64 bytes from 10.0.30.1: icmp_seq=1 ttl=64 time=0.304 ms
64 bytes from 10.0.30.1: icmp_seq=2 ttl=64 time=0.316 ms
64 bytes from 10.0.30.1: icmp_seq=3 ttl=64 time=0.349 ms
64 bytes from 10.0.30.1: icmp_seq=4 ttl=64 time=0.349 ms

--- 10.0.30.1 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3080ms
rtt min/avg/max/mdev = 0.304/0.329/0.349/0.019 ms
```

```text
ondrej@kali:~$ ping -c 4 10.0.40.1
PING 10.0.40.1 (10.0.40.1) 56(84) bytes of data.
64 bytes from 10.0.40.1: icmp_seq=1 ttl=64 time=0.256 ms
64 bytes from 10.0.40.1: icmp_seq=2 ttl=64 time=0.306 ms
64 bytes from 10.0.40.1: icmp_seq=3 ttl=64 time=0.286 ms
64 bytes from 10.0.40.1: icmp_seq=4 ttl=64 time=0.268 ms

--- 10.0.40.1 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3055ms
rtt min/avg/max/mdev = 0.256/0.279/0.306/0.018 ms
```

---

### 3. Internet Access

Repeat from a device on each VLAN (20, 30, 40):

```text
ping -c 4 8.8.8.8
ping -c 4 google.com
```

Expected: 0% packet loss on both. `google.com` resolving also confirms DNS is working
through the MikroTik.

```text
ondrej@kali:~$ ping -c 4 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=116 time=3.31 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=116 time=3.49 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=116 time=3.74 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=116 time=3.46 ms

--- 8.8.8.8 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3007ms
rtt min/avg/max/mdev = 3.311/3.501/3.744/0.155 ms
```

```text
ondrej@kali:~$ ping -c 4 google.com
PING google.com (142.251.141.174) 56(84) bytes of data.
64 bytes from lcprga-ag-in-f14.1e100.net (142.251.141.174): icmp_seq=1 ttl=116 time=3.16 ms
64 bytes from lcprga-ag-in-f14.1e100.net (142.251.141.174): icmp_seq=2 ttl=116 time=3.51 ms
64 bytes from lcprga-ag-in-f14.1e100.net (142.251.141.174): icmp_seq=3 ttl=116 time=3.63 ms
64 bytes from lcprga-ag-in-f14.1e100.net (142.251.141.174): icmp_seq=4 ttl=116 time=3.54 ms

--- google.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3006ms
rtt min/avg/max/mdev = 3.159/3.459/3.625/0.178 ms
```

---

### 4. VLAN Isolation — Negative Test (Baseline)

From a device on VLAN 30 (IoT), ping a device on VLAN 20 (User):

At this stage, without firewall rules, this **should succeed** — inter-VLAN routing is
intentionally open. This output is the baseline. When firewall rules are added in the
next phase, re-running this test should **fail**, giving a concrete before/after diff.

### 5. Traceroute — Routing Path Confirmation

Traceroute to confirm traffic is routed through the MikroTik and not bridged:

```text
traceroute 10.0.30.<device-ip>
```

Expected first hop: `10.0.20.1` — the User VLAN gateway. If the first hop is the
destination device directly, there is VLAN leakage.

```text
ondrej@kali:~$ traceroute 10.0.30.252
traceroute to 10.0.30.252 (10.0.30.252), 30 hops max, 60 byte packets
 1  10.0.20.1 (10.0.20.1)  0.277 ms  0.136 ms  0.195 ms
 2  10.0.30.252 (10.0.30.252)  0.322 ms  0.286 ms  0.224 ms
```

---

## Additional Evidence Methods

Beyond the CLI verification above, the following approaches strengthen the
evidence trail for this build and are worth adding to the post or as linked artifacts.

### Network Scan Before / After

Run from a device on VLAN 20 before firewall rules are applied. Save output — this is
the before-baseline to diff against after the next phase.

```text
sudo nmap -sn 10.0.30.0/24
sudo nmap -sn 10.0.40.0/24
```

```text
ondrej@kali:~$ sudo nmap -sn 10.0.30.0/24
Starting Nmap 7.95 ( https://nmap.org ) at 2026-02-18 17:10 CET
Nmap scan report for 10.0.30.1
Host is up (0.00030s latency).
Nmap scan report for 10.0.30.251
Host is up (0.038s latency).
Nmap scan report for 10.0.30.252
Host is up (0.00028s latency).
Nmap scan report for 10.0.30.253
Host is up (0.00031s latency).
Nmap done: 256 IP addresses (4 hosts up) scanned in 4.00 seconds
```

```text
ondrej@kali:~$ sudo nmap -sn 10.0.40.0/24
Starting Nmap 7.95 ( https://nmap.org ) at 2026-02-18 17:10 CET
Nmap scan report for 10.0.40.1
Host is up (0.00030s latency).
Nmap done: 256 IP addresses (1 host up) scanned in 4.05 seconds
```

---

## What Failed and Why

| Attempt | What I tried | What happened | Root cause |
|---------|-------------|---------------|------------|
| 1 | Enable VLAN filtering while ether5 in bridge | Lost management access | Bridge can't be both tagged (routing) and accessible untagged |
| 2 | PVID left at 1 on access ports | Wired devices got no DHCP | PVID must match the untagged VLAN the port is a member of |
| 3 | Ports 2–5 left as VLAN 1 Untagged + VLAN 20 Untagged | Traffic confusion, wrong DHCP pool | A port can only be Untagged in one VLAN |

---

## Current State and Next Steps

**Status:** Operational. All five success criteria met.

1. **Firewall rules** — block Guest and IoT from reaching User VLAN; restrict IoT to
   internet only. The negative test in criterion 4 above provides the baseline to diff
   against once rules are in place.

2. **Management VLAN** — create VLAN 10 for all infrastructure management (switch, APs,
   MikroTik), separate from user-facing VLANs.

3. **Pi-hole local DNS resolver** — Pi-hole on VLAN 20 (`10.0.20.x`) serving all VLANs.
   Adding this has several downstream consequences that will each need handling:
   - **DHCP** — `dns-server` on all three DHCP networks must be updated from the gateway
     IP to the Pi-hole IP
   - **Firewall rules** — DNS allow rules for VLANs 30 and 40 to reach Pi-hole on VLAN 20
     must be inserted *before* the inter-VLAN deny rules, or IoT and Guest clients lose
     name resolution the moment firewall rules go live
   - **DNS enforcement** — NAT redirect rule to catch clients bypassing Pi-hole with a
     hardcoded upstream (e.g. `8.8.8.8`) and redirect them silently to Pi-hole
   - **Redundancy** — Pi-hole becomes a single point of failure for DNS across all VLANs;
     a fallback or second instance needs to be planned
   - **IDS visibility** — Pi-hole query logs per VLAN enable detection scenarios not
     visible in packet capture alone: IoT beaconing to new domains, DNS tunnelling,
     bypass attempts; cross-correlate with Zeek `dns.log`
   - **Per-VLAN policy** — IoT group on strict allowlist (only known manufacturer domains),
     User and Guest on standard ad/tracking blocklists

4. **mDNS across VLANs** — placing IoT devices on VLAN 30 breaks mDNS-dependent
   features (Chromecast, AirPlay, printers, smart home discovery) since mDNS is
   link-local and does not cross VLAN boundaries by design. Needs evaluation before
   moving devices: either accept the limitation, use an mDNS reflector/repeater
   (e.g. Avahi on the Shuttle or a dedicated service on the MikroTik) to selectively
   bridge mDNS between VLANs 20 and 30, or keep specific devices on VLAN 20 if
   discovery is essential. The mDNS reflector approach has security implications —
   it partially defeats the isolation goal — so the scope of what gets reflected
   needs to be intentional.

5. **Port mirroring + Shuttle connection** — physically connect the Shuttle and configure
   port mirroring on the switch (source ports 1, 6, 7 → destination port 8, both
   directions). Evidence plan for that post:
   - `tcpdump -i eth1 -nn -c 20` to confirm frames arrive on the sensor interface
   - `tcpdump -i eth1 -nn -e vlan` to confirm VLAN tags are preserved through the mirror
   - A short `.pcap` opened in Wireshark — Protocol Hierarchy screenshot and per-VLAN
     filter as publishable artifacts

6. **Zeek deployment** — configure on Shuttle `eth1`, validate `conn.log` shows entries
   from all three VLAN subnets.

7. **Alert on inter-VLAN anomalies** — first detection use case: IoT device initiating
   connections to User VLAN addresses.
