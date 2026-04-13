---
layout: objective
title: "Security+ 2.4 — Given a scenario, analyze indicators of malicious activity."
objective_id: "2.4"
domain: "2.0 Threats, Vulnerabilities, and Mitigations"
status: "done"
tags:
  - secplus701
permalink: /secplus/objectives/2-4/
---

# Security+ 2.4 — Given a scenario, analyze indicators of malicious activity.

Status: <span class="status-badge done">done</span>

## Exam objective
Given a scenario, analyze indicators of malicious activity.

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

This is a **scenario-based** objective — the exam gives you observable symptoms and asks you to identify the attack type or malware category. Learn to map indicators to their corresponding attack. Malware types, attack indicators, and network/host/physical signs are all tested.

---

### Malware types: quick-reference table

| Malware Type | How it works | Key Identifier | Spread method |
|---|---|---|---|
| **Virus** | Attaches to legitimate files; executes when file is opened | Requires host file; requires user action | User opening infected file |
| **Worm** | Self-replicates without user interaction; spreads across network | **No host file needed; no user action required** | Network automatically |
| **Trojan** | Disguised as legitimate software; provides unauthorized access | Appears harmless; does not self-replicate | User installing "useful" software |
| **RAT (Remote Access Trojan)** | Full remote control of victim machine via C2 channel | Command-and-control connection | Delivered via Trojan |
| **Ransomware** | Encrypts user files; demands payment for decryption key | Files suddenly inaccessible; ransom note | Phishing, drive-by download |
| **Spyware** | Monitors user activity; collects keystrokes, browsing, credentials | Silent data collection; no visible symptoms | Bundled software, malicious sites |
| **Rootkit** | Hides presence on system; operates at OS/kernel level (Ring 0) | Antivirus can't detect; system behaves oddly | Exploits, Trojans |
| **Botnet / zombie** | Compromised device controlled remotely by C2 server | Unexplained outbound traffic; CPU spikes | Exploits, phishing, drive-by |
| **Keylogger** | Records all keystrokes (software or hardware) | Captured passwords; unexpected credential reuse | Phishing, physical tampering |
| **Logic bomb** | Dormant code; executes when specific condition is met | No symptoms until triggered | Insider threat, malicious update |
| **Backdoor** | Hidden access mechanism; bypasses normal authentication | Persistent unauthorized access | Trojans, malicious updates, insiders |
| **Bloatware** | Pre-installed unwanted software consuming resources | Sluggish performance; unexpected apps | Pre-installed on devices |

---

### Virus types (deeper detail)

| Virus Type | Behavior |
|---|---|
| **Boot sector** | Stored in the first sector of a hard drive; loads into memory at every boot |
| **Macro** | Embedded in document files (Word, Excel); runs when document is opened |
| **Program / file infector** | Infects executable (.exe) files |
| **Multipartite** | Combines boot sector + program infection |
| **Encrypted** | Encrypts its payload to evade signature detection |
| **Polymorphic** | Changes its code on each execution (mutation of decryption module) |
| **Metamorphic** | Rewrites itself entirely before infecting — no consistent signature |
| **Stealth** | Intercepts OS calls to hide its presence from scanners |
| **Armored** | Adds obfuscation layers to confuse analysis |

> **Exam tip:** Polymorphic = changes decryption code. Metamorphic = rewrites the entire virus. Both evade signature-based AV.

---

### Malware attack techniques

#### Multi-stage malware deployment

1. **Stage 1 — Dropper/Downloader:** Lightweight shellcode that executes on the victim; retrieves the main payload.
   - **Dropper:** Installs/runs the next stage directly.
   - **Downloader:** Downloads additional malware from a remote server.
2. **Stage 2 — RAT installation:** Downloads and installs a Remote Access Trojan for persistent C2.
3. **Actions on Objectives:** Data exfiltration, file encryption, lateral movement.
4. **Concealment:** Erases logs, hides files, deletes evidence of the intrusion.

#### Fileless malware

- Creates processes entirely **in memory** — no files written to disk.
- Evades traditional signature-based antivirus (no file to scan).
- Uses built-in system tools: PowerShell, WMI, cmd.exe — **"Living off the Land"** (LotL).

> **Living off the Land:** Threat actors exploit legitimate built-in tools (LOLBins) to avoid detection. No custom malware needed.

#### Rootkits and ring levels

- System permission rings: **Ring 3** (user mode) → **Ring 0** (kernel mode, highest privilege).
- Rootkits aim to operate at **Ring 0** — the closer to the kernel, the more damage and the harder to detect.
- **DLL injection:** Inserts malicious DLL into a legitimate process's address space.
- **Shim:** Software placed between two components to intercept and redirect calls.
- **Detection:** Boot from external media and scan the internal drive with a clean antivirus tool.

