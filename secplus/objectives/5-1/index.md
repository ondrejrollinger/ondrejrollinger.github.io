---
layout: objective
title: "Security+ 5.1 — Summarize elements of effective security governance."
objective_id: "5.1"
domain: "5.0 Security Program Management and Oversight"
status: "done"
tags:
  - secplus701
permalink: /secplus/objectives/5-1/
---

# Security+ 5.1 — Summarize elements of effective security governance.

Status: <span class="status-badge done">done</span>

## Exam objective
Summarize elements of effective security governance.

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

Governance elements provide structure and accountability for security programs. This includes policies, standards, procedures, regulations, and frameworks that guide security decision-making. The exam emphasizes recognizing which regulation, standard, or framework applies to a given scenario — especially across industries.

---

## Governance Structure

**Governance definition:** System of rules, practices, and processes directing and controlling security activities.

**Purpose:**
- Define authority and accountability
- Ensure compliance with laws/regulations
- Align security with business objectives
- Manage risk appropriately

**Governance components:**

**Board of Directors:**
- **Role:** Oversight of organizational risk
- **Responsibilities:** Approve policies, review risk reports, ensure compliance
- **Security involvement:** Receive CISO reports, approve major security investments

**Executive Management (C-suite):**
- **CEO:** Ultimate accountability for organizational security
- **CISO/CSO:** Security program leadership
- **CIO:** IT infrastructure and security
- **CFO:** Security budget approval
- **General Counsel:** Legal/regulatory compliance

**Security Steering Committee:**
- **Composition:** CISO, IT leaders, business unit heads, legal, HR
- **Purpose:** Strategic security decisions
- **Activities:** Review policies, prioritize initiatives, approve budgets

**Security Operations:**
- **SOC (Security Operations Center):** 24/7 monitoring and response
- **Risk management team:** Assess and manage risks
- **Compliance team:** Ensure regulatory adherence
- **Security engineering:** Implement controls

**Exam tip:** The CISO leads the security program but the Board of Directors holds ultimate *oversight* of organizational risk. Questions may ask who receives CISO reports or who approves major security investments.

---

## Regulations, Standards, and Legislation

**Regulations (legally binding):**

**General Data Protection Regulation (GDPR):**
- **Jurisdiction:** European Union
- **Scope:** Personal data of EU citizens (regardless of where the company is based)
- **Requirements:**
  - Consent for data collection
  - Right to be forgotten (data deletion)
  - Data breach notification within **72 hours**
  - Privacy by design
- **Penalties:** Up to 4% of annual global revenue or €20M (whichever is higher)

**Health Insurance Portability and Accountability Act (HIPAA):**
- **Jurisdiction:** United States
- **Scope:** Protected Health Information (PHI)
- **Requirements:**
  - Privacy Rule (who can access PHI)
  - Security Rule (safeguards for ePHI)
  - Breach Notification Rule (notify within **60 days**)
- **Penalties:** $100–$50,000 per violation

**Payment Card Industry Data Security Standard (PCI DSS):**
- **Jurisdiction:** Global (card brand requirement — not a government law)
- **Scope:** Any organization that stores, processes, or transmits credit card data
- **12 Requirements:** Firewall configuration, no default passwords, protect stored cardholder data, encrypt transmissions, antivirus, secure systems/applications, restrict access (need-to-know), unique IDs, restrict physical access, track/monitor access, test security systems, maintain security policy
- **Penalties:** Fines from card brands; loss of ability to process card payments

**Sarbanes-Oxley Act (SOX):**
- **Jurisdiction:** United States
- **Scope:** Publicly traded companies
- **Requirements:** Financial reporting controls, IT general controls (access, change management), executive certification of financial statements
- **Penalties:** Criminal penalties for executives who certify false statements

**Gramm-Leach-Bliley Act (GLBA):**
- **Jurisdiction:** United States
- **Scope:** Financial institutions
- **Requirements:** Privacy notice to customers, safeguard customer information, pretexting protection
- **Penalties:** Civil and criminal penalties

