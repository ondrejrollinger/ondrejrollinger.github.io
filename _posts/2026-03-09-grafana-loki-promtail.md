---
layout: post
title: "Grafana, Loki and Promtail Log Stack"
date: 2026-03-09
toc: true
tags: [lab, grafana, loki, promtail]
summary: >
  Building the log visualisation stack on the Shuttle sensor. Loki chosen over
  Elasticsearch for RAM efficiency. Full pipeline from Promtail log shipping through
  to structured Grafana dashboards — Suricata alert trends by signature, Zeek top
  talkers, and DNS query volume over time. Includes Zeek JSON output switch,
  eve.json migration, and LogQL field parsing patterns.
---

## Why This Post Exists

Tailing log files directly is fine for initial verification but does not scale for
ongoing monitoring. Grafana with Loki provides a queryable, visual interface over
all Zeek and Suricata logs — enabling dashboards, historical queries, and eventually
alerting.

This post covers the full stack installation: Grafana (UI), Loki (log aggregation),
and Promtail (log shipping agent).

---

## Stack Choice — Loki vs Elasticsearch

The more common approach for security log analysis is Elasticsearch + Kibana (the ELK
stack). Loki was chosen instead for this lab:

| Consideration | Elasticsearch | Loki |
|--------------|--------------|------|
| RAM usage | 4–8GB minimum | ~50MB |
| Indexing model | Full text index of all fields | Index only labels, store raw log lines |
| Query language | Lucene / KQL | LogQL |
| Setup complexity | High | Low |
| Suitable for 16GB system | Possible but tight | Comfortable |

With Zeek and Suricata already consuming ~4–6GB combined, Elasticsearch would leave
little headroom. Loki's label-based indexing uses a fraction of the RAM while still
supporting rich log queries via LogQL in Grafana.

---

## Storage Planning

```
df -h
```

```
Filesystem                         Size  Used Avail Use%
/dev/mapper/ubuntu--vg-ubuntu--lv   98G  8.5G   85G  10% /
```

Ubuntu's LVM installer only allocated 98GB from the 1TB NVMe. Extended to use the
full disk:

```
sudo lvextend -l +100%FREE /dev/mapper/ubuntu--vg-ubuntu--lv
sudo resize2fs /dev/mapper/ubuntu--vg-ubuntu--lv
df -h
```

```
/dev/mapper/ubuntu--vg-ubuntu--lv  914G  8.5G  867G   1% /
```

867GB available. **Retention set to 90 days** — conservative until actual daily log
volume is established after a week of operation. At estimated 1–5GB/day for a home
network with 2 APs and ~20 devices, 90 days represents 90–450GB worst case.

---

## Grafana Installation

```
sudo apt install -y apt-transport-https software-properties-common
wget -q -O - https://packages.grafana.com/gpg.key | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/grafana.gpg
echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee /etc/apt/sources.list.d/grafana.list
sudo apt update
sudo apt install grafana -y
sudo systemctl enable grafana-server
sudo systemctl start grafana-server
```

```
● grafana-server.service - Grafana instance
     Active: active (running) since Fri 2026-03-06 16:08:27 UTC
     Memory: 38.7M
```

Grafana accessible at `http://10.0.20.5:3000`. Default credentials `admin/admin`,
password changed on first login.

---

## Loki Installation and Configuration

Loki is distributed as a single binary — no package manager installation:

```
cd /tmp
curl -LO https://github.com/grafana/loki/releases/latest/download/loki-linux-amd64.zip
sudo apt install unzip -y
unzip loki-linux-amd64.zip
sudo mv loki-linux-amd64 /usr/local/bin/loki
loki --version
```

```
loki, version 3.6.7
```

### Configuration

```
sudo mkdir -p /etc/loki /var/lib/loki
sudo nano /etc/loki/loki.yaml
```

```
auth_enabled: false

server:
  http_listen_port: 3100
  grpc_listen_port: 9096

common:
  path_prefix: /var/lib/loki
  storage:
    filesystem:
      chunks_directory: /var/lib/loki/chunks
      rules_directory: /var/lib/loki/rules
  replication_factor: 1
  ring:
    instance_addr: 127.0.0.1
    kvstore:
      store: inmemory

schema_config:
  configs:
    - from: 2024-01-01
      store: tsdb
      object_store: filesystem
      schema: v13
      index:
        prefix: index_
        period: 24h

compactor:
  working_directory: /var/lib/loki/compactor
  compaction_interval: 10m
  retention_enabled: true
  retention_delete_delay: 2h
  retention_delete_worker_count: 150

limits_config:
  retention_period: 2160h
```

