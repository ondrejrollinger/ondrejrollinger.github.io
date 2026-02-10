---
layout: default
title: "Security+ 1.1 — Compare and contrast various types of security controls."
objective_id: "1.1"
domain: "1.0 General Security Concepts"
status: "done"
tags:
  - secplus701
permalink: /secplus/objectives/1-1/
---

# Security+ 1.1 — Compare and contrast various types of security controls.

Status: <span class="status-badge done">done</span>

## Exam objective
Compare and contrast various types of security controls.

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

Security controls are safeguards or countermeasures put in place to reduce risk. The SY0-701 exam expects you to classify controls along **two independent axes**:

1. **Categories** — _what the control is_ (Technical, Managerial, Operational, Physical)
2. **Control types** — _what the control does_ (Preventive, Deterrent, Detective, Corrective, Compensating, Directive)

Any single control can be described by combining one category with one type. For example, a firewall is a **Technical Preventive** control; a security policy is a **Managerial Directive** control. A single control can also serve multiple types depending on context.

---

### Security control categories (the four pillars)

| Category | Also called | Description | Exam tip | Examples |
|---|---|---|---|---|
| **Technical** | Logical | Technologies, hardware, and software mechanisms | "If it requires IT systems or software, it's technical" | Firewalls, encryption, ACLs, IDS/IPS, antivirus, MFA, biometric scanners |
| **Managerial** | Administrative | Strategic planning and governance — the policies and procedures | "Think paperwork and planning" | Risk assessments, security policies, background checks, vulnerability management programs, change management processes |
| **Operational** | Procedural | Day-to-day processes carried out by people | "Think people doing things" | Backup procedures, account reviews, log monitoring, configuration management, incident response activities, security awareness training delivery |
| **Physical** | — | Tangible, real-world measures to protect assets | "If you can physically touch it, it's physical" | Locks, badge readers, security guards, CCTV, fences, bollards, mantraps, fire suppression, HVAC |

#### Memory aid — TMOP

> **T**ech **M**anagers **O**perate **P**hysically

---

### Security control types (the six functions)

| Type | Purpose | When it acts | Key phrase | Examples |
|---|---|---|---|---|
| **Preventive** | Stop an incident before it occurs | Before | "Pre-event" | Firewall rules, door locks, encryption, system hardening, separation of duties |
| **Deterrent** | Discourage a threat actor from acting | Before | "Discourages" | Warning signs, visible security cameras, login banners, cable locks, guard presence |
| **Detective** | Identify that an incident has occurred or is in progress | During/After | "Detect it" | IDS, log monitoring, SIEM, motion detectors, file integrity monitoring, security audits |
| **Corrective** | Fix or restore after an incident | After | "Correct the problem" | Backup restores, patching, IPS blocking traffic, antivirus quarantine |
| **Compensating** | Substitute when primary control is not feasible | Any time | "Plan B" | Network segmentation when encryption is impossible; increased monitoring when patching a legacy system is not an option |
| **Directive** | Direct or mandate behavior through policy | Before | "Directs behavior through rules" | AUPs, SOPs, compliance requirements, training materials |

#### Quick decision tree

- Is it stopping something BEFORE?    → Preventive
- Is it discouraging via warning?      → Deterrent
- Is it finding/alerting?              → Detective
- Is it fixing after?                  → Corrective
- Is it a backup plan?                 → Compensating
- Is it a rule/guideline?              → Directive

#### Memory aid — PP-DD-CC

> **P**reventive, "**P**lease don't" (deterrent), **D**etective, "**D**o this" (directive), **C**orrective, **C**ompensating

---

### Combining categories and types — the control matrix

The exam often asks you to identify which cell a specific control falls into. Controls can be **both a category AND a type** — and a single control can serve multiple types:

| Control Example | Category | Type(s) |
|---|---|---|
| Firewall | Technical | Preventive |
| IDS | Technical | Detective |
| Security policy | Managerial | Directive |
| Security awareness training | Managerial/Operational | Preventive |
| Security guard | Physical | Deterrent/Detective/Preventive |
| CCTV cameras | Physical | Detective/Deterrent |
| Backup procedures | Operational | Corrective |

**Full matrix with example controls:**

