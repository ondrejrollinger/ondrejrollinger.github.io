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

Incident response is the systematic approach to managing security incidents — from preparation through lessons learned. This objective covers the IR process, team roles, digital forensics, threat hunting, root cause analysis, and training/testing methods.

---

### Incident response process

CompTIA uses a **7-step framework** for the exam (NIST condenses these into 4 phases):

| Step | Name | Key actions |
|---|---|---|
| 1 | **Preparation** | Build the team, create playbooks, deploy tools (SIEM, EDR), train staff, run tabletops |
| 2 | **Detection** | Identify that an incident has occurred via SIEM alerts, EDR, user reports; triage real vs. false positive |
| 3 | **Analysis** | Determine scope, impact, timeline, and affected systems; collect evidence |
| 4 | **Containment** | Stop the incident from spreading — short-term (isolate systems) and long-term (temporary fixes) |
| 5 | **Eradication** | Remove the threat completely — delete malware, close vulnerabilities, revoke attacker access |
| 6 | **Recovery** | Restore systems to normal operation; restore from backups, apply patches, monitor for reinfection |
| 7 | **Lessons Learned** | Post-incident review (1–2 weeks after recovery); document what worked, update procedures |

> **Exam tip:** The steps must be followed **in order** — you cannot eradicate before containing, and lessons learned always comes *after* recovery.

**NIST vs. CompTIA:**

| NIST (4 phases) | CompTIA equivalent |
|---|---|
| Preparation | Preparation |
| Detection & Analysis | Detection + Analysis |
| Containment, Eradication & Recovery | Containment + Eradication + Recovery |
| Post-Incident Activity | Lessons Learned |

---

### Incident response team roles

| Role | Responsibilities |
|---|---|
| **IR Manager** | Coordinates response, makes critical decisions, communicates with executives |
| **Security Analysts** | Investigate alerts, analyze logs, execute containment actions |
| **Forensic Specialists** | Preserve and analyze evidence; provide expert testimony in legal proceedings |
| **IT Operations** | Restore backups, apply patches, implement firewall rules |
| **Legal Counsel** | Breach notification requirements, law enforcement coordination, liability assessment |
| **Human Resources** | Insider threat investigations, employee discipline |
| **Public Relations** | External communications to customers and media; reputation management |

---

### Digital forensics

**Three core principles:**

| Principle | Meaning |
|---|---|
| **Avoid bias** | Let evidence guide conclusions; independent verification; peer review |
| **Repeatable actions** | Document every step (commands, results) so a third party can reproduce the analysis |
| **Evidence preservation** | Maintain chain of custody; always work on a **copy**, never the original |

**Order of volatility** (collect most volatile first):

| Priority | Source | Why it disappears |
|---|---|---|
| 1 | CPU registers & cache | Lost in milliseconds |
| 2 | **System memory (RAM)** | Lost when power is cut — **collect first** |
| 3 | Network state (active connections) | Closes when session ends |
| 4 | Running processes | Terminate when system reboots |
| 5 | Temporary files & swap | Cleared on reboot |
| 6 | Hard disk data | Persistent — but capture early avoids modification |
| 7 | Remote logs & monitoring data | May be overwritten by rotation |
| 8 | Archival media | Most persistent; collect last |

> **Exam tip:** RAM must be captured **before** disk imaging. Disk imaging can take hours — during that time, running processes and network connections (which only exist in RAM) are lost.

**Forensic imaging process:**
1. Attach a **write blocker** (hardware device preventing any writes to the original)
2. Create a bit-by-bit copy (tools: `dd`, FTK Imager)
3. Calculate hash of original (MD5 or SHA-256)
4. Calculate hash of image
5. Verify hashes match — proves the copy is an exact, unmodified duplicate

**Chain of custody:**
- Documents who collected evidence, when, how it was stored, and every person who accessed it
- Required to prove evidence was not tampered with in legal proceedings

---

### Threat hunting

**Definition:** Proactive, manual search for threats that have already evaded automated detection.

| | Threat Hunting | Automated Detection |
|---|---|---|
| **Approach** | Manual, analyst-driven | Automated (SIEM rules, EDR signatures) |
| **Trigger** | Hypothesis or anomaly | Alert threshold |
| **Goal** | Find unknown threats | Alert on known patterns |

**Threat hunting process:**

| Step | Description | Example |
|---|---|---|
| **Establish hypothesis** | Form a testable question about attacker behavior | "Is PowerShell being used for fileless malware?" |
| **Profile threat actors** | Identify likely TTPs based on actor type | APT: slow and low, uses living-off-the-land tools |
| **Conduct hunt** | Query logs, EDR telemetry, network traffic for indicators | Search Event ID 4624/4625 for off-hours authentication |
| **Document findings** | Escalate to IR if threat found; create detection rules; refine hypothesis if not | New SIEM rule created from hunt results |

