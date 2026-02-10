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

### The CIA Triad (foundation of security)

The foundational model of information security. Every security decision maps back to one or more of these three goals.

#### Confidentiality

**Definition:** Protection of information from unauthorized access and disclosure. Only authorized people can VIEW the data.

**Why it matters:** Protect personal privacy (PII, PHI), maintain business advantage (trade secrets), achieve regulatory compliance (GDPR, HIPAA, PCI-DSS).

**Methods to ensure confidentiality:**
- **Encryption** — At rest (stored data), in transit (network traffic), in use (data being processed)
- **Access controls** — User permissions, least privilege
- **Data masking** — Obscure specific data (e.g., show only last 4 digits of SSN)
- **Physical security** — Locked server rooms, badge access
- **Training & awareness** — Educate users on data protection

**Exam example:** Encrypting laptop hard drives = Confidentiality

---

#### Integrity

**Definition:** Data remains accurate and unchanged unless modified by authorized personnel. Data is TRUSTWORTHY and UNALTERED.

**Why it matters:** Ensure data accuracy (financial records, medical data), maintain trust (customers, partners), ensure system operability (corrupted configs break systems).

**Methods to ensure integrity:**
- **Hashing** — Create fixed-size value (MD5, SHA-256). Any change = different hash.
- **Digital signatures** — Hash + encryption = authenticity + integrity
- **Checksums** — Verify data during transmission (CRC)
- **Access controls** — Prevent unauthorized modifications
- **Regular audits** — Review logs for unauthorized changes
- **Version control** — Track changes over time

**Exam example:** Using SHA-256 hash to verify downloaded file wasn't tampered with = Integrity

---

#### Availability

**Definition:** Information and resources are accessible when needed by authorized users. System UPTIME and ACCESS.

**Why it matters:** Business continuity (24/7 operations), customer trust (e-commerce availability), reputation (downtime = lost revenue).

**Key concept — REDUNDANCY** (duplication of critical components to enhance reliability):
- **Server redundancy** — Load balancing, failover clustering
- **Data redundancy** — RAID, backups (3-2-1 rule)
- **Network redundancy** — Multiple ISPs, redundant switches/routers
- **Power redundancy** — UPS (Uninterruptible Power Supply), generators

**Availability metrics:**
- **Uptime percentage** — 99.999% ("five nines") = 5.26 minutes downtime/year
- **RTO (Recovery Time Objective)** — Maximum acceptable downtime
- **RPO (Recovery Point Objective)** — Maximum acceptable data loss

**Exam example:** Implementing RAID 5 for server storage = Availability

---

#### CIA Triad summary

| Pillar | Goal | Threat example | Control example | Key method |
|---|---|---|---|---|
| **Confidentiality** | Only authorized parties can access the data | Data breach, shoulder surfing, eavesdropping | Encryption, access controls, data masking | Encryption |
| **Integrity** | Data is accurate, complete, and unaltered | Man-in-the-middle, data tampering | Hashing, digital signatures, version control | Hashing |
| **Availability** | Systems and data are accessible when needed | DDoS, ransomware, hardware failure | Redundancy, backups, load balancing | Redundancy |

#### Memory aid

> **C**an't see it = **C**onfidentiality (encryption). **I**s it accurate? = **I**ntegrity (hashing). **A**lways available = **A**vailability (redundancy).

---

### Non-repudiation

**Definition:** Proof that someone performed an action — they cannot deny it.

**How it works:**
1. User creates/sends message
2. Hash the message
3. Encrypt hash with user's PRIVATE key = digital signature
4. Recipient decrypts with user's PUBLIC key
5. Proves sender identity (only they have that private key)

**Technologies:**
- **Digital signatures** — Primary mechanism for non-repudiation
- **Audit logs** — Timestamped records that prove who did what and when
- **Certificates** — Tie a public key to an identity via a trusted Certificate Authority (CA)
- **Delivery receipts** — Email read receipts, blockchain transactions

**Exam focus:** Non-repudiation is most commonly associated with digital signatures and PKI. It is distinct from authentication — authentication proves who you are *now*; non-repudiation proves you did something *in the past* and cannot deny it.

**Exam keyword:** "Cannot deny" = Non-repudiation

---

