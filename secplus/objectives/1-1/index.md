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

Any single control can be described by combining one category with one type. For example, a firewall is a **Technical Preventive** control; a security policy is a **Managerial Directive** control.

---

### Categories of controls

| Category | Also called | Description | Examples |
|---|---|---|---|
| **Technical** | Logical | Implemented through technology — hardware, software, firmware | Firewalls, encryption, ACLs, IDS/IPS, antivirus |
| **Managerial** | Administrative | Policies, procedures, and governance frameworks defined by management | Risk assessments, security policies, background checks, training programs |
| **Operational** | Procedural | Day-to-day processes carried out by people | Patch management, change management, incident response procedures, guard patrols |
| **Physical** | — | Tangible mechanisms that protect facilities and hardware | Locks, fences, cameras, mantraps, bollards, security guards |

#### Memory aid

> **T-M-O-P** — "**T**ech **M**anagers **O**perate **P**hysically"

---

### Control types

| Type | Purpose | When it acts | Examples |
|---|---|---|---|
| **Preventive** | Stop an incident before it occurs | Before | Firewall rules, door locks, encryption, separation of duties |
| **Deterrent** | Discourage a threat actor from acting | Before | Warning banners, security cameras (visible), guard dogs, "Trespassers will be prosecuted" signs |
| **Detective** | Identify that an incident has occurred or is in progress | During/After | IDS, log monitoring, SIEM alerts, motion sensors, audit trails |
| **Corrective** | Fix or restore after an incident | After | Backup restores, patching a vulnerability, fire extinguishers, antivirus quarantine |
| **Compensating** | Substitute when primary control is not feasible | Any time | MFA when password policy cannot be enforced; using an application-layer firewall because a network firewall cannot inspect encrypted traffic |
| **Directive** | Direct or mandate behavior through policy | Before | Acceptable use policies (AUP), standard operating procedures (SOPs), regulatory requirements |

#### Memory aid

> Think of a timeline: **Prevent → Deter → Detect → Correct**. Then add **Compensating** (plan B) and **Directive** (the rule book).

---

### Combining categories and types — the control matrix

The exam often asks you to identify which cell a specific control falls into. Here is a sample matrix:

| | Preventive | Deterrent | Detective | Corrective | Compensating | Directive |
|---|---|---|---|---|---|---|
| **Technical** | Firewall, encryption | Login banner warning | IDS, SIEM alert | Antivirus quarantine | Temporary additional logging | ACL enforcing policy |
| **Managerial** | Pre-employment screening | Termination policies | Review of audit reports | Lessons-learned process | Risk exception approval | Security policy |
| **Operational** | Security guard checking IDs | Posted guard at entrance | Log review procedure | Incident response actions | Manual review when scanner is down | Change management SOP |
| **Physical** | Mantrap / access vestibule | Security cameras (visible) | Motion sensor | Fire suppression system | Backup generator | Posted "Authorized Only" sign |

---

### Key distinctions to know for the exam

**Preventive vs. Deterrent:**
A *preventive* control physically or logically blocks the action. A *deterrent* control discourages the action but does not block it. A locked door is preventive; a "Do Not Enter" sign is a deterrent.

**Detective vs. Corrective:**
*Detective* finds the problem; *corrective* fixes it. An IDS detects an attack; an IPS that drops packets is both detective and corrective (or preventive, depending on framing).

**Compensating controls:**
These exist because the ideal primary control is too costly, technically impossible, or operationally disruptive. They must provide a comparable level of protection. Compensating controls are commonly referenced in PCI DSS compliance.

**Directive controls:**
Often overlooked — these are the written rules. Policies, standards, guidelines, and procedures all fall here. They tell people what to do but do not enforce anything by themselves.

---

### Exam tips

1. **Read the scenario carefully.** The same physical object can be different control types depending on context. A security camera recording footage is **detective**; a prominently displayed camera intended to scare people away is **deterrent**.
2. **Watch for "compensating."** If a question says "because the organization cannot implement X, they instead do Y," that is a compensating control.
3. **Directive is policy-based.** If the answer choice is a written policy, procedure, or regulation, it is directive.
4. **"Compare and contrast" means know the differences.** Be prepared for questions that present two similar controls and ask you to identify which type each one is.
5. **Category vs. type is a two-dimensional classification.** Don't confuse "technical" (category) with "preventive" (type) — a control has both.

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

**Scenario 3:** An organization cannot enforce full-disk encryption on legacy laptops, so it requires those laptops to remain in a locked, secure room.
- The locked room is a **Physical Compensating** control (it compensates for the lack of encryption).

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

**Answer:** Deterrent (Technical Deterrent). It discourages unauthorized users but does not prevent them from attempting to log in.
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

---

## Navigation

**Domain 1: General Security Concepts**

| Objective | Title | Status |
|---|---|---|
| **1.1** | Compare and contrast various types of security controls (current) | done |
| [1.2]({{ '/secplus/objectives/1-2/' | relative_url }}) | Summarize fundamental security concepts | done |
| [1.3]({{ '/secplus/objectives/1-3/' | relative_url }}) | Explain the importance of change management processes | pending |
| [1.4]({{ '/secplus/objectives/1-4/' | relative_url }}) | Explain the importance of using appropriate cryptographic solutions | pending |

[← Back to Dashboard]({{ '/secplus/' | relative_url }}) | [Next: Objective 1.2 →]({{ '/secplus/objectives/1-2/' | relative_url }})