---

### Root cause analysis

**Purpose:** Identify the fundamental *why* behind an incident — not just what happened.

**5 Whys technique:**

> Problem: Ransomware encrypted 50 systems → User clicked malicious attachment → Email filter didn't catch it → No sandbox to detonate attachments → Sandbox procurement was delayed by budget.
> **Root cause:** Lack of email sandbox. Remediation: deploy sandbox + improve training.

**Fishbone (Ishikawa) diagram** — organizes contributing factors into categories:
- People, Process, Technology, Environment

> **Exam tip:** Root cause analysis is distinct from incident analysis. Analysis asks *what happened*; root cause analysis asks *why it was possible*.

---

### Training and testing methods

| Method | Format | Benefit | Limitation |
|---|---|---|---|
| **Tabletop exercise** | Discussion-based, conference room | Low cost; identifies process and communication gaps | No hands-on technical practice |
| **Simulation** | Hands-on in lab/isolated environment | Realistic technical practice | Requires setup; more expensive |
| **Full interruption test** | Actually fail over to backup systems | Proves DR truly works | Expensive and disruptive; done rarely |

**Red team vs. Purple team:**

| | Red Team | Purple Team |
|---|---|---|
| **Goal** | Attack systems (adversarial) | Improve detection (collaborative) |
| **Method** | Exploit vulnerabilities, evade detection | Red demonstrates attack while blue improves detection in real time |
| **Output** | Report on weaknesses | Enhanced detection capabilities and new SIEM rules |

---

### Key distinctions

| Comparison | Distinction |
|---|---|
| **Containment vs. Eradication** | Containment stops the spread (temporary, immediate); eradication removes the threat (permanent, thorough) |
| **Detection vs. Analysis** | Detection: is this an incident? (yes/no); analysis: what happened, scope, and impact |
| **Playbook vs. Runbook** | Playbook: manual checklist; runbook: automated workflow |
| **Tabletop vs. Simulation** | Tabletop: discussion only; simulation: hands-on technical exercise |
| **Threat Hunting vs. Detection** | Hunting: manual, proactive search by analyst; detection: automated alerts from rules/signatures |
| **Root cause vs. Lessons learned** | Root cause: why was this possible; lessons learned: what do we change going forward |
| **Chain of custody vs. Evidence preservation** | Evidence preservation protects the data; chain of custody documents who touched it and when |

---

### Common exam traps

**Trap: Treating containment and eradication as the same step.**
Reality: Containment is about stopping the spread quickly (isolate the host). Eradication is the thorough removal of the threat (delete malware, close the vulnerability). Both are required.

**Trap: Thinking forensic analysis should be done on the original disk.**
Reality: Always work on a verified copy. The original is preserved with a write blocker and maintained with chain of custody.

**Trap: Ignoring order of volatility.**
Reality: RAM must be captured before disk. Disk imaging can take hours — running processes, network connections, and encryption keys only exist in RAM and disappear when power is cut.

**Trap: Thinking lessons learned happens during the incident.**
Reality: Lessons learned is a post-incident activity, conducted 1–2 weeks *after* recovery — not during the active response.

**Trap: Assuming all incidents require law enforcement notification.**
Reality: Only specific incident types (financial fraud, major data breaches meeting legal thresholds) require law enforcement. Legal counsel determines this.

**Trap: Confusing tabletop exercises with simulations.**
Reality: A tabletop is a discussion — no systems are touched. A simulation involves hands-on technical activity in a lab environment.

---

### Exam tips

1. **7 steps in order:** Preparation → Detection → Analysis → Containment → Eradication → Recovery → Lessons Learned
2. **Containment before eradication** — always stop the spread first, then remove the threat
3. **Preserve evidence during containment** — don't destroy forensic artifacts while isolating
4. **Order of volatility:** RAM first — most volatile data; disk last — most persistent
5. **Forensics:** always work on a copy; verify with hash comparison; maintain chain of custody
6. **Root cause analysis:** answers *why* — 5 Whys and fishbone diagram are the two key techniques
7. **Lessons learned:** post-incident only — after recovery, typically 1–2 weeks later
8. **Tabletop = discussion; simulation = hands-on** — know which is which
9. **Threat hunting = manual + proactive** — distinct from automated detection
10. **Purple team = collaborative improvement** — red attacks, blue learns in real time

---

### Key terms

- **Incident response** — A systematic, structured approach to managing and mitigating security incidents.
- **Preparation** — IR phase focused on building teams, policies, tools, and training before an incident occurs.
- **Containment** — Stopping an incident from spreading; may be short-term (isolate host) or long-term (temporary fix).
- **Eradication** — Permanently removing a threat from the environment after containment.
- **Lessons learned** — Post-incident review conducted after recovery to improve future response.
- **Digital forensics** — The collection, preservation, and analysis of electronic evidence using sound, repeatable methodology.
- **Order of volatility** — The sequence in which evidence should be collected, prioritizing the most transient data first.
- **Chain of custody** — Documentation tracking who collected evidence, how it was stored, and every person who accessed it.
- **Write blocker** — Hardware device that prevents any writes to original evidence media during forensic imaging.
- **Threat hunting** — Proactive, analyst-driven search for threats that have evaded automated detection.
- **Root cause analysis** — The process of identifying the fundamental reason an incident was possible.
- **5 Whys** — Root cause analysis technique that iteratively asks "why" to trace a problem to its origin.
- **Tabletop exercise** — Discussion-based IR training where participants talk through a scenario without hands-on activity.
- **Simulation** — Hands-on IR training conducted in a lab or isolated environment with a realistic attack scenario.
- **Playbook** — Manual checklist of steps for responding to a specific incident type.
- **Runbook** — Automated workflow that executes IR steps programmatically.
- **Red team** — Adversarial group that attacks systems to identify weaknesses.
- **Purple team** — Collaborative exercise where red team attacks and blue team improves detection in real time.

---

### Examples / scenarios

**Scenario 1:** A security analyst receives a SIEM alert at 2 AM indicating a host is communicating with a known C2 server. The analyst confirms the connection is active. What should happen next?
- **Answer:** Analysis (confirm scope), then Containment (isolate the host). The analyst must not power off the system yet — RAM must be captured first to preserve forensic evidence including the running malware and active connection details.

**Scenario 2:** A forensic specialist is handed a hard drive from a compromised server. Before beginning analysis, they connect the drive through a hardware device that prevents any writes. They then create a bit-by-bit copy and compare MD5 hashes of both.
- **Answer:** Correct forensic procedure: write blocker protects original, hash comparison verifies integrity of the copy. All analysis proceeds on the copy.

**Scenario 3:** A threat hunter hypothesizes that an attacker may be using encoded PowerShell commands to execute fileless malware. They search EDR telemetry for processes launched with `-EncodedCommand` parameters, correlate with authentication logs, and find no evidence of compromise.
- **Answer:** Correct threat hunting process — hypothesis formed, hunt conducted, negative result documented, detection rule created to automate future monitoring.

**Scenario 4:** Three weeks after recovering from a ransomware attack, the IR manager schedules a meeting to review what happened, identify what failed, and update the incident response plan.
- **Answer:** Lessons learned phase. This is explicitly post-incident and typically occurs 1–2 weeks after recovery.

**Scenario 5:** A company's IR team discusses what to do when ransomware is detected at 2 AM — but does not actually touch any systems. Afterward, they identify gaps in their notification procedures.
- **Answer:** Tabletop exercise. Discussion-only, no systems touched, gaps in process identified.

---

### Mini quiz

<details>
<summary><strong>Question 1:</strong> Why must RAM be collected before a disk image during forensic response?</summary>

**Answer:** RAM is volatile — its contents are lost when the system is powered off. Disk imaging can take hours, during which time the running malware process, active network connections, and encryption keys (which only exist in RAM) would be destroyed. Order of volatility requires collecting the most transient evidence first.
</details>

<details>
<summary><strong>Question 2:</strong> What is the difference between containment and eradication?</summary>

**Answer:** Containment stops the incident from spreading — it is immediate and may be temporary (e.g., isolate the affected host, block a malicious IP). Eradication permanently removes the threat — deleting malware, closing the exploited vulnerability, and revoking attacker access. Both steps are required; eradication cannot begin until containment is in place.
</details>

<details>
<summary><strong>Question 3:</strong> What makes threat hunting different from automated detection?</summary>

**Answer:** Threat hunting is a proactive, manual process driven by an analyst forming a hypothesis and searching for evidence of threats that have already evaded automated detection. Automated detection relies on predefined rules and signatures to generate alerts. Hunting finds the unknown; detection alerts on the known.
</details>

<details>
<summary><strong>Question 4:</strong> What is the purpose of chain of custody?</summary>

**Answer:** Chain of custody documents who collected evidence, when, how it was stored, and every individual who accessed it. It is required for legal proceedings to prove the evidence was not tampered with between collection and presentation.
</details>

<details>
<summary><strong>Question 5:</strong> When does the lessons learned phase occur and what is its purpose?</summary>

**Answer:** Lessons learned occurs after recovery — typically 1–2 weeks post-incident. Its purpose is to identify what worked, what failed, update the IR plan and playbooks, and implement changes to prevent recurrence. It is not conducted during the active incident.
</details>

### CompTIA-style practice questions

<details>
<summary><strong>Question 6:</strong> A security team has confirmed active ransomware on three servers. The malware is still running and communicating with an external IP. Which action should the team take FIRST?<br>A. Wipe and restore the servers from backup<br>B. Power off the servers to stop the ransomware<br>C. Isolate the servers from the network while preserving RAM<br>D. Run a root cause analysis to determine how ransomware entered</summary>

**Correct Answer: C. Isolate the servers from the network while preserving RAM**

Containment comes before eradication or recovery. Isolating the servers stops the spread and blocks C2 communication. RAM must be preserved before any power-off to capture forensic evidence including encryption keys and the running process.

- A: Recovery comes after containment and eradication — wiping now destroys forensic evidence.
- B: Powering off destroys volatile evidence in RAM (encryption keys, active connections) before it can be captured.
- D: Root cause analysis occurs post-incident, not during active response.
</details>

<details>
<summary><strong>Question 7:</strong> A forensic analyst is tasked with investigating a compromised workstation. After attaching a write blocker and creating a bit-by-bit image, the analyst calculates the MD5 hash of the image but not the original drive. What is the PRIMARY concern with this procedure?<br>A. The write blocker was unnecessary since imaging is read-only<br>B. MD5 is not approved for forensic use<br>C. Without hashing the original, there is no way to prove the image is an unmodified copy<br>D. Bit-by-bit imaging takes too long for forensic investigations</summary>

**Correct Answer: C. Without hashing the original, there is no way to prove the image is an unmodified copy**

Forensic integrity requires hashing **both** the original and the image, then comparing the two values. If only the image is hashed, there is no baseline to verify the copy is accurate — which undermines chain of custody and evidence admissibility.

- A: The write blocker is essential regardless of read intent — it is a safeguard, not an optional accessory.
- B: MD5 is widely accepted in forensics, though SHA-256 is preferred for stronger collision resistance.
- D: Imaging speed is a practical consideration, not a procedural concern in this scenario.
</details>

<details>
<summary><strong>Question 8:</strong> An organization's security team suspects an attacker may be using DNS queries to exfiltrate data slowly over several months. No SIEM alert has fired. An analyst forms a hypothesis and begins reviewing DNS logs for anomalously long query strings and unusual domain patterns. Which activity BEST describes this?<br>A. Vulnerability scanning<br>B. Automated threat detection<br>C. Incident analysis<br>D. Threat hunting</summary>

**Correct Answer: D. Threat hunting**

The analyst is conducting a proactive, manual investigation based on a hypothesis about a threat that has not triggered any automated alert. This is the defining characteristic of threat hunting — searching for the unknown rather than responding to a known alert.

- A: Vulnerability scanning identifies weaknesses in systems, not active threat behavior.
- B: Automated detection relies on rules/signatures that fire alerts; no alert fired here.
- C: Incident analysis investigates a confirmed incident; no incident has been confirmed yet.
</details>

<details>
<summary><strong>Question 9 (Multi-select):</strong> Following a ransomware incident, the IR manager is planning training to reduce future risk. Which TWO activities involve hands-on technical practice rather than discussion only? (Select TWO.)<br>A. Tabletop exercise with the executive team<br>B. Red team simulation in an isolated lab environment<br>C. Reviewing and updating the incident response playbook<br>D. Full interruption test that fails over to backup infrastructure<br>E. Reviewing SIEM alert logs from the incident</summary>

**Correct Answers: B and D**

Both simulations (B) and full interruption tests (D) involve actively exercising technical systems and procedures — not just talking through them.

- A: A tabletop exercise is discussion-based only; no systems are touched.
- C: Reviewing a playbook is documentation work, not hands-on practice.
- E: Log review is analysis activity, not a training exercise.
</details>

---

### Related objectives

- [**4.3**]({{ '/secplus/objectives/4-3/' | relative_url }}) — Vulnerability management feeds directly into preparation and eradication phases of incident response.
- [**4.4**]({{ '/secplus/objectives/4-4/' | relative_url }}) — Security alerting and monitoring tools (SIEM, EDR) are the primary detection and analysis instruments.
- [**4.7**]({{ '/secplus/objectives/4-7/' | relative_url }}) — Automation and orchestration (SOAR) enables runbook execution and speeds containment during IR.
- [**4.9**]({{ '/secplus/objectives/4-9/' | relative_url }}) — Data sources used during investigations directly support the analysis and threat hunting phases.
- [**2.4**]({{ '/secplus/objectives/2-4/' | relative_url }}) — Indicators of malicious activity are what detection and analysis phases rely on to confirm and scope incidents.

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
