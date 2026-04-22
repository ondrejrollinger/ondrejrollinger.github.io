---
layout: objective
title: "Security+ 4.9 — Given a scenario, use data sources to support an investigation."
objective_id: "4.9"
domain: "4.0 Security Operations"
status: "done"
tags:
  - secplus701
permalink: /secplus/objectives/4-9/
---

# Security+ 4.9 — Given a scenario, use data sources to support an investigation.

Status: <span class="status-badge done">done</span>

## Exam objective
Given a scenario, use data sources to support an investigation.

{% assign objective_slug = page.slug %}
{% if objective_slug == nil or objective_slug == '' or objective_slug == 'index' %}
  {% assign url_parts = page.url | split: '/' %}
  {% assign objective_slug = url_parts | last %}
  {% if objective_slug == '' %}
    {% assign objective_slug = url_parts | slice: -2, 1 | first %}
  {% endif %}
{% endif %}
{% assign objective_id = objective_slug | replace: '-', '.' %}
{% include official_scope_pdf.html objective_id=objective_id %}

---

## My notes

### Overview

Investigation data sources provide the evidence needed to understand security incidents. This includes log files, network captures, forensic artifacts, and automated scanning results. The exam tests your ability to select the *right* data source for a given investigation scenario — knowing what each source captures (and what it does not) is essential.

---

### Log files

#### Windows Event Logs

| Log | Purpose | Key Event IDs |
|---|---|---|
| **Security log** | Authentication, privilege use, object access | 4624, 4625, 4648, 4720, 4732 |
| **System log** | Service starts/stops, driver loading, errors | 7045 (service installed) |
| **Application log** | Application-specific events | Varies by application |

**Key Windows Event IDs to memorize:**

| Event ID | Meaning | Category |
|---|---|---|
| **4624** | Successful logon | Authentication |
| **4625** | Failed logon | Authentication |
| **4648** | Logon using explicit credentials (runas) | Authentication |
| **4768** | Kerberos TGT requested | Authentication |
| **4769** | Kerberos service ticket requested | Authentication |
| **4720** | User account created | Account management |
| **4722** | User account enabled | Account management |
| **4724** | Password reset attempted | Account management |
| **4728** | User added to security-enabled global group | Account management |
| **4732** | User added to security-enabled local group | Account management |
| **4756** | User added to security-enabled universal group | Account management |
| **4688** | New process created | Process/service |
| **4697** | Service installed | Process/service |
| **7045** | Service installed (System log) | Process/service |
| **4663** | Object accessed (file/folder) | Object access |
| **5140** | Network share accessed | Object access |
| **5145** | Network share object accessed | Object access |

> **Exam tip:** 4624 = successful logon; 4625 = failed logon. These two are the most tested. A spike in 4625 followed by a single 4624 is a classic brute-force success pattern.

#### Linux logs

| Log path | Purpose |
|---|---|
| **/var/log/auth.log** | Authentication attempts (SSH, sudo) — Debian/Ubuntu |
| **/var/log/secure** | Security-related events — RHEL/CentOS |
| **/var/log/syslog** | General system messages |
| **/var/log/wtmp** | Login history (binary; read with `last`) |
| **/var/log/lastlog** | Last login per user |

#### Network device logs

| Source | What it captures |
|---|---|
| **Firewall** | Allowed/denied connections, rule matches |
| **Router/Switch** | Interface status, routing changes, port security violations |
| **Wireless** | Client associations, authentication failures |
| **VPN** | Remote access sessions, tunnel establishments |

#### Application logs

| Log type | Investigative value |
|---|---|
| **Web server (access log)** | All HTTP requests — source IP, URL, response code, user-agent |
| **Web server (error log)** | Failed requests, application errors |
| **Database** | Queries, access patterns — detect SQLi or unauthorized access |
| **Email** | Message delivery, spam filtering, authentication results |

---

### Network traffic analysis

| Tool / Technology | What it captures | What it does NOT capture |
|---|---|---|
| **NetFlow / IPFIX** | Metadata: source/dest IP, ports, protocol, bytes transferred, duration | Actual packet contents |
| **Packet capture (PCAP)** | Full packet contents: headers + payload | Nothing — captures everything |
| **Wireshark** | Full packet inspection with protocol decode | Requires PCAP file or live capture |
| **tcpdump / tshark** | Command-line PCAP capture and filter | GUI analysis |

