---
layout: default
title: "Security+ 1.2 — Summarize fundamental security concepts."
objective_id: "1.2"
domain: "1.0 General Security Concepts"
status: "done"
tags:
  - secplus701
permalink: /secplus/objectives/1-2/
---

# Security+ 1.2 — Summarize fundamental security concepts.

Status: <span class="status-badge done">done</span>

## Exam objective
Summarize fundamental security concepts.

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

### The CIA Triad

The foundational model of information security. Every security decision maps back to one or more of these three goals.

| Pillar | Goal | Threat example | Control example |
|---|---|---|---|
| **Confidentiality** | Only authorized parties can access the data | Data breach, shoulder surfing, eavesdropping | Encryption, access controls, data masking |
| **Integrity** | Data is accurate, complete, and unaltered without authorization | Man-in-the-middle attack, data tampering | Hashing, digital signatures, version control |
| **Availability** | Systems and data are accessible when needed | DDoS, ransomware, hardware failure | Redundancy, backups, load balancing, failover |

#### Memory aid

> **CIA** — if you can remember the acronym, remember: **C**onceal it, **I**t's accurate, **A**lways accessible.

---

### Non-repudiation

Non-repudiation ensures that a party cannot deny having performed an action. It provides proof of origin, proof of delivery, or proof of action.

**How it is achieved:**
- **Digital signatures** — Cryptographically binds a message to the sender's private key. The sender cannot deny authorship because only they possess the key.
- **Audit logs** — Timestamped records that prove who did what and when.
- **Certificates** — Tie a public key to an identity via a trusted Certificate Authority (CA).

**Exam focus:** Non-repudiation is most commonly associated with digital signatures and PKI. It is distinct from authentication — authentication proves who you are *now*; non-repudiation proves you did something *in the past* and cannot deny it.

---

### Authentication, Authorization, and Accounting (AAA)

AAA is the framework for controlling access to resources.

| Component | Question it answers | Examples |
|---|---|---|
| **Authentication** | "Who are you?" | Username/password, biometrics, smart cards, MFA |
| **Authorization** | "What are you allowed to do?" | ACLs, RBAC, file permissions, security groups |
| **Accounting** | "What did you do?" | Log files, SIEM events, session recordings, audit trails |

**Protocols that implement AAA:**
- **RADIUS** — Remote Authentication Dial-In User Service. Commonly used for network access (VPN, Wi-Fi). Encrypts only the password.
- **TACACS+** — Terminal Access Controller Access-Control System Plus. Cisco-favored. Encrypts the entire payload. Separates authentication, authorization, and accounting.

#### Memory aid

> **AAA** = "**A**re you who you say? **A**re you allowed? **A**nd we're watching."

---

### Gap analysis

A gap analysis compares an organization's **current security posture** against a **desired or required state** (a framework, standard, or policy).

**Process:**
1. Define the target state (e.g., NIST CSF, ISO 27001, CIS Controls)
2. Assess the current state
3. Identify the gaps
4. Prioritize and create a remediation plan

**Why it matters for the exam:** Gap analysis is a foundational governance activity. It drives budget decisions, project prioritization, and compliance efforts.

---

### Zero Trust

Zero Trust is a security model that assumes **no implicit trust** — regardless of whether a request originates inside or outside the network perimeter.

**Core principles:**
- **Verify explicitly** — Always authenticate and authorize based on all available data points (identity, location, device health, service/workload, data classification, anomalies).
- **Use least privilege access** — Grant the minimum permissions needed and use just-in-time (JIT) and just-enough-access (JEA) policies.
- **Assume breach** — Minimize blast radius and segment access. Verify end-to-end encryption. Use analytics for threat detection.

**Key components on the exam:**

| Component | Description |
|---|---|
| **Control plane** | The decision-making layer. Includes the policy engine (decides whether to grant access) and the policy administrator (establishes/shuts down the communication path). |
| **Data plane** | The actual data flow. Includes policy enforcement points (PEPs) that allow or block traffic based on control plane decisions. |
| **Adaptive identity** | Authentication and authorization decisions adapt based on context (risk level, time, location, device state). |
| **Threat scope reduction** | Minimize attack surface through microsegmentation and limiting lateral movement. |
| **Policy-driven access control** | Access decisions made by a centralized policy engine, not by network location. |
| **Policy engine** | Evaluates access requests against policy and decides to grant, deny, or revoke access. |
| **Policy administrator** | Executes the policy engine's decisions by signaling the PEP to establish or tear down sessions. |
| **Policy enforcement point (PEP)** | The gatekeeper that enables, monitors, and terminates connections between subjects and resources. |