**Federal Information Security Management Act (FISMA):**
- **Jurisdiction:** United States federal agencies
- **Scope:** Government information systems
- **Requirements:** Risk-based security programs, annual FISMA audits, NIST framework compliance

**Exam tip:** PCI DSS is frequently tested as a trap — it is a *card brand contractual requirement*, not a government regulation. GDPR and HIPAA are laws. ISO 27001 and NIST CSF are voluntary standards.

---

**Standards (voluntary best practices):**

**ISO/IEC 27001:**
- **Purpose:** Information security management system (ISMS) — the certifiable standard
- **Scope:** International; any organization type or size
- **Benefits:** Certification demonstrates security commitment to customers and partners
- **Requirements:** 114 controls across 14 domains

**ISO/IEC 27002:**
- **Purpose:** Code of practice providing implementation guidance for ISO 27001 controls
- **Key distinction:** Not independently certifiable — it is the companion guide to 27001

**NIST Cybersecurity Framework (CSF):**
- **Purpose:** Voluntary framework for managing cybersecurity risk
- **Five Functions:**
  1. **Identify** — Asset management, risk assessment
  2. **Protect** — Access control, training, data security
  3. **Detect** — Monitoring, detection processes
  4. **Respond** — Incident response, communications
  5. **Recover** — Recovery planning, improvements
- **Tiers:** Partial (1) → Risk Informed (2) → Repeatable (3) → Adaptive (4)
- **Profiles:** Current state vs. target state

**NIST SP 800-53:**
- **Purpose:** Detailed security and privacy controls for federal systems
- **Scope:** US federal agencies (required for FISMA compliance)
- **Control families:** 20 families (e.g., Access Control, Incident Response, Audit)

**CIS Controls (Center for Internet Security):**
- **Purpose:** Prioritized, actionable cybersecurity best practices
- **Implementation Groups:** IG1 (essential), IG2 (foundational), IG3 (organizational)
- **Examples:** Control 1 (asset inventory), Control 2 (software inventory), Control 4 (secure configuration), Control 5 (account management)

**Industry-specific standards:**
- **NERC CIP:** North American Electric Reliability Corporation — Critical Infrastructure Protection (power grid)
- **HITRUST:** Health Information Trust Alliance (healthcare)
- **FedRAMP:** Federal Risk and Authorization Management Program (cloud services for US government)

**Exam tip:** Know NIST CSF's five functions by name. "Identify, Protect, Detect, Respond, Recover" is a common exam topic. NIST 800-53 provides the *detailed controls* behind the framework.

---

## National vs. International Standards

| Dimension | National | International |
|---|---|---|
| **Examples** | FISMA (US), PIPEDA (Canada), Data Protection Act (UK) | GDPR (EU/global impact), ISO 27001 |
| **Enforcement** | National government | EU member states (GDPR); industry bodies (ISO) |
| **Scope** | Within country borders | Multiple countries or global |
| **Extraterritorial reach** | Generally limited to country | GDPR applies to *any* org processing EU citizen data |

**Exam tip:** GDPR's extraterritorial reach is a key exam topic. A US-based company with EU customers must comply with GDPR — jurisdiction is determined by where the *data subject* is located, not where the company is headquartered.

---

## Industry-Specific Considerations

| Industry | Key Regulations | Standards | Primary Focus |
|---|---|---|---|
| **Healthcare** | HIPAA, HITECH Act | HITRUST | Patient privacy, PHI/ePHI protection |
| **Financial** | GLBA, SOX (if public), PCI DSS | ISO 27001, COBIT | Financial data, fraud prevention |
| **Government** | FISMA, CJIS | NIST SP 800-53, FedRAMP | National security, classified info |
| **Retail** | PCI DSS, state breach laws | ISO 27001 | Payment card data, customer PII |
| **Critical Infrastructure** | NERC CIP (power), TSA (transportation) | NIST CSF, ICS standards | Operational technology (OT) security |

---

## Benchmarks and Secure Configuration Guides

**Purpose:** Establish security baseline configurations for systems and applications.

**CIS Benchmarks:**
- **Coverage:** 100+ technology platforms (Windows, Linux, Cisco, AWS, Azure, etc.)
- **Levels:**
  - **Level 1:** Basic security hardening with minimal business impact
  - **Level 2:** Defense in depth; may impact functionality or usability