`grpc_listen_port: 9096` is required — the default `9095` conflicts with Promtail's
metrics port.

---

## Promtail Installation and Configuration

Promtail is the log shipping agent that tails log files and sends them to Loki:

```
cd /tmp
curl -LO https://github.com/grafana/loki/releases/latest/download/promtail-linux-amd64.zip
unzip promtail-linux-amd64.zip
sudo mv promtail-linux-amd64 /usr/local/bin/promtail
```

```
sudo mkdir -p /etc/promtail
sudo nano /etc/promtail/promtail.yaml
```

```
server:
  http_listen_port: 9080

positions:
  filename: /var/lib/promtail/positions.yaml

clients:
  - url: http://localhost:3100/loki/api/v1/push

scrape_configs:
  - job_name: zeek
    static_configs:
      - targets:
          - localhost
        labels:
          job: zeek
          __path__: /opt/zeek/logs/current/*.log

  - job_name: suricata
    static_configs:
      - targets:
          - localhost
        labels:
          job: suricata
          __path__: /var/log/suricata/*.log
```

Promtail tails all log files in Zeek's current log directory and Suricata's log
directory, labelling them by job for easy filtering in Grafana.

---

## Systemd Services

### Loki

```
sudo nano /etc/systemd/system/loki.service
```

```
[Unit]
Description=Loki log aggregation system
After=network.target

[Service]
Type=simple
User=root
ExecStart=/usr/local/bin/loki -config.file=/etc/loki/loki.yaml
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

### Promtail

```
sudo nano /etc/systemd/system/promtail.service
```

```
[Unit]
Description=Promtail log shipper
After=network.target

[Service]
Type=simple
User=root
ExecStart=/usr/local/bin/promtail -config.file=/etc/promtail/promtail.yaml
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

```
sudo mkdir -p /var/lib/promtail
sudo systemctl daemon-reload
sudo systemctl enable loki promtail
sudo systemctl start loki promtail
```

```
● loki.service
     Active: active (running) since Fri 2026-03-06 16:23:36 UTC
     Memory: 42.8M

● promtail.service
     Active: active (running) since Fri 2026-03-06 16:19:28 UTC
     Memory: 30.3M
```

---

## Switching Suricata to eve.json

`fast.log` is plain text — not parseable in Loki. `eve.json` is Suricata's structured
JSON output containing the same alerts plus flow data, DNS, HTTP, TLS and more. Update
Promtail to ship `eve.json` instead:

```
sudo nano /etc/promtail/promtail.yaml
```

Update the suricata job:

```
  - job_name: suricata
    static_configs:
      - targets:
          - localhost
        labels:
          job: suricata
          __path__: /var/log/suricata/eve.json
```

```
sudo systemctl restart promtail
```

Verify `eve.json` content:

```
sudo tail -3 /var/log/suricata/eve.json
```

Each line contains structured fields including `event_type`, `src_ip`, `dest_ip`,
`community_id`, `alert.signature`, `alert.severity`, and `vlan` — far richer than
`fast.log`.

---

## Loki Data Source in Grafana

In Grafana: **Connections → Data Sources → Add data source → Loki**

- URL: `http://localhost:3100`
- Click **Save & Test**

Result: **Data source connected and labels found** — Zeek and Suricata log labels
visible immediately.

---

## First Dashboard

**Dashboards → New → New Dashboard → Add visualization → Loki**

Switch query editor to **Code** mode.

Suricata alerts panel:
```
{job="suricata", filename="/var/log/suricata/fast.log"}
```

Zeek connections panel:
```
{job="zeek", filename="/opt/zeek/logs/current/conn.log"}
```

Visualization type: **Logs** (not Table) — shows raw log stream with timestamps
and colour coding. Table panels are better suited for parsed, structured queries
built later.

The first dashboard immediately showed live Suricata alerts and Zeek connection
logs including DNS queries from `10.0.20.10` (Pi-hole) to upstream resolvers and
SSH session traffic from `10.0.20.227`.

---

## Dashboard Panels

Two dashboards built — **Suricata** and **Zeek** — each as a separate Grafana dashboard.