#### Memory aid

> **"Never trust, always verify."** — This one phrase captures the entire Zero Trust philosophy.

---

### Physical security

Physical security controls protect facilities, hardware, and people.

**Bollards** — Short, sturdy posts that prevent vehicle-borne attacks against buildings. May be fixed, removable, or retractable.

**Access control vestibules (mantraps)** — A small room with two interlocking doors. Only one door can be open at a time, preventing tailgating/piggybacking.

**Fencing** — Perimeter barriers. Height matters for the exam:
- 3–4 feet: deters casual trespassers
- 6–7 feet: too hard to climb easily
- 8+ feet with barbed wire: deters determined intruders

**Video surveillance** — CCTV systems for monitoring and recording. Can serve as both detective (recording incidents) and deterrent (visible cameras discouraging behavior).

**Security guards** — Human element of physical security. Can make judgment calls that technology cannot.

**Access badges** — Smart cards or proximity cards that authenticate identity for facility access. Can integrate with logical access systems.

**Lighting** — Adequate lighting deters criminal activity and supports video surveillance. Exam may reference it as deterrent or detective support.

**Sensors:**
- **Infrared** — Detects body heat (motion detection)
- **Pressure** — Detects weight on floors or surfaces
- **Microwave** — Detects movement via microwave radiation reflection
- **Ultrasonic** — Uses sound waves to detect motion

---

### Deception and disruption technology

Security tools designed to mislead, detect, or delay attackers.

| Technology | Description | Purpose |
|---|---|---|
| **Honeypot** | A single decoy system that appears to be a legitimate target | Detect and study attacker behavior |
| **Honeynet** | A network of honeypots simulating an entire environment | Lure attackers into a monitored fake network |
| **Honeyfile** | A decoy file (e.g., "passwords.xlsx") placed to detect unauthorized access | Detect insider threats or lateral movement |
| **Honeytoken** | A fake data element (fake credentials, fake database record, fake API key) that triggers an alert when used | Detect credential theft or data exfiltration |

**Key distinction:** Honeypots are *systems*; honeytokens are *data*. A honeytoken could be a fake email address inserted into a database — if spam arrives at that address, the database has been compromised.

**DNS sinkhole** — A DNS server that returns false results for known malicious domains, redirecting traffic to a safe location (or nowhere). Used to disrupt malware command-and-control (C2) communication.

---

### Exam tips

1. **CIA Triad appears everywhere.** Almost any security concept can be tied back to confidentiality, integrity, or availability. Practice identifying which pillar a given control supports.
2. **Zero Trust control plane vs. data plane** is a high-frequency exam topic. Know the three components: policy engine, policy administrator, and policy enforcement point.
3. **Non-repudiation is not authentication.** Authentication proves identity at login; non-repudiation proves you cannot deny a past action (digital signatures are the key mechanism).
4. **Honeypot vs. honeytoken** — Systems vs. data. The exam likes to test this distinction.
5. **Physical security is testable.** Don't skip bollards, access vestibules, and sensor types — these appear regularly on the exam.
6. **Gap analysis** is a planning/governance concept. It does not fix anything by itself; it identifies what needs to be fixed.

---

## Key terms

- **CIA Triad** — Confidentiality, Integrity, Availability — the three core pillars of information security.
- **Confidentiality** — Ensuring information is accessible only to authorized parties.
- **Integrity** — Ensuring data is accurate and unaltered without authorization.
- **Availability** — Ensuring systems and data are accessible when needed by authorized users.
- **Non-repudiation** — Assurance that someone cannot deny the validity of their actions (commonly through digital signatures).
- **Authentication** — The process of verifying an entity's identity.
- **Authorization** — The process of determining what an authenticated entity is permitted to do.
- **Accounting** — Recording and tracking user activities for audit purposes.
- **AAA** — Authentication, Authorization, and Accounting framework.
- **Gap analysis** — Comparing current security posture against a desired state to identify deficiencies.
- **Zero Trust** — Security model based on "never trust, always verify" regardless of network location.
- **Control plane** — The decision-making component of Zero Trust (policy engine + policy administrator).
- **Data plane** — The traffic-carrying component where policy enforcement points operate.
- **Policy engine** — Evaluates access requests and makes grant/deny decisions.
- **Policy enforcement point (PEP)** — The component that enforces access decisions by allowing or blocking connections.
- **Honeypot** — A decoy system designed to attract and detect attackers.
- **Honeynet** — A network of honeypots simulating a real environment.
- **Honeytoken** — A fake data element that triggers alerts when accessed or used.
- **Honeyfile** — A decoy file placed to detect unauthorized access.
- **DNS sinkhole** — A DNS server that returns false results for malicious domains to disrupt attacker infrastructure.
- **Bollard** — A sturdy post designed to prevent vehicle ramming attacks.
- **Access control vestibule** — A mantrap; a small room with interlocking doors to prevent tailgating.

