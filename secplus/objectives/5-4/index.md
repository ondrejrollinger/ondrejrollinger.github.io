---
layout: objective
title: "Security+ 5.4 — Summarize elements of effective security compliance."
objective_id: "5.4"
domain: "5.0 Security Program Management and Oversight"
status: "done"
tags:
  - secplus701
permalink: /secplus/objectives/5-4/
---

# Security+ 5.4 — Summarize elements of effective security compliance.

Status: <span class="status-badge done">done</span>

## Exam objective
Summarize elements of effective security compliance.

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

Compliance ensures organizations meet regulatory requirements and industry standards through a cycle of audits, attestation, evidence collection, continuous monitoring, and remediation. This objective covers audit types, attestation vs. acknowledgement, due diligence vs. due care, compliance frameworks, and how findings are managed.

---

### Types of audits

| Audit type | Conducted by | Purpose | Examples |
|---|---|---|---|
| **Internal** | Internal audit team | Self-assessment; identify gaps before external review | Annual controls review, quarterly access review |
| **External** | Independent third-party | Verify compliance; issue certification/attestation | ISO 27001 audit, SOC 2, PCI DSS QSA assessment |
| **Regulatory** | Government regulator | Verify compliance with law/regulation | HIPAA (HHS OCR), GDPR (EU DPA), SOX (PCAOB) |

> **Exam tip:** Internal audits find gaps early at lower cost; external audits are required for formal certification. Regulatory audits are government-initiated and can result in fines and sanctions.

---

### Attestation and acknowledgement

| Concept | Definition | Examples |
|---|---|---|
| **Attestation** | Formal declaration that something is true | SOC 2 report, ISO 27001 cert, manager access certification, FedRAMP authorization |
| **Acknowledgement** | Confirmation of receipt or understanding | Policy sign-off, training completion, breach notification receipt |

**Attestation types:**

| Type | Who attests | What they declare |
|---|---|---|
| **System / process** | External auditor or certification body | Controls are effective (SOC 2) / ISMS meets standard (ISO 27001) |
| **User** | Employee | "I have read and understand the Acceptable Use Policy" |
| **Access recertification** | Manager | "This user still requires this level of access" |

> **Exam tip:** Attestation = declaration of *truth or compliance*. Acknowledgement = confirmation of *receipt or understanding*. These are different — confusing them is a common trap.

**Access recertification process (example):**
```
1. System generates access report (who has access to what)
2. Manager reviews each entry — Is access still needed? Is level appropriate?
3. Manager attests with digital signature
4. IT revokes uncertified access
5. Compliance team retains attestation as audit evidence
```

---

### Compliance monitoring and reporting

**Automated monitoring tools:**

| Tool type | Example | Frequency |
|---|---|---|
| Configuration compliance | CIS-CAT (CIS benchmark scanner) | Daily |
| Log / event monitoring | SIEM (Splunk, Microsoft Sentinel) | Real-time |
| Vulnerability scanning | Nessus, Qualys | Weekly |

**Manual activities:**
- **Access reviews** — Manager certifies access is appropriate (quarterly for privileged, annually for standard)
- **Policy reviews** — Annual policy update and approval cycle
- **Vendor assessments** — Periodic review of third-party security posture

**Compliance metrics to know:**

| Metric | What it measures |
|---|---|
| Compliance score | % of controls currently implemented |
| Open findings | Number of outstanding audit findings |
| Mean time to remediate | Average time to close a finding |
| Repeat findings | Issues recurring across multiple audit cycles |
| Attestation completion rate | % of required attestations completed on time |

> **Exam tip:** Compliance monitoring is continuous, not a once-per-year activity. Real-time dashboards track control status; audit reports document point-in-time snapshots.

---

### Due diligence vs. due care

| Concept | Definition | Security example |
|---|---|---|
| **Due diligence** | Research and investigation before making a decision | Vendor risk assessment; reviewing audit reports before signing a contract |
| **Due care** | Reasonable steps taken to protect assets (acting on what you know) | Patching vulnerabilities promptly; training employees; deploying EDR |

> **Exam tip:** Due diligence = *knowing what to do*. Due care = *doing it*. Both are legally required — having only one is not sufficient. Failing to exercise either constitutes **negligence**.

**Legal implications:**