**DISA STIGs (Security Technical Implementation Guides):**
- **Purpose:** US Department of Defense security configuration standards
- **Scope:** Required for military and federal contractor systems
- **Coverage:** Operating systems, applications, network devices

**Vendor hardening guides:**
- Microsoft Security Baselines, Red Hat Security Guide, Cisco Security Configuration Guide, AWS Security Best Practices

**Implementation process:**
1. Select appropriate benchmark (CIS, DISA STIG)
2. Test in a non-production environment
3. Document any deviations (with business justification)
4. Apply to production with change control
5. Audit compliance regularly
6. Update when new benchmark versions are released

**Exam tip:** Benchmarks do not need to be followed *exactly*. Deviations are permitted — they must be **documented with business justification**. This often appears in exam scenarios as a trap implying any deviation is a violation.

---

## Key distinctions to know for the exam

| Comparison | Distinction |
|---|---|
| **Regulation vs. standard** | Regulation: legally binding (GDPR, HIPAA). Standard: voluntary best practice (ISO 27001, NIST CSF). |
| **GDPR vs. HIPAA** | GDPR covers all EU personal data (any type). HIPAA covers US health information (PHI) only. |
| **ISO 27001 vs. ISO 27002** | 27001 is certifiable ISMS framework. 27002 is the implementation guidance — not independently certifiable. |
| **NIST CSF vs. NIST 800-53** | CSF is a high-level framework with 5 functions (all organizations). 800-53 provides detailed controls for federal systems. |
| **National vs. international** | National: single country jurisdiction. International: cross-border or global scope. |
| **PCI DSS vs. GDPR** | PCI DSS is a contractual card brand requirement (not a law). GDPR is binding EU law with extraterritorial reach. |
| **CIS Level 1 vs. Level 2** | Level 1: basic, low-impact hardening. Level 2: deeper hardening, may affect functionality. |

---

## Common exam traps

**Trap: Thinking all standards are legally required.**
Reality: ISO 27001, NIST CSF, and CIS Benchmarks are voluntary. Only regulations (GDPR, HIPAA, SOX) are legally mandated.

**Trap: Believing GDPR only applies to EU-based companies.**
Reality: GDPR applies to any organization anywhere in the world that processes personal data belonging to EU citizens.

**Trap: Assuming PCI DSS is a government law.**
Reality: PCI DSS is a contractual requirement enforced by card brands (Visa, Mastercard, etc.), not a government regulation. Penalties come from card brands, not government agencies.

**Trap: Thinking benchmark deviations are always violations.**
Reality: Deviations from CIS Benchmarks or DISA STIGs are permitted when documented with a valid business justification.

**Trap: Believing one framework fits all industries.**
Reality: Healthcare uses HIPAA/HITRUST; government uses FISMA/NIST 800-53; power grid uses NERC CIP. Industry context determines the applicable framework.

**Trap: Confusing ISO 27001 and ISO 27002.**
Reality: Only 27001 can be certified. 27002 is a supporting guidance document — an organization cannot "achieve ISO 27002 certification."

---

## Exam tips

1. **GDPR = EU personal data** — 72-hour breach notification; extraterritorial reach
2. **HIPAA = US healthcare** — PHI protection; 60-day breach notification
3. **PCI DSS = payment cards** — 12 requirements; *not a law*, card brand requirement
4. **SOX = financial reporting** — US public companies; criminal penalties for executives
5. **GLBA = financial institutions** — customer data privacy; pretexting protection
6. **FISMA = US federal agencies** — requires NIST framework compliance
7. **ISO 27001 = certifiable ISMS** — 27002 is the implementation guidance only
8. **NIST CSF = 5 functions** — Identify, Protect, Detect, Respond, Recover
9. **NIST 800-53 = detailed controls** — for federal systems; 20 control families
10. **CIS Benchmarks = configuration** — Level 1 (basic) and Level 2 (deep hardening)
11. **DISA STIGs = DoD** — required for military and federal contractor systems
12. **Regulations are mandatory** — standards are voluntary

