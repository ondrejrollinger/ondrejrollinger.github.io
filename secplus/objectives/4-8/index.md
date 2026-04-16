---
layout: objective
title: "Security+ 4.8 — Explain appropriate incident response activities."
objective_id: "4.8"
domain: "4.0 Security Operations"
status: "done"
tags:
  - secplus701
permalink: /secplus/objectives/4-8/
---

# Security+ 4.8 — Explain appropriate incident response activities.

Status: <span class="status-badge done">done</span>

## Exam objective
Explain appropriate incident response activities.

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

Incident response is the systematic approach to managing security incidents. This objective covers the incident response process, team roles, forensics, threat hunting, and post-incident activities.

---

## Incident Response Process

**7 steps (CompTIA framework):**

### 1. Preparation
- Establish incident response team
- Create policies and procedures (playbooks)
- Deploy security tools (SIEM, EDR, forensic tools)
- Train team members
- Conduct tabletop exercises

### 2. Detection  
- Identify that security incident occurred
- Sources: SIEM alerts, EDR, user reports, threat intelligence
- Triage: Determine if real incident or false positive

### 3. Analysis
- Investigate scope and impact
- Determine: What happened? When? How? Which systems affected?
- Collect evidence (logs, memory dumps, network captures)

### 4. Containment
- Stop incident from spreading
- **Short-term:** Immediate actions (isolate systems, block IPs)
- **Long-term:** Temporary fixes while planning permanent solution

### 5. Eradication
- Remove threat from environment
- Delete malware, close vulnerabilities, remove attacker access
- Verify threat completely eliminated

### 6. Recovery
- Restore systems to normal operation
- Restore from backups, apply patches, return to production
- Monitor for reinfection

### 7. Lessons Learned
- Post-incident review (1-2 weeks after recovery)
- Document what worked and what didn't
- Update procedures to prevent recurrence

**Key principle:** Each phase builds on previous, can't skip steps

**Comparison to NIST:**
- NIST has 4 phases (Preparation, Detection & Analysis, Containment/Eradication/Recovery, Post-Incident)
- CompTIA expands to 7 distinct phases for exam

---

## Incident Response Team

**Roles:**

**Incident Response Manager:**
- Coordinate response activities
- Make critical decisions
- Communicate with executives

**Security Analysts:**
- Investigate alerts
- Analyze logs
- Execute containment

**Forensic Specialists:**
- Preserve evidence
- Conduct detailed analysis
- Expert testimony (if legal proceedings)

**IT Operations:**
- System administrators (restore backups, patch systems)
- Network engineers (implement firewall rules)

**Legal Counsel:**
- Breach notification requirements
- Law enforcement coordination
- Liability assessment

**Human Resources:**
- Insider threat investigations
- Employee discipline

**Public Relations:**
- External communications (customers, media)
- Reputation management

---

## Digital Forensics

**Three core principles:**

### 1. Avoid Bias
- Objective analysis (let evidence guide conclusions)
- Independent verification
- Peer review

### 2. Repeatable Actions
- Document every step
- Commands used, results obtained
- Third party can reproduce analysis

### 3. Evidence Preservation
- Chain of custody (who collected, when, how stored)
- Work on copies (never original)
- Write protection (prevent modification)

**Order of volatility (most volatile first):**
1. CPU registers and cache (milliseconds)
2. System memory (RAM) - **MOST IMPORTANT TO COLLECT FIRST**
3. Network state (active connections)
4. Running processes
5. Temporary files and swap
6. Hard disk data
7. Remote logging and monitoring
8. Physical configuration
9. Archival media

**Why order matters:**
```
Incident: Malware detected on workstation

Correct order:
1. Memory dump FIRST (captures running malware, encryption keys)
2. Network connections (shows active C2 communication)
3. Running processes
4. Disk image (takes hours but data is persistent)

If reversed (disk first):
- Disk imaging takes 3 hours
- During that time, malware process stops
- RAM contents lost (attacker may detect investigation)
- Network connections closed
- Critical evidence GONE

Result: Order of volatility ensures you capture most time-sensitive evidence first
```

**Forensic imaging:**

**Process:**
1. Write blocker (hardware prevents modification)
2. Create bit-by-bit copy (dd, FTK Imager)
3. Calculate hashes (MD5, SHA-256)
4. Verify hashes match (original = image)
5. Work on image, preserve original

**Hash verification:**
```bash
# Hash original drive
md5sum /dev/sda > original-hash.txt

# Create image
dd if=/dev/sda of=/mnt/forensics/evidence.dd bs=4M

# Hash image
md5sum evidence.dd > image-hash.txt

# Compare
diff original-hash.txt image-hash.txt
# If identical: Image is exact copy (integrity verified)
```

**Chain of custody:**
```
Evidence ID: HD-2024-042
Description: Laptop hard drive
Serial: WD-WCAV29374628

Collected by: J. Smith
Date/Time: 2024-04-14 14:00 UTC
Location: Building A, 3rd floor

Transferred to: Forensic lab
Date/Time: 2024-04-14 16:00 UTC
Received by: M. Johnson

Stored: Evidence locker #3
Access log: Maintained

Purpose: Legal proceedings require proving evidence not tampered with
```

---

## Threat Hunting

**Definition:** Proactive search for threats that evaded detection

**Difference from detection:**
- **Detection:** Automated (SIEM rules, EDR signatures)
- **Hunting:** Manual investigation by analyst

**Threat hunting process:**

### 1. Establish Hypothesis
```
Example hypotheses:
- "Attacker may be using stolen credentials during off-hours"
- "PowerShell being used for fileless malware"
- "Data exfiltration via DNS tunneling"
- "Lateral movement using PsExec"

Hypothesis sources:
- Threat intelligence (new attack campaign)
- Industry trends (increase in specific attack type)
- Anomalies (unusual patterns observed)
```

