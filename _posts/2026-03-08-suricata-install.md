---
layout: post
title: "Suricata Installation and Configuration"
date: 2026-03-08
toc: true
tags: [lab, suricata, network-monitoring, ids, signature-detection]
summary: >
  Installing Suricata 8.0.3 via the OISF PPA on Ubuntu Server. Emerging Threats
  Open ruleset enabled with 48,887 rules. Community ID configured for cross-tool
  correlation with Zeek. Initial alert classification and false positive analysis.
---

## Why This Post Exists

Zeek provides deep protocol analysis and behavioural logging. Suricata complements it
with signature-based detection — matching traffic against known-bad patterns from the
Emerging Threats ruleset. Together they cover both known threats (Suricata) and
anomalous behaviour (Zeek).

This post covers installing Suricata 8.0.3, configuring it to capture on `enp2s0`,
enabling the ET Open ruleset, and interpreting the first alerts.

---

## Installation

Suricata is available via the official OISF PPA:

```
sudo add-apt-repository ppa:oisf/suricata-stable -y
sudo apt update
sudo apt install suricata -y
suricata -V
```

```
This is Suricata version 8.0.3 RELEASE
```

---

## Configuration

The main config is `/etc/suricata/suricata.yaml`. Two key changes:

### 1. Interface

Find the `af-packet` section and set the monitoring interface:

```
af-packet:
  - interface: enp2s0
```

### 2. Community ID

```
community-id: true
```

Community ID generates a standardised hash for each network flow based on the
5-tuple (src IP, src port, dst IP, dst port, protocol). The same flow gets the
same hash in both Suricata and Zeek, enabling instant cross-tool correlation
without manually matching IPs and timestamps.

Practical example: Suricata fires an alert with community-id `1:abc123`. Search
Zeek's `conn.log` for `1:abc123` and immediately get the full session context —
duration, bytes transferred, associated DNS lookups.

---

## Emerging Threats Ruleset

```
sudo suricata-update
```

```
6/3/2026 -- 15:40:44 - <Info> -- No sources configured, will use Emerging Threats Open
6/3/2026 -- 15:40:44 - <Info> -- Fetching https://rules.emergingthreats.net/open/suricata-8.0.3/emerging.rules.tar.gz.
 100% - 5373634/5373634
6/3/2026 -- 15:40:49 - <Info> -- Loaded 64742 rules.
6/3/2026 -- 15:40:49 - <Info> -- Disabled 15 rules.
6/3/2026 -- 15:40:49 - <Info> -- Enabled 136 rules for flowbit dependencies.
6/3/2026 -- 15:40:49 - <Info> -- Writing rules to /var/lib/suricata/rules/suricata.rules:
     total: 64742; enabled: 48887; added: 64742; removed 0; modified: 0
6/3/2026 -- 15:41:12 - <Info> -- Done.
```

48,887 rules enabled after `suricata-update` runs a config test (`-T`) automatically.

---

## Starting Suricata

```
sudo systemctl enable suricata
sudo systemctl start suricata
sudo systemctl status suricata
```

```
● suricata.service - Suricata IDS/IPS/NSM/FW daemon
     Active: active (running) since Fri 2026-03-06 15:43:13 UTC; 6s ago
   Main PID: 9160 (Suricata-Main)
     Memory: 265.0M (peak: 265.0M)
```

Suricata loads ~265MB into memory — consistent with 48,887 active rules.

---

## Initial Alert Analysis

```
sudo tail -f /var/log/suricata/fast.log
```

Two alert types dominated the initial output:

### 1. Ethertype Unknown (SID 2200121)

```
[**] [1:2200121:1] SURICATA Ethertype unknown [**]
[Raw pkt: FF FF FF FF FF FF 8C 86 DD AD 74 3B 88 99 ...]
[Raw pkt: 01 80 C2 00 00 00 F4 1E 57 XX XX XX 00 27 ...]
```

Two distinct frame types:

- `FF FF FF FF FF FF` broadcasts with ethertype `0x8899` — **Realtek proprietary
  protocol** from the TP-Link switch
- `01 80 C2 00 00 00` with MAC `F4:1E:57:XX:XX:XX` — **STP BPDUs** from the
  MikroTik (that is the router's MAC address)

Both are Layer 2 housekeeping frames that Suricata does not recognise. Neither
represents a threat. These are expected when monitoring a mirrored port that
includes raw switch traffic.

### 2. QUIC Error on Data (SID 2231001)

```
[**] [1:2231001:1] SURICATA QUIC error on data [**]
{UDP} 10.0.20.235:53960 -> 163.116.244.35:443
```

`10.0.20.235` is a device using HTTP/3 (QUIC runs over UDP port 443). This is
normal browser traffic — Chrome, Firefox, and YouTube all use QUIC by default.
Suricata flags it when it cannot fully parse the encrypted QUIC payload, which is
expected behaviour.

### Decision: No Suppression at This Stage

Rather than suppressing these rules now, they will be filtered at the Grafana/Loki
layer instead — keeping the raw alert stream intact for completeness. Suppression
will be applied later after baselining normal traffic patterns and understanding
what else appears in `fast.log`.

---

## Community ID — Cross-Tool Correlation

With Community ID enabled in both Suricata and Zeek, a correlation query in Zeek for
a specific Suricata alert looks like:

```
sudo cat /opt/zeek/logs/current/conn.log | \
  /opt/zeek/bin/zeek-cut community_id id.orig_h id.resp_h id.resp_p | \
  grep "1:abc123xyz"
```

This workflow becomes the core of alert triage once dashboards are built in Grafana.

---

## What Failed and Why

| Attempt | What I tried | What happened | Root cause |
|---------|-------------|---------------|------------|
| 1 | Attempted to suppress SID 2200121 via `threshold.conf` | Alerts continued | `threshold-file` line was commented out in `suricata.yaml` and pointed to wrong filename extension (`.config` vs `.conf`) |

The suppression attempt was reverted — filtering in Grafana is a cleaner approach
for a home lab than modifying Suricata config to silence rule categories.

---

## Current State and Next Steps

**Status:** Suricata 8.0.3 running as a systemd service. ET Open ruleset active with
48,887 rules. Alerts flowing to `/var/log/suricata/fast.log` and `eve.json`.
Community ID enabled for cross-tool correlation with Zeek.

1. **Install Grafana + Loki + Promtail** — ship Zeek and Suricata logs to Loki and
   build dashboards
2. **Baseline normal traffic** — document what regular alert noise looks like on this
   network before building detection rules
3. **Write first custom Zeek script** — port scan detection as initial detection use case
