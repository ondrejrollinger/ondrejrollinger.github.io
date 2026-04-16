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

Compliance and audit ensure organizations meet regulatory requirements and industry standards. This includes internal/external audits, attestation, evidence collection, and compliance reporting.

---

## Types of Audits

**Internal audit:**
- **Conducted by:** Internal audit team (within organization)
- **Purpose:** Self-assessment, identify gaps before external audit
- **Frequency:** Quarterly or annually
- **Scope:** Can be comprehensive or focused
- **Reporting:** Internal (management, board)
- **Advantage:** Identify issues early, lower cost

**External audit:**
- **Conducted by:** Independent third-party auditor
- **Purpose:** Verify compliance for certification/attestation
- **Frequency:** Annual (typically)
- **Scope:** Defined by standard/regulation
- **Reporting:** External (regulators, customers, public)
- **Examples:** ISO 27001 audit, PCI DSS assessment, SOC 2 audit

**Regulatory audit:**
- **Conducted by:** Government regulator
- **Purpose:** Verify regulatory compliance
- **Trigger:** Scheduled, complaint-driven, or incident-driven
- **Examples:**
  - HIPAA audit by HHS Office for Civil Rights
  - GDPR audit by EU Data Protection Authority
  - SOX audit by PCAOB (Public Company Accounting Oversight Board)
- **Consequences:** Fines, sanctions if non-compliant

---

## Attestation and Acknowledgement

**Attestation:**

**Definition:** Formal declaration that something is true

**Types:**

**System/process attestation:**
- **SOC 2 report:** Auditor attests controls are effective
- **ISO 27001 certificate:** Certification body attests ISMS meets standard
- **FedRAMP authorization:** Government attests cloud service is secure

**User attestation:**
- **Acceptable Use Policy:** User attests they read and understand policy
- **Code of conduct:** Employee attests compliance with ethics policy
- **Data classification:** Data owner attests classification level is correct

**Access recertification:**
- **Manager attestation:** Manager attests user still needs access
- **Frequency:** Quarterly for privileged access, annually for standard
- **Process:** Review access list, approve or revoke

**Example attestation process:**
```
Annual Access Review:

1. System generates access report (who has access to what)
2. Sends to managers for review
3. Manager reviews each user:
   - User still on team? (Yes/No)
   - Access still needed? (Yes/No)
   - Access level appropriate? (Yes/No)
4. Manager attests (digital signature):
   "I attest that the above access is appropriate and necessary"
5. IT implements changes (remove uncertified access)
6. Compliance team retains attestation (audit evidence)
```

**Acknowledgement:**

**Definition:** Confirmation of receipt/understanding

**Common acknowledgements:**
- **Policy acknowledgement:** Employee confirms reading security policy
- **Training completion:** User confirms completing security awareness training
- **Incident notification:** User confirms receiving breach notification

**Difference from attestation:**
- **Attestation:** Declaration of truth/compliance
- **Acknowledgement:** Confirmation of receipt/understanding

---

## Compliance Monitoring and Reporting

**Continuous compliance monitoring:**

**Automated tools:**
- **Configuration compliance:** Tools scan systems for compliance violations
  - **Example:** CIS-CAT (CIS benchmark compliance)
  - **Frequency:** Daily
- **Log monitoring:** SIEM tracks compliance events
  - **Example:** Failed login attempts, privilege escalation
  - **Frequency:** Real-time
- **Vulnerability scanning:** Identifies security weaknesses
  - **Example:** Nessus, Qualys
  - **Frequency:** Weekly

**Manual activities:**
- **Access reviews:** Manager certifies user access appropriate
- **Policy reviews:** Annual policy update and approval
- **Vendor assessments:** Quarterly vendor security reviews

**Compliance reporting:**

**Dashboard (real-time):**
```
Compliance Status Dashboard:

PCI DSS Compliance: 95% (5 findings open)
- Critical: 0
- High: 2 (patch management gaps)
- Medium: 3 (password complexity)

HIPAA Compliance: 98% (2 findings)
- Risk assessments: Complete ✓
- Encryption: Complete ✓
- Access controls: 2 gaps (user access reviews overdue)

ISO 27001: Certification valid (expires 2025-03-15)
- Last audit: 2024-03-01
- Findings: 3 minor (all remediated)
```

**Compliance reports (periodic):**
- **Executive summary:** High-level status (monthly)
- **Detailed report:** All controls, findings (quarterly)
- **Audit reports:** External audit results (annual)