### The CIA + Non-repudiation + Authentication = CIANA Pentagon

---

### Authentication, Authorization, and Accounting (AAA)

#### Authentication

**Definition:** Verifying identity — proving you are who you claim to be.

**The five authentication factors:**

| Factor | Type | Examples | Weakness |
|---|---|---|---|
| **Something you know** | Knowledge | Passwords, PINs, passphrases, security questions | Can be forgotten, shared, stolen |
| **Something you have** | Possession | Smart cards, key fobs, mobile device (SMS codes), hardware tokens (RSA SecurID) | Can be lost, stolen |
| **Something you are** | Inherence | Fingerprints, iris scans, facial recognition, voice recognition | Can't be changed if compromised |
| **Something you do** | Action | Typing patterns (keystroke dynamics), signature dynamics, gait analysis | Behavioral patterns can change |
| **Somewhere you are** | Location | GPS coordinates, IP geolocation, network location | Can be spoofed |

**Multi-Factor Authentication (MFA):**
- Uses TWO or MORE **different** factors
- **Not MFA:** Password + security question (both "something you know")
- **Is MFA:** Password + SMS code (knowledge + possession)

**Exam tip:** Count the TYPES of factors, not the NUMBER of items.

#### Memory aid — KHAIL

> **K**nowledge, **H**ave, **A**re, **I** do, **L**ocation

---

#### Authorization

**Definition:** Determining what an authenticated user can ACCESS or DO. Happens AFTER authentication.

**Key principles:**
- **Least privilege** — Minimum access needed to perform job
- **Need-to-know** — Access only to data required for specific tasks
- **Separation of duties** — No single person has complete control

**Authorization models:**
- **DAC (Discretionary Access Control)** — Owner controls access
- **MAC (Mandatory Access Control)** — System enforces based on labels
- **RBAC (Role-Based Access Control)** — Access based on job role
- **ABAC (Attribute-Based Access Control)** — Access based on attributes

---

#### Accounting

**Also called:** Auditing

**Definition:** Tracking and recording user activities.

**What it provides:**
1. **Audit trail** — Chronological record of who did what, when, where
2. **Regulatory compliance** — Maintain activity records (SOX, HIPAA)
3. **Forensic analysis** — Understand security incidents
4. **Resource optimization** — Track usage for capacity planning
5. **User accountability** — Deter misuse through monitoring

**Technologies used:**
- **Syslog servers** — Aggregate logs from network devices
- **Network analysis tools** — Capture and analyze traffic (Wireshark, tcpdump)
- **SIEM systems** — Real-time analysis of security alerts (Splunk, QRadar)

---

#### AAA summary

| Component | Question it answers | Examples |
|---|---|---|
| **Authentication** | "Who are you?" | Username/password, biometrics, smart cards, MFA |
| **Authorization** | "What are you allowed to do?" | ACLs, RBAC, file permissions, security groups |
| **Accounting** | "What did you do?" | Log files, SIEM events, session recordings, audit trails |

**AAA is a sequence:** Authenticate first, THEN authorize, THEN account.

**Protocols that implement AAA:**
- **RADIUS** — Remote Authentication Dial-In User Service. Commonly used for network access (VPN, Wi-Fi). Encrypts only the password.
- **TACACS+** — Terminal Access Controller Access-Control System Plus. Cisco-favored. Encrypts the entire payload. Separates authentication, authorization, and accounting.

#### Memory aid

> **"Who, What, When"** — Authentication: WHO are you? Authorization: WHAT can you access? Accounting: WHEN did you do it?

---

### Gap analysis

**Definition:** Evaluating differences between CURRENT state and DESIRED state to identify security gaps and prioritize improvements.

**Process steps:**
1. **Define scope** — What are we analyzing? (entire infrastructure, specific system, compliance requirement)
2. **Assess current state** — Document existing security controls, policies, configurations
3. **Identify desired state** — Based on standards, regulations, best practices (NIST CSF, ISO 27001, CIS Controls)
4. **Identify gaps** — Where do we fall short?
5. **Prioritize** — Risk-based prioritization
6. **Develop plan** — Create remediation roadmap