| | Preventive | Deterrent | Detective | Corrective | Compensating | Directive |
|---|---|---|---|---|---|---|
| **Technical** | Firewall, encryption | Login banner warning | IDS, SIEM alert | Antivirus quarantine | Temporary additional logging | ACL enforcing policy |
| **Managerial** | Pre-employment screening | Termination policies | Review of audit reports | Lessons-learned process | Risk exception approval | Security policy |
| **Operational** | Security guard checking IDs | Posted guard at entrance | Log review procedure | Incident response actions | Manual review when scanner is down | Change management SOP |
| **Physical** | Mantrap / access vestibule | Security cameras (visible) | Motion sensor | Fire suppression system | Backup generator | Posted "Authorized Only" sign |

---

### Key distinctions to know for the exam

| Comparison | Distinction |
|---|---|
| **Preventive vs. Deterrent** | Preventive **stops** it; deterrent **discourages** it. A locked door is preventive; a "Do Not Enter" sign is a deterrent. |
| **Detective vs. Corrective** | Detective **finds** it; corrective **fixes** it. An IDS detects; backup restores correct. |
| **Managerial vs. Operational** | Managerial **plans** it; operational **does** it. Training *program* = managerial; training *delivery* = operational. |
| **Technical vs. Physical** | Technical is **digital**; physical is **tangible**. |
| **Compensating vs. Corrective** | Compensating is used **instead of** primary control (proactive alternative); corrective is used **after** an incident (reactive fix). |

---

### Common exam traps

**Trap: Thinking a security guard is ONLY physical.**
Reality: A security guard can be Physical (category) AND Preventive + Deterrent + Detective (types) simultaneously.

**Trap: Assuming all managerial controls are directive.**
Reality: Security policies are Managerial + Directive, but risk assessments are Managerial + Detective.

**Trap: Confusing "compensating" with "corrective".**
Reality: Compensating = used INSTEAD of primary control (proactive alternative). Corrective = used AFTER an incident (reactive fix).

**Trap: Thinking training is only one category.**
Reality: Training *program* = Managerial. Training *delivery* = Operational. Training *content* = Directive.

---

### Exam tips

1. **Read the scenario carefully.** The same physical object can be different control types depending on context. A security camera recording footage is **detective**; a prominently displayed camera intended to scare people away is **deterrent**.
2. **Watch for "compensating."** If a question says "because the organization cannot implement X, they instead do Y," that is a compensating control.
3. **Directive is policy-based.** If the answer choice is a written policy, procedure, or regulation, it is directive.
4. **"Compare and contrast" means know the differences.** Be prepared for questions that present two similar controls and ask you to identify which type each one is.
5. **Category vs. type is a two-dimensional classification.** Don't confuse "technical" (category) with "preventive" (type) — a control has both.
6. **Look for keywords:** "Prevents/Blocks" = Preventive. "Warns/Discourages" = Deterrent. "Detects/Monitors/Alerts" = Detective. "Restores/Fixes" = Corrective. "Alternative/Instead of" = Compensating. "Policy/Guideline" = Directive.

---

## Key terms

- **Security control** — A safeguard or countermeasure designed to protect confidentiality, integrity, and availability of information and systems.
- **Preventive control** — Blocks an unwanted action before it happens.
- **Detective control** — Identifies and alerts when an unwanted event occurs.
- **Corrective control** — Mitigates damage and restores normal operations after an incident.
- **Deterrent control** — Discourages threat actors from attempting an action.
- **Compensating control** — An alternative control used when the primary control is not feasible.
- **Directive control** — Specifies required behavior through policies, standards, or procedures.
- **Technical control** — Technology-based mechanism (firewall, encryption, ACL).
- **Managerial control** — Administrative mechanism driven by management decisions (policies, risk assessments).
- **Operational control** — Process carried out by people on a daily basis (patch management, guard patrols).
- **Physical control** — Tangible mechanism protecting physical assets (locks, fences, cameras).

---

## Examples / scenarios

**Scenario 1:** A company deploys a firewall to block unauthorized traffic.
- **Category:** Technical
- **Type:** Preventive

**Scenario 2:** After a breach, the security team restores systems from backup.
- **Category:** Operational
- **Type:** Corrective

**Scenario 3:** A healthcare organization cannot encrypt a legacy medical device due to compatibility issues. They place it in a separate VLAN with restricted access and enhanced monitoring.
- **Type:** Compensating (alternative measures because the primary control — encryption — cannot be used)

**Scenario 4:** A company publishes an Acceptable Use Policy stating that employees must not install unapproved software.
- **Category:** Managerial
- **Type:** Directive

**Scenario 5:** Motion-activated lights are installed around the perimeter of a building.
- If the lights are primarily to help cameras record better images: **Physical Detective** (supporting detection)
- If the lights are primarily to scare off intruders: **Physical Deterrent**