**Metrics tracked:**
- **Compliance score:** % of controls implemented
- **Open findings:** Number of outstanding audit findings
- **Mean time to remediate:** Average time to close findings
- **Repeat findings:** Issues found in multiple audits
- **Attestation completion rate:** % of users who completed attestations

---

## Due Diligence and Due Care

**Due diligence:**
- **Definition:** Investigation/research before making decision
- **Security context:** Assessing risks, evaluating controls
- **Example:**
  - Vendor assessment before contract
  - Risk assessment before new project
  - Reviewing audit reports before certification

**Due care:**
- **Definition:** Reasonable steps to protect assets (acting responsibly)
- **Security context:** Implementing and maintaining controls
- **Example:**
  - Patching vulnerabilities promptly
  - Training employees on security
  - Monitoring for threats

**Relationship:**
```
Due diligence = Knowing what to do (research, assessment)
Due care = Doing it (implementation, action)

Legal requirement:
Organizations must exercise BOTH due diligence and due care
Failure = Negligence (legal liability)

Example:
Due diligence: Conduct risk assessment, identify ransomware risk
Due care: Deploy EDR, train users, backup data
Negligence: Knowing ransomware risk but doing nothing
```

**Legal implications:**
- **Negligence:** Failure to exercise due care (liability)
- **Breach of fiduciary duty:** Officers/directors must act in organization's best interest
- **Regulatory penalties:** GDPR, HIPAA require due diligence and care

---

## Audit Preparation and Evidence

**Audit preparation:**

**Pre-audit activities:**
```
1. Scope confirmation
   - Which systems/processes in scope?
   - Time period covered?
   - Standards/regulations being audited?

2. Documentation review
   - Gather policies, procedures
   - Collect evidence (logs, reports, attestations)
   - Identify gaps (missing documentation)

3. Internal readiness assessment
   - Conduct mock audit
   - Identify and remediate gaps
   - Train staff on audit procedures

4. Evidence organization
   - Create evidence repository
   - Index documents for easy retrieval
   - Assign evidence custodian
```

**Evidence types:**

**Logs:**
- **Access logs:** Who accessed what (compliance with least privilege)
- **Change logs:** System modifications (change management)
- **Security logs:** Authentication attempts, incidents
- **Retention:** Per regulation (PCI = 1 year, HIPAA = 6 years)

**Attestations:**
- User policy acknowledgements
- Manager access certifications
- Vendor security questionnaires

**Reports:**
- Vulnerability scan results
- Penetration test reports
- Incident response reports
- Risk assessments

**Policies and procedures:**
- Security policy (acceptable use, password policy)
- Incident response plan
- Business continuity plan
- Vendor management policy

**Configurations:**
- System hardening baselines
- Firewall rulesets
- Network diagrams
- Access control lists

**Evidence management:**
```
Best practices:
- Centralized repository (SharePoint, secure file share)
- Version control (track document changes)
- Access control (limit who can modify)
- Retention policy (retain per compliance requirements)
- Audit trail (who accessed evidence, when)

Example structure:
/Audit_2024/
  /Policies/
    - Security_Policy_v2.1.pdf
    - Incident_Response_Plan_v1.3.pdf
  /Logs/
    - Access_Logs_Q1_2024.zip
    - SIEM_Reports_Q1_2024.pdf
  /Assessments/
    - Risk_Assessment_2024-01.xlsx
    - Vuln_Scan_Results_2024-03.pdf
  /Attestations/
    - User_Policy_Acknowledgements_2024.csv
    - Access_Reviews_Q1_2024.xlsx
```

---

## Audit Findings and Remediation

**Finding severity:**

**Critical:**
- **Definition:** Severe control failure, immediate risk
- **Example:** No encryption for customer PII
- **Timeline:** Remediate immediately (within days)

**High:**
- **Definition:** Significant control weakness
- **Example:** Admin accounts without MFA
- **Timeline:** Remediate within 30 days

**Medium:**
- **Definition:** Control gap, manageable risk
- **Example:** Password policy doesn't meet complexity requirements
- **Timeline:** Remediate within 90 days

**Low:**
- **Definition:** Minor improvement opportunity
- **Example:** Security policy missing revision date
- **Timeline:** Remediate within 6 months

**Observation/Advisory:**
- **Definition:** Recommendation, not required
- **Example:** Consider implementing SIEM for better visibility
- **Timeline:** At organization's discretion