| Failure | Consequence |
|---|---|
| No due diligence (didn't assess risks) | Negligence — legal liability |
| No due care (knew risks, did nothing) | Negligence; breach of fiduciary duty |
| Both absent | Regulatory penalties (GDPR fines, HIPAA sanctions) |

---

### Audit evidence types

| Evidence type | Examples | Retention note |
|---|---|---|
| **Logs** | Access logs, change logs, authentication logs | PCI DSS = 1 year; HIPAA = 6 years |
| **Attestations** | Policy acknowledgements, access certifications, vendor questionnaires | Per compliance requirement |
| **Reports** | Vulnerability scans, pen test results, risk assessments, IR reports | Typically 1–3 years |
| **Policies and procedures** | Security policy, IRP, BCP, vendor management policy | Current + prior versions |
| **Configurations** | Hardening baselines, firewall rulesets, network diagrams, ACLs | At time of audit |

> **Exam tip:** Evidence must be collected, centralized, version-controlled, and access-restricted. The audit trail itself (who accessed evidence, when) is also evidence.

---

### Audit finding severity and remediation timelines

| Severity | Definition | Remediation timeline |
|---|---|---|
| **Critical** | Severe control failure; immediate risk | Days (immediate) |
| **High** | Significant control weakness | Within 30 days |
| **Medium** | Control gap; manageable risk | Within 90 days |
| **Low** | Minor improvement opportunity | Within 6 months |
| **Observation / Advisory** | Recommendation; not required | At organization's discretion |

**Remediation process:**
```
1. Acknowledge finding (accept or dispute with evidence)
2. Root cause analysis
3. Develop remediation plan (actions, timeline, owner)
4. Implement remediation and collect evidence
5. Validate (retest; auditor may verify)
6. Close finding and prevent recurrence (update procedures, train staff)
```

> **Exam tip:** Finding severity drives timeline — not all findings require immediate action. Regulators and auditors expect a documented remediation plan even for low-severity findings.

---

### Compliance frameworks: key audit processes

| Framework | Key audit mechanism | Cadence | Attestation document |
|---|---|---|---|
| **PCI DSS** | Report on Compliance (ROC) by QSA (large); SAQ (small merchants) | Annual ROC + quarterly ASV scans | Attestation of Compliance (AOC) |
| **SOC 2** | Type I (point-in-time) or Type II (6–12 month period) | Annual | SOC 2 report (shared under NDA) |
| **ISO 27001** | Stage 1 (docs) + Stage 2 (on-site) by certification body | 3-year cert + annual surveillance | ISO 27001 certificate |
| **HIPAA** | Audit by HHS Office for Civil Rights | As scheduled or triggered | N/A (regulatory, not certification) |

> **Exam tip:** SOC 2 Type I tests *design* of controls (snapshot); SOC 2 Type II tests *operating effectiveness* over a period. ISO 27001 certificates are valid for 3 years with annual surveillance audits in between.

---

### Key distinctions to know for the exam

| Comparison | Distinction |
|---|---|
| **Internal vs. external audit** | Internal = self-assessment by the organization; external = independent third-party verification |
| **Attestation vs. acknowledgement** | Attestation = declaration of truth/compliance; acknowledgement = confirmation of receipt/understanding |
| **Due diligence vs. due care** | Due diligence = research and assessment; due care = implementation and action |
| **SOC 2 Type I vs. Type II** | Type I = controls design at a point in time; Type II = controls operating effectiveness over 6–12 months |
| **Regulatory audit vs. external audit** | Regulatory = government-initiated, can impose fines; external = voluntary/contractual, results in certification |
| **Compensating control vs. remediation** | Compensating control = risk reduction when full fix isn't possible; remediation = actually fixing the finding |

---

### Common exam traps

**Trap:** Assuming an internal audit satisfies external compliance requirements.
Reality: External audits by independent third parties are required for formal certifications (ISO 27001, SOC 2, PCI ROC).

**Trap:** Treating attestation and acknowledgement as the same thing.
Reality: Attestation is a formal declaration of truth or compliance. Acknowledgement is simply confirming receipt or understanding of something.

**Trap:** Believing due diligence alone is legally sufficient.
Reality: Organizations must exercise both due diligence (knowing what to do) and due care (doing it). Either alone is insufficient — the absence of either constitutes negligence.

**Trap:** Thinking all audit findings must be remediated immediately.
Reality: Severity drives timeline. Only critical findings require immediate action; lower findings have defined remediation windows (30, 90, 180 days).

**Trap:** Treating compliance as a one-time project.
Reality: Compliance is continuous — automated monitoring, periodic access reviews, annual audits, and ongoing evidence collection are all required.

**Trap:** Confusing a SOC 2 Type I report with full compliance assurance.
Reality: Type I only evaluates control design at a point in time. Type II — which covers a full operating period — provides stronger assurance and is what most enterprise customers require.

---

### Exam tips

1. "Self-assessment to find gaps before an external audit" → **internal audit**
2. "Independent third party issues a certificate" → **external audit**
3. "Government audits for regulatory compliance, can impose fines" → **regulatory audit**
4. "Formal declaration that controls are effective" → **attestation**
5. "Employee confirms reading the security policy" → **acknowledgement**
6. "Research before making a security decision" → **due diligence**
7. "Taking reasonable steps to protect assets" → **due care**
8. "Knew the risk but did nothing" → **negligence** (failed due care)
9. "SOC 2 over a 6–12 month observation period" → **Type II**
10. "ISO 27001 certificate expires after 3 years" → annual surveillance audits keep it current
11. "PCI DSS requires quarterly" → **ASV vulnerability scans** (plus annual ROC/SAQ)
12. "Critical audit finding" → remediate **immediately**; low → **6 months**

---

## Key terms

- **Audit** — Formal examination of an organization's controls, policies, and processes to assess compliance with a standard or regulation.
- **Internal audit** — Self-assessment conducted by the organization's own audit team to identify gaps before external review.
- **External audit** — Independent third-party examination resulting in formal certification or attestation.
- **Regulatory audit** — Government-initiated audit to verify compliance with law; non-compliance can result in fines or sanctions.
- **Attestation** — A formal declaration that something is true or that controls are effective; e.g., SOC 2 report, ISO 27001 certificate.
- **Acknowledgement** — Confirmation that something has been received or understood; e.g., signing an acceptable use policy.
- **Access recertification** — Periodic process where managers formally attest that users' access rights remain appropriate.
- **Due diligence** — Research and risk assessment performed before making a decision (knowing what to do).
- **Due care** — Reasonable steps taken to implement controls and protect assets (doing what you know you should).
- **Negligence** — Failure to exercise due diligence and/or due care, resulting in legal liability.
- **Report on Compliance (ROC)** — PCI DSS audit document produced by a Qualified Security Assessor (QSA) for large merchants/service providers.
- **SOC 2 Type I** — Audit report evaluating the *design* of controls at a single point in time.
- **SOC 2 Type II** — Audit report evaluating the *operating effectiveness* of controls over a 6–12 month period.
- **Compensating control** — An alternative control that reduces risk when the primary control cannot be implemented.
- **Remediation** — The process of fixing an identified finding or control gap.
- **Compliance monitoring** — Continuous automated and manual activities to ensure controls remain effective over time.

---

## Examples / scenarios

**Scenario 1:** A cloud service provider undergoes a 9-month observation period during which an external auditor evaluates whether their security controls actually work in practice. At the end, a report is issued to enterprise customers.
- **Answer:** SOC 2 Type II audit. The observation period (operating effectiveness over time) distinguishes this from Type I.

**Scenario 2:** Before signing a contract with a new payroll vendor, a company reviews the vendor's SOC 2 report, conducts a security questionnaire, and assesses the vendor's data handling practices.
- **Answer:** Due diligence. The company is researching and assessing risk before making a decision.

**Scenario 3:** A CISO knows from the annual risk assessment that unpatched servers are a critical risk. Six months later, the servers are still unpatched and ransomware hits. Legal counsel warns the CISO the organization may face liability.
- **Answer:** Failure of due care. The risk was known (due diligence done) but no corrective action was taken — this constitutes negligence.

**Scenario 4:** An auditor finds that admin accounts do not require MFA. The finding is rated High. The security team documents a 30-day remediation plan, enables Conditional Access, and collects screenshots as evidence. The auditor re-tests and closes the finding.
- **Answer:** Standard audit finding remediation process. High severity = 30-day timeline; evidence of remediation closes the finding.

**Scenario 5:** During an annual review, each manager receives a report of their team members' system access and must digitally sign a statement confirming that all access shown is still appropriate and necessary.
- **Answer:** Access recertification / attestation. The manager's digital signature is a formal attestation of compliance with the principle of least privilege.

**Scenario 6:** An employee receives an email with a link to the new Acceptable Use Policy. After reading it, they click "I confirm I have read and understood this policy."
- **Answer:** Acknowledgement — not attestation. The employee is confirming receipt and understanding, not declaring that controls are effective.

---

## Mini quiz

<details>
<summary><strong>Question 1:</strong> What is the difference between attestation and acknowledgement?</summary>

**Answer:** Attestation is a formal declaration that something is *true or compliant* — for example, a manager declaring that a user's access is appropriate, or an auditor declaring that controls are effective. Acknowledgement is simply confirming *receipt or understanding* — for example, an employee confirming they read the security policy. The distinction matters on the exam: SOC 2 reports and access certifications involve attestation; policy sign-offs are acknowledgements.
</details>

<details>
<summary><strong>Question 2:</strong> How does due diligence differ from due care, and why must an organization exercise both?</summary>

**Answer:** Due diligence is the research and assessment phase — understanding risks, evaluating controls, reviewing vendor security posture. Due care is the action phase — implementing controls, patching vulnerabilities, training staff. Both are legally required. An organization that conducts due diligence (identifies a risk) but takes no action (fails due care) is still negligent. Knowing the risk is not sufficient; reasonable steps must be taken to address it.
</details>

<details>
<summary><strong>Question 3:</strong> What distinguishes a SOC 2 Type I report from a SOC 2 Type II report?</summary>

**Answer:** SOC 2 Type I evaluates the *design* of controls at a single point in time — it answers "are the controls designed correctly?" Type II evaluates *operating effectiveness* over a period of 6–12 months — it answers "did the controls actually work consistently over time?" Enterprise customers typically require Type II because it provides stronger assurance.
</details>

<details>
<summary><strong>Question 4:</strong> A penetration test finding identifies that admin accounts lack MFA. What determines how quickly this must be remediated?</summary>

**Answer:** Finding severity. Admin accounts without MFA would typically be rated **High** (significant control weakness), requiring remediation within 30 days. Only Critical findings require immediate (within days) remediation. The organization must document a remediation plan, implement the fix, collect evidence, and have the finding validated and closed.
</details>

<details>
<summary><strong>Question 5:</strong> Why is compliance considered a continuous process rather than an annual event?</summary>

**Answer:** Because controls can fail, configurations can drift, access can accumulate, and new vulnerabilities emerge at any time. Continuous compliance monitoring — automated configuration scans, real-time SIEM alerting, periodic access reviews — maintains control effectiveness between formal audits. An annual audit is a snapshot; continuous monitoring ensures the organization is compliant every day, not just on audit day.
</details>

### CompTIA-style practice questions

<details>
<summary><strong>Question 6:</strong> A financial services firm undergoes an annual review conducted by an independent firm hired by their payment card acquirer. The firm's QSA produces a formal document confirming whether the company meets all cardholder data protection requirements. Which document does this process produce?<br>A. SOC 2 Type II report<br>B. Attestation of Compliance (AOC)<br>C. ISO 27001 certificate<br>D. System Security Plan (SSP)</summary>

**Correct Answer: B. Attestation of Compliance (AOC)**

The scenario describes a PCI DSS audit by a Qualified Security Assessor (QSA). The output is a Report on Compliance (ROC) and an accompanying **Attestation of Compliance (AOC)** — the document submitted to the acquiring bank confirming PCI DSS compliance.

- A: SOC 2 Type II is a trust services audit; it is not initiated by a payment card acquirer.
- C: ISO 27001 is an ISMS standard; its output is a certificate, not a compliance attestation for payment card data.
- D: An SSP is associated with FedRAMP/NIST frameworks for federal cloud systems.
</details>

<details>
<summary><strong>Question 7:</strong> A security manager performed a detailed risk assessment identifying that outdated TLS configurations on public-facing servers posed a high risk. Six months later, no remediation has been implemented and a breach occurs exploiting those configurations. Which concept BEST describes the organization's legal exposure?<br>A. Violation of due diligence<br>B. Failure of due care<br>C. Lack of attestation<br>D. Insufficient audit evidence</summary>

**Correct Answer: B. Failure of due care**

The organization exercised due diligence (the risk assessment identified the vulnerability) but failed due care — it did not take reasonable steps to remediate a known, documented risk. This constitutes negligence and creates legal liability.

- A: Due diligence was actually performed; the risk was identified. The failure came in the action phase.
- C: Attestation is about formal declarations of compliance, not the failure to act on known risks.
- D: Audit evidence is a documentation concept; the issue here is inaction on a known risk.
</details>

<details>
<summary><strong>Question 8:</strong> A manager receives a quarterly report listing all access rights held by members of their team. The manager reviews each entry, removes three accounts that belong to employees who transferred to another department, and digitally signs the report with the statement: "I confirm the access shown is appropriate and necessary for all listed personnel." Which process does this BEST describe?<br>A. Acknowledgement<br>B. Access recertification / attestation<br>C. Security audit<br>D. Compliance monitoring</summary>

**Correct Answer: B. Access recertification / attestation**

The manager is formally declaring (attesting) that the access rights shown are appropriate — this is access recertification. The digital signature constitutes the attestation. The output serves as audit evidence for compliance with least privilege requirements.

- A: Acknowledgement would be confirming receipt of a document, not making a formal declaration about the appropriateness of access rights.
- C: A security audit is a broader examination of controls by an auditor, not a manager's periodic review of their team's access.
- D: Compliance monitoring refers to automated and manual tools tracking control status; access recertification is one input to it, not the monitoring itself.
</details>

<details>
<summary><strong>Question 9 (Multi-select):</strong> An organization is preparing for its first ISO 27001 certification audit. Which TWO activities are part of the formal certification process? (Select TWO.)<br>A. Manager attestation that all user access is appropriate<br>B. Stage 1 audit reviewing documentation and the ISMS design<br>C. Quarterly vulnerability scans by an Approved Scanning Vendor (ASV)<br>D. Stage 2 on-site audit by an external certification body<br>E. Submission of an Attestation of Compliance to the acquiring bank</summary>

**Correct Answers: B and D**

ISO 27001 certification requires a two-stage external audit: Stage 1 (documentation and design review) followed by Stage 2 (on-site assessment of implementation). A 3-year certificate is issued upon success, with annual surveillance audits.

- A: Access recertification is a control activity, not a formal stage in ISO 27001 certification.
- C: ASV scans are a PCI DSS requirement, not part of ISO 27001.
- E: AOC submission is a PCI DSS process; ISO 27001 results in a certificate, not an AOC.
</details>

---

## Related objectives

- [**5.2**]({{ '/secplus/objectives/5-2/' | relative_url }}) — Risk management provides the foundation for compliance: identifying which risks require control and driving the due diligence / due care cycle.
- [**5.3**]({{ '/secplus/objectives/5-3/' | relative_url }}) — Third-party risk management directly applies compliance monitoring to vendors, MSPs, and supply chain partners.
- [**5.5**]({{ '/secplus/objectives/5-5/' | relative_url }}) — Audits and assessments elaborates on specific audit types (vulnerability assessments, penetration tests) that generate compliance evidence.
- [**4.1**]({{ '/secplus/objectives/4-1/' | relative_url }}) — Security monitoring tools (SIEM, log management) are the operational mechanisms that support continuous compliance monitoring.

---

## Navigation

**Domain 5.0: Security Program Management and Oversight**

| Objective | Title | Status |
|---|---|---|
| [5.1]({{ '/secplus/objectives/5-1/' | relative_url }}) | Summarize elements of effective security governance. | done |
| [5.2]({{ '/secplus/objectives/5-2/' | relative_url }}) | Explain elements of the risk management process. | done |
| [5.3]({{ '/secplus/objectives/5-3/' | relative_url }}) | Explain the processes associated with third-party risk assessment and management. | done |
| **5.4** | Summarize elements of effective security compliance. (current) | done |
| [5.5]({{ '/secplus/objectives/5-5/' | relative_url }}) | Explain types and purposes of audits and assessments. | done |
| [5.6]({{ '/secplus/objectives/5-6/' | relative_url }}) | Given a scenario, implement security awareness practices. | done |

[← Previous: Objective 5.3]({{ '/secplus/objectives/5-3/' | relative_url }}) | [Back to Dashboard]({{ '/secplus/' | relative_url }}) | [Next: Objective 5.5 →]({{ '/secplus/objectives/5-5/' | relative_url }})