---

## Key terms

- **Governance** — The system of rules, practices, and processes directing and controlling an organization's security activities.
- **CISO (Chief Information Security Officer)** — Executive responsible for leading the security program and reporting to the Board of Directors.
- **Regulation** — A legally binding rule issued by a government body; non-compliance results in legal penalties (e.g., GDPR, HIPAA, SOX).
- **Standard** — A voluntary best-practice framework or set of guidelines; not legally mandated (e.g., ISO 27001, NIST CSF, CIS Controls).
- **GDPR (General Data Protection Regulation)** — EU regulation protecting personal data of EU citizens; applies globally to any organization handling EU data; 72-hour breach notification.
- **HIPAA (Health Insurance Portability and Accountability Act)** — US law protecting Protected Health Information (PHI); requires Privacy, Security, and Breach Notification rules.
- **PCI DSS (Payment Card Industry Data Security Standard)** — Card brand contractual requirement (not law) for organizations handling credit card data; 12 requirements.
- **SOX (Sarbanes-Oxley Act)** — US law requiring financial reporting controls for publicly traded companies; criminal penalties for executives.
- **GLBA (Gramm-Leach-Bliley Act)** — US law requiring financial institutions to protect customer data and provide privacy notices.
- **FISMA (Federal Information Security Management Act)** — US law requiring federal agencies to implement risk-based security programs aligned to NIST.
- **ISO/IEC 27001** — International certifiable standard for an Information Security Management System (ISMS).
- **ISO/IEC 27002** — Implementation guidance for ISO 27001 controls; not independently certifiable.
- **NIST Cybersecurity Framework (CSF)** — Voluntary framework with five functions (Identify, Protect, Detect, Respond, Recover) for managing cybersecurity risk.
- **NIST SP 800-53** — Detailed security and privacy control catalog for US federal information systems.
- **CIS Controls** — Prioritized set of cybersecurity best practices organized by implementation group (IG1–IG3).
- **CIS Benchmark** — Detailed secure configuration guide for specific technologies; Level 1 (basic) and Level 2 (hardened).
- **DISA STIG (Security Technical Implementation Guide)** — DoD configuration standards required for military and federal contractor systems.
- **NERC CIP** — Critical Infrastructure Protection standards for the North American electric grid.
- **FedRAMP** — US government authorization program for cloud service providers serving federal agencies.
- **HITRUST** — Healthcare-specific security and privacy framework aligned to HIPAA requirements.
- **Extraterritorial reach** — A regulation's authority extending beyond the issuing country's borders (e.g., GDPR applies globally when EU citizen data is involved).

---

## Examples / scenarios

**Scenario 1:** A US-based e-commerce company collects shipping addresses and purchase history from customers in Germany and France. The company's legal team asks whether EU privacy law applies.
- **Answer:** Yes — GDPR applies. Jurisdiction is based on where the *data subject* (customer) is located, not where the company is headquartered. The company must comply with GDPR, including consent, data deletion rights, and 72-hour breach notification.

**Scenario 2:** A healthcare provider is breached and patient records are exposed. The security team asks how long they have to notify affected patients under US law.
- **Answer:** HIPAA's Breach Notification Rule requires notification within **60 days** of discovery. If more than 500 individuals in a state are affected, the media must also be notified.

**Scenario 3:** A financial services company processes Visa and Mastercard payments for customers worldwide. An auditor asks which security standard governs their cardholder data environment.
- **Answer:** PCI DSS — enforced by the card brands (not the government). Failure to comply can result in fines from Visa/Mastercard and loss of card processing privileges, not criminal prosecution.

**Scenario 4:** A federal agency is implementing a new information system and must select a controls framework for FISMA compliance.
- **Answer:** NIST SP 800-53. FISMA requires federal agencies to implement security controls from NIST 800-53, documented in a System Security Plan (SSP).

**Scenario 5:** A security team is hardening new Linux servers using CIS Benchmarks. One control requires disabling a legacy service that a business-critical application depends on. The team decides not to apply that control.
- **Answer:** This is an acceptable deviation — provided it is **documented with a business justification**. Benchmarks do not require 100% compliance; compensating controls or documented exceptions are permitted.

