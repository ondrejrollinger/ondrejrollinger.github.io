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

Vulnerability management is the continuous process of identifying, evaluating, prioritizing, and remediating security weaknesses in systems. This objective covers scanning methods, CVSS scoring, risk-based remediation, patch management, and validation. The exam emphasizes *choosing the right action* in scenario-based questions — not just naming tools.

---

### Vulnerability scanning

#### Scanner types

| Scanner type | Examples | Targets | Finds |
|---|---|---|---|
| **Network vulnerability scanner** | Nessus, OpenVAS, Qualys | Servers, workstations, network devices | Missing patches, misconfigurations, weak passwords |
| **Web application scanner** | Burp Suite, OWASP ZAP, Acunetix | Web apps and APIs | SQLi, XSS, CSRF, authentication flaws |

#### Agent-based vs. agentless

| Method | How it works | Pros | Cons |
|---|---|---|---|
| **Agent-based** | Software installed on target system | Deep visibility: installed software, file permissions | Installation overhead; agent consumes resources |
| **Agentless** | Scans over the network; no installation | Easy deployment; no target-side impact | Limited visibility; may miss locally installed components |

#### Credentialed vs. non-credentialed scans

| Scan type | How it works | Pros | Cons | Best use |
|---|---|---|---|---|
| **Credentialed** | Scanner logs in with admin credentials | Internal view — sees all vulnerabilities | Requires credentials; security risk if scanner is compromised | Internal vulnerability assessments |
| **Non-credentialed** | External probe — no login | Simulates attacker perspective | May miss internal vulnerabilities | External pen tests, compliance checks |

> **Exam tip:** Credentialed scans are more thorough. Non-credentialed scans reflect what an external attacker would see.

#### False positives vs. false negatives

| Term | Definition | Impact | Mitigation |
|---|---|---|---|
| **False positive** | Scanner reports a vulnerability that doesn't exist | Wasted investigation time | Tune scanner rules; verify findings manually |
| **False negative** | Scanner misses an actual vulnerability | Real risk goes undetected | Use multiple scanners; supplement with manual testing |

> **Exam tip:** False negatives are more dangerous than false positives — a missed vulnerability leaves real risk unaddressed while false positives only waste time.

---

### Vulnerability assessment vs. penetration testing

| | Vulnerability assessment | Penetration testing |
|---|---|---|
| **Goal** | Identify and catalog vulnerabilities | Exploit vulnerabilities to demonstrate business impact |
| **Method** | Automated scanning, limited manual verification | Manual exploitation by skilled security professionals |
| **Output** | List of vulnerabilities with severity ratings | Proof of compromise, attack narrative, business impact |
| **Frequency** | Ongoing (weekly, monthly) | Annual or after major changes |
| **Invasiveness** | Low — read-only, safe checks | High — actual exploitation; may cause disruption |

> **Exam tip:** Assessment = identify. Penetration test = exploit. They are not interchangeable.

---

### CVSS (Common Vulnerability Scoring System)

CVSS provides a standardized severity rating that enables consistent prioritization across organizations.

#### Score ranges

| Score | Severity |
|---|---|
| 0.0 | None |
| 0.1 – 3.9 | Low |
| 4.0 – 6.9 | Medium |
| 7.0 – 8.9 | High |
| 9.0 – 10.0 | Critical |

#### Score components

| Component | What it measures | Notes |
|---|---|---|
| **Base score** | Inherent severity of the vulnerability | Attack vector, complexity, privileges required, user interaction, CIA impact |
| **Temporal score** | Time-sensitive factors | Exploit availability, remediation level, report confidence |
| **Environmental score** | Organization-specific context | Asset value, compensating controls already in place |

> **Exam tip:** CVSS Base score alone does not determine patch priority. Environmental and temporal scores — plus asset criticality — must be factored in. A Critical CVSS score on an isolated internal system may be lower priority than a High score on an internet-facing payment server.

#### Risk-based prioritization

Beyond CVSS, prioritization considers:

| Factor | Higher priority when… |
|---|---|
| **Asset criticality** | System holds PII, supports critical business functions, or faces the internet |
| **Exploit availability** | Proof-of-concept or working exploit is publicly available |
| **Threat intelligence** | Vulnerability is actively exploited in the wild or targeted at your industry |
| **Compensating controls** | No WAF, no segmentation, no MFA reducing the attack surface |

---

### Remediation strategies

