---
layout: post
title: "Zeek Installation and Configuration"
date: 2026-03-07
toc: true
tags: [lab, zeek, ids, network-monitoring]
summary: >
  Installing Zeek 8.1.1 from the official OBS repository on Ubuntu Server.
  ZeekControl configuration for standalone operation on the passive monitoring
  interface, log rotation, and initial live traffic analysis.
---

## Why This Post Exists

Zeek is the primary network analysis tool in this lab. Unlike signature-based IDS,
Zeek performs deep protocol analysis and generates structured logs for every connection,
DNS query, HTTP request, TLS handshake, and more. This makes it ideal for behavioral
detection and threat hunting rather than just matching known-bad patterns.

This post covers installing Zeek from the official OpenSUSE Build Service repository,
configuring it via ZeekControl for multi-core operation on `enp2s0`, and verifying
live log output.

---

## Installation

Zeek is not in the default Ubuntu repos — the official packages are hosted on OBS
(OpenSUSE Build Service):

```
echo 'deb http://download.opensuse.org/repositories/security:/zeek/xUbuntu_24.04/ /' | \
  sudo tee /etc/apt/sources.list.d/zeek.list

curl -fsSL https://download.opensuse.org/repositories/security:/zeek/xUbuntu_24.04/Release.key | \
  sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/zeek.gpg

sudo apt update
sudo apt install zeek -y
```

### Add Zeek to PATH

Zeek installs to `/opt/zeek/bin/` which is not in the default PATH:

```
echo 'export PATH=$PATH:/opt/zeek/bin' >> ~/.bashrc
source ~/.bashrc
zeek --version
```

```
zeek version 8.1.1
```

---

## ZeekControl Configuration

ZeekControl manages Zeek as a service — handles start/stop, log rotation, and worker
process management. Configuration is in `/opt/zeek/etc/node.cfg`:

```
sudo nano /opt/zeek/etc/node.cfg
```

The `[zeek]` section defines the standalone node:

```
[zeek]
type=standalone
host=localhost
interface=enp2s0
```

`enp2s0` is the passive monitoring interface — no IP, promiscuous mode, connected to
the TP-Link mirror port.

### Log Retention

In `/opt/zeek/etc/zeekctl.cfg`:

```
LogRotationInterval = 3600
LogExpireInterval = 90
```

Logs rotate every hour and expire after 90 days. With 867GB free on the NVMe, 90 days
is a conservative setting — actual Zeek log volume will be measured over the first week
before adjusting.

---

## Deployment and Verification

```
sudo /opt/zeek/bin/zeekctl deploy
```

```
Warning: zeekctl option UseWebSocket is set, but websockets non-functional:
Failed to import websockets module - is it installed? (ModuleNotFoundError(...))
checking configurations ...
installing ...
creating policy directories ...
installing site policies ...
generating standalone-layout.zeek ...
generating zeekctl-config.zeek ...
stopping zeek ...
starting zeek ...
```

The websockets warning is harmless — it does not affect packet capture or logging.

```
sudo /opt/zeek/bin/zeekctl status
```

```
Name         Type       Host          Status    Pid    Started
zeek         standalone localhost     running   2843   06 Mar 15:31:02
```

### Log Files

```
sudo ls -la /opt/zeek/logs/current/
```

```
-rw-r--r-- 1 root zeek   695 Mar  6 15:31 analyzer.log
-rw-r--r-- 1 root zeek   254 Mar  6 15:32 capture_loss.log
-rw-r--r-- 1 root zeek  5159 Mar  6 15:31 conn.log
-rw-r--r-- 1 root zeek  6632 Mar  6 15:32 dns.log
-rw-r--r-- 1 root zeek   265 Mar  6 15:31 known_hosts.log
-rw-r--r-- 1 root zeek   763 Mar  6 15:32 notice.log
-rw-r--r-- 1 root zeek  2535 Mar  6 15:32 ntp.log
-rw-r--r-- 1 root zeek  1192 Mar  6 15:31 ssl.log
-rw-r--r-- 1 root zeek   924 Mar  6 15:31 weird.log
```

