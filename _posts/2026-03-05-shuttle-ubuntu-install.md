---
layout: post
title: "Ubuntu Server Installation on Shuttle DL30N"
date: 2026-03-05
toc: true
tags: [lab, ubuntu, shuttle, ssh, networking]
summary: >
  Installing Ubuntu Server 24.04 LTS on the Shuttle DL30N security sensor.
  Covers bootable USB creation from Kali, OS installation, static IP via
  netplan, SSH key-based authentication, and DNS verification via Pi-hole.
---

## Why This Post Exists

The Shuttle DL30N is the dedicated security sensor for this lab — running Zeek, Suricata,
and the Grafana stack. Before any of that can happen, it needs a clean OS install, remote
management via SSH, and a stable static IP on the management VLAN.

This post covers the full process from creating the bootable USB on Kali through to a
verified, hardened SSH connection.

---

## Creating a Bootable USB from Kali

The goal is to flash an Ubuntu Server ISO to a USB drive without any GUI tools directly from the Kali terminal.

### Identifying the USB Drive

```
lsblk
lsusb
```

`lsblk` shows block devices with sizes — easiest way to spot the USB drive. `lsusb`
confirms the device manufacturer.

```
ondrej@kali:~$ lsblk
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda      8:0    0   1.8T  0 disk
sdb      8:16   0 232.9G  0 disk   # internal SSD — Kali system
sdc      8:32   1  28.7G  0 disk   # ← USB drive
└─sdc1   8:33   1  28.7G  0 part

ondrej@kali:~$ lsusb
Bus 002 Device 002: ID 0781:55ab SanDisk Corp.  SanDisk 3.2Gen1
```

`sdc` confirmed as the 28.7GB SanDisk. `sda` and `sdb` are internal — do not touch these.

### Flashing the ISO

```
sudo dd if=/home/ondrej/Downloads/ubuntu-24.04.4-live-server-amd64.iso \
         of=/dev/sdc \
         bs=4M status=progress oflag=sync
```

Important: target the device (`/dev/sdc`), not a partition (`/dev/sdc1`).

```
3405469696 bytes (3.4 GB, 3.2 GiB) copied, 142 s, 24.0 MB/s
811+1 records in
811+1 records out
3405469696 bytes (3.4 GB, 3.2 GiB) copied, 142.689 s, 23.9 MB/s
```

3.4GB written at ~24 MB/s. Then eject safely:

```
sudo eject /dev/sdc
```

---

## Ubuntu Version Choice

**Decision: 24.04.4 LTS.** For a long-running home lab sensor, LTS is the right call.
Zeek and Suricata both have official packages and PPA support targeting Ubuntu, and most
security tool documentation assumes Ubuntu specifically. The stability and longevity of
LTS matters more than the newer packages in 25.10.

---

## Installation

Boot the Shuttle from the USB (F7 at POST for boot menu). GRUB menu appeared cleanly:

- Selected: **Try or Install Ubuntu Server**
- Language: English
- Network: DHCP on `enp1s0` (temporary — static IP configured post-install)
- Storage: Full 1TB NVMe, LVM
- Profile: username `ondrej`, hostname `shuttle`
- **OpenSSH server: enabled during install** — critical for headless management

---

## Post-Install: SSH and Static IP

After first boot, the Shuttle was accessible via DHCP-assigned address. Confirmed SSH
was running:

```
sudo systemctl enable ssh
sudo systemctl start ssh
ip a show enp1s0
```

Identified IP `10.0.20.221` — temporary DHCP address. Connected from Kali:

```
ssh ondrej@10.0.20.221
```

### Setting a Static IP via Netplan

The Shuttle sits on VLAN 20 (trusted devices) at `10.0.20.5`. Infrastructure IP
assignments:

| IP | Device |
|----|--------|
| `10.0.20.1` | MikroTik gateway |
| `10.0.20.5` | Shuttle sensor (this device) |
| `10.0.20.10` | Pi-hole |

```
sudo nano /etc/netplan/50-cloud-init.yaml
```

```
network:
  version: 2
  ethernets:
    enp1s0:
      dhcp4: false
      addresses:
        - 10.0.20.5/24
      routes:
        - to: default
          via: 10.0.20.1
      nameservers:
        addresses:
          - 10.0.20.10
          - 1.1.1.1
    enp2s0:
      dhcp4: false
      match:
        macaddress: 80:ee:73:xx:xx:xx
      set-name: enp2s0
```

Pi-hole is primary DNS, Cloudflare as fallback. `enp2s0` is declared with no IP —
the monitoring interface, configured later.

```
sudo netplan apply
```

SSH session dropped (IP changed). Reconnected immediately to `10.0.20.5`.

### Verification

```
ping -c 3 10.0.20.1    # gateway
ping -c 3 1.1.1.1      # internet
ping -c 3 google.com   # DNS resolution
```

```
64 bytes from 10.0.20.1: icmp_seq=1 ttl=64 time=0.280 ms
64 bytes from 1.1.1.1: icmp_seq=1 ttl=55 time=3.46 ms
64 bytes from lbg02s03-in-f14.1e100.net: icmp_seq=1 ttl=113 time=122 ms
```

All three pass. DNS confirmed via Pi-hole:

```
resolvectl status | grep "DNS Server"
```

```
Current DNS Server: 10.0.20.10
       DNS Servers: 10.0.20.10 1.1.1.1
```

---

## SSH Key Auth and Hardening

### Generate Key on Kali

```
ssh-keygen -t ed25519 -C "kali-to-shuttle"
```

### Copy to Shuttle

```
ssh-copy-id -i ~/.ssh/id_ed25519.pub ondrej@10.0.20.5
```

### Test Key Login

```
ssh -i ~/.ssh/id_ed25519 ondrej@10.0.20.5
```

Confirmed working. Then disabled password authentication on the Shuttle:

```
sudo nano /etc/ssh/sshd_config
```

```
PasswordAuthentication no
PubkeyAuthentication yes
```

```
sudo systemctl restart ssh
```

Tested from a new terminal before closing existing session — key-only login confirmed.

### SSH Config Shortcut on Kali

```
nano ~/.ssh/config
```

```
Host shuttle
    HostName 10.0.20.5
    User ondrej
    IdentityFile ~/.ssh/id_ed25519
```

From this point: `ssh shuttle` connects directly, no flags needed.

---

## DNS Verification

`nslookup` shows `127.0.0.53` as the server — this is systemd-resolved's local stub,
not an indication that Pi-hole is being bypassed. The stub forwards to the configured
upstream, confirmed by:

```
resolvectl status | grep "DNS Server"
```

```
Current DNS Server: 10.0.20.10
       DNS Servers: 10.0.20.10 1.1.1.1
```

Queries from `10.0.20.5` appear in Pi-hole's query log as expected.

---

## What Failed and Why

| Attempt | What I tried | What happened | Root cause |
|---------|-------------|---------------|------------|
| 1 | SSH before enabling the service | Connection refused | OpenSSH not started post-install |

---

## Current State and Next Steps

**Status:** Operational. Shuttle is reachable at `10.0.20.5` via key-based SSH from Kali.
Password auth disabled. Static IP persistent across reboots. DNS via Pi-hole confirmed.

1. **Configure enp2s0** as passive monitoring interface — no IP, promiscuous mode
2. **Connect to TP-Link switch mirror port** and verify traffic is received via tcpdump
3. **Connect to MikroTik ether3** as VLAN 20 access port
4. **Install Zeek and Suricata**