**Scenario 6:** A company achieves ISO 27001 certification. A vendor then asks if the company also "holds ISO 27002 certification."
- **Answer:** ISO 27002 is not certifiable — it is implementation guidance for ISO 27001 controls. Only ISO 27001 can be certified. The vendor's question reflects a common misconception.

---

## Mini quiz

<details>
<summary><strong>Question 1:</strong> What is the key difference between a regulation and a standard in the context of security governance?</summary>

**Answer:** A regulation (e.g., GDPR, HIPAA) is *legally binding* — non-compliance results in government-imposed penalties. A standard (e.g., ISO 27001, NIST CSF) is *voluntary* — organizations choose to adopt it for business, insurance, or contractual reasons, but there is no legal mandate.
</details>

<details>
<summary><strong>Question 2:</strong> A US company has no offices in Europe but has customers in the EU. Does GDPR apply to them?</summary>

**Answer:** Yes. GDPR has extraterritorial reach — it applies to any organization anywhere in the world that processes personal data belonging to EU citizens. The company must comply with GDPR regardless of where it is headquartered.
</details>

<details>
<summary><strong>Question 3:</strong> What are the five functions of the NIST Cybersecurity Framework?</summary>

**Answer:** Identify, Protect, Detect, Respond, Recover. A helpful mnemonic: **I P D R R** ("I Please Don't Run Risks"). These functions represent a continuous cycle of cybersecurity risk management, not a linear process.
</details>

<details>
<summary><strong>Question 4:</strong> Why is PCI DSS commonly mistaken for a law, and why does the distinction matter?</summary>

**Answer:** PCI DSS is enforced contractually by card brands (Visa, Mastercard) — it is not enacted by any government. The distinction matters because penalties come from card brands (fines, loss of processing ability), not government prosecutors. An organization cannot be criminally prosecuted under PCI DSS alone.
</details>

<details>
<summary><strong>Question 5:</strong> What is the difference between ISO 27001 and ISO 27002?</summary>

**Answer:** ISO 27001 is the certifiable ISMS standard — organizations can achieve formal certification demonstrating they have implemented a compliant information security management system. ISO 27002 provides implementation guidance for the controls listed in 27001, but it cannot be independently certified.
</details>

### CompTIA-style practice questions

<details>
<summary><strong>Question 6:</strong> A company that processes credit card payments discovers that several of its servers are not compliant with the applicable data security standard. The security team is concerned about legal prosecution by federal authorities. Which BEST describes the nature of PCI DSS enforcement?<br>A. PCI DSS is enforced by federal law enforcement; violations can result in criminal prosecution<br>B. PCI DSS is enforced by card brands through fines and potential loss of card processing privileges<br>C. PCI DSS is a voluntary standard; there are no formal penalties for non-compliance<br>D. PCI DSS violations are prosecuted under GLBA by the FTC</summary>

**Correct Answer: B. PCI DSS is enforced by card brands through fines and potential loss of card processing privileges**

PCI DSS is a contractual requirement set by payment card brands (Visa, Mastercard, etc.), not a government law. Enforcement comes from the card brands — penalties include fines and the revocation of the merchant's ability to accept card payments.

- A: No government agency prosecutes PCI DSS non-compliance — it is not a law.
- C: While technically voluntary, merchants who accept cards are contractually required to comply; meaningful penalties do apply.
- D: GLBA applies to financial institutions and is enforced by the FTC — not PCI DSS.
</details>

<details>
<summary><strong>Question 7:</strong> A US healthcare organization suffers a ransomware attack that exposes protected health information for 800 patients. Under which regulation must the organization notify affected individuals, and within what timeframe?<br>A. GDPR; within 72 hours of discovery<br>B. HIPAA; within 60 days of discovery<br>C. SOX; within 30 days of discovery<br>D. GLBA; within 14 days of discovery</summary>

**Correct Answer: B. HIPAA; within 60 days of discovery**

HIPAA's Breach Notification Rule requires covered entities to notify affected individuals within 60 days of discovering a breach of unsecured PHI. GDPR's 72-hour rule applies to EU personal data, not US healthcare data.