**NetFlow use cases:**
- Detect data exfiltration (large outbound transfer to external IP)
- Identify DNS tunneling (DNS queries with unusually large payloads)
- Spot off-hours traffic patterns
- Map lateral movement between internal systems

**Packet capture use cases:**
- Deep protocol analysis
- Detect malware C2 beaconing (regular-interval connections to external host)
- Capture credentials sent over unencrypted protocols
- Analyse unusual user-agent strings or non-standard port usage

**Common Wireshark display filters:**

| Filter | Purpose |
|---|---|
| `http.request.method == "POST"` | Find HTTP POST requests (data submissions) |
| `dns.qry.name contains "suspect"` | Find DNS queries for a specific domain |
| `tcp.flags.syn == 1 && tcp.flags.ack == 0` | Detect SYN scan (no ACK = incomplete handshake) |
| `ip.src == 192.168.1.100` | Filter traffic from a specific source IP |

> **Exam tip:** NetFlow = metadata only (who talked to whom, how much). Packet capture = full content (what was said). If a question asks about detecting exfiltration volume, NetFlow is sufficient. If it asks about recovering credentials or payload content, you need PCAP.

---

### Endpoint artifacts

#### Windows artifacts

| Artifact | Location | Forensic value |
|---|---|---|
| **Registry Run keys** | `HKLM\...\CurrentVersion\Run` / `HKCU\...\CurrentVersion\Run` | Persistence — programs set to auto-start |
| **Prefetch** | `C:\Windows\Prefetch\` | Proves a program was executed; includes execution count and timestamps |
| **Browser history** | `%AppData%\` (varies by browser) | URLs visited, downloads, cookies, cached pages |
| **MFT (Master File Table)** | NTFS volume metadata | File creation, modification, and access timestamps |
| **USN Journal** | NTFS change journal | Tracks all file system changes — even deleted files |
| **Recycle Bin** | `C:\$Recycle.Bin\` | Deleted files that were not permanently wiped |

**Memory artifacts (volatile — collected first):**
- Running processes — may reveal active malware with no disk footprint
- Open network connections — active C2 communication
- Loaded DLLs — injected malicious code
- Plaintext credentials — passwords or tokens cached in memory

> **Exam tip:** Prefetch files prove a program was executed on Windows even if the executable has been deleted. This is a key artifact for proving attacker tool usage.

#### Linux artifacts

| Artifact | Location | Forensic value |
|---|---|---|
| **Shell history** | `~/.bash_history`, `~/.zsh_history` | Commands executed by the user — attacker commands, lateral movement |
| **Cron jobs** | `/etc/crontab`, `/var/spool/cron/` | Scheduled tasks — persistence mechanisms |
| **APT package log** | `/var/log/apt/history.log` | Packages installed — attacker-installed tools |
| **YUM log** | `/var/log/yum.log` | Same for RHEL/CentOS systems |
| **Auth log** | `/var/log/auth.log` | SSH logins, sudo usage |

> **Exam tip:** Order of volatility — collect RAM (most volatile) before disk, and disk before network metadata. This is fundamental to forensic integrity.

---

### Automated reports and dashboards

#### Vulnerability scan results

Sources: Nessus, OpenVAS, Qualys

| Field | Purpose |
|---|---|
| **Vulnerability name** | Identifies the specific CVE or finding |
| **CVSS score / severity** | Prioritises remediation (Critical/High/Medium/Low) |
| **Affected systems** | Scope of exposure |
| **Remediation recommendation** | Patch, configuration change, or workaround |

#### SIEM dashboards

| Dashboard type | Key metrics shown |
|---|---|
| **SOC operational** | Alerts per day, MTTD, MTTR, open incidents, false positive rate |
| **Threat landscape** | Top attacked systems, top attack types, geographic attack sources |
| **Executive / compliance** | Security posture score, critical vuln count, compliance status (PCI, HIPAA, SOX) |

**Common automated report types:**

| Report | Frequency | Contents |
|---|---|---|
| **Daily security summary** | Daily | New incidents, critical alerts, failed login summary, top talkers |
| **Vulnerability report** | Weekly | New vulns, remediation progress, overdue patches |
| **Compliance report** | Monthly | PCI DSS status, HIPAA audit trail, SOX controls, policy violations |

> **Exam tip:** MTTD (Mean Time to Detect) and MTTR (Mean Time to Respond) are the key SOC metrics used to evaluate incident response effectiveness.

---

### Metadata

**Definition:** Data *about* data — descriptive information attached to a file, image, or message rather than the primary content itself.

| Metadata type | Key fields | Forensic value |
|---|---|---|
| **File metadata** | Creation time, modification time, access time, owner, permissions, size | Establishes timeline; identifies who created or modified a file |
| **Email metadata** | From/To, Subject, Date, Message-ID, X-headers (routing, spam score, auth results) | Traces message path; identifies spoofing or forged headers |
| **Image (EXIF)** | Camera make/model, GPS coordinates, date/time taken | Places a photo at a specific location and time; identifies device |
| **Document metadata** | Author, created/modified timestamps, application used | Identifies document creator; may reveal internal usernames |

> **Exam tip:** Metadata often reveals more than the file contents themselves. GPS coordinates in a photo, the author field in a Word document, or email routing headers are all examples of metadata with high investigative value.

---

### Threat intelligence feeds

#### Intelligence sources

| Type | Examples |
|---|---|
| **Open-source (OSINT)** | AlienVault OTX, Abuse.ch, MISP, US-CERT alerts |
| **Commercial** | Recorded Future, ThreatConnect, Mandiant, CrowdStrike Threat Graph |

#### Intelligence types

| Type | Description | Example |
|---|---|---|
| **Indicators of Compromise (IOCs)** | Specific, observable artifacts linked to known malicious activity | File hashes (MD5/SHA-256), malicious IPs, phishing domains, URLs |
| **Tactics, Techniques, and Procedures (TTPs)** | Behavioral patterns describing *how* an attacker operates | MITRE ATT&CK T1078 "Valid Accounts" — attacker using stolen credentials |

**How threat intelligence is used:**

- **Proactive blocking:** Threat feeds ingested by SIEM/firewall to auto-block known malicious IPs and domains before they reach the network.
- **Alert enrichment:** A bare IP address in an alert is cross-referenced against threat intel to reveal it is a known APT C2 server — context that drives faster, better-prioritised response.
- **Signature updates:** IDS/IPS rules and email gateway filters updated from feed data.

> **Exam tip:** IOCs identify *specific* known-bad artifacts (a hash, an IP). TTPs describe *how* attackers behave and are more durable — attackers change IPs frequently, but their techniques change slowly.

---

### Key distinctions to know for the exam

| Comparison | Distinction |
|---|---|
| **NetFlow vs. packet capture** | NetFlow = metadata only (who, when, how much); PCAP = full packet content (what was said) |
| **Windows Event Log vs. Syslog** | Event logs are the Windows standard (Event Viewer); Syslog is the Linux/Unix standard logging facility |
| **IOC vs. TTP** | IOC = specific observable artifact (hash, IP, domain); TTP = behavioral pattern (attack technique) |
| **Metadata vs. file content** | Metadata = information *about* the file (author, timestamps, GPS); content = what is inside the file |
| **4624 vs. 4625** | 4624 = successful logon; 4625 = failed logon |
| **Prefetch vs. MFT** | Prefetch proves *execution* of a program; MFT tracks file creation/modification/access timestamps |
| **MTTD vs. MTTR** | MTTD = Mean Time to Detect (how long until the incident was found); MTTR = Mean Time to Respond (how long to contain/resolve) |

---

### Common exam traps

**Trap:** Assuming NetFlow captures full packet contents.
**Reality:** NetFlow is metadata only — source/destination, ports, bytes, and duration. You need a full packet capture (PCAP) to recover payload content or credentials.

**Trap:** Believing deleted files are unrecoverable.
**Reality:** The Recycle Bin, NTFS USN Journal, volume shadow copies, and forensic tools can often recover deleted files unless they have been securely wiped.

**Trap:** Treating all logs as trustworthy by default.
**Reality:** Logs can be tampered with by an attacker who has compromised the system. Log integrity protection (write-once storage, SIEM forwarding in real time) is necessary to establish evidentiary value.

**Trap:** Thinking threat intelligence feeds replace detection rules.
**Reality:** Feeds provide IOCs for known threats. Novel or unknown attacks still require behavioral detection rules, anomaly detection, and human analysis.

**Trap:** Believing metadata is less important than file contents.
**Reality:** Metadata frequently reveals more — a document's author field, a photo's GPS coordinates, or an email's routing headers can definitively identify origin, location, and timing.

**Trap:** Confusing MTTD and MTTR.
**Reality:** MTTD measures how long it took to *find* the incident; MTTR measures how long it took to *fix* it. Both are key SOC performance metrics but measure different phases.

---

### Exam tips

1. **Event ID 4624** = successful logon
2. **Event ID 4625** = failed logon
3. **NetFlow = metadata** (source, destination, bytes — not content)
4. **Packet capture = full content** (headers + payload)
5. **Prefetch proves** a program was executed on Windows
6. **Metadata includes** author, creation time, GPS — data *about* data
7. **IOCs = specific indicators** (hash, IP, domain)
8. **TTPs = behavioral patterns** (attack techniques, MITRE ATT&CK)
9. **Order of volatility:** RAM first, then disk, then network metadata
10. **Threat intelligence enriches** alerts with context — turning a bare IP into a known APT C2
11. **MTTD** = time to detect; **MTTR** = time to respond

---

## Key terms

- **NetFlow / IPFIX** — A network protocol that captures flow metadata (IP addresses, ports, bytes, duration) without recording packet contents.
- **Packet capture (PCAP)** — A full recording of network packets, including headers and payload; captured via tools such as Wireshark or tcpdump.
- **Syslog** — The standard logging protocol used by Linux/Unix systems and network devices; forwards log messages to a central collector.
- **Windows Event Log** — The Windows logging subsystem; records security, system, and application events accessible via Event Viewer.
- **Prefetch** — Windows files in `C:\Windows\Prefetch\` that record program execution history, including execution count and last-run timestamps.
- **MFT (Master File Table)** — The NTFS metadata store that records file creation, modification, and access timestamps for every file on a volume.
- **Metadata** — Data that describes other data — file creation time, document author, image GPS coordinates — rather than the primary content.
- **IOC (Indicator of Compromise)** — A specific, observable artifact associated with malicious activity: a file hash, IP address, domain, or URL.
- **TTP (Tactics, Techniques, and Procedures)** — Behavioral descriptions of how an attacker operates; catalogued in the MITRE ATT&CK framework.
- **SIEM (Security Information and Event Management)** — A platform that aggregates logs from multiple sources, correlates events, and generates alerts.
- **Threat intelligence feed** — A regularly updated stream of IOCs and threat data from commercial or open-source providers used to enrich detection and blocking.
- **MTTD (Mean Time to Detect)** — The average time between an incident occurring and it being identified by the security team.
- **MTTR (Mean Time to Respond)** — The average time between incident detection and full containment or resolution.
- **Order of volatility** — The principle that the most transient evidence (RAM) must be collected before less volatile evidence (disk, logs) during forensic investigation.
- **EXIF (Exchangeable Image File Format)** — Metadata embedded in image files recording camera details, date/time, and often GPS coordinates.

---

## Examples / scenarios

**Scenario 1:** An analyst is investigating a suspected insider threat. HR wants to know who created a sensitive document that was leaked externally.
- **Answer:** Examine the document's metadata — specifically the Author field, Created timestamp, and Last Modified timestamp. These can identify the creating user and the timeline of access without needing to inspect file contents.

**Scenario 2:** The SOC receives an alert that a workstation communicated with an external IP for 45 minutes, transferring 2.1 GB of data. The analyst needs to confirm whether sensitive data was included.
- **Answer:** NetFlow confirms the volume and destination, but to determine *what* was transferred, a full packet capture (PCAP) is needed. NetFlow alone cannot prove data content.

**Scenario 3:** A threat hunter suspects a host was compromised three weeks ago. The suspected malware binary has since been deleted from disk.
- **Answer:** Check Prefetch files — they record program execution history even after the executable is deleted, proving the program ran and capturing timestamps. Also check the USN Journal for file system change records.

**Scenario 4:** An analyst receives an alert: "Connection to 198.51.100.22." With no other context, it is unclear whether this is malicious.
- **Answer:** Enrich the alert using a threat intelligence feed. If the IP is a known C2 server associated with a threat actor, the alert becomes high-confidence malicious. TTPs from MITRE ATT&CK can further describe the threat actor's behavior.

**Scenario 5:** A security manager wants to evaluate how quickly the SOC is detecting and resolving incidents over time.
- **Answer:** Review MTTD (Mean Time to Detect) and MTTR (Mean Time to Respond) trends from the SIEM dashboard. These are the key operational metrics for measuring detection and response efficiency.

---

## Mini quiz

<details>
<summary><strong>Question 1:</strong> What is the difference between NetFlow and a packet capture, and when would you choose each?</summary>

**Answer:** NetFlow captures metadata only — source/destination IP, ports, protocol, bytes transferred, and duration. It does not record packet contents. A packet capture (PCAP) records full packet headers and payloads. Choose NetFlow for bandwidth analysis, detecting exfiltration by volume, or mapping traffic patterns. Choose PCAP when you need to recover actual content — credentials sent in cleartext, malware payload, or specific data in a transaction.
</details>

<details>
<summary><strong>Question 2:</strong> What do Windows Prefetch files prove, and why are they useful in investigations?</summary>

**Answer:** Prefetch files prove that a specific program was executed on the system. They record the program name, number of executions, and the last several execution timestamps. Forensically, they are valuable because they persist even after the executable is deleted — allowing an investigator to prove tool usage by an attacker who tried to cover their tracks.
</details>

<details>
<summary><strong>Question 3:</strong> What is the difference between an IOC and a TTP?</summary>

**Answer:** An IOC (Indicator of Compromise) is a specific, observable artifact — a file hash, IP address, domain, or URL — associated with known malicious activity. A TTP (Tactic, Technique, Procedure) describes *how* an attacker behaves — for example, using valid credentials to move laterally. IOCs change frequently (attackers rotate IPs and domains); TTPs are more stable and therefore more durable for detection.
</details>

<details>
<summary><strong>Question 4:</strong> Why must logs be treated with caution as evidence in a forensic investigation?</summary>

**Answer:** Logs can be tampered with by an attacker who has gained sufficient access to the system. An attacker may delete or modify log entries to hide their activity. To establish evidentiary integrity, logs should be forwarded in real time to a SIEM or write-once storage that the attacker cannot access — ensuring the log record cannot be retroactively altered.
</details>

<details>
<summary><strong>Question 5:</strong> What is the order of volatility and why does it matter?</summary>

**Answer:** The order of volatility refers to how quickly different types of evidence disappear. RAM (running processes, open connections, credentials in memory) is the most volatile and must be captured first. Disk artifacts (files, logs, Prefetch) are less volatile. Remote logs and network metadata are the least volatile. Collecting in the wrong order risks losing critical evidence that cannot be recovered once power is removed or the system is rebooted.
</details>

### CompTIA-style practice questions

<details>
<summary><strong>Question 6:</strong> A security analyst is investigating a data breach and needs to determine the exact content of data sent from a workstation to an external server last Tuesday. Which data source would BEST provide this information?<br>A. NetFlow records<br>B. SIEM dashboard alerts<br>C. Full packet capture (PCAP)<br>D. Windows Event Log</summary>

**Correct Answer: C. Full packet capture (PCAP)**

Only a full packet capture records the actual payload of network communications. NetFlow captures metadata (who, when, how much) but not content. SIEM dashboards aggregate alerts, not raw packet data. Windows Event Logs record system events, not network payload content.

- A: NetFlow would show the transfer occurred and its volume — but not *what* was sent.
- B: SIEM alerts are derived from log correlation; they do not contain raw packet content.
- D: Event Logs record authentication, service, and object-access events — not network payload.
</details>

<details>
<summary><strong>Question 7:</strong> An investigator is examining a Windows workstation and suspects that malware was executed and then deleted to cover its tracks. Which artifact would BEST confirm that the malware was actually run on the system?<br>A. Windows Registry Run keys<br>B. Prefetch files<br>C. Browser history<br>D. Event ID 4625</summary>

**Correct Answer: B. Prefetch files**

Prefetch files record program execution history including program name, execution count, and timestamps — and persist even after the executable has been deleted. This makes them the best artifact for proving execution of a deleted program.

- A: Registry Run keys show programs *configured* to auto-start, not necessarily whether they ran.
- C: Browser history records web activity, not program execution.
- D: Event ID 4625 records failed logon attempts — unrelated to program execution.
</details>

<details>
<summary><strong>Question 8 (Multi-select):</strong> A SOC analyst receives an alert containing only an unfamiliar external IP address. Which TWO actions would BEST help the analyst determine whether this connection is malicious? (Select TWO.)<br>A. Check NetFlow records for the volume of data transferred to the IP<br>B. Look up the IP in a threat intelligence feed to identify known associations<br>C. Review the SIEM compliance dashboard<br>D. Examine EXIF metadata from recent image files<br>E. Analyse full packet capture of the connection for payload content</summary>

**Correct Answers: B and E**

Enriching the alert with threat intelligence (B) provides context — known threat actor, C2 classification, or reputation score. Packet capture (E) reveals what was actually communicated, confirming or ruling out malicious activity.

- A: NetFlow confirms volume and duration but not whether the communication was malicious.
- C: Compliance dashboards track regulatory posture, not individual IP reputation.
- D: EXIF metadata is relevant to image forensics, not network connection analysis.
</details>

<details>
<summary><strong>Question 9:</strong> A security manager reviews a report showing the average time between when an attacker first gains access and when the SOC identifies the breach is 12 days. Which metric does this represent?<br>A. MTTR<br>B. RPO<br>C. MTTD<br>D. RTO</summary>

**Correct Answer: C. MTTD**

MTTD (Mean Time to Detect) measures the average time between an incident occurring and the security team identifying it. The 12-day figure describes detection latency, not response time.

- A: MTTR (Mean Time to Respond) measures the time from detection to resolution — not discovery.
- B: RPO (Recovery Point Objective) relates to acceptable data loss in a disaster recovery context.
- D: RTO (Recovery Time Objective) defines the maximum acceptable downtime for a system after failure.
</details>

---

## Related objectives

- [**4.4**]({{ '/secplus/objectives/4-4/' | relative_url }}) — Security alerting and monitoring tools (SIEM, IDS/IPS) are the collection layer that generates the data sources used here.
- [**4.8**]({{ '/secplus/objectives/4-8/' | relative_url }}) — Incident response activities define the process that consumes these data sources during investigation.
- [**2.4**]({{ '/secplus/objectives/2-4/' | relative_url }}) — Indicators of malicious activity describe the patterns that investigators look for across these data sources.
- [**1.3**]({{ '/secplus/objectives/1-3/' | relative_url }}) — Change management and data classification affect how logs and metadata are retained and protected.

---

## Navigation

**Domain 4.0: Security Operations**

| Objective | Title | Status |
|---|---|---|
| [4.1]({{ '/secplus/objectives/4-1/' | relative_url }}) | Given a scenario, apply common security techniques to computing resources. | done |
| [4.2]({{ '/secplus/objectives/4-2/' | relative_url }}) | Explain the security implications of proper hardware, software, and data asset management. | done |
| [4.3]({{ '/secplus/objectives/4-3/' | relative_url }}) | Explain various activities associated with vulnerability management. | done |
| [4.4]({{ '/secplus/objectives/4-4/' | relative_url }}) | Explain security alerting and monitoring concepts and tools. | done |
| [4.5]({{ '/secplus/objectives/4-5/' | relative_url }}) | Given a scenario, modify enterprise capabilities to enhance security. | done |
| [4.6]({{ '/secplus/objectives/4-6/' | relative_url }}) | Given a scenario, implement and maintain identity and access management. | done |
| [4.7]({{ '/secplus/objectives/4-7/' | relative_url }}) | Explain the importance of automation and orchestration related to secure operations. | done |
| [4.8]({{ '/secplus/objectives/4-8/' | relative_url }}) | Explain appropriate incident response activities. | done |
| **4.9** | Given a scenario, use data sources to support an investigation. (current) | done |

[← Previous: Objective 4.8]({{ '/secplus/objectives/4-8/' | relative_url }}) | [Back to Dashboard]({{ '/secplus/' | relative_url }}) | [Next: Domain 5 →]({{ '/secplus/objectives/5-1/' | relative_url }})