---

## Examples / scenarios

**Scenario 1:** A hospital's patient records system goes offline during a DDoS attack. Patients cannot be treated because doctors cannot access medication histories.
- **CIA pillar affected:** Availability

**Scenario 2:** An attacker intercepts network traffic and modifies a wire transfer amount from $10,000 to $100,000.
- **CIA pillar affected:** Integrity

**Scenario 3:** A disgruntled employee emails a confidential client list to a competitor.
- **CIA pillar affected:** Confidentiality

**Scenario 4:** A security team deploys a file named `employee_salaries_2026.xlsx` on a file share. The file contains fake data and is monitored for access.
- **Technology:** Honeyfile
- **Purpose:** Detect unauthorized access or insider threats

**Scenario 5:** An organization notices that its firewall rules allow all internal traffic without inspection. After reading the NIST Cybersecurity Framework, the team documents 47 controls they have not yet implemented.
- **Activity:** Gap analysis

**Scenario 6:** A user signs a contract electronically using a PKI-based digital signature. Later, the user claims they never signed it. The organization presents the digital signature and certificate chain as proof.
- **Concept:** Non-repudiation

---

## Mini quiz

<details>
<summary><strong>Question 1:</strong> Which component of the CIA Triad is most directly addressed by implementing RAID and backup solutions?</summary>

**Answer:** Availability. RAID and backups ensure data remains accessible even if hardware fails.
</details>

<details>
<summary><strong>Question 2:</strong> In a Zero Trust architecture, which component makes the decision to grant or deny an access request?</summary>

**Answer:** The policy engine. It evaluates access requests against defined policies and makes the grant/deny/revoke decision.
</details>

<details>
<summary><strong>Question 3:</strong> An organization inserts fake credentials into a database. When those credentials are used to attempt a login, a security alert fires. What is this technique called?</summary>

**Answer:** Honeytoken. The fake credentials are data elements designed to detect unauthorized use.
</details>

<details>
<summary><strong>Question 4:</strong> A user sends a digitally signed email. The recipient verifies the signature using the sender's public key. Which security concept does this primarily demonstrate?</summary>

**Answer:** Non-repudiation. The digital signature proves the sender authored the message and cannot deny it.
</details>

<details>
<summary><strong>Question 5:</strong> What is the difference between a honeypot and a honeynet?</summary>

**Answer:** A honeypot is a single decoy system; a honeynet is a network of multiple honeypots designed to simulate an entire environment and lure attackers into a monitored fake network.
</details>

<details>
<summary><strong>Question 6:</strong> A company redirects DNS queries for known malware command-and-control domains to a non-routable address. What technique is this?</summary>

**Answer:** DNS sinkhole. It disrupts malware C2 communication by returning false DNS results for malicious domains.
</details>

<details>
<summary><strong>Question 7:</strong> In the AAA framework, which component is responsible for tracking what a user did after they logged in?</summary>

**Answer:** Accounting. It records user activities for audit and forensic purposes.
</details>

---

## Navigation

**Domain 1: General Security Concepts**

| Objective | Title | Status |
|---|---|---|
| [1.1]({{ '/secplus/objectives/1-1/' | relative_url }}) | Compare and contrast various types of security controls | done |
| **1.2** | Summarize fundamental security concepts (current) | done |
| [1.3]({{ '/secplus/objectives/1-3/' | relative_url }}) | Explain the importance of change management processes | pending |
| [1.4]({{ '/secplus/objectives/1-4/' | relative_url }}) | Explain the importance of using appropriate cryptographic solutions | pending |

[← Previous: Objective 1.1]({{ '/secplus/objectives/1-1/' | relative_url }}) | [Back to Dashboard]({{ '/secplus/' | relative_url }}) | [Next: Objective 1.3 →]({{ '/secplus/objectives/1-3/' | relative_url }})