### Suricata Dashboard

**Alert count by signature over time** — time series showing which rules fire and when:

```
sum by (alert_signature) (count_over_time({job="suricata"} | json | event_type="alert" [5m]))
```

Visualization: **Time series**. Reveals distinct alert categories and traffic pattern
changes — a drop in alerts around a specific time is as interesting as a spike.

**Raw alert log** — formatted log stream for triage:

```
{job="suricata"} | json | event_type="alert" | line_format "{{.timestamp}} {{.src_ip}} {{.dest_ip}} {{.alert_signature}} {{.alert_severity}}"
```

Visualization: **Logs**

### Zeek Dashboard

**Top talkers** — top 10 source IPs by connection count:

```
topk(10, sum by (id_orig_h) (count_over_time({job="zeek", filename=~".*conn.log"} | json | __error__="" [1h])))
```

Visualization: **Bar chart**, horizontal orientation, query **Type: Instant**.
Use **Transformations → Rename by regex** with match `\{id_orig_h="(.+)"\}` and
replace `$1` to show clean IP addresses without the label wrapper.

Observations from first run:

| IP | Connections | Device |
|----|-------------|--------|
| 10.0.20.10 | 7687 | Pi-hole — expected, proxies all DNS |
| 10.0.20.235 | 529 | Device generating QUIC/HTTP3 traffic |
| 10.0.20.216 | 408 | Active wired device |

IPv6 `fe80::` addresses in the list are link-local — LG TV and other devices doing
mDNS discovery.

**DNS query volume over time** — network activity trend:

```
sum(count_over_time({job="zeek", filename=~".*dns.log"} | json | query != "" [5m]))
```

Visualization: **Time series**. A spike at ~08:30 was visible on first run — worth
investigating what triggered it (device waking up, update check, or scheduled task).

**Raw DNS log** — formatted stream:

```
{job="zeek", filename=~".*dns.log"} | json | query != "" | line_format "{{.ts}} {{.id_orig_h}} {{.query}} {{.qtype_name}} {{.rcode_name}}"
```

Visualization: **Logs**

---

## What Failed and Why

| Attempt | What I tried | What happened | Root cause |
|---------|-------------|---------------|------------|
| 1 | Started Loki with default config | `listen tcp :9095: bind: address already in use` | Promtail grabbed port 9095 first. Fixed by setting `grpc_listen_port: 9096` in Loki config |
| 2 | Checked Promtail logs after Loki fix | `connection refused` errors to `localhost:3100` | Historical retry entries from when Loki was down — cleared after Promtail restart |
| 3 | Top talkers query on conn.log | `JSONParserErr: Value looks like object, but can't find closing } symbol` | Zeek's nested JSON objects trip Loki's parser. Fixed by adding `\| __error__=""` filter |

---

## Current State and Next Steps

**Status:** Full stack operational. Grafana at `http://10.0.20.5:3000`. Loki ingesting
logs from Zeek and Suricata via Promtail. 90-day retention configured. First dashboard
live with Suricata fast.log and Zeek conn.log panels.

1. **Baseline normal traffic** — document what regular alert noise looks like on this
   network before building detection rules
2. **DNS bypass detection** — Zeek query to find devices querying `8.8.8.8` or `1.1.1.1`
   directly instead of Pi-hole at `10.0.20.10`, then enforce via MikroTik NAT redirect
3. **Grafana alerting** — configure notifications for high-priority Suricata rules
4. **Custom Zeek scripts** — port scan detection as first detection use case
5. **VLAN 10 management network** — migrate infrastructure management off VLAN 20
6. **IoT device migration** — move LG TV and Overkiz device to VLAN 30
7. **Pi-hole** — Promtail on Raspberry Pi tailing `/var/log/pihole/pihole.log`, shipped to Loki on Shuttle. Adds per-device DNS queries and block events from all VLANs
8. **MikroTik** — native syslog forwarding to Promtail syslog receiver on Shuttle. Adds firewall events, DHCP leases, and authentication events
9. **TP-Link switch** — SNMP exporter on Shuttle polling interface counters. Adds per-port bandwidth and mirror port load — embedded device, Promtail cannot run on it
10. **Shuttle health** — Node Exporter on Shuttle. Adds CPU, RAM, disk and `enp2s0` packet drop counter — critical for detecting sensor overload
