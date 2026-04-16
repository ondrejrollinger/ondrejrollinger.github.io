---
layout: objective
title: "4.9 Investigation Data Sources"
objective_id: "4.9"
domain: "4.0 Security Operations"
status: "done"
tags: ["logs", "forensics", "network-analysis", "SIEM"]
permalink: /objectives/4-9/
---

## Overview

Investigation data sources provide the evidence needed to understand security incidents. This includes log files, network captures, forensic artifacts, and automated scanning results.

---

## Log Files

**System logs:**

**Windows Event Logs:**
- **Security log:** Authentication (Event ID 4624/4625), privilege use
- **System log:** Service starts/stops, driver loading, system errors
- **Application log:** Application-specific events
- **Location:** Event Viewer

**Linux logs:**
- **/var/log/auth.log:** Authentication attempts (SSH, sudo)
- **/var/log/syslog:** General system messages
- **/var/log/secure:** Security-related (RHEL/CentOS)
- **journalctl:** systemd log viewer

**Network device logs:**
- **Firewall:** Allowed/denied connections, rule matches
- **Router/Switch:** Interface status, routing changes, port security violations
- **Wireless:** Client associations, authentication failures
- **VPN:** Remote access sessions, tunnel establishments

**Application logs:**
- **Web server:** Access logs (requests), error logs (failures)
- **Database:** Queries, access patterns, errors
- **Email:** Message delivery, spam filtering, authentication

**Important Windows Event IDs:**
```
Authentication:
- 4624: Successful logon
- 4625: Failed logon
- 4648: Logon using explicit credentials (runas)
- 4768: Kerberos TGT requested
- 4769: Kerberos service ticket requested

Account Management:
- 4720: User account created
- 4722: User account enabled
- 4724: Password reset attempted
- 4728: User added to security-enabled global group
- 4732: User added to security-enabled local group
- 4756: User added to security-enabled universal group

Process/Service:
- 4688: New process created
- 4697: Service installed
- 7045: Service installed (System log)

Object Access:
- 4663: Object accessed (file/folder)
- 5140: Network share accessed
- 5145: Network share object accessed
```

---

## Network Traffic Analysis