| Strategy | Description | When to use |
|---|---|---|
| **Patching** | Apply vendor-provided security update | Primary remediation; permanent fix |
| **Configuration change** | Disable vulnerable service, remove default credentials | When patch is delayed or unavailable |
| **Compensating control** | WAF rule, firewall ACL, network segmentation | Temporary measure until remediation; does *not* fix the underlying flaw |
| **Virtual patching** | IPS/WAF rule blocks known exploit attempts | Short-term protection while vendor patch is tested |
| **Removal / decommissioning** | Remove software or service entirely | Vulnerable component is no longer needed |
| **Isolation / segmentation** | VLAN or firewall restricts access to the vulnerable system | System cannot be patched but must remain operational |

> **Exam tip:** Virtual patching (IPS/WAF rule) does not fix the vulnerability — it only blocks known exploit patterns. It is a temporary measure, not a substitute for patching.

---

### Patch management

#### Patch deployment process

1. **Identify** — Review vendor security bulletins and CVE feeds.
2. **Assess** — Determine applicability and assign priority.
3. **Test** — Deploy to test / staging environment first.
4. **Approve** — Submit through change control process.
5. **Deploy** — Staged rollout: pilot group → broader production.
6. **Verify** — Rescan to confirm patch is applied and effective.

#### Deployment strategies

| Strategy | Use case | Risk |
|---|---|---|
| **Automated patching** | Low-risk patches, workstations, off-hours | Patch may break application without prior testing |
| **Manual patching** | Critical or complex systems requiring validation | Human error; inconsistent application |
| **Emergency patching** | Critical vulnerability with active exploitation (zero-day) | Expedited testing increases breaking-change risk |

> **Exam tip:** Patches should always be tested before production deployment — even emergency patches when time allows. "Deploy immediately without testing" is almost never the correct answer.

---

### Validation and reporting

#### Confirming remediation

| Method | Description |
|---|---|
| **Re-scanning** | Run the same vulnerability scan after patching; verify the finding is gone |
| **Manual verification** | Confirm configuration change was applied; review logs |
| **Penetration testing** | Attempt to exploit the vulnerability under controlled conditions to confirm it is resolved |

#### Reporting levels

| Report type | Audience | Content |
|---|---|---|
| **Executive (high-level)** | Leadership, board | Vulnerability trends, critical/high count, mean time to remediate, compliance status |
| **Technical (detailed)** | Security team, IT | CVE/CVSS details, affected systems, remediation steps, compensating controls in place |

#### Key metrics to track

- Total vulnerabilities found
- Vulnerabilities by severity (Critical / High / Medium / Low)
- Mean time to remediate (MTTR) by severity
- Remediation rate (% closed per month)
- Recurring vulnerabilities (same issue appearing repeatedly)

---

### Key distinctions to know for the exam

| Comparison | Distinction |
|---|---|
| **Vulnerability assessment vs. pen test** | Assessment identifies vulnerabilities (scanning); pen test exploits them (manual hacking). |
| **False positive vs. false negative** | False positive = reported but doesn't exist (wastes time); false negative = exists but not reported (leaves real risk). |
| **Remediation vs. mitigation** | Remediation fixes the vulnerability (patch); mitigation reduces risk without fixing it (compensating control). |
| **Credentialed vs. non-credentialed scan** | Credentialed = internal full-visibility view; non-credentialed = external attacker view. |
| **Virtual patching vs. real patching** | Virtual patching (WAF/IPS rule) blocks exploits temporarily; only a vendor patch addresses the root cause. |
| **CVSS base vs. environmental score** | Base score = universal severity; environmental score = adjusted for your specific context and controls. |

---

### Common exam traps

**Trap: Using CVSS score alone to determine patch priority.**
Reality: CVSS base score is a starting point only. Asset criticality, exploit availability, and existing compensating controls all change the real-world priority.

**Trap: Believing automated scanners find all vulnerabilities.**
Reality: Scanners miss logic flaws, chained vulnerabilities, and novel attack paths. Manual testing and penetration testing are necessary for comprehensive coverage.

**Trap: Thinking patches should be deployed to production immediately.**
Reality: Patches must be tested in a staging environment first. Breaking a production system while patching can be as disruptive as the vulnerability itself.

**Trap: Treating vulnerability management as a one-time project.**
Reality: It is a continuous cycle — identify, prioritize, remediate, validate, repeat.

**Trap: Treating false positives as harmless.**
Reality: A high false positive rate erodes analyst trust, causing real vulnerabilities in future reports to be dismissed or deprioritized.

---

### Exam tips

1. **CVSS ranges:** 0–3.9 Low | 4–6.9 Medium | 7–8.9 High | 9–10 Critical.
2. "Identify vulnerabilities, automated scanning" → **vulnerability assessment**.
3. "Exploit vulnerabilities, demonstrate impact" → **penetration testing**.
4. "Block exploit via WAF/IPS rule while awaiting patch" → **virtual patching**.
5. "Can't patch, system must stay running" → **compensating control / isolation**.
6. "Scanner says vulnerable, but manual check confirms it's not" → **false positive**.
7. "Vulnerable system not flagged in scan results" → **false negative**.
8. **Credentialed scans** give internal view; **non-credentialed** give attacker view.
9. Patch testing order: test environment → staging → production.
10. **Validation** = rescan after remediation to confirm the finding is closed.

