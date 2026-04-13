---
layout: objective
title: "Security+ 2.5 — Explain the purpose of mitigation techniques used to secure the enterprise."
objective_id: "2.5"
domain: "2.0 Threats, Vulnerabilities, and Mitigations"
status: "done"
tags:
  - secplus701
permalink: /secplus/objectives/2-5/
---

# Security+ 2.5 — Explain the purpose of mitigation techniques used to secure the enterprise.

Status: <span class="status-badge done">done</span>

## Exam objective
Explain the purpose of mitigation techniques used to secure the enterprise.

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

Mitigation techniques are the defensive controls and processes used to reduce the likelihood or impact of threats and vulnerability exploitation. This objective ties directly back to 2.3 (vulnerabilities) and 2.4 (malicious activity): for each type of threat, there is a corresponding mitigation. The exam tests whether you can select the **right** mitigation for the given scenario — not just list defences generically.

---

### Patching and system hardening

| Technique | Purpose |
|---|---|
| **Patch Management** | Systematically identify, test, and apply software/OS updates to fix known CVEs |
| **System Hardening** | Reducing the attack surface by disabling unnecessary services, removing default accounts, enforcing least privilege |
| **Configuration Management** | Establishing and enforcing secure baseline configurations across all systems |
| **Disable Unnecessary Services** | Every open port and running service is a potential entry point — eliminate what is not needed |
| **Remove Default Credentials** | Default usernames/passwords are public knowledge; change them immediately on deployment |

> **Exam Tip:** Patching addresses *known* vulnerabilities with existing CVEs. It cannot address zero-days.

---

### Network segmentation and isolation

| Technique | Purpose |
|---|---|
| **Network Segmentation** | Dividing a network into separate segments (VLANs, subnets) to contain breaches and limit lateral movement |
| **DMZ (Demilitarised Zone)** | Isolated network segment hosting public-facing services, separated from the internal network |
| **Air Gap** | Complete physical isolation from other networks — used for critical systems (ICS, classified systems) |
| **Micro-segmentation** | Fine-grained segmentation at the workload/application level; enforces Zero Trust between internal systems |

**Primary value:** Contains breach impact — even if an attacker enters one segment, they cannot freely move laterally to others.

---

### Access control mitigations

| Technique | Purpose |
|---|---|
| **Least Privilege** | Users/processes have only the minimum access required to perform their function |
| **Separation of Duties** | No single person has complete control over a critical process; requires collusion to misuse |
| **Need-to-Know** | Access to data is granted only when operationally necessary |
| **Account Reviews / Auditing** | Periodic review of user accounts; remove excessive permissions and dormant accounts |
| **MFA (Multi-Factor Authentication)** | Requires two or more authentication factors; mitigates credential theft |
| **Privileged Access Management (PAM)** | Tightly controls, monitors, and audits privileged (admin) accounts |

---

### Endpoint and application security

| Technique | Purpose |
|---|---|
| **Antivirus / Anti-malware** | Signature-based and heuristic detection of known and unknown malware |
| **EDR (Endpoint Detection and Response)** | Advanced endpoint monitoring; behavioural analysis, threat hunting, automated response |
| **Application Whitelisting (Allow Lists)** | Only pre-approved applications may execute; blocks unknown/malicious executables |
| **Application Blacklisting (Deny Lists)** | Specific known-bad applications are blocked; everything else is permitted |
| **Input Validation** | Sanitise all user input before processing; primary defence against injection attacks (SQLi, XSS) |
| **Sandboxing** | Isolate and execute untrusted code in a contained environment; observe behaviour without risk |
| **Code Signing** | Cryptographic signature verifies software authenticity and integrity |

> **Whitelist vs. Blacklist:** Whitelist = secure by default (deny all, permit exceptions). Blacklist = permit by default (allow all, deny known-bad). Whitelist is more secure; blacklist is easier to manage.

---

### Network security controls