All expected log types are present and growing.

---

## Live Log Inspection

`zeek-cut` extracts specific fields from Zeek's TSV logs:

```
sudo cat /opt/zeek/logs/current/dns.log | \
  /opt/zeek/bin/zeek-cut ts query qtype_name | tail -20
```

```
1772811104.030495   ns4.fastly.net                                          AAAA
1772811104.030104   ns3.fastly.net                                          AAAA
1772811129.747614   api6f4e2df3b0ca426e96c251470b8accf3...westeurope.cloudapp.azure.com   A
1772811098.827549   lg webos tv 1372._hap._tcp.local                        SRV
1772811099.829600   lg webos tv 1372._hap._tcp.local                        SRV
1772811162.939958   ha101-1.overkiz.com                                     A
```

Notable observations from first live capture:

- **Fastly CDN** — standard web traffic from devices on VLAN 20
- **Azure westeurope** — cloud service calling home from a network device
- **LG WebOS TV** — mDNS/HomeKit (`_hap._tcp.local`) SRV queries, repeated every ~1s.
  Typical smart TV behaviour — good candidate for VLAN 30 (IoT) once that migration
  is complete
- **Overkiz** (`ha101-1.overkiz.com`) — smart home device, likely a Somfy shutter
  controller. Same IoT migration candidate

This is exactly the kind of device profiling Zeek enables — understanding what
devices are doing before writing detection rules.

---

## Switching to JSON Output

Zeek's default TSV format works for command-line inspection but blocks structured
queries in Grafana/Loki — fields cannot be extracted from TSV lines. Switching to
JSON unlocks LogQL field parsing and proper dashboard aggregations.

Edit `/opt/zeek/share/zeek/site/local.zeek` and make three changes:

**1. Uncomment Community ID logging** — adds a community-id hash to `conn.log` for
cross-correlation with Suricata alerts:

```
@load policy/protocols/conn/community-id-logging
```

**2. Uncomment VLAN logging** — adds VLAN fields to `conn.log`, useful since traffic
arrives on a mirrored port carrying VLAN-tagged frames:

```
@load policy/protocols/conn/vlan-logging
```

**3. Add JSON output at the bottom of the file:**

```
@load policy/tuning/json-logs.zeek
```

Then redeploy:

```
sudo /opt/zeek/bin/zeekctl deploy
```

Verify JSON output:

```
sudo cat /opt/zeek/logs/current/dns.log | head -2
```

```json
{"ts":1773041819.735986,"uid":"Cgoir83w1hXMwum9R4","id.orig_h":"10.0.20.10","id.orig_p":63355,"id.resp_h":"150.171.10.37","id.resp_p":53,"proto":"udp","trans_id":18298,"rtt":0.013972,"query":"login.live.com","qtype_name":"A","rcode_name":"NOERROR","answers":["login.msa.msidentity.com"]}
```

All log files in `/opt/zeek/logs/current/` are now JSON. LogQL queries in Grafana
can now use `| json | field_name` to extract and aggregate individual fields.

---

## What Failed and Why

| Attempt | What I tried | What happened | Root cause |
|---------|-------------|---------------|------------|
| 1 | sudo zeek -i enp2s0 | sudo: zeek: command not found | `sudo` does not inherit user PATH — use full path `/opt/zeek/bin/zeek` |

---

## Current State and Next Steps

**Status:** Zeek 8.1.1 running as a managed service via ZeekControl. Logging to
`/opt/zeek/logs/current/`. 90-day log retention configured.

1. **Install Suricata** — signature-based detection to complement Zeek's behavioural logging
2. **Update Promtail** — point Suricata job to `eve.json` instead of `fast.log`
3. **Build Grafana dashboards** — structured LogQL queries now possible with JSON output
4. **Write custom detection scripts** — port scan detection, DNS tunnelling, IoT profiling