**NetFlow/IPFIX:**
- **What it captures:** Metadata (source/dest IP, ports, protocol, bytes transferred)
- **What it doesn't capture:** Actual packet contents
- **Use cases:** Bandwidth analysis, detect data exfiltration, traffic patterns
- **Advantage:** Low overhead (doesn't store full packets)

**Packet capture (PCAP):**
- **Tools:** Wireshark, tcpdump, tshark
- **What it captures:** Full packet contents (headers + payload)
- **Use cases:** Deep protocol analysis, malware communication, credential theft
- **Limitation:** High storage requirements

**Network analysis use cases:**

**Detecting data exfiltration:**
```
NetFlow indicators:
- Large outbound transfer to external IP
- Unusual protocols (DNS with large payloads = tunneling)
- High volume to single destination
- Transfer during off-hours
```

**Malware C2 detection:**
```
Packet analysis:
- Beaconing pattern (regular intervals)
- Connections to newly registered domains
- Unusual user-agent strings
- Encrypted traffic to non-standard ports
```

**Protocol analysis:**
```
Wireshark filters:
http.request.method == "POST" (find POST requests)
dns.qry.name contains "malicious" (DNS queries)
tcp.flags.syn == 1 && tcp.flags.ack == 0 (SYN scans)
ip.src == 192.168.1.100 (filter by source IP)
```

---

## Endpoint Artifacts

**Windows artifacts:**

**Registry:**
- **Run keys:** Programs that auto-start
  - `HKLM\Software\Microsoft\Windows\CurrentVersion\Run`
  - `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`
- **Recently used:** Recent documents, searches
- **USB devices:** History of connected USB drives
- **User accounts:** Account creation dates, last login

**Prefetch:**
- **Location:** `C:\Windows\Prefetch\`
- **Purpose:** Optimize program loading
- **Forensic value:** Proves program executed, execution count, timestamps

**Event logs:**
- Already covered above (Security, System, Application)

**Browser history:**
- **Location:** User profile (AppData)
- **Contains:** URLs visited, downloads, cookies, cache
- **Use:** Identify phishing sites visited, malware downloads

**File system:**
- **MFT (Master File Table):** NTFS metadata, file creation/modification times
- **USN Journal:** Change journal (tracks file system changes)
- **Recycle Bin:** Deleted files (may contain evidence)

**Memory artifacts:**
- **Running processes:** Active malware
- **Network connections:** Active C2 communication
- **Loaded DLLs:** Injected malicious code
- **Passwords:** Credentials in memory

**Linux artifacts:**

**Shell history:**
- **Location:** `~/.bash_history`, `~/.zsh_history`
- **Contains:** Commands executed by user
- **Forensic value:** Attacker commands, lateral movement

**Cron jobs:**
- **Location:** `/etc/crontab`, `/var/spool/cron/`
- **Purpose:** Scheduled tasks
- **Forensic value:** Persistence mechanisms

**Authentication logs:**
- **/var/log/auth.log:** SSH logins, sudo usage
- **/var/log/wtmp:** Login history
- **/var/log/lastlog:** Last login per user

**Package manager logs:**
- **APT:** `/var/log/apt/history.log` (installed packages)
- **YUM:** `/var/log/yum.log`
- **Forensic value:** Attacker-installed tools

---

## Automated Reports and Dashboards

**Vulnerability scan results:**
- **Source:** Nessus, OpenVAS, Qualys
- **Contains:** Vulnerabilities found, severity (CVSS), affected systems
- **Use:** Prioritize patching, identify attack vectors

**SIEM dashboards:**
- **Real-time monitoring:** Current threat activity
- **Historical trends:** Security posture over time
- **Compliance reports:** PCI, HIPAA, SOX reporting

**Key metrics to display:**

**Security Operations Center (SOC):**
```
Operational metrics:
- Alerts per day (volume)
- Mean time to detect (MTTD)
- Mean time to respond (MTTR)
- Open incidents (current workload)
- False positive rate (tuning effectiveness)

Threat landscape:
- Top attacked systems
- Top attack types (malware, brute force, etc.)
- Geographic source of attacks
- Blocked vs allowed connections
```

**Executive dashboard:**
```
High-level metrics:
- Security posture score (0-100)
- Critical vulnerabilities (count)
- Open high-severity incidents
- Compliance status (% compliant)
- Trend: Improving or declining?
```

**Automated report examples:**

**Daily Security Summary:**
- New incidents created
- Incidents closed
- Critical alerts
- Failed login summary
- Top talkers (most active systems)

**Weekly Vulnerability Report:**
- New vulnerabilities discovered
- Remediation progress
- Overdue patches
- Systems missing critical updates

**Monthly Compliance Report:**
- PCI DSS compliance status
- HIPAA audit trail
- SOX controls validation
- Policy violations

---

## Metadata

**Definition:** Data about data

**File metadata:**
- **Creation time:** When file created
- **Modification time:** When last changed
- **Access time:** When last opened
- **Owner:** User who owns file
- **Permissions:** Read/write/execute for user/group/others
- **File size:** Bytes
- **File type:** Extension, MIME type

**Email metadata:**
- **From/To:** Sender and recipient
- **Subject:** Email subject line
- **Date/Time:** When sent
- **Message-ID:** Unique identifier
- **X-headers:** Routing information, spam scores, authentication results

**Image metadata (EXIF):**
- **Camera make/model:** Device used
- **GPS coordinates:** Where photo taken
- **Date/Time:** When photo taken
- **Forensic value:** Prove photo location/time, identify device

**Document metadata:**
- **Author:** Who created document
- **Created/Modified:** Timestamps
- **Application:** Software used (Word, PDF creator)
- **Forensic value:** Identify document source

**Metadata analysis example:**
```
Incident: Leaked confidential document

Metadata examination:
- Author: john.doe
- Created: 2024-04-10 15:32:18
- Last modified: 2024-04-11 09:15:42
- Application: Microsoft Word 2019
- File path: C:\Users\john.doe\Documents\Confidential\Q2_Strategy.docx

Conclusion:
- John Doe created document (insider threat investigation)
- Modified day before leak (timing)
- File path shows it was in Confidential folder (unauthorized disclosure)
```

---

## Threat Feeds and Intelligence

**Threat intelligence sources:**

**Open-source:**
- AlienVault OTX (Open Threat Exchange)
- Abuse.ch (malware samples, C2 IPs)
- MISP (Malware Information Sharing Platform)
- US-CERT alerts

**Commercial:**
- Recorded Future
- ThreatConnect
- Mandiant Threat Intelligence
- CrowdStrike Threat Graph

**Intelligence types:**

**Indicators of Compromise (IOCs):**
- **File hashes:** MD5, SHA-1, SHA-256 of known malware
- **IP addresses:** Known C2 servers, malicious hosts
- **Domains:** Phishing sites, malware distribution
- **URLs:** Specific malicious links
- **Email addresses:** Phishing sender addresses

**Tactics, Techniques, and Procedures (TTPs):**
- **MITRE ATT&CK framework:** Catalog of adversary behaviors
- **Example TTP:** "T1078 - Valid Accounts" (attacker using stolen credentials)
- **Use:** Detect attack patterns, not just specific indicators

**Threat intelligence use cases:**

**Proactive blocking:**
```
Threat feed: List of known malicious IPs

Integration:
1. SIEM ingests threat feed
2. Firewall automatically blocks IPs from feed
3. IDS/IPS signatures updated
4. Email gateway blocks domains

Result: Prevent known threats before they reach network
```

**Enrichment:**
```
Alert: Connection to 203.0.113.45

Threat intel lookup:
- IP reputation: Known C2 server (APT28)
- First seen: 2024-03-15
- Associated malware: Fancy Bear toolkit
- Geographic location: Russia

Enriched alert:
"Connection to KNOWN C2 (APT28), high confidence malicious"
vs
"Connection to 203.0.113.45" (no context)

Result: Better prioritization, faster response
```

---

## Key Distinctions

**NetFlow vs Packet Capture:**
- NetFlow: Metadata only (who, when, how much)
- Packet capture: Full content (what was said)

**Event logs vs Syslog:**
- Event logs: Windows (Event Viewer)
- Syslog: Linux/Unix standard logging

**IOC vs TTP:**
- IOC: Specific indicator (file hash, IP)
- TTP: Behavior pattern (attack technique)

**Metadata vs Data:**
- Metadata: Information about file (creation time, author)
- Data: Actual file contents

---

## Common Exam Traps

1. **Trap:** Thinking NetFlow captures full packet contents
   - **Reality:** NetFlow is metadata only (need PCAP for full content)

2. **Trap:** Believing deleted files are unrecoverable
   - **Reality:** Recycle Bin, volume shadow copies, forensic tools can recover

3. **Trap:** Assuming logs are always accurate
   - **Reality:** Logs can be tampered with (need log integrity protection)

4. **Trap:** Thinking threat intelligence eliminates need for detection
   - **Reality:** Feeds provide IOCs, still need detection rules

5. **Trap:** Believing metadata is less important than file contents
   - **Reality:** Metadata often reveals more (who created, when, where)

---

## Exam Tips

1. **Windows Event 4624** = successful logon
2. **Windows Event 4625** = failed logon  
3. **NetFlow = metadata** (not full packets)
4. **Packet capture = full content** (headers + payload)
5. **Prefetch proves** program executed on Windows
6. **Metadata includes** creation time, author, location
7. **IOCs = specific indicators** (hash, IP)
8. **TTPs = behavior patterns** (attack techniques)
9. **Order of volatility:** RAM first, disk later
10. **Threat intelligence enriches** alerts with context

---

## Quick Navigation
- [← Previous: 4.8 Incident Response](../4-8/)
- [↑ Back to Domain 4](../)
- [⌂ Home](/)