---

## Key terms

- **Vulnerability management** — Continuous process of identifying, evaluating, prioritizing, and remediating security weaknesses.
- **CVSS (Common Vulnerability Scoring System)** — Standardized framework for rating vulnerability severity; scores from 0.0 to 10.0.
- **Vulnerability assessment** — Automated scanning process to identify and catalog vulnerabilities; does not exploit them.
- **Penetration testing** — Manual security testing that attempts to exploit vulnerabilities to demonstrate real-world impact.
- **Credentialed scan** — Vulnerability scan performed with admin credentials; provides an internal, comprehensive view.
- **Non-credentialed scan** — Vulnerability scan with no login; simulates an external attacker's perspective.
- **False positive** — Scanner reports a vulnerability that does not actually exist.
- **False negative** — Scanner fails to report a vulnerability that does exist.
- **Patch management** — Structured process to test, approve, and deploy vendor security updates.
- **Virtual patching** — Temporary IPS/WAF rule that blocks known exploit attempts while a vendor patch is prepared.
- **Compensating control** — Alternative security measure that reduces risk when direct remediation is not immediately possible.
- **Remediation** — Permanently fixing a vulnerability (e.g., applying a patch or correcting a misconfiguration).
- **Mitigation** — Reducing the impact or likelihood of exploitation without fully fixing the underlying vulnerability.
- **Agent-based scanning** — Vulnerability scanning using software installed directly on the target system.
- **Agentless scanning** — Vulnerability scanning performed over the network without installing software on targets.

---

## Examples / scenarios

**Scenario 1:** A security team scans a web server and receives 47 findings. After manual review, 30 of them describe vulnerabilities that do not actually exist on the hardened server.
- **Answer:** False positives. The scanner is over-reporting; the team needs to tune scanner rules and verify findings before acting.

**Scenario 2:** A critical Apache web server receives a CVSS 9.8 CVE with a public exploit. The server is internet-facing and processes customer payments.
- **Answer:** Critical priority — patch immediately. High CVSS + internet-facing + public exploit + sensitive data = highest urgency. Emergency patching process applies.

**Scenario 3:** An organization cannot patch a legacy SCADA system because the vendor no longer supports it, but the system controls physical infrastructure.
- **Answer:** Compensating controls. Apply network segmentation (isolated VLAN), enhanced monitoring, and restrict access. Remediation is not possible — mitigation is the goal.

**Scenario 4:** A vulnerability scanner reports a finding as resolved after patching, but the security team wants to confirm the exploit no longer works before closing the ticket.
- **Answer:** Validation via penetration testing or manual verification. Rescanning confirms the patch is installed; a hands-on test confirms the vulnerability is no longer exploitable.

**Scenario 5:** A WAF rule is deployed to block a known SQL injection exploit pattern targeting a web application while the development team prepares and tests the code fix.
- **Answer:** Virtual patching — a temporary compensating control that blocks exploit attempts until the root cause is remediated in the application code.

---

## Mini quiz

<details>
<summary><strong>Question 1:</strong> What is the difference between a vulnerability assessment and a penetration test?</summary>

**Answer:** A vulnerability assessment uses automated scanning to identify and catalog vulnerabilities — it does not exploit them. A penetration test goes further: a skilled tester manually attempts to exploit vulnerabilities to demonstrate real business impact (e.g., data exfiltration, privilege escalation). Assessments are run frequently; pen tests are typically annual or after major changes.
</details>

<details>
<summary><strong>Question 2:</strong> Why is a false negative more dangerous than a false positive in vulnerability scanning?</summary>

**Answer:** A false negative means a real vulnerability was not detected — the risk remains unaddressed while the team believes they are protected. A false positive means the scanner flagged something that isn't actually vulnerable — it wastes investigation time but does not leave a real exposure. Undetected vulnerabilities can be exploited; wasted time cannot.
</details>

<details>
<summary><strong>Question 3:</strong> What factors beyond CVSS score should influence patch prioritization?</summary>

**Answer:** Asset criticality (does it hold PII? is it internet-facing?), exploit availability (is there a public PoC or active exploitation in the wild?), compensating controls already in place (WAF, segmentation, MFA), and business context (critical business period, acceptable downtime). A Critical CVSS on an isolated internal test server may be lower priority than a High CVSS on a public-facing payment system with a published exploit.
</details>

<details>
<summary><strong>Question 4:</strong> What is virtual patching and what is its key limitation?</summary>