### 2. Profile Threat Actors
```
Identify likely attacker TTPs:
- APT: Custom malware, living-off-the-land, long dwell time
- Cybercriminal: Automated tools, quick smash-and-grab
- Insider: Slow data exfiltration, after-hours access

Expected indicators:
- APT: Subtle, low-and-slow, uses legitimate tools
- Cybercriminal: Noisy, known malware, rapid activity
- Insider: USB usage, large file transfers, access to unrelated systems
```

### 3. Conduct Hunt
```
Data sources:
- Windows Event Logs (Event ID 4624/4625 for authentication)
- EDR telemetry (process execution, network connections)
- Network traffic (NetFlow, packet captures)
- DNS logs (unusual queries)

Hunt queries:
- "Find PowerShell with -EncodedCommand"
- "Detect network logons from workstations using admin accounts"
- "Identify large outbound data transfers to external IPs"
```

### 4. Document Findings
```
If threat found:
- Escalate to incident response
- Create detection rules (automate future detection)
- Update threat intelligence

If no threat found:
- Document methodology
- Refine hypothesis
- Plan next hunt
```

**Hunt metrics:**
- Hunts conducted per month
- Threats detected
- New detection rules created
- Time per hunt

---

## Root Cause Analysis

**Purpose:** Identify fundamental reason incident occurred

**5 Whys technique:**
```
Problem: Ransomware encrypted 50 systems

Why? User clicked malicious email attachment
Why? Email appeared legitimate
Why? Email filtering didn't catch it
Why? No sandbox to detonate suspicious attachments
Why? Sandbox procurement delayed (budget)

Root cause: Lack of email sandbox solution

Remediation: Deploy sandbox, enhance training
```

**Fishbone diagram (Ishikawa):**
```
Categories: People, Process, Technology, Environment

People:
- User clicked without verification
- No security awareness training

Process:
- No email verification procedure
- Backup process incomplete

Technology:
- Email filter outdated
- No EDR on all endpoints

Environment:
- Remote work reduces security culture
- Vendor delay in updates

Result: Multiple contributing factors identified
```

---

## Training and Testing

**Tabletop exercise:**
- **Format:** Discussion-based, conference room
- **Participants:** Team discusses scenario
- **Benefit:** Low cost, identifies process gaps
- **Example:** "Ransomware detected at 2 AM, what do you do?"

**Simulation:**
- **Format:** Hands-on in lab environment
- **Participants:** Team responds to simulated attack
- **Benefit:** Technical practice, realistic
- **Example:** Red team launches attack in isolated network

**Full interruption test:**
- **Format:** Actually fail over to backup systems
- **Benefit:** Proves disaster recovery works
- **Limitation:** Expensive, disruptive
- **Frequency:** Rarely (once a year for mature programs)

**Red team vs Purple team:**

**Red team:**
- **Goal:** Attack systems (adversarial)
- **Method:** Exploit vulnerabilities, evade detection
- **Output:** Report on weaknesses

**Purple team:**
- **Goal:** Improve detection (collaborative)
- **Method:** Red demonstrates attack, blue improves detection
- **Output:** Enhanced detection capabilities

---

## Key Distinctions

**Detection vs Analysis:**
- Detection: Is this an incident? (yes/no)
- Analysis: What happened? (scope, impact)

**Containment vs Eradication:**
- Containment: Stop spread (temporary, immediate)
- Eradication: Remove threat (permanent, thorough)

**Playbook vs Runbook:**
- Playbook: Manual checklist
- Runbook: Automated workflow

**Tabletop vs Simulation:**
- Tabletop: Discussion only
- Simulation: Hands-on technical exercise

**Threat Hunting vs Detection:**
- Hunting: Manual, proactive search
- Detection: Automated alerts

---

## Common Exam Traps

1. **Trap:** Thinking containment and eradication are same step
   - **Reality:** Containment stops spread, eradication removes threat

2. **Trap:** Believing forensics should analyze original disk
   - **Reality:** Always work on copy (preserve evidence)

3. **Trap:** Assuming order of volatility doesn't matter
   - **Reality:** Collect RAM before disk (RAM lost when powered off)

4. **Trap:** Thinking lessons learned happens during incident
   - **Reality:** Post-incident (1-2 weeks after recovery)

5. **Trap:** Believing all incidents require law enforcement
   - **Reality:** Only specific cases (financial fraud, major breaches)

---

## Exam Tips

1. **7 steps in order:** Preparation, Detection, Analysis, Containment, Eradication, Recovery, Lessons Learned
2. **Containment first** before eradication (stop spread, then remove)
3. **Preserve evidence** during containment (don't destroy forensic artifacts)
4. **Order of volatility:** RAM first, disk second (most volatile collected first)
5. **Forensics:** Work on copy, never original
6. **Chain of custody:** Document who, what, when for evidence
7. **Root cause analysis:** Identify WHY (not just what)
8. **Lessons learned:** Post-incident only (after recovery)
9. **Tabletop:** Discussion-based training (low cost)
10. **Threat hunting:** Proactive manual search (not automated detection)

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
| **4.8** | Explain appropriate incident response activities. (current) | done |
| [4.9]({{ '/secplus/objectives/4-9/' | relative_url }}) | Given a scenario, use data sources to support an investigation. | done |

[← Previous: Objective 4.7]({{ '/secplus/objectives/4-7/' | relative_url }}) | [Back to Dashboard]({{ '/secplus/' | relative_url }}) | [Next: Objective 4.9 →]({{ '/secplus/objectives/4-9/' | relative_url }})