---

### Indicators of malicious activity

#### Behavioral / log indicators

| Indicator | What it suggests |
|---|---|
| **Account lockouts** | Brute-force credential attack triggering failed login thresholds |
| **Concurrent session utilization** | Single account active from multiple geographic locations simultaneously |
| **Impossible travel** | Account accessed from two distant locations in an impossibly short time | 
| **Blocked content** | Sudden spike in security tool blocks — malware attempting outbound connections |
| **Resource consumption** | Unexplained spikes in CPU, memory, or network bandwidth — botnet/crypto-miner activity |
| **Resource inaccessibility** | Files or systems suddenly unavailable — ransomware encryption in progress |
| **Out-of-cycle logging** | Log entries generated at unusual hours — attacker activity when no staff present |
| **Missing logs** | Gaps or cleared logs — attacker covering tracks; concealment phase |
| **Published / documented attacks** | Threat intel reports naming your organization as part of a known botnet or campaign |

#### Network attack indicators

| Indicator | Possible Cause |
|---|---|
| Unexpected outbound connections to unfamiliar IPs | C2 (command-and-control) communication by malware |
| Port scanning activity originating from internal host | Compromised internal host performing reconnaissance |
| Large data transfers to external destinations | Data exfiltration |
| DNS queries to known malicious domains | Malware calling home; DNS-based C2 |
| Unusual protocols on unexpected ports | Covert channel / tunneling |

#### Host-based indicators

| Indicator | Possible Cause |
|---|---|
| New admin accounts created without authorization | Attacker establishing persistence |
| Processes running from temp directories (`%TEMP%`, `/tmp`) | Malware execution; fileless techniques |
| Scheduled tasks or services added without authorization | Persistence mechanism |
| Antivirus disabled or uninstalled | Attacker removing defenses |
| Files modified in system directories | Rootkit or malware installation |
| Browser extensions added without user action | Spyware / adware |

#### Physical / environmental indicators

| Indicator | Possible Cause |
|---|---|
| Hardware keylogger found on workstation | Physical insider or targeted attack |
| Unknown USB devices in machines | Baiting success or insider threat |
| Access card reader tampered with | Skimming device for badge cloning |

---

### Attack type indicators: match the symptom

| Scenario Symptom | Attack Type |
|---|---|
| Files encrypted; ransom note demanding cryptocurrency | **Ransomware** |
| System appears normal but connects out at night; slow internet | **Botnet / zombie** |
| Antivirus can't find malware; system behaving strangely | **Rootkit** (Ring 0 hiding) |
| Credentials stolen without any malware installed | **Hardware keylogger** |
| Network floods with traffic from many sources simultaneously | **DDoS via botnet** |
| Executable triggers destructive behavior on a specific date | **Logic bomb** |
| Attacker has persistent, silent remote control of the system | **RAT / backdoor** |
| Replication across the network with no user action | **Worm** |

---

### Key distinctions to know for the exam

| Comparison | Distinction |
|---|---|
| **Virus vs. worm** | Virus requires a host file and user action; worm self-replicates and spreads without user interaction. |
| **Trojan vs. virus** | Trojan doesn't self-replicate; disguises itself as legitimate software. |
| **Backdoor vs. logic bomb** | Backdoor = persistent unauthorized access; logic bomb = dormant until triggered by a condition. |
| **Rootkit vs. spyware** | Rootkit hides itself at kernel level; spyware silently collects data but doesn't necessarily hide from OS. |
| **Dropper vs. downloader** | Dropper installs the payload directly; downloader fetches it from a remote server first. |
| **Polymorphic vs. metamorphic** | Polymorphic changes the decryption routine; metamorphic rewrites the entire virus body. |
| **Fileless vs. traditional malware** | Fileless lives in memory and uses system tools; traditional writes files to disk and can be detected by signature scanning. |

---

### Common exam traps

**Trap: Thinking a worm needs a user to open a file.**
Reality: Worms self-propagate across networks with no user interaction — that's their defining characteristic.

**Trap: Confusing a Trojan with a virus.**
Reality: A Trojan disguises itself but does not self-replicate. A virus attaches to files and spreads by infecting them.

**Trap: Assuming rootkits are detected by standard antivirus.**
Reality: Rootkits operate at Ring 0 (kernel level) and can hide from the OS itself. You must boot from external media to detect them.

**Trap: Thinking "impossible travel" alerts indicate a stolen credential immediately.**
Reality: It's a strong indicator, but it could also indicate a VPN or proxy — context matters. It warrants immediate investigation.

**Trap: Treating missing logs as a system failure.**
Reality: Missing or cleared logs during an incident are a key indicator of attacker activity — specifically the concealment phase.

---

