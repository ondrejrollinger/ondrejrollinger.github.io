---
layout: objective
title: "Security+ 4.3 — Explain various activities associated with vulnerability management."
objective_id: "4.3"
domain: "4.0 Security Operations"
status: "done"
tags:
  - secplus701
permalink: /secplus/objectives/4-3/
---

# Security+ 4.3 — Explain various activities associated with vulnerability management.

Status: <span class="status-badge done">done</span>

## Exam objective
Explain various activities associated with vulnerability management.

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

Vulnerability management is the continuous process of identifying, evaluating, prioritizing, and remediating security weaknesses in systems. This includes vulnerability scanning, patch management, and risk-based remediation strategies.

---

## Vulnerability Identification Methods

**Vulnerability scanning:**

**Definition:** Automated process of probing systems for known vulnerabilities.

**Scanner types:**

**Network vulnerability scanners:**
- Examples: Nessus, OpenVAS, Qualys
- Scan: Servers, workstations, network devices
- Method: Send probes, analyze responses
- Finds: Missing patches, misconfigurations, weak passwords

**Web application scanners:**
- Examples: Burp Suite, OWASP ZAP, Acunetix
- Scan: Web apps and APIs
- Finds: SQL injection, XSS, CSRF, authentication flaws

**Agent-based vs agentless:**

**Agent-based:**
- Software installed on target system
- **Pros:** Detailed information (installed software, file permissions)
- **Cons:** Installation overhead, agent may consume resources