| Technique | Purpose |
|---|---|
| **Firewall** | Filters traffic based on rules (packet filtering, stateful inspection, NGFW) |
| **IDS (Intrusion Detection System)** | Monitors and alerts on suspicious traffic; passive — does not block |
| **IPS (Intrusion Prevention System)** | Monitors and actively blocks suspicious traffic; inline — can block |
| **Web Application Firewall (WAF)** | Protects web apps from layer 7 attacks (SQLi, XSS, CSRF) |
| **DLP (Data Loss Prevention)** | Monitors and prevents unauthorised transmission of sensitive data |
| **DNS Filtering** | Blocks resolution of known malicious domains; prevents C2 communication |
| **Proxy / Content Filtering** | Inspects and filters web traffic; blocks malicious URLs and categories |
| **VPN / Encryption in Transit** | Protects data in transit; prevents eavesdropping and MITM |

---

### Vulnerability management as mitigation

The full cycle:
1. **Identify** — scanning (Nessus, OpenVAS), penetration testing, audits.
2. **Analyse** — CVSS scoring, true/false positive classification, prioritisation.
3. **Remediate** — patching, configuration changes, compensating controls.
4. **Validate** — rescan, penetration test, audit to confirm fix.
5. **Report** — internal and external reporting; responsible disclosure.

**Compensating Controls** — alternative measures when the primary control cannot be applied (e.g., network segmentation for a legacy system that cannot be patched).

**Exception vs. Exemption:**
- **Exception** — temporary relaxation of a control for business needs (time-limited).
- **Exemption** — permanent waiver, often for legacy systems; requires risk acceptance documentation.

---

### Data protection techniques

| Technique | Purpose |
|---|---|
| **Encryption (at rest)** | Protects stored data from unauthorised access (FDE, TDE, file encryption) |
| **Encryption (in transit)** | Protects data moving across networks (TLS, IPSec, VPN) |
| **Tokenisation** | Replaces sensitive data with non-sensitive tokens; original stored in secure vault |
| **Data Masking** | Partially obscures data while retaining format (SSN to XXX-XX-1234) |
| **Hashing** | One-way transformation; password storage; integrity verification |
| **DLP Systems** | Endpoint, network, storage, and cloud-based DLP prevent data exfiltration |
| **Backups (3-2-1 Rule)** | 3 copies, 2 different media, 1 offsite; primary defence against ransomware |

---

### Awareness and process controls

| Technique | Purpose |
|---|---|
| **Security Awareness Training** | Reduces the human vector; teaches users to recognise phishing, social engineering |
| **Anti-Phishing Simulations** | Simulated phishing campaigns; identify and train susceptible users |
| **Incident Response Plan** | Documented, rehearsed procedures for detecting, containing, and recovering from incidents |
| **Change Management** | Controlled change process prevents accidental misconfiguration |
| **Background Checks** | Reduce insider threat risk during hiring |
| **Clean Desk / Clean Screen Policy** | Physical security for sensitive information; prevents shoulder surfing and dumpster diving |

---

### Choosing the right mitigation for the scenario

| Scenario / Threat | Best Mitigation |
|---|---|
| Known CVE on a live server | **Patch management** |
| Legacy system that cannot be patched | **Network segmentation + compensating controls** |
| Zero-day vulnerability | **Behaviour-based detection, segmentation, defence in depth** |
| Phishing emails reaching employees | **Email gateway, DKIM/SPF/DMARC, user awareness training** |
| Ransomware attack | **Backups (3-2-1), MFA, patch management** |
| Insider threat | **Least privilege, separation of duties, PAM, audit logging** |
| SQL injection risk | **Input validation, WAF, parameterised queries** |
| Botnet/C2 communication | **DNS filtering, firewall egress rules** |
| Credentials stolen / account takeover | **MFA, PAM, account auditing** |
| Lateral movement after breach | **Network segmentation, micro-segmentation** |
| Data exfiltration via USB | **DLP (endpoint), removable media policy** |
| Phishing (human vector) | **Security awareness training, anti-phishing simulations** |

---

### Key distinctions to know for the exam