**Answer:** Virtual patching deploys an IPS or WAF rule to detect and block known exploit attempts for a vulnerability, providing protection while the organization tests and deploys the vendor's official patch. The limitation: it only blocks *known* exploit patterns for that specific vulnerability. It does not fix the underlying flaw, and novel or modified exploits may bypass the rule. It is a temporary control, not a substitute for remediation.
</details>

<details>
<summary><strong>Question 5:</strong> What is the correct sequence for deploying a security patch in an enterprise environment?</summary>

**Answer:** (1) Identify the patch and assess applicability; (2) test in a non-production environment; (3) obtain change control approval; (4) staged deployment — pilot group first, then broader rollout; (5) verify via rescan that the vulnerability is remediated.
</details>

### CompTIA-style practice questions

<details>
<summary><strong>Question 6:</strong> A security analyst reviews a scan report and finds a vulnerability rated CVSS 9.4 on an internal development server that is isolated from production and holds no sensitive data. A separate finding rated CVSS 7.2 affects the organization's public-facing e-commerce application, which processes credit card transactions, and a working exploit is publicly available. Which vulnerability should be patched FIRST?<br>A. The CVSS 9.4 vulnerability on the development server, because it has the higher base score<br>B. The CVSS 7.2 vulnerability on the e-commerce application, because of asset criticality and exploit availability<br>C. Both vulnerabilities simultaneously to minimize total exposure<br>D. Neither — both are below the Critical threshold of 10.0</summary>

**Correct Answer: B. The CVSS 7.2 vulnerability on the e-commerce application**

CVSS base score is not the only prioritization factor. The e-commerce system is internet-facing, processes payment card data, and has a public working exploit — all factors that dramatically increase real-world risk. The isolated dev server's high CVSS score is theoretical risk; the e-commerce vulnerability is being actively weaponized.

- A: CVSS score alone does not determine priority — context matters.
- C: Resource-constrained teams must triage; "patch both simultaneously" avoids the prioritization decision the question requires.
- D: CVSS thresholds do not define whether patching is required; business impact does.
</details>

<details>
<summary><strong>Question 7:</strong> An organization deploys a WAF rule to block a recently disclosed remote code execution vulnerability in their web application framework. The development team estimates the application patch will be ready in two weeks. Which term BEST describes the WAF rule deployment?<br>A. Remediation<br>B. Patch management<br>C. Virtual patching<br>D. Vulnerability assessment</summary>

**Correct Answer: C. Virtual patching**

A WAF or IPS rule deployed to block exploit attempts for a known vulnerability — as a temporary measure while the real fix is prepared — is the definition of virtual patching.

- A: Remediation would fix the underlying vulnerability in the application code itself.
- B: Patch management refers to the process of testing and deploying the vendor's official software update.
- D: Vulnerability assessment is the process of identifying vulnerabilities through scanning; it has no protective function.
</details>

<details>
<summary><strong>Question 8 (Multi-select):</strong> A security manager is reviewing the organization's vulnerability management program. Which TWO practices represent validation activities that should occur AFTER remediation? (Select TWO.)<br>A. Running a credentialed scan to identify missing patches before remediation begins<br>B. Rescanning the affected system to confirm the vulnerability no longer appears<br>C. Assigning a CVSS environmental score to newly discovered findings<br>D. Attempting to manually exploit the previously vulnerable system to confirm it is no longer susceptible<br>E. Reviewing threat intelligence feeds for emerging vulnerabilities</summary>

**Correct Answers: B and D**

Validation occurs after remediation to confirm the fix was successful. Rescanning (B) verifies the patch is installed and the scanner no longer detects the finding. Manual exploitation testing (D) provides stronger assurance by confirming the vulnerability cannot actually be leveraged.

- A: Pre-remediation scanning is the identification phase, not validation.
- C: CVSS environmental scoring is part of the prioritization/analysis phase.
- E: Reviewing threat intelligence is an ongoing identification and prioritization activity, not post-remediation validation.
</details>

---

## Related objectives

- [**2.3**]({{ '/secplus/objectives/2-3/' | relative_url }}) — Vulnerability types covered here are the same weaknesses that vulnerability management aims to find and remediate.
- [**4.4**]({{ '/secplus/objectives/4-4/' | relative_url }}) — Security alerting and monitoring tools surface indicators that feed the vulnerability management process.
- [**4.1**]({{ '/secplus/objectives/4-1/' | relative_url }}) — Security hardening techniques directly reduce the misconfigurations and weak settings that vulnerability scans detect.
- [**5.1**]({{ '/secplus/objectives/5-1/' | relative_url }}) — Risk management frameworks inform how vulnerability severity is weighted against business impact during prioritization.

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