**Agentless:**
- Scans over network (no software installation)
- **Pros:** Easy deployment, no target system impact
- **Cons:** Limited information (can't see all installed software)

**Scan types:**

**Credentialed scan:**
- Scanner logs into system with admin credentials
- **Pros:** Sees all vulnerabilities (internal view)
- **Cons:** Requires credentials, security risk if scanner compromised
- **Use:** Internal vulnerability assessments

**Non-credentialed scan:**
- Scanner probes from outside (no login)
- **Pros:** Simulates external attacker view
- **Cons:** May miss vulnerabilities (limited visibility)
- **Use:** External pen tests, compliance scans

**Scan frequency:**
- **Critical systems:** Weekly or after changes
- **Standard systems:** Monthly
- **After major patch releases:** Immediately
- **Continuous:** Ongoing monitoring in mature programs

**False positives vs false negatives:**

**False positive:**
- Scanner reports vulnerability that doesn't exist
- **Impact:** Wasted time investigating
- **Mitigation:** Tune scanner, verify findings

**False negative:**
- Scanner misses actual vulnerability
- **Impact:** Security risk remains undetected
- **Mitigation:** Use multiple scanners, manual testing

---

## Vulnerability Assessment vs Penetration Testing

**Vulnerability assessment:**
- **Goal:** Identify and report vulnerabilities
- **Method:** Automated scanning, some manual verification
- **Output:** List of vulnerabilities with severity ratings
- **Frequency:** Regular (weekly, monthly)
- **Invasiveness:** Low (read-only, safe checks)

**Penetration testing:**
- **Goal:** Exploit vulnerabilities to demonstrate impact
- **Method:** Manual exploitation by security professionals
- **Output:** Proof of compromise, business impact assessment
- **Frequency:** Annual or after major changes
- **Invasiveness:** High (actual exploitation, may cause disruption)

**When to use each:**
- Vulnerability assessment: Ongoing security monitoring
- Penetration testing: Validate defenses, demonstrate risk to management

---

## Vulnerability Analysis and Prioritization

**CVSS (Common Vulnerability Scoring System):**

**Purpose:** Standardized severity rating for vulnerabilities

**CVSS score ranges:**
- 0.0: None
- 0.1-3.9: Low
- 4.0-6.9: Medium
- 7.0-8.9: High
- 9.0-10.0: Critical

**CVSS metrics:**

**Base score (inherent severity):**
- Attack vector: Network (most severe) vs Local vs Physical
- Attack complexity: Low (easy) vs High (difficult)
- Privileges required: None vs Low vs High
- User interaction: None (automatic) vs Required (user must act)
- Impact: Confidentiality, Integrity, Availability (CIA)

**Temporal score (time-based factors):**
- Exploit availability: Proof-of-concept exists? Exploit in the wild?
- Remediation level: Official fix available? Workaround only?
- Report confidence: Confirmed vs Reasonable vs Unknown

**Environmental score (organization-specific):**
- Modified base metrics for specific environment
- Collateral damage potential
- Target distribution (how many systems affected)

**Example CVSS scoring:**
```
Vulnerability: CVE-2024-1234 (Remote Code Execution in Apache)

Base metrics:
- Attack Vector: Network (exploitable remotely)
- Attack Complexity: Low (easy to exploit)
- Privileges Required: None
- User Interaction: None
- Confidentiality Impact: High
- Integrity Impact: High  
- Availability Impact: High

Base Score: 9.8 (Critical)

Temporal metrics:
- Exploit Code Maturity: Functional (exploit published)
- Remediation Level: Official Fix (patch available)
- Report Confidence: Confirmed

Temporal Score: 9.3

Environmental (organization-specific):
- Modified Impact: Lower (system not internet-facing in our environment)
- Environmental Score: 7.5 (High, downgraded from Critical)

Final prioritization: High priority (not Critical) because not internet-facing
```

**Prioritization factors beyond CVSS:**

**Asset criticality:**
- Critical business system > Standard workstation
- Database with customer PII > Test environment
- Internet-facing > Internal only

**Threat intelligence:**
- Vulnerability actively exploited in wild? (prioritize high)
- Targeted attacks against our industry? (prioritize)

**Compensating controls:**
- WAF blocking exploit? (lower priority)
- Network segmentation limiting access? (lower priority)
- Multi-factor auth required? (reduces credential theft impact)

**Business context:**
- System downtime acceptable? (can patch immediately)
- Critical business period? (delay non-critical patches)

**Risk-based prioritization matrix:**

| CVSS Score | Internet-facing | Contains PII | Exploit available | Priority |
|------------|-----------------|--------------|-------------------|----------|
| 9.0-10.0 | Yes | Yes | Yes | Critical (patch immediately) |
| 9.0-10.0 | Yes | Yes | No | High (patch within 24h) |
| 9.0-10.0 | No | No | Yes | High (patch within 72h) |
| 7.0-8.9 | Yes | Yes | Yes | High (patch within 72h) |
| 7.0-8.9 | No | No | No | Medium (patch within 30 days) |
| 4.0-6.9 | Any | Any | Any | Low (patch in normal cycle) |

---

## Remediation and Mitigation

**Remediation strategies:**

**Patching:**
- **Definition:** Apply vendor-provided security update
- **Best:** Permanent fix, addresses root cause
- **Timeline:** Test in dev → Deploy to staging → Production
- **Challenge:** May cause compatibility issues, requires testing

**Configuration change:**
- **Example:** Disable vulnerable service, change default password
- **Use:** When patch not available or delayed
- **Pro:** Quick implementation
- **Con:** May impact functionality

**Compensating controls:**
- **Definition:** Alternative control that reduces risk
- **Example:** WAF blocks SQL injection while awaiting app patch
- **Use:** Temporary measure until remediation
- **Limitation:** Doesn't fix underlying vulnerability

**Removal/decommissioning:**
- **Use:** Vulnerable software no longer needed
- **Best:** Eliminates risk entirely
- **Example:** Remove obsolete web server, disable unused service

**Isolation/segmentation:**
- **Use:** Vulnerable system required but can't be patched
- **Method:** VLAN isolation, firewall rules
- **Effect:** Limits exposure (can't eliminate vulnerability)

**Patch management:**

**Patch testing process:**
1. **Identify:** Review vendor security bulletins
2. **Assess:** Determine applicability and priority
3. **Test:** Deploy to test environment
4. **Approve:** Change control approval
5. **Deploy:** Staged rollout (pilot group → all systems)
6. **Verify:** Confirm patch installed and effective

**Patch deployment strategies:**

**Automated patching:**
- **Tools:** WSUS (Windows), SCCM, Patch management software
- **Use:** Low-risk patches, workstations
- **Schedule:** After-hours, maintenance windows

**Manual patching:**
- **Use:** Critical systems, require testing
- **Process:** IT admin applies patch
- **Risk:** Human error, inconsistent application

**Emergency patching:**
- **Trigger:** Critical vulnerability, active exploitation
- **Process:** Expedited testing and deployment
- **Example:** Zero-day exploit with public exploit code

**Virtual patching:**
- **Definition:** IPS/WAF rule blocks exploit attempts
- **Use:** Temporary protection while testing vendor patch
- **Limitation:** Doesn't fix vulnerability, only blocks known exploits

---

## Validation and Reporting

**Vulnerability validation:**

**Re-scanning:**
- Scan after remediation to confirm fix
- Verify vulnerability no longer detected
- Document remediation success

**Manual verification:**
- Attempt to exploit (safely)
- Confirm configuration change applied
- Review logs for proper hardening

**Penetration testing:**
- Validate remediation under realistic attack conditions
- Confirm exploits no longer work

**Reporting:**

**Executive report (high-level):**
- Vulnerability trends (improving or worsening?)
- Critical/High vulnerabilities count
- Mean time to remediate
- Compliance status (met SLA?)

**Technical report (detailed):**
- Vulnerability details (CVE, CVSS, description)
- Affected systems list
- Remediation steps
- Compensating controls in place

**Metrics to track:**
- Total vulnerabilities found
- Vulnerabilities by severity
- Time to remediate (by severity)
- Remediation rate (% closed per month)
- Recurring vulnerabilities (same issue multiple times)

---

## Common Vulnerability Types

**Configuration vulnerabilities:**
- Default credentials
- Unnecessary services enabled
- Weak encryption settings
- Improper file permissions

**Software vulnerabilities:**
- Buffer overflow
- SQL injection
- Cross-site scripting (XSS)
- Remote code execution (RCE)

**Missing patches:**
- Outdated OS (Windows, Linux)
- Unpatched applications (browsers, Java)
- Firmware not updated

**Weak authentication:**
- No multi-factor authentication
- Weak password policy
- Hardcoded credentials

---

## Key Distinctions

**Vulnerability Assessment vs Penetration Testing:**
- Assessment: Identify vulnerabilities (automated scanning)
- Penetration testing: Exploit vulnerabilities (manual hacking)

**False Positive vs False Negative:**
- False positive: Report says vulnerable but isn't (waste of time)
- False negative: Vulnerable but not reported (security risk)

**Remediation vs Mitigation:**
- Remediation: Fix vulnerability (patch, configuration change)
- Mitigation: Reduce risk without fixing (compensating control)

**Credentialed vs Non-credentialed scan:**
- Credentialed: Scanner logs in (internal view)
- Non-credentialed: External probe (attacker view)

---

## Common Exam Traps

1. **Trap:** Thinking CVSS score alone determines patch priority
   - **Reality:** Consider asset criticality, business context, compensating controls

2. **Trap:** Believing automated scanning finds all vulnerabilities
   - **Reality:** Manual testing and pen testing required for comprehensive coverage

3. **Trap:** Assuming patches should be deployed immediately
   - **Reality:** Test first to prevent breaking production systems

4. **Trap:** Thinking vulnerability management is one-time activity
   - **Reality:** Continuous process (identify, remediate, validate, repeat)

5. **Trap:** Believing false positives are acceptable
   - **Reality:** High false positive rate reduces trust, leads to ignored real vulnerabilities

---

## Exam Tips

1. **CVSS scores:** 0-3.9 Low, 4-6.9 Medium, 7-8.9 High, 9-10 Critical
2. **Vulnerability assessment** = identify (scanning)
3. **Penetration testing** = exploit (hacking)
4. **Patch testing** required before production deployment
5. **Virtual patching** = IPS/WAF rule (temporary protection)
6. **Compensating controls** reduce risk when remediation delayed
7. **Credentialed scans** more comprehensive than non-credentialed
8. **False negative** = missed vulnerability (worse than false positive)
9. **Prioritize based on:** CVSS + asset criticality + exploit availability
10. **Validation** = rescan after remediation to confirm fix

---

## Navigation

**Domain 4.0: Security Operations**

| Objective | Title | Status |
|---|---|---|
| [4.1]({{ '/secplus/objectives/4-1/' | relative_url }}) | Given a scenario, apply common security techniques to computing resources. | done |
| [4.2]({{ '/secplus/objectives/4-2/' | relative_url }}) | Explain the security implications of proper hardware, software, and data asset management. | done |
| **4.3** | Explain various activities associated with vulnerability management. (current) | done |
| [4.4]({{ '/secplus/objectives/4-4/' | relative_url }}) | Explain security alerting and monitoring concepts and tools. | done |
| [4.5]({{ '/secplus/objectives/4-5/' | relative_url }}) | Given a scenario, modify enterprise capabilities to enhance security. | done |
| [4.6]({{ '/secplus/objectives/4-6/' | relative_url }}) | Given a scenario, implement and maintain identity and access management. | done |
| [4.7]({{ '/secplus/objectives/4-7/' | relative_url }}) | Explain the importance of automation and orchestration related to secure operations. | done |
| [4.8]({{ '/secplus/objectives/4-8/' | relative_url }}) | Explain appropriate incident response activities. | done |
| [4.9]({{ '/secplus/objectives/4-9/' | relative_url }}) | Given a scenario, use data sources to support an investigation. | done |

[← Previous: Objective 4.2]({{ '/secplus/objectives/4-2/' | relative_url }}) | [Back to Dashboard]({{ '/secplus/' | relative_url }}) | [Next: Objective 4.4 →]({{ '/secplus/objectives/4-4/' | relative_url }})