**Types of gap analysis:**
- **Technical gap analysis** — Evaluate technical infrastructure, identify capability shortfalls (e.g., legacy systems can't support modern encryption)
- **Business gap analysis** — Evaluate business processes, identify process shortfalls (e.g., no formal change management process)

**Output: Plan of Action and Milestones (POA&M)** — Specific measures to address each vulnerability with resource allocation, timelines, and milestones.

**Exam scenario:** "Organization wants to achieve SOX compliance. What should they do first?" Answer: Conduct gap analysis to identify compliance gaps.

---

### Zero Trust

**Core principle:** "Never trust, always verify"

- No implicit trust based on network location
- Verify every user, device, and transaction
- Assume breach has already occurred

#### Control plane (policy layer)

Makes decisions about WHO gets access to WHAT.

| Element | Description | Example |
|---|---|---|
| **Adaptive identity** | Real-time validation based on context (behavior, device, location, time, risk score) | Login from new country triggers extra verification |
| **Threat scope reduction** | Minimize attack surface, limit access to only what's needed, reduce "blast radius" of breach | Microsegmentation |
| **Policy-driven access control** | Access based on roles and responsibilities, dynamic policies, continuous evaluation | Contextual access rules |
| **Secured zones** | Isolated network segments for sensitive data, separate high-value assets | Network microsegmentation |

**Components:**
- **Policy engine** — Evaluates access requests against policies, makes grant/deny/revoke decisions
- **Policy administrator** — Manages and establishes policies, signals PEP to establish or tear down sessions

---

#### Data plane (enforcement layer)

WHERE access decisions are enforced.

- **Subject/System** — User or device requesting access
- **Policy Enforcement Point (PEP)** — Where access grant/deny is executed (network gateways, application proxies, endpoint agents)

---

#### Zero Trust workflow

1. Subject requests access to resource
2. Request goes to Policy Engine
3. Policy Engine evaluates: Identity verified? Device trusted? Location authorized? Time appropriate? Risk score acceptable?
4. Policy Administrator makes decision
5. Policy Enforcement Point grants/denies access
6. Continuous monitoring and re-evaluation

**Exam tip:** Know difference between Control Plane (decisions) and Data Plane (enforcement). PEP is part of the DATA plane, not the control plane — this is a common exam trap.

#### Memory aid

> **"Never trust, always verify, enforce everywhere"**

---

### Physical security

Physical security controls protect facilities, hardware, and people.

- **Bollards** — Short, sturdy posts that prevent vehicle-borne attacks against buildings. May be fixed, removable, or retractable.
- **Access control vestibules (mantraps)** — A small room with two interlocking doors. Only one door can be open at a time, preventing tailgating/piggybacking.
- **Fencing** — Perimeter barriers. Height matters: 3–4 feet deters casual trespassers; 6–7 feet too hard to climb easily; 8+ feet with barbed wire deters determined intruders.
- **Video surveillance** — CCTV systems for monitoring and recording. Can serve as both detective (recording) and deterrent (visible).
- **Security guards** — Human element. Can make judgment calls that technology cannot.
- **Access badges** — Smart cards or proximity cards for facility access. Can integrate with logical access systems.
- **Lighting** — Adequate lighting deters criminal activity and supports video surveillance.
- **Sensors:** Infrared (detects body heat), pressure (detects weight), microwave (detects movement via radiation reflection), ultrasonic (uses sound waves to detect motion).

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

### Common exam traps

**Trap: Confusing integrity and confidentiality.**
- Hashing DETECTS unauthorized changes (integrity), it does NOT prevent unauthorized access (confidentiality).
- Confidentiality = can't SEE it (encryption). Integrity = can't CHANGE it (hashing).

**Trap: Multi-factor misconceptions.**
- Password + security question = NOT MFA (both "something you know" = single factor).
- Count factor TYPES, not number of items.

**Trap: Authentication vs. authorization order.**
- You must prove WHO you are (authenticate) before determining WHAT you can do (authorize).

**Trap: Zero Trust = zero access.**
- Zero Trust does NOT mean no one gets access. It means verify everyone, no implicit trust. It's about VERIFICATION, not DENIAL.

**Trap: Non-repudiation vs. authentication.**
- Authentication proves identity at login; non-repudiation proves you cannot deny a past action.

---

### Exam tips

1. **CIA Triad appears everywhere.** Almost any security concept can be tied back to confidentiality, integrity, or availability. When you see a scenario, ask "Which part of CIA does this protect?"
2. **Zero Trust control plane vs. data plane** is a high-frequency exam topic. Know the three components: policy engine, policy administrator, and policy enforcement point. Remember PEP = data plane.
3. **Non-repudiation is not authentication.** Authentication proves identity at login; non-repudiation proves you cannot deny a past action (digital signatures are the key mechanism).
4. **Honeypot vs. honeytoken** — Systems vs. data. The exam likes to test this distinction.
5. **Physical security is testable.** Don't skip bollards, access vestibules, and sensor types.
6. **Gap analysis** is a planning/governance concept. It does not fix anything by itself; it identifies what needs to be fixed.
7. **MFA requires DIFFERENT factors** — Two passwords are not MFA.

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
- **MFA** — Multi-Factor Authentication; requires two or more different factor types.
- **Gap analysis** — Comparing current security posture against a desired state to identify deficiencies.
- **POA&M** — Plan of Action and Milestones; remediation roadmap output from gap analysis.
- **Zero Trust** — Security model based on "never trust, always verify" regardless of network location.
- **Control plane** — The decision-making component of Zero Trust (policy engine + policy administrator).
- **Data plane** — The traffic-carrying component where policy enforcement points operate.
- **Policy engine** — Evaluates access requests and makes grant/deny decisions.
- **Policy administrator** — Manages policies and signals PEP to establish/tear down sessions.
- **Policy enforcement point (PEP)** — The component that enforces access decisions by allowing or blocking connections.
- **Adaptive identity** — Context-aware authentication that adjusts based on risk signals.
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
<summary><strong>Question 6:</strong> A company redirects DNS queries for known malware C2 domains to a non-routable address. What technique is this?</summary>

**Answer:** DNS sinkhole. It disrupts malware C2 communication by returning false DNS results for malicious domains.
</details>

<details>
<summary><strong>Question 7:</strong> In the AAA framework, which component is responsible for tracking what a user did after they logged in?</summary>

**Answer:** Accounting. It records user activities for audit and forensic purposes.
</details>

<details>
<summary><strong>Question 8:</strong> A hospital implements disk encryption on all servers storing patient records. Which principle of the CIA triad does this primarily support?</summary>

**Answer:** Confidentiality. Encryption protects data from unauthorized viewing, even if physical media is stolen.
</details>

<details>
<summary><strong>Question 9:</strong> A user logs in with username/password, then receives a code on their smartphone that they must enter. How many authentication factors are being used?</summary>

**Answer:** Two factors (MFA). Password = something you know. Smartphone code = something you have. This is proper multi-factor authentication because it uses two DIFFERENT types of factors.
</details>

<details>
<summary><strong>Question 10:</strong> A company allows remote workers to access internal resources without VPN, but requires device health checks, geolocation verification, and behavior analysis before granting access. What security model is this?</summary>

**Answer:** Zero Trust. Key indicators: no implicit trust (no automatic VPN trust), continuous verification (device health, location, behavior), context-based access decisions.
</details>

### CompTIA-style practice questions

<details>
<summary><strong>Question 11:</strong> Which of the following BEST describes the difference between authentication and authorization?<br>A. Authentication verifies identity; authorization determines access rights<br>B. Authorization verifies identity; authentication determines access rights<br>C. Authentication is done first; authorization is optional<br>D. Authorization requires MFA; authentication does not</summary>

**Correct Answer: A**

- Authentication = Proving WHO you are (ID verification)
- Authorization = Determining WHAT you can do (permissions)

They happen in sequence: authenticate FIRST, then authorize.

- B: Backwards
- C: Authorization is not optional in secure systems
- D: Either can use MFA; not a distinguishing factor
</details>

<details>
<summary><strong>Question 12:</strong> A financial services company implements a system that creates tamper-evident logs of all transactions with timestamps and digital signatures. Which security concept is primarily being addressed?<br>A. Confidentiality<br>B. Availability<br>C. Non-repudiation<br>D. Authorization</summary>

**Correct Answer: C. Non-repudiation**

Digital signatures + timestamps = proof of action that cannot be denied. Key words: "tamper-evident" and "digital signatures" point to non-repudiation.

- A: Not about keeping data secret
- B: Not about system uptime
- D: Not about determining access rights
</details>

<details>
<summary><strong>Question 13:</strong> An organization conducts an assessment comparing their current security controls against industry best practices and compliance requirements. What is this called?<br>A. Penetration test<br>B. Gap analysis<br>C. Risk assessment<br>D. Vulnerability scan</summary>

**Correct Answer: B. Gap analysis**

Gap analysis specifically compares CURRENT state vs DESIRED state (best practices, compliance). Keywords: "comparing current" + "against requirements."

- A: Penetration test = simulated attack
- C: Risk assessment = identifying and analyzing risks
- D: Vulnerability scan = identifying technical vulnerabilities
</details>

<details>
<summary><strong>Question 14:</strong> Which of the following is NOT a component of the Zero Trust control plane?<br>A. Policy engine<br>B. Adaptive identity<br>C. Policy enforcement point<br>D. Threat scope reduction</summary>

**Correct Answer: C. Policy enforcement point**

PEP is part of the DATA PLANE (where enforcement happens), not the CONTROL PLANE (where decisions are made).

- Control Plane: Policy engine, policy administrator, adaptive identity, threat scope reduction, secured zones
- Data Plane: Subject/system, policy enforcement point

This is a common exam trap!
</details>

<details>
<summary><strong>Question 15 (Multi-select):</strong> A company wants to implement MFA. Which TWO combinations provide true multi-factor authentication?<br>A. Password + PIN<br>B. Password + Fingerprint scan<br>C. Smart card + PIN for the smart card<br>D. Fingerprint + Iris scan<br>E. Username + Password</summary>

**Correct Answers: B and C**

- **B**: Password (knowledge) + Fingerprint (inherence) = 2 different factors
- **C**: Smart card (possession) + PIN (knowledge) = 2 different factors

Why others are wrong:
- A: Both are "something you know" (same factor)
- D: Both are "something you are" (same factor)
- E: Both are "something you know" (not even MFA)

**Key Point:** Count the TYPES of factors, not the number of credentials!
</details>

---

## Real-world applications

**Confidentiality:** Healthcare encrypting patient records (HIPAA), finance protecting credit card numbers (PCI-DSS), government classifying sensitive documents.

**Integrity:** Software code signing certificates, hash verification of downloaded files, blockchain immutable transaction records.

**Availability:** E-commerce load-balanced web servers, banking redundant data centers, emergency services backup communication systems.

**Zero Trust:** Google's BeyondCorp, Microsoft's Conditional Access, cloud access security brokers (CASB).

---

## Related objectives

- [**1.1**]({{ '/secplus/objectives/1-1/' | relative_url }}) — Security controls implement these concepts
- [**1.4**]({{ '/secplus/objectives/1-4/' | relative_url }}) — Cryptographic solutions enable confidentiality, integrity, non-repudiation
- [**2.5**]({{ '/secplus/objectives/2-5/' | relative_url }}) — Mitigation techniques protect CIA
- [**3.1**]({{ '/secplus/objectives/3-1/' | relative_url }}) — Architecture models implement Zero Trust
- [**4.6**]({{ '/secplus/objectives/4-6/' | relative_url }}) — IAM implements authentication, authorization, accounting
- [**5.2**]({{ '/secplus/objectives/5-2/' | relative_url }}) — Risk management addresses CIA threats

---

## Navigation

**Domain 1: General Security Concepts**

| Objective | Title | Status |
|---|---|---|
| [1.1]({{ '/secplus/objectives/1-1/' | relative_url }}) | Compare and contrast various types of security controls | done |
| **1.2** | Summarize fundamental security concepts (current) | done |
| [1.3]({{ '/secplus/objectives/1-3/' | relative_url }}) | Explain the importance of change management processes | done |
| [1.4]({{ '/secplus/objectives/1-4/' | relative_url }}) | Explain the importance of using appropriate cryptographic solutions | done |

[← Previous: Objective 1.1]({{ '/secplus/objectives/1-1/' | relative_url }}) | [Back to Dashboard]({{ '/secplus/' | relative_url }}) | [Next: Objective 1.3 →]({{ '/secplus/objectives/1-3/' | relative_url }})