| Comparison | Distinction |
|---|---|
| **IDS vs. IPS** | IDS = passive (detects and alerts only); IPS = active (detects AND blocks). IPS is inline; IDS is out-of-band. |
| **Whitelist vs. Blacklist** | Whitelist = deny-by-default, explicit allow; Blacklist = allow-by-default, explicit deny. Whitelist is more secure. |
| **Compensating vs. Corrective control** | Compensating = alternative used INSTEAD of primary control; Corrective = applied AFTER an incident to fix damage. |
| **Exception vs. Exemption** | Exception = temporary relaxation; Exemption = permanent waiver. Both require risk documentation. |
| **Patch vs. Compensating Control** | Patch = removes the vulnerability; Compensating control = reduces risk when patching is not possible. |
| **Encryption vs. Tokenisation** | Encryption = reversible with key; Tokenisation = token has no mathematical link to original data, stored separately. |
| **Network Segmentation vs. Air Gap** | Segmentation = logical isolation (VLANs, firewalls); Air gap = physical disconnection — no network path at all. |

---

### Common exam traps

**Trap: Thinking IDS and IPS are interchangeable.**
Reality: IDS is passive — it detects and alerts but takes no action. IPS is inline and actively blocks traffic matching signatures. Deploying an IDS when blocking is needed = wrong answer.

**Trap: Assuming patching solves all vulnerability problems.**
Reality: Patching only addresses *known, patchable* vulnerabilities. Zero-days, hardware flaws, and legacy systems that cannot be patched require compensating controls.

**Trap: Treating a compensating control as equivalent to the primary control.**
Reality: Compensating controls are *better than nothing* but do not fully replace the protection of the primary control. They are explicitly a risk-acceptance strategy.

**Trap: Confusing data masking with encryption.**
Reality: Masking replaces data with placeholders (irreversible); encryption transforms data (reversible with key). Masked data cannot be "unmasked" — encryption can be decrypted.

**Trap: Thinking MFA alone prevents all account compromise.**
Reality: MFA reduces account takeover risk significantly but does not stop session hijacking after authentication, SIM swapping attacks, or social engineering to bypass the second factor.

---

### Exam tips

1. When a question asks how to protect a **legacy system that cannot be patched**, the answer is always a combination of **network segmentation** and **compensating controls**.
2. If the scenario says an attacker is **communicating with a C2 server**, the mitigation is **DNS filtering** and **firewall egress rules** — block outbound C2 traffic.
3. **Defence in depth** (layered security) is the overarching principle when no single control is sufficient — always valid as a concept answer.
4. **Backups** are the most critical ransomware mitigation. A 3-2-1 backup strategy means ransomware cannot permanently destroy data.
5. When the question is about stopping **lateral movement after a breach**, think **network segmentation / micro-segmentation**.
6. For questions about **human-factor attacks** (phishing, social engineering), the answer almost always includes **user awareness training**.

---

## Key terms

- **Patch Management** — Process of applying software updates to fix known vulnerabilities.
- **System Hardening** — Reducing the attack surface by removing unnecessary components and enforcing secure configurations.
- **Network Segmentation** — Dividing a network into isolated segments to contain breaches and prevent lateral movement.
- **DMZ (Demilitarised Zone)** — Isolated network segment for public-facing services, shielded from the internal network.
- **Air Gap** — Physical isolation of a system from all external networks.
- **Micro-segmentation** — Fine-grained, workload-level network segmentation supporting Zero Trust.
- **Least Privilege** — Granting users and processes only the minimum access required for their function.
- **Separation of Duties** — Dividing critical tasks among multiple individuals to prevent unilateral misuse.
- **MFA (Multi-Factor Authentication)** — Using two or more authentication factors; critical defence against credential theft.
- **EDR (Endpoint Detection and Response)** — Advanced endpoint security with behavioural analysis and automated response.
- **IDS (Intrusion Detection System)** — Passive monitoring tool that detects and alerts on suspicious traffic.
- **IPS (Intrusion Prevention System)** — Inline monitoring tool that detects AND blocks suspicious traffic.
- **WAF (Web Application Firewall)** — Application-layer firewall protecting against SQLi, XSS, and other web attacks.
- **DLP (Data Loss Prevention)** — Controls to detect and prevent unauthorised data exfiltration.
- **Compensating Control** — An alternative security measure used when the primary control cannot be implemented.
- **Exception** — Temporary relaxation of a security control for business purposes.
- **Exemption** — Permanent waiver of a security control, typically for legacy systems with accepted risk.
- **Defence in Depth** — Layering multiple security controls so that failure of one does not compromise the whole.
- **3-2-1 Backup Rule** — Maintain 3 copies on 2 different media with 1 offsite; standard ransomware resilience strategy.