**Remediation process:**
```
1. Acknowledge finding
   - Accept or dispute
   - If dispute: Provide evidence to auditor

2. Develop remediation plan
   - Root cause analysis
   - Corrective actions
   - Timeline
   - Owner assignment

3. Implement remediation
   - Execute plan
   - Document actions
   - Collect evidence

4. Validate remediation
   - Test that control now works
   - Auditor may re-test
   - Close finding

5. Prevent recurrence
   - Update procedures
   - Train staff
   - Monitor for similar issues
```

**Example finding remediation:**
```
Finding: High - Admin accounts do not require MFA

Root cause: MFA policy not enforced for all privileged accounts

Remediation plan:
1. Enable MFA for all admin accounts (Owner: IT Security)
2. Configure Conditional Access to require MFA (Owner: Azure Admin)
3. Verify all admins enrolled in MFA (Owner: IT Manager)
4. Update access control policy to mandate MFA (Owner: CISO)
Timeline: 30 days

Evidence of remediation:
- Screenshot of Conditional Access policy
- Report of admin accounts with MFA enabled (100%)
- Updated policy document (version 2.2, dated 2024-04-01)

Validation: Auditor tested admin login, MFA required ✓
Status: CLOSED
```

---

## Compliance Frameworks

**PCI DSS audit process:**
```
Annual requirement:
1. Self-Assessment Questionnaire (SAQ) - Small merchants
   OR
2. Report on Compliance (ROC) - Large merchants/service providers
   - Performed by Qualified Security Assessor (QSA)

Quarterly requirement:
- Vulnerability scans by Approved Scanning Vendor (ASV)

Attestation of Compliance (AOC):
- Signed statement confirming compliance
- Required annually
- Submitted to acquiring bank
```

**SOC 2 audit:**
```
Audit types:
- Type I: Point-in-time (controls design)
- Type II: Period (6-12 months, controls operating effectiveness)

Process:
1. Scoping: Define systems in scope
2. Readiness assessment: Internal prep
3. Audit (Type II: 6-12 month period)
4. Report issuance: SOC 2 report
5. Distribution: Share with customers (under NDA)

Trust Service Criteria:
- Security (always required)
- Availability (optional)
- Processing Integrity (optional)
- Confidentiality (optional)
- Privacy (optional)
```

**ISO 27001 certification:**
```
Process:
1. Gap analysis: Identify missing controls
2. Remediation: Implement required controls
3. Internal audit: Verify controls work
4. Stage 1 audit: Documentation review (external auditor)
5. Stage 2 audit: On-site audit (external auditor)
6. Certification: 3-year certificate issued
7. Surveillance audits: Annual (years 1-2)
8. Recertification: Year 3

Certificate maintenance:
- Annual surveillance audits
- Recertification every 3 years
- Continuous improvement required
```

---

## Key Distinctions

**Internal vs External Audit:**
- Internal: Self-assessment by organization
- External: Independent third-party verification

**Attestation vs Acknowledgement:**
- Attestation: Declaration of truth/compliance
- Acknowledgement: Confirmation of receipt

**Due Diligence vs Due Care:**
- Due diligence: Research and assessment
- Due care: Implementation and action

**SOC 2 Type I vs Type II:**
- Type I: Controls design (point in time)
- Type II: Operating effectiveness (period)

---

## Common Exam Traps

1. **Trap:** Thinking internal audits sufficient for compliance
   - **Reality:** External audits required for certification/attestation

2. **Trap:** Confusing attestation with acknowledgement
   - **Reality:** Attestation = declaration, acknowledgement = receipt

3. **Trap:** Believing due diligence is enough
   - **Reality:** Must have BOTH due diligence and due care

4. **Trap:** Assuming audit findings must all be remediated immediately
   - **Reality:** Severity drives timeline (critical = immediate, low = months)

5. **Trap:** Thinking compliance is one-time activity
   - **Reality:** Continuous monitoring and periodic audits required

---

## Exam Tips

1. **Internal audit** = self-assessment, **external audit** = third-party
2. **SOC 2 Type II** covers period (Type I = point in time)
3. **Attestation** = declaration of truth/compliance
4. **Due diligence** = research, **due care** = action
5. **PCI DSS requires** annual ROC and quarterly scans
6. **ISO 27001 certificate** valid for 3 years (annual surveillance audits)
7. **Compliance monitoring** = continuous (not one-time)
8. **Audit evidence** includes logs, policies, attestations, reports
9. **Finding remediation** based on severity (critical = immediate)
10. **Regulatory audit** conducted by government (can result in fines)

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