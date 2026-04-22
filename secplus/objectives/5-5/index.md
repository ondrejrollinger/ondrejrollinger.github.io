---
layout: objective
title: "Security+ 5.5 — Explain types and purposes of audits and assessments."
objective_id: "5.5"
domain: "5.0 Security Program Management and Oversight"
status: "done"
tags:
  - secplus701
permalink: /secplus/objectives/5-5/
---

# Security+ 5.5 — Explain types and purposes of audits and assessments.

Status: <span class="status-badge done">done</span>

## Exam objective
Explain types and purposes of audits and assessments.

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

Audits and assessments are systematic methods for evaluating the security posture of an organization. This objective covers the full spectrum — from internal compliance audits and third-party attestation, to technical assessments like penetration tests and vulnerability scans. The exam emphasizes knowing *which* assessment type fits a given scenario and what each reveals.

---

### Attestation

Attestation is the formal process of confirming or vouching for the accuracy of security-related information.

| Type | Description | Exam keyword |
|---|---|---|
| **Software Bill of Materials (SBOM)** | A formal inventory of all components, libraries, and dependencies in a software product | Supply chain transparency; identifies vulnerable third-party components |
| **Attestation of findings** | A formal statement (signed by an auditor or responsible party) confirming the accuracy of an audit's results | Regulatory submissions, third-party audit reports |

> **Exam tip:** An SBOM is used to understand *what is in* software — critical for supply chain risk management. If a zero-day hits an open-source library, the SBOM tells you immediately which of your products are affected.

---

### Internal audits

Internal audits are conducted by personnel within the organization — typically an internal audit team or IT/security staff.

| Type | Description |
|---|---|
| **Compliance audit** | Verifies the organization is meeting regulatory or policy requirements (e.g., PCI DSS, HIPAA, internal policy) |
| **Audit committee** | A governance body (often board-level) that oversees audit activities, reviews findings, and ensures accountability |
| **Self-assessment** | Teams evaluate their own controls against a standard or framework (e.g., NIST CSF self-assessment) |

> **Exam tip:** Internal audits are less independent than external audits — they may be biased toward favorable results. Regulators often require external audits for this reason.

---

### External audits

External audits are performed by independent parties outside the organization, providing greater objectivity.

| Type | Description | Example |
|---|---|---|
| **Regulatory audit** | Required by law or regulation; failure results in fines or penalties | HIPAA audit by HHS, PCI DSS QSA assessment |
| **Examination** | Formal review by a regulatory authority or examiner to verify compliance | OCC bank examination, FedRAMP assessment |
| **Assessment** | Broader evaluation of security posture, not necessarily tied to a specific regulation | SOC 2 Type II readiness assessment |
| **Independent third-party audit** | Audit conducted by a qualified, neutral external firm with no affiliation to the organization | ISO 27001 certification audit |

> **Exam tip:** A **SOC 2 Type II** report is a common external audit output — it covers security controls over a period of time (usually 6–12 months), not just a point-in-time snapshot.

---

### Penetration testing

Penetration testing (pen testing) is an authorized, simulated attack against a system to identify exploitable vulnerabilities before real attackers do.

#### Pen test types by scope

| Type | Description |
|---|---|
| **Physical** | Tests physical security controls — locks, badge readers, tailgating, dumpster diving |
| **Offensive** | Red team–style attack simulation; mimics real threat actors to test detection and response |
| **Defensive** | Blue team evaluation — assesses how well the organization detects and responds to simulated attacks |
| **Integrated** | Red and blue team work together (purple team); real-time knowledge sharing to improve defenses |

#### Pen test types by knowledge level

| Type | Also called | Description |
|---|---|---|
| **Known environment** | White box | Tester has full knowledge — network diagrams, source code, credentials; most thorough coverage |
| **Partially known environment** | Gray box | Tester has some information (e.g., IP ranges, user-level credentials); simulates insider threat |
| **Unknown environment** | Black box | Tester has no prior knowledge; simulates an external attacker; most realistic but may miss coverage |

#### Reconnaissance

Reconnaissance is the first phase of a pen test — gathering information about the target before active exploitation.

| Type | Description | Example techniques |
|---|---|---|
| **Passive reconnaissance** | Gathering information without directly interacting with the target | OSINT, WHOIS lookups, Google dorking, LinkedIn scraping |
| **Active reconnaissance** | Directly probing the target system — detectable by IDS/IPS | Port scanning (Nmap), banner grabbing, ping sweeps |

> **Exam tip:** Passive recon leaves **no footprint** on the target — it uses publicly available sources. Active recon *touches* the target and can trigger alerts. The question "Which method would not be detected by the target?" → **passive reconnaissance**.

---

### Vulnerability scans

A vulnerability scan is an automated, non-exploitative assessment that identifies known weaknesses in systems, applications, and configurations.

| Characteristic | Vulnerability Scan | Penetration Test |
|---|---|---|
| **Method** | Automated tool (Nessus, Qualys, OpenVAS) | Manual + automated; human-driven |
| **Exploitation** | No — identifies weaknesses only | Yes — actively exploits vulnerabilities |
| **Depth** | Broad coverage, lower depth | Narrow focus, higher depth |
| **Frequency** | Continuous or scheduled (weekly/monthly) | Periodic (annually or after major changes) |
| **Output** | List of CVEs and severity ratings | Narrative report with attack chains and business impact |

> **Exam tip:** The key distinction the exam tests — a vulnerability scan **finds** weaknesses; a pen test **exploits** them to prove impact.

---

### Bug bounty programs

A bug bounty program is a formalized program that rewards external researchers for responsibly reporting security vulnerabilities.

| Characteristic | Description |
|---|---|
| **Scope** | Organization defines what systems are in/out of scope |
| **Reward** | Cash payments, hall of fame recognition, or both |
| **Purpose** | Crowdsource security testing; find vulnerabilities before attackers do |
| **Participants** | Independent security researchers (ethical hackers) |
| **Examples** | HackerOne, Bugcrowd platforms; Google, Microsoft, Apple programs |

> **Exam tip:** Bug bounty programs leverage the broader security community as an extension of internal testing — cost-effective and scalable, but require a mature vulnerability management process to handle incoming reports.

---

### Responsible disclosure programs

Responsible disclosure (also called coordinated disclosure) defines the process by which researchers report vulnerabilities to vendors *before* public disclosure.

| Concept | Description |
|---|---|
| **Responsible disclosure** | Researcher reports vulnerability to vendor privately; vendor gets time to patch before public announcement |
| **Coordinated disclosure** | Structured timeline agreed upon between researcher and vendor (e.g., 90-day disclosure window) |
| **Full disclosure** | Researcher publishes vulnerability details immediately, with or without vendor patch — controversial |
| **Disclosure window** | Typical window is 90 days (Google Project Zero standard); vendor must patch within this period |

> **Exam tip:** Responsible disclosure protects users by giving vendors time to patch. Full disclosure pressures vendors but may expose users to risk before a patch is available.

---

### Key distinctions

| Comparison | Distinction |
|---|---|
| **Internal audit vs. external audit** | Internal = conducted by organization's own staff, less independent; external = independent third party, higher objectivity |
| **Compliance audit vs. self-assessment** | Compliance audit is formal and often required; self-assessment is voluntary and internally driven |
| **Vulnerability scan vs. penetration test** | Scan = automated, finds vulnerabilities, no exploitation; pen test = manual, actively exploits, proves business impact |
| **Known vs. unknown environment** | Known (white box) = tester has full info, most thorough; unknown (black box) = no prior info, most realistic |
| **Passive vs. active reconnaissance** | Passive = no target interaction, leaves no trace; active = directly probes target, detectable |
| **Bug bounty vs. responsible disclosure** | Bug bounty = financial reward for finding bugs; responsible disclosure = structured process for *reporting* them to the vendor |
| **Attestation vs. audit** | Attestation = formal sign-off that findings are accurate; audit = the systematic evaluation process itself |

---

### Common exam traps

**Trap: Thinking a vulnerability scan and a penetration test are the same thing.**
Reality: A vulnerability scan is automated and non-exploitative — it identifies what might be exploitable. A pen test is manual, actively exploits confirmed vulnerabilities, and demonstrates real business impact.

**Trap: Confusing black box with "bad" and white box with "better."**
Reality: Neither is universally better. Black box is more realistic (simulates an outside attacker); white box is more thorough (maximizes coverage). The right choice depends on the testing goal.

**Trap: Assuming active reconnaissance is always part of a pen test.**
Reality: In some engagements, only passive recon is authorized. Active recon is explicitly in-scope when the rules of engagement permit it.

**Trap: Believing responsible disclosure means the vendor controls the timeline forever.**
Reality: Coordinated disclosure programs (like Google's 90-day window) give vendors a defined period to patch — after which researchers may publish regardless of whether the patch is ready.

**Trap: Thinking internal audits are unreliable.**
Reality: Internal audits have real value for continuous compliance monitoring. They are less independent, not less valid. Regulators typically require *both* internal and external audit activity.

---

### Exam tips

1. **Attestation of findings** = formal signed confirmation that audit results are accurate
2. **SBOM** = inventory of all software components; key for supply chain risk
3. **Internal audits** = less independent; include compliance audits, self-assessments, audit committee oversight
4. **External audits** = independent; regulatory, examinations, third-party assessments
5. **Pen test phases:** Recon → Scan → Exploit → Report
6. **White box** = known environment (full info); **gray box** = partially known; **black box** = unknown (most realistic)
7. **Passive recon** = no target contact, undetectable; **active recon** = touches target, detectable
8. **Vulnerability scan** = automated, no exploitation; **pen test** = manual, actively exploits
9. **Bug bounty** = pay researchers to find bugs; **responsible disclosure** = structured process to report them
10. **90-day disclosure window** = Google Project Zero coordinated disclosure standard

---

## Key terms

- **Attestation** — Formal confirmation that security findings or system states are accurate; typically signed by an auditor or responsible party.
- **SBOM (Software Bill of Materials)** — A complete inventory of all components, libraries, and dependencies in a software product.
- **Internal audit** — An audit conducted by personnel within the organization to assess compliance or control effectiveness.
- **External audit** — An audit performed by an independent third party, providing higher objectivity than internal audits.
- **Self-assessment** — An internal, voluntary evaluation of controls measured against a standard or framework.
- **Penetration test** — An authorized simulated attack against a system to identify and exploit vulnerabilities before real attackers do.
- **Known environment (white box)** — Pen test where the tester has full knowledge of the target environment.
- **Partially known environment (gray box)** — Pen test where the tester has limited prior knowledge (e.g., user credentials, IP ranges).
- **Unknown environment (black box)** — Pen test where the tester has no prior knowledge; simulates an external attacker.
- **Passive reconnaissance** — Gathering target information through publicly available sources without directly interacting with the target.
- **Active reconnaissance** — Directly probing a target system; detectable by security monitoring.
- **Vulnerability scan** — Automated, non-exploitative tool that identifies known weaknesses based on CVEs and configuration checks.
- **Bug bounty program** — A formal program offering rewards to external researchers for responsibly reporting security vulnerabilities.
- **Responsible disclosure** — The practice of reporting vulnerabilities to the vendor privately before public disclosure, giving time to patch.
- **Coordinated disclosure** — A structured responsible disclosure process with an agreed timeline (typically 90 days) before public release.
- **Red team** — Offensive security team simulating real-world attacker techniques.
- **Blue team** — Defensive security team focused on detection and response.
- **Purple team** — Integrated exercise where red and blue teams collaborate in real time to improve defenses.

---

## Examples / scenarios

**Scenario 1:** A CISO wants to know whether a recently deployed web application has any known CVEs in its open-source dependencies before it goes live.
- **Answer:** Request an **SBOM** from the development team. The SBOM lists all third-party libraries and their versions, which can be cross-referenced against vulnerability databases.

**Scenario 2:** A financial services firm must demonstrate to regulators that its controls meet SOX requirements. An internal team reviews its own controls and documents the results.
- **Answer:** This is an **internal compliance audit** (or self-assessment). Regulators may also require an independent **external audit** to supplement this.

**Scenario 3:** A security consultant is hired to test an organization's defenses but is given no information about the target systems beforehand. The consultant must find and exploit weaknesses the same way a real attacker would.
- **Answer:** **Unknown environment (black box) penetration test**. Simulates a real external threat actor with no insider knowledge.

**Scenario 4:** A pen tester uses Shodan, WHOIS, and LinkedIn to build a profile of a target company's exposed services and key personnel — without scanning or touching the target systems.
- **Answer:** **Passive reconnaissance**. Uses publicly available sources only; leaves no trace on the target.

**Scenario 5:** A security researcher discovers a critical SQL injection vulnerability in a popular e-commerce platform. They notify the vendor privately and agree to wait 90 days before publishing details.
- **Answer:** **Coordinated (responsible) disclosure**. The researcher gives the vendor time to patch before the vulnerability becomes public knowledge.

---

## Mini quiz

<details>
<summary><strong>Question 1:</strong> What is the key difference between a vulnerability scan and a penetration test?</summary>

**Answer:** A vulnerability scan is automated and non-exploitative — it identifies potential weaknesses and maps them to CVEs. A penetration test is manual and actively exploits confirmed vulnerabilities to demonstrate real business impact. Scans are broad and frequent; pen tests are deep and periodic.
</details>

<details>
<summary><strong>Question 2:</strong> What does "black box" mean in the context of penetration testing?</summary>

**Answer:** Black box (unknown environment) means the tester has no prior knowledge of the target — no network diagrams, no credentials, no architecture details. It simulates a real external attacker and is the most realistic test scenario.
</details>

<details>
<summary><strong>Question 3:</strong> How does passive reconnaissance differ from active reconnaissance?</summary>

**Answer:** Passive recon gathers information without directly interacting with the target — using OSINT, WHOIS, public records, and social media. It leaves no trace. Active recon directly probes the target (port scans, banner grabbing) and can be detected by IDS/IPS.
</details>

<details>
<summary><strong>Question 4:</strong> What is a Software Bill of Materials (SBOM) and why is it important?</summary>

**Answer:** An SBOM is a formal inventory of all components, libraries, and dependencies in a software product. It's important for supply chain risk management — when a vulnerability is discovered in a common library (e.g., Log4Shell), an SBOM tells you immediately which of your products are affected.
</details>

<details>
<summary><strong>Question 5:</strong> What distinguishes a bug bounty program from a responsible disclosure program?</summary>

**Answer:** A bug bounty program offers financial rewards (or other incentives) to external researchers for finding and reporting vulnerabilities. Responsible disclosure is the process by which those (or any) researchers report vulnerabilities to the vendor privately before going public — it may or may not involve a reward.
</details>

### CompTIA-style practice questions

<details>
<summary><strong>Question 6:</strong> A security team wants to simulate a real-world attacker with no prior knowledge of the organization's systems. Which type of penetration test BEST fits this requirement?<br>A. White box<br>B. Gray box<br>C. Black box<br>D. Integrated</summary>

**Correct Answer: C. Black box**

A black box (unknown environment) test gives the tester no advance information, simulating the perspective of an external attacker. This is the most realistic test scenario.

- A: White box (known environment) provides full information — most thorough, least realistic.
- B: Gray box provides partial information — simulates an insider or a compromised credential scenario.
- D: Integrated (purple team) involves red and blue teams working together in real time — not an adversarial simulation.
</details>

<details>
<summary><strong>Question 7:</strong> A security analyst uses Nmap to perform a port scan against a target during the reconnaissance phase of a penetration test. Which type of reconnaissance does this represent?<br>A. Passive reconnaissance<br>B. Active reconnaissance<br>C. OSINT gathering<br>D. Social engineering</summary>

**Correct Answer: B. Active reconnaissance**

Nmap directly probes target systems by sending packets — this is active reconnaissance. It interacts with the target and can be detected by IDS/IPS.

- A: Passive recon uses publicly available sources and does not touch the target.
- C: OSINT (Open Source Intelligence) is a passive technique using public data sources.
- D: Social engineering targets people, not systems.
</details>

<details>
<summary><strong>Question 8 (Multi-select):</strong> An organization wants to assess its security posture using both internal and external methods. Which TWO activities represent an external assessment? (Select TWO.)<br>A. An internal audit team reviews firewall rule compliance against policy<br>B. A QSA (Qualified Security Assessor) evaluates the organization for PCI DSS certification<br>C. The security team conducts a self-assessment against the NIST CSF<br>D. An independent pen testing firm performs a black box test of production systems<br>E. The CISO reviews access control logs for anomalies</summary>

**Correct Answers: B and D**

External assessments are conducted by independent parties outside the organization.

- B: A QSA is an independent, certified external assessor — required for PCI DSS compliance.
- D: An independent pen testing firm is an external party conducting a formal assessment.
- A: Internal audit team = internal assessment.
- C: Self-assessment = internal activity by the organization's own staff.
- E: Log review by the CISO = internal monitoring activity.
</details>

---

## Related objectives

- [**5.1**]({{ '/secplus/objectives/5-1/' | relative_url }}) — Security governance establishes the policies and frameworks that audits measure compliance against.
- [**5.2**]({{ '/secplus/objectives/5-2/' | relative_url }}) — Risk management informs which systems and assets are prioritized for assessment.
- [**5.3**]({{ '/secplus/objectives/5-3/' | relative_url }}) — Third-party risk assessment is a specific application of external audit and attestation.
- [**4.3**]({{ '/secplus/objectives/4-3/' | relative_url }}) — Vulnerability management operationalizes the vulnerability scanning activity covered here.
- [**2.3**]({{ '/secplus/objectives/2-3/' | relative_url }}) — Vulnerability types are what assessments and scans are designed to find.

---

## Navigation

**Domain 5.0: Security Program Management and Oversight**

| Objective | Title | Status |
|---|---|---|
| [5.1]({{ '/secplus/objectives/5-1/' | relative_url }}) | Summarize elements of effective security governance. | done |
| [5.2]({{ '/secplus/objectives/5-2/' | relative_url }}) | Explain elements of the risk management process. | done |
| [5.3]({{ '/secplus/objectives/5-3/' | relative_url }}) | Explain the processes associated with third-party risk assessment and management. | done |
| [5.4]({{ '/secplus/objectives/5-4/' | relative_url }}) | Summarize elements of effective security compliance. | done |
| **5.5** | Explain types and purposes of audits and assessments. (current) | done |
| [5.6]({{ '/secplus/objectives/5-6/' | relative_url }}) | Given a scenario, implement security awareness practices. | done |

[← Previous: Objective 5.4]({{ '/secplus/objectives/5-4/' | relative_url }}) | [Back to Dashboard]({{ '/secplus/' | relative_url }}) | [Next: Objective 5.6 →]({{ '/secplus/objectives/5-6/' | relative_url }})