### Exam tips

1. "Files encrypted, ransom note" → **ransomware**. Response: isolate, don't pay, restore from backup.
2. "Self-replicates across network without user action" → **worm**.
3. "Appears to be a useful program but grants remote access" → **Trojan / RAT**.
4. "Dormant code activates on a specific date/condition" → **logic bomb**.
5. "Hides from antivirus at kernel level" → **rootkit** → boot from external media to detect.
6. "Records keystrokes" → **keylogger** (software or hardware).
7. "Living off the land / uses built-in tools / fileless" → **fileless malware / LotL technique**.
8. For ransomware response: **never pay**, **isolate**, **notify authorities**, **restore from backups**.

---

## Key terms

- **Malware** — Malicious software designed to infiltrate or damage systems without user consent.
- **Virus** — Malware that attaches to files and requires user action to spread.
- **Worm** — Self-replicating malware that spreads across networks without user action.
- **Trojan** — Malware disguised as legitimate software; does not self-replicate.
- **RAT (Remote Access Trojan)** — Trojan providing the attacker with full remote control via a C2 channel.
- **Ransomware** — Encrypts victim files; demands payment for decryption.
- **Rootkit** — Hides at kernel level (Ring 0); evades standard antivirus detection.
- **Logic bomb** — Dormant malicious code that executes when specific conditions are met.
- **Backdoor** — Hidden mechanism bypassing normal authentication for persistent access.
- **Keylogger** — Records keystrokes (software or physical hardware device).
- **Botnet** — Network of compromised devices (zombies) controlled via C2 servers.
- **Zombie** — A compromised device that is part of a botnet.
- **Fileless malware** — Malware that runs entirely in memory using legitimate system tools; leaves no files on disk.
- **Living off the Land (LotL)** — Using built-in OS tools (PowerShell, WMI) rather than custom malware to avoid detection.
- **Dropper** — Malware stage that installs the next payload; runs on the victim.
- **Downloader** — Malware stage that retrieves additional components from a remote server.
- **Impossible travel** — Security alert when an account is accessed from two geographically distant locations in an impossibly short time.
- **C2 (Command and Control)** — Infrastructure used by attackers to communicate with and control compromised systems.

---

## Examples / scenarios

**Scenario 1:** A security analyst sees that a server is sending encrypted traffic to an unfamiliar IP address in Eastern Europe every night at 2 AM. CPU usage also spikes during these windows. No legitimate job is scheduled.
- **Answer:** Botnet / zombie behavior with C2 communication. The server is likely part of a botnet performing tasks on the attacker's behalf.

**Scenario 2:** A user reports that all their documents have been renamed with a `.locked` extension and a text file demanding $500 in Bitcoin appeared on their desktop.
- **Answer:** Ransomware. Response: isolate the machine immediately, do not pay, notify IR team, restore from clean backups.

**Scenario 3:** Antivirus scans consistently return clean results but the system is behaving strangely — processes appear and disappear, the firewall keeps disabling itself.
- **Answer:** Rootkit. It operates at Ring 0, hiding itself from the OS and antivirus. Boot from external media to detect.

**Scenario 4:** An employee's credentials are used at 9 AM in New York and 9:15 AM in Tokyo on the same day.
- **Answer:** Impossible travel indicator — the account is compromised. Investigate immediately; disable the account.

**Scenario 5:** A developer notices that a critical production system crashes every year on the day a former employee was terminated. The crashes are destructive.
- **Answer:** Logic bomb. Dormant code embedded by the departing employee triggers on a specific date/condition.

---

## Mini quiz

<details>
<summary><strong>Question 1:</strong> What is the key difference between a virus and a worm?</summary>

**Answer:** A virus requires a host file and user action to spread (e.g., a user opens an infected file). A worm self-replicates and propagates across networks without any user interaction — it spreads automatically.
</details>

<details>
<summary><strong>Question 2:</strong> What is fileless malware and why is it difficult to detect?</summary>

**Answer:** Fileless malware executes entirely in system memory without writing files to disk. It uses legitimate built-in OS tools (PowerShell, WMI) — a technique called "living off the land." Because nothing is written to disk, signature-based antivirus has no file to scan.
</details>

<details>
<summary><strong>Question 3:</strong> How do you detect a rootkit when standard antivirus fails?</summary>

**Answer:** Boot the system from external media (e.g., a live Linux USB) and run an antivirus/antimalware scan against the internal drive. Since the rootkit cannot load when the OS is not booted from the internal drive, it can no longer hide itself from the scanner.
</details>

<details>
<summary><strong>Question 4:</strong> What are the 9 common indicators of malware infection listed in the course materials?</summary>