---

## Mini quiz

<details>
<summary><strong>Question 1:</strong> A company posts a banner on its login screen warning that unauthorized access is prohibited and will be prosecuted. What type of control is this?</summary>

**Answer:** Deterrent (also Directive). It discourages unauthorized access by warning of consequences, but doesn't actually prevent someone from attempting to log in. It also directs behavior by stating what is/isn't allowed.
</details>

<details>
<summary><strong>Question 2:</strong> An organization requires all employees to complete annual security awareness training. Classify this control by category and type.</summary>

**Answer:** Managerial Directive. The requirement is a management-driven policy mandate directing employee behavior.
</details>

<details>
<summary><strong>Question 3:</strong> A SIEM system generates an alert when it detects anomalous network traffic patterns. What type of control is this?</summary>

**Answer:** Technical Detective. It uses technology to identify (detect) potentially malicious activity.
</details>

<details>
<summary><strong>Question 4:</strong> A company's password policy requires 12-character passwords, but a legacy application only supports 8-character passwords. The company adds MFA to that application. What type of control is the MFA in this context?</summary>

**Answer:** Technical Compensating. MFA compensates for the inability to meet the primary password length requirement.
</details>

<details>
<summary><strong>Question 5:</strong> After a ransomware incident, the IT team uses clean backups to restore affected servers. What category and type of control is this?</summary>

**Answer:** Operational Corrective. It is a people-driven process (operational) that restores normal operations after an incident (corrective).
</details>

### CompTIA-style practice questions

<details>
<summary><strong>Question 6:</strong> A security administrator implements a system that automatically blocks IP addresses after three failed login attempts. Which type of security control is being described?<br>A. Detective  B. Deterrent  C. Corrective  D. Preventive</summary>

**Correct Answer: D. Preventive**

The system PREVENTS further unauthorized access attempts by blocking the IP address. While it detects the failed attempts (detective aspect), its PRIMARY function is prevention of future attacks from that IP.

- A: Detective would only alert, not block
- B: Deterrent would warn but not enforce
- C: Corrective would fix after an incident occurred
</details>

<details>
<summary><strong>Question 7:</strong> Which of the following is the BEST example of a compensating control?<br>A. Installing antivirus on all workstations  B. Using network segmentation when encryption isn't possible  C. Creating a disaster recovery plan  D. Implementing multi-factor authentication</summary>

**Correct Answer: B. Using network segmentation when encryption isn't possible**

This is compensating because it's an ALTERNATIVE measure used when the primary control (encryption) cannot be implemented. Keywords: "when X isn't possible" = compensating.

- A: Standard preventive control, not compensating
- C: Standard operational control for business continuity
- D: Standard preventive control, not an alternative to something else
</details>

<details>
<summary><strong>Question 8 (Multi-select):</strong> A company installs visible security cameras at all entrances. Select TWO types of controls this represents.<br>A. Preventive  B. Detective  C. Deterrent  D. Corrective  E. Compensating</summary>

**Correct Answers: B. Detective and C. Deterrent**

- **Detective**: Cameras record and allow security to detect incidents
- **Deterrent**: VISIBLE cameras discourage would-be attackers

Note: CompTIA typically views cameras as primarily detective/deterrent since they don't physically prevent entry.
</details>

---

## Related objectives

- [**1.2**]({{ '/secplus/objectives/1-2/' | relative_url }}) — CIA Triad ties to control goals
- [**2.5**]({{ '/secplus/objectives/2-5/' | relative_url }}) — Mitigation techniques implement these controls
- [**3.2**]({{ '/secplus/objectives/3-2/' | relative_url }}) — Security principles use these controls
- [**5.1**]({{ '/secplus/objectives/5-1/' | relative_url }}) — Governance includes control frameworks

---

## Navigation

**Domain 1: General Security Concepts**

| Objective | Title | Status |
|---|---|---|
| **1.1** | Compare and contrast various types of security controls (current) | done |
| [1.2]({{ '/secplus/objectives/1-2/' | relative_url }}) | Summarize fundamental security concepts | done |
| [1.3]({{ '/secplus/objectives/1-3/' | relative_url }}) | Explain the importance of change management processes | done |
| [1.4]({{ '/secplus/objectives/1-4/' | relative_url }}) | Explain the importance of using appropriate cryptographic solutions | done |

[← Back to Dashboard]({{ '/secplus/' | relative_url }}) | [Next: Objective 1.2 →]({{ '/secplus/objectives/1-2/' | relative_url }})