- A: GDPR governs EU personal data, not US PHI; and its 72-hour window applies to the supervisory authority, not individuals.
- C: SOX governs financial reporting controls for publicly traded companies — not patient data.
- D: GLBA applies to financial institutions, not healthcare; 14 days is not a GLBA notification window.
</details>

<details>
<summary><strong>Question 8:</strong> An organization is deploying a new cloud environment and wants to adopt a high-level voluntary framework to guide its cybersecurity risk management strategy. Which framework is MOST appropriate?<br>A. NIST SP 800-53<br>B. DISA STIG<br>C. NIST Cybersecurity Framework (CSF)<br>D. FISMA</summary>

**Correct Answer: C. NIST Cybersecurity Framework (CSF)**

NIST CSF is a voluntary, high-level framework designed to help any organization — regardless of size or sector — manage cybersecurity risk using its five functions: Identify, Protect, Detect, Respond, Recover.

- A: NIST 800-53 provides detailed security controls for *federal* information systems — it is prescriptive and targeted at FISMA compliance, not a general-purpose strategic framework.
- B: DISA STIGs are configuration standards required for DoD and federal contractor systems — not a strategic risk management framework.
- D: FISMA is a US law requiring federal agencies to implement security programs — not applicable to private organizations.
</details>

<details>
<summary><strong>Question 9 (Multi-select):</strong> A global company is expanding into the European market and beginning to collect personal data from customers in Germany and France. Which TWO regulatory requirements MOST directly apply to their data collection activities? (Select TWO.)<br>A. HIPAA<br>B. GDPR<br>C. NERC CIP<br>D. SOX<br>E. GDPR's right to be forgotten and 72-hour breach notification requirement</summary>

**Correct Answers: B and E**

GDPR governs the collection and processing of personal data belonging to EU citizens and applies to any organization globally that handles such data. The right to be forgotten (erasure) and 72-hour breach notification to supervisory authorities are core GDPR requirements.

- A: HIPAA applies to US healthcare organizations handling Protected Health Information — not EU customer data.
- C: NERC CIP applies to the North American electric grid — not data collection activities.
- D: SOX applies to publicly traded companies' financial reporting — not customer data privacy.
</details>

---

## Related objectives

- [**5.2**]({{ '/secplus/objectives/5-2/' | relative_url }}) — Risk management processes operate within the governance structure established in this objective.
- [**5.3**]({{ '/secplus/objectives/5-3/' | relative_url }}) — Third-party risk assessment extends governance principles to vendors and suppliers.
- [**5.4**]({{ '/secplus/objectives/5-4/' | relative_url }}) — Security compliance is the operational application of the regulations and standards covered here.
- [**5.5**]({{ '/secplus/objectives/5-5/' | relative_url }}) — Audits and assessments verify compliance with the governance frameworks covered in this objective.
- [**4.1**]({{ '/secplus/objectives/4-1/' | relative_url }}) — Security policies and procedures are the documents that translate governance into operational controls.

---

## Navigation

**Domain 5.0: Security Program Management and Oversight**

| Objective | Title | Status |
|---|---|---|
| **5.1** | Summarize elements of effective security governance. (current) | done |
| [5.2]({{ '/secplus/objectives/5-2/' | relative_url }}) | Explain elements of the risk management process. | done |
| [5.3]({{ '/secplus/objectives/5-3/' | relative_url }}) | Explain the processes associated with third-party risk assessment and management. | done |
| [5.4]({{ '/secplus/objectives/5-4/' | relative_url }}) | Summarize elements of effective security compliance. | done |
| [5.5]({{ '/secplus/objectives/5-5/' | relative_url }}) | Explain types and purposes of audits and assessments. | done |
| [5.6]({{ '/secplus/objectives/5-6/' | relative_url }}) | Given a scenario, implement security awareness practices. | done |

[← Previous: Domain 4]({{ '/secplus/objectives/4-9/' | relative_url }}) | [Back to Dashboard]({{ '/secplus/' | relative_url }}) | [Next: Objective 5.2 →]({{ '/secplus/objectives/5-2/' | relative_url }})