---

## Examples / scenarios

**Scenario 1:** A hospital runs a critical patient monitoring system that cannot be patched due to vendor support constraints. The system has a known CVE with a CVSS score of 9.8.
- **Answer:** Apply compensating controls: place the system on an isolated VLAN (network segmentation), implement strict firewall rules allowing only necessary traffic, add enhanced monitoring/IDS, and document a formal exemption with risk acceptance sign-off.

**Scenario 2:** A web application is vulnerable to SQL injection. The development team will not be able to release a fix for 60 days.
- **Answer:** Deploy a **WAF** to detect and block SQLi patterns immediately (compensating control). Also enable input validation at the application layer and implement parameterised queries in the fix. Use the WAF as a short-term bridge while the permanent fix is developed.

**Scenario 3:** After a ransomware incident, executives ask what single control would have most limited the damage.
- **Answer:** A **3-2-1 backup strategy** — if clean, tested backups existed, data restoration would have been straightforward without paying the ransom. Segmentation would have limited spread; backups would have enabled recovery.

**Scenario 4:** Security analysts are overwhelmed by thousands of daily alerts from the IDS, most of which are false positives related to legacy application traffic.
- **Answer:** Tune the IDS alert rules to reduce false positives (alert tuning/threshold adjustment). Consider upgrading to an **IPS** with more context-aware detection. Implement a SIEM for alert correlation to reduce analyst fatigue.

**Scenario 5:** Employees regularly fall for phishing simulations. The CISO asks for the single most effective control to address this.
- **Answer:** Targeted **security awareness training** with follow-up simulations and remedial training for repeat failures. Technical controls (email gateways, anti-phishing) are also needed, but the human vector requires human-focused mitigation.

---

## Mini quiz

<details>
<summary><strong>Question 1:</strong> What is the difference between an IDS and an IPS?</summary>

**Answer:** An **IDS (Intrusion Detection System)** is passive — it monitors traffic, detects suspicious patterns, and generates alerts, but takes no blocking action. An **IPS (Intrusion Prevention System)** is active/inline — it both detects *and* blocks matching traffic in real time. Use IDS when you want visibility without risk of false-positive blocking; use IPS when active protection is needed.
</details>

<details>
<summary><strong>Question 2:</strong> A legacy medical device cannot be patched due to vendor certification constraints. What is the recommended approach?</summary>

**Answer:** Apply **compensating controls**: isolate the device on a dedicated VLAN (network segmentation), restrict firewall rules to only allow necessary communication, implement enhanced monitoring (IDS), and document an official **exemption** with risk acceptance sign-off from management.
</details>

<details>
<summary><strong>Question 3:</strong> Explain the 3-2-1 backup rule and why it matters for ransomware defence.</summary>

**Answer:** Keep **3** total copies of data, on **2** different storage media types, with **1** copy stored offsite (or in a separate cloud environment). Ransomware typically encrypts all reachable local data. If the offsite/offline copy is unreachable by the malware, recovery is possible without paying the ransom.
</details>

<details>
<summary><strong>Question 4:</strong> What is the difference between a security exception and a security exemption?</summary>

**Answer:** An **exception** is a *temporary* relaxation of a security control for a specific business need — it has an expiry date and requires risk acknowledgement. An **exemption** is a *permanent* waiver of a control, typically for legacy systems that cannot comply. Both require formal documentation and risk acceptance.
</details>

<details>
<summary><strong>Question 5:</strong> An organisation wants to prevent employees from copying sensitive customer data to personal cloud storage. Which control category addresses this?</summary>

**Answer:** **DLP (Data Loss Prevention)** — specifically endpoint DLP that monitors file transfers and blocks uploads to unauthorised destinations. Combined with a user awareness policy and acceptable use policy (directive control) for complete coverage.
</details>

### CompTIA-style practice questions