**Answer:** Account lockouts, concurrent session utilization, blocked content, impossible travel, resource consumption, resource inaccessibility, out-of-cycle logging, missing logs, and published/documented attacks.
</details>

<details>
<summary><strong>Question 5:</strong> What should an organization do immediately when ransomware is discovered?</summary>

**Answer:** Immediately **isolate** the infected machine from the network to prevent spread, **do not pay** the ransom (payment doesn't guarantee recovery), **notify authorities**, and **restore** data from known-clean backups.
</details>

### CompTIA-style practice questions

<details>
<summary><strong>Question 6:</strong> A SIEM alert shows a single user account authenticated from Los Angeles at 8:00 AM and from Singapore at 8:22 AM on the same morning. Which indicator of compromise does this represent?<br>A. Account lockout<br>B. Concurrent session utilization<br>C. Impossible travel<br>D. Out-of-cycle logging</summary>

**Correct Answer: C. Impossible travel**

Accessing a system from two geographically distant locations within an impossibly short time (Los Angeles to Singapore in 22 minutes) is the definition of impossible travel — a strong indicator of credential compromise.

- A: account lockout indicates failed authentication attempts, not successful logins from two locations.
- B: concurrent session utilization refers to multiple active sessions, but impossible travel specifically emphasizes the geographic impossibility.
- D: out-of-cycle logging refers to log entries at unusual times, not geographic anomalies.
</details>

<details>
<summary><strong>Question 7:</strong> An analyst finds that a server is running a PowerShell process that loaded entirely from memory with no associated files on disk, and is communicating with an external C2 server. Which malware technique does this BEST describe?<br>A. Rootkit<br>B. Logic bomb<br>C. Fileless malware / Living off the Land<br>D. Macro virus</summary>

**Correct Answer: C. Fileless malware / Living off the Land**

Running entirely in memory using a legitimate OS tool (PowerShell) with no disk artifacts is the defining characteristic of fileless malware using Living off the Land techniques.

- A: a rootkit hides itself at kernel level; nothing here indicates kernel-level hiding.
- B: a logic bomb is dormant until triggered by a specific condition; this is active C2 communication.
- D: a macro virus is embedded in document files and runs when documents are opened.
</details>

<details>
<summary><strong>Question 8 (Multi-select):</strong> A cybersecurity analyst is investigating a suspected compromise. Which TWO of the following findings most strongly suggest that an attacker has been present and is now covering their tracks? (Select TWO.)<br>A. A new user account was created with administrator privileges<br>B. Log files for the past 72 hours are completely absent<br>C. The system's CPU usage has been normal<br>D. Security software was uninstalled with no change-management ticket<br>E. The system has not been rebooted in 30 days</summary>

**Correct Answers: B and D**

Missing logs (B) indicate the attacker cleared evidence during the concealment phase. Security software being uninstalled without authorization (D) is a direct action attackers take to remove defenses and avoid detection.

- A: a new admin account is concerning but suggests persistence establishment, not specifically covering tracks.
- C: normal CPU usage is not an indicator of malicious activity.
- E: uptime alone is not an indicator of compromise.
</details>

---

## Related objectives

- [**2.3**]({{ '/secplus/objectives/2-3/' | relative_url }}) — The vulnerability types in 2.3 are what attackers exploit to deploy the malware analyzed here.
- [**2.5**]({{ '/secplus/objectives/2-5/' | relative_url }}) — Mitigation techniques prevent or limit the malicious activity described in this objective.
- [**4.4**]({{ '/secplus/objectives/4-4/' | relative_url }}) — Security alerting and monitoring is the toolset used to detect these indicators.
- [**4.9**]({{ '/secplus/objectives/4-9/' | relative_url }}) — Incident response is triggered when these indicators are confirmed.

---

## Navigation

**Domain 2.0: Threats, Vulnerabilities, and Mitigations**

| Objective | Title | Status |
|---|---|---|
| [2.1]({{ '/secplus/objectives/2-1/' | relative_url }}) | Compare and contrast common threat actors and motivations. | done |
| [2.2]({{ '/secplus/objectives/2-2/' | relative_url }}) | Explain common threat vectors and attack surfaces. | done |
| [2.3]({{ '/secplus/objectives/2-3/' | relative_url }}) | Explain various types of vulnerabilities. | done |
| **2.4** | Given a scenario, analyze indicators of malicious activity. (current) | done |
| [2.5]({{ '/secplus/objectives/2-5/' | relative_url }}) | Explain the purpose of mitigation techniques used to secure the enterprise. | done |

[← Previous: Objective 2.3]({{ '/secplus/objectives/2-3/' | relative_url }}) | [Back to Dashboard]({{ '/secplus/' | relative_url }}) | [Next: Objective 2.5 →]({{ '/secplus/objectives/2-5/' | relative_url }})