<details>
<summary><strong>Question 6:</strong> A security administrator needs to ensure that malware on a compromised workstation cannot spread to other segments of the network or reach financial systems. Which mitigation technique BEST achieves this?<br>A. Applying the latest OS patches<br>B. Enabling full-disk encryption<br>C. Implementing network segmentation<br>D. Deploying antivirus on the workstation</summary>

**Correct Answer: C. Implementing network segmentation**

Network segmentation contains lateral movement by isolating the compromised workstation in its own network segment, preventing spread to financial systems. Patching (A) addresses vulnerabilities but does not contain an active compromise. Full-disk encryption (B) protects data confidentiality, not network spread. Antivirus (D) may clean the workstation but does not prevent network-based lateral movement if the malware has already established a foothold.
</details>

<details>
<summary><strong>Question 7:</strong> An organisation's web application is experiencing SQL injection attempts. The development team estimates 90 days to implement parameterised queries. Which control provides the BEST immediate protection?<br>A. Intrusion Detection System (IDS)<br>B. Web Application Firewall (WAF)<br>C. Input validation in the database<br>D. Network segmentation</summary>

**Correct Answer: B. Web Application Firewall (WAF)**

A WAF operates at the application layer and can detect and block SQL injection patterns in real time, serving as an immediate compensating control while the development fix is prepared. IDS (A) is passive — it detects but does not block. Input validation in the database (C) is too deep in the stack and is not a real mitigation. Network segmentation (D) does not protect against application-layer attacks on a public-facing service.
</details>

<details>
<summary><strong>Question 8 (Multi-select):</strong> An organisation wants to reduce the risk of insider threats. Which TWO of the following controls are MOST effective? (Choose TWO)<br>A. Deploy a honeypot to attract external attackers<br>B. Implement least privilege access controls<br>C. Configure DNS filtering for known malicious domains<br>D. Conduct regular account access reviews and audits<br>E. Apply OS patches on a monthly schedule</summary>

**Correct Answers: B. Implement least privilege access controls and D. Conduct regular account access reviews and audits**

Least privilege (B) limits what an insider can access — reducing the blast radius of malicious or negligent actions. Regular access reviews (D) detect and remove excessive permissions, dormant accounts, and anomalous access patterns. Honeypots (A) target external attackers. DNS filtering (C) blocks external C2 communication. OS patching (E) addresses technical vulnerabilities, not the insider human risk.
</details>

---

## Related objectives

- [**2.3**]({{ '/secplus/objectives/2-3/' | relative_url }}) — Vulnerability types define what mitigations are needed; every vulnerability has a corresponding mitigation strategy.
- [**2.4**]({{ '/secplus/objectives/2-4/' | relative_url }}) — Indicators of malicious activity drive the selection of detective and responsive mitigations.
- [**1.1**]({{ '/secplus/objectives/1-1/' | relative_url }}) — Security control categories (Technical, Managerial, Operational, Physical) are the framework within which all mitigations sit.
- [**3.1**]({{ '/secplus/objectives/3-1/' | relative_url }}) — Security architecture decisions (Zero Trust, defence in depth) determine which mitigation layers are deployed and how.

---

## Navigation

**Domain 2.0: Threats, Vulnerabilities, and Mitigations**

| Objective | Title | Status |
|---|---|---|
| [2.1]({{ '/secplus/objectives/2-1/' | relative_url }}) | Compare and contrast common threat actors and motivations. | done |
| [2.2]({{ '/secplus/objectives/2-2/' | relative_url }}) | Explain common threat vectors and attack surfaces. | done |
| [2.3]({{ '/secplus/objectives/2-3/' | relative_url }}) | Explain various types of vulnerabilities. | done |
| [2.4]({{ '/secplus/objectives/2-4/' | relative_url }}) | Given a scenario, analyze indicators of malicious activity. | done |
| **2.5** | Explain the purpose of mitigation techniques used to secure the enterprise. (current) | done |

[← Previous: Objective 2.4]({{ '/secplus/objectives/2-4/' | relative_url }}) | [Back to Dashboard]({{ '/secplus/' | relative_url }}) | [Next: Domain 3 →]({{ '/secplus/objectives/3-1/' | relative_url }})
