---
layout: objective
title: "Security+ 4.5 — Given a scenario, modify enterprise capabilities to enhance security."
objective_id: "4.5"
domain: "4.0 Security Operations"
status: "done"
tags:
  - secplus701
permalink: /secplus/objectives/4-5/
---

# Security+ 4.5 — Given a scenario, modify enterprise capabilities to enhance security.

Status: <span class="status-badge done">done</span>

## Exam objective
Given a scenario, modify enterprise capabilities to enhance security.

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

Identity and Access Management (IAM) ensures the right users have the right access to the right resources — and nothing more. This objective covers the full user lifecycle (provisioning to deprovisioning), privileged access management (PAM), multi-factor authentication (MFA), and federated identity (SSO). The exam presents scenarios where you must identify the appropriate IAM control or diagnose what went wrong when a control was absent.

---

### Provisioning and deprovisioning

The user lifecycle governs how accounts are created, modified, and removed as people join, change roles within, or leave an organization.

**Onboarding (provisioning):**
1. HR creates employee record
2. IT creates user account (Active Directory, cloud IAM)
3. Assign to groups — groups determine access scope
4. Provision email, apps, and file shares
5. Issue temporary credentials; require change on first login
6. Deliver security awareness training and acceptable use policy

**Role changes:**
- Promotion or lateral move: add new access, but **remove** access that no longer applies
- Key risk: failing to remove old access leads to **privilege creep**

**Offboarding (deprovisioning):**
1. HR initiates termination
2. IT **immediately disables** account (before employee is notified for involuntary separations)
3. Revoke badges, VPN tokens, and remote access
4. Transfer data ownership (email, files) to manager
5. Retrieve company property (laptop, phone, access cards)
6. **Disable now; delete after retention period** (30–90 days) — keeps account available for forensic investigations

**Automated provisioning:**

| Concept | Description |
|---|---|
| **Identity Provider (IdP)** | Centralized user directory (Azure AD, Okta); single source of truth for identities |
| **HR → IdP integration** | Termination in HR system automatically triggers account disable in IdP |
| **Just-in-Time (JIT) provisioning** | Account is created the first time a user authenticates to an application |

> **Exam tip:** For involuntary terminations, **disable the account immediately** — before the employee is notified. Delaying creates a window for data exfiltration or sabotage. Disable ≠ delete; keep the account for data retention and potential investigation.

---

### Permission auditing and recertification

Regular access reviews validate that users still need the permissions they hold, catching privilege creep before it becomes a liability.

**Review frequency:**

| Account type | Recommended frequency |
|---|---|
| High-privilege / admin accounts | Quarterly |
| Standard user accounts | Annually |
| After any role change | Immediately |

**Review process:**
1. Generate access report (who has access to what)
2. Send report to each manager for certification
3. Manager approves or revokes each access entry
4. IT implements removals for uncertified access
5. Document results as compliance evidence

**Privilege creep:**
- **Definition:** A user gradually accumulates permissions over time — through project assignments and role changes — that are never removed.
- **Risk:** Violates least privilege; a compromised account has far more damage potential than necessary.
- **Prevention:** Regular access reviews + automated deprovisioning triggers.

**Separation of duties (SoD):**
- No single person controls an entire critical process end-to-end.
- Classic example: the person who *approves* an invoice is different from the person who *pays* it.
- Implemented as mutually exclusive roles in an IAM system.
- Purpose: prevent fraud and reduce insider threat risk.

> **Exam tip:** Separation of duties and least privilege often appear together in exam scenarios. SoD prevents a single person from committing fraud alone; least privilege limits the blast radius if an account is compromised.

---

### Privileged Access Management (PAM)

Privileged accounts (admins, service accounts, emergency "break-glass" accounts) require stricter controls than standard user accounts because their compromise can be catastrophic.

**PAM capabilities:**

| Capability | Description | Example tools |
|---|---|---|
| **Password vaulting** | Privileged credentials stored in an encrypted vault; users check out passwords rather than knowing them permanently | CyberArk, BeyondTrust, Thycotic |
| **Automatic rotation** | Password changes after each check-in or on a schedule | Eliminates shared/static admin passwords |
| **Session recording** | All privileged sessions recorded (video + keystroke logging) | Provides audit trail; deters abuse |
| **Real-time monitoring** | Suspicious commands trigger alerts during live sessions | Admin runs `rm -rf /`; alert fires |
| **Just-in-Time (JIT) access** | Admin rights granted on demand for a defined window, then automatically revoked | Developer gets production access for 2 hours |

> **Exam tip:** PAM's core value is eliminating **standing privileges** — permanent admin rights that sit idle but represent constant risk. JIT access and password vaulting both reduce the window of exposure. "Session recording" = accountability + audit trail.

---

### Multi-Factor Authentication (MFA)

MFA requires users to prove identity using two or more **different** factor types.

**The five factor categories:**

| Factor | Type | Examples |
|---|---|---|
| **Something you know** | Knowledge | Password, PIN, security question |
| **Something you have** | Possession | Smart card, hardware token, phone |
| **Something you are** | Inherence (biometric) | Fingerprint, facial recognition, iris scan |
| **Somewhere you are** | Location | GPS coordinates, network location |
| **Something you do** | Behavioral | Typing rhythm, gait analysis |

**MFA = two or more factors from different categories.** Two knowledge factors (e.g., password + security question) is not MFA.

**MFA method comparison:**

| Method | Strength | Key weakness |
|---|---|---|
| **SMS / email code** | Low-medium | Vulnerable to SIM swapping and interception |
| **Authenticator app (TOTP)** | Medium-high | Requires app install; phishing still possible |
| **Push notification** | Medium | MFA fatigue — users may approve without reading |
| **Hardware token (FIDO2/WebAuthn)** | Highest | Cost; can be lost; but phishing-resistant |
| **Biometric** | High | Cannot be changed if compromised; false accept/reject rates |

> **Exam tip:** Security hierarchy for MFA methods: **Hardware token > Authenticator app > Push notification > SMS**. If a scenario asks for the "most secure" MFA option, hardware tokens (FIDO2/WebAuthn) are the answer. If it asks about a weakness unique to push notifications, the answer is **MFA fatigue**.

---

### Single Sign-On (SSO)

SSO allows a user to authenticate once and access multiple applications without re-entering credentials.

**SSO components:**

| Component | Role | Examples |
|---|---|---|
| **Identity Provider (IdP)** | Performs authentication; issues tokens/assertions | Azure AD, Okta, Auth0 |
| **Service Provider (SP)** | Relies on IdP's assertion to grant access | Salesforce, Office 365, custom apps |

**SSO protocols:**

| Protocol | Purpose | Key detail |
|---|---|---|
| **SAML** | Enterprise SSO | XML-based; browser-based SSO; most common in corporate environments |
| **OAuth 2.0** | Authorization delegation | Grants app access to resources on user's behalf ("Allow X to access your Drive") |
| **OpenID Connect (OIDC)** | Authentication layer on OAuth 2.0 | Returns an ID token; modern SSO protocol |

**SAML SSO flow:**
1. User accesses a Service Provider (e.g., Salesforce)
2. SP redirects user to IdP for authentication
3. User authenticates at IdP (credentials + MFA)
4. IdP sends a signed SAML assertion back to SP
5. SP validates the assertion and grants access — no separate login required

> **Exam tip:** **SAML = enterprise SSO (XML)**; **OAuth = authorization, not authentication**; **OIDC = authentication built on OAuth**. SSO's main risk is that the IdP becomes a single point of failure — compromise the IdP and all connected apps are exposed. Mitigate with strong IdP security and mandatory MFA.

---

### Federation

Federation extends SSO across organizational boundaries — allowing users from one organization to access resources in another without creating duplicate accounts.

**Use case:** Company A (partner) employees need access to Company B's project portal. Federation lets Company B trust Company A's IdP; Company A users authenticate with their own credentials.

| Concept | Description |
|---|---|
| **Trust relationship** | Established via metadata exchange between organizations' IdPs |
| **Home organization** | Where the user's account lives and authentication happens |
| **Resource organization** | Where the resource being accessed is hosted |
| **Shibboleth** | Federation protocol common in academic and research institutions |

> **Exam tip:** Federation = SSO across organizations. The key benefit is that neither organization needs to manage accounts for the other's users — each manages its own identity store.

---

### Key distinctions to know for the exam

| Comparison | Distinction |
|---|---|
| **Provisioning vs. deprovisioning** | Provisioning creates and grants access (onboarding); deprovisioning disables and revokes access (offboarding) |
| **Authentication vs. authorization** | Authentication verifies identity ("who are you?"); authorization verifies permissions ("what can you access?") |
| **MFA vs. 2FA** | 2FA is specifically two factors; MFA is two or more — 2FA is a subset of MFA |
| **SSO vs. federation** | SSO = single login for multiple apps within one organization; federation = cross-organization SSO |
| **PAM vs. IAM** | IAM covers all users; PAM specifically focuses on privileged accounts (admins, service accounts) |
| **Least privilege vs. separation of duties** | Least privilege limits what any one account can do; SoD requires multiple people for critical processes |
| **Disable vs. delete (offboarding)** | Disable immediately upon termination; delete only after the retention period for data/forensic purposes |
| **Privilege creep vs. least privilege** | Privilege creep is the *problem* (accumulating excess access); least privilege is the *principle* that prevents it |

---

### Common exam traps

**Trap: Thinking password + security question = MFA.**
Reality: Both are knowledge factors ("something you know"). MFA requires factors from *different* categories — a second password is not a second factor.

**Trap: Assuming SSO weakens security.**
Reality: SSO centralizes authentication, which enables consistent MFA enforcement, better monitoring, and fewer passwords (fewer phishing targets). Properly implemented, SSO improves security.

**Trap: Believing deprovisioning means deleting the account immediately.**
Reality: The account should be **disabled** immediately, but kept (not deleted) for the data retention period (30–90 days) to support forensic investigations and data transfer.

**Trap: Treating least privilege as "no access."**
Reality: Least privilege means the *minimum* access necessary to perform the job function — not zero access, not convenient access.

**Trap: Assuming all MFA methods are equally secure.**
Reality: Security varies significantly — hardware tokens (FIDO2) are phishing-resistant and the strongest; SMS codes are weakest and vulnerable to SIM swapping.

---

### Exam tips

1. **Two knowledge factors** (password + security question) **= NOT MFA** — need different factor types.
2. **Deprovisioning = immediately disable**, not delete — keep for retention period.
3. **Least privilege = minimum necessary access**, not zero access.
4. **Privilege creep = accumulating excess permissions** through role changes never cleaned up.
5. **PAM = privileged accounts** → password vaulting, session recording, JIT access.
6. **JIT access = temporary elevated rights** granted on demand, auto-revoked after the window.
7. **SSO = authenticate once**, access many apps; **SAML = the XML enterprise protocol**.
8. **Federation = cross-organization SSO** — trust between two organizations' identity systems.
9. **Separation of duties prevents fraud** — no single person controls an entire critical process.
10. **MFA fatigue** = a push notification weakness where users approve requests without reading them.

---

## Key terms

- **Provisioning** — Creating and assigning access rights to a user account during onboarding.
- **Deprovisioning** — Disabling or deleting a user account and revoking all associated access upon offboarding.
- **Privilege creep** — The gradual accumulation of access rights beyond what a user's role requires, typically through unreviewed role changes.
- **Least privilege** — The principle of granting only the minimum permissions necessary for a user or process to perform its function.
- **Separation of duties (SoD)** — Requiring multiple individuals to complete a critical process, preventing any single person from committing fraud alone.
- **PAM (Privileged Access Management)** — Tools and processes for managing, monitoring, and securing privileged accounts (admins, service accounts).
- **Password vaulting** — Storing privileged credentials in an encrypted vault; users check out credentials rather than knowing them permanently.
- **JIT (Just-in-Time) access** — Granting elevated privileges on demand for a defined time window, then automatically revoking them.
- **MFA (Multi-Factor Authentication)** — Requiring two or more authentication factors from different categories (knowledge, possession, inherence, location, behavior).
- **MFA fatigue** — An attack or usability failure where users habitually approve push notification MFA requests without verifying them.
- **TOTP (Time-based One-Time Password)** — A rotating code generated by an authenticator app, valid for ~30 seconds.
- **FIDO2 / WebAuthn** — A phishing-resistant hardware token standard using cryptographic challenge-response; the strongest MFA method.
- **SSO (Single Sign-On)** — Authenticating once to gain access to multiple applications without re-entering credentials.
- **IdP (Identity Provider)** — The central authentication service that manages user identities and issues tokens/assertions (e.g., Azure AD, Okta).
- **SP (Service Provider)** — An application that trusts and relies on an IdP's authentication decision.
- **SAML** — XML-based protocol for enterprise SSO; the most common enterprise federation standard.
- **OAuth 2.0** — An authorization delegation framework; grants applications access to resources on a user's behalf (not an authentication protocol).
- **OpenID Connect (OIDC)** — An authentication layer built on top of OAuth 2.0; returns an ID token confirming user identity.
- **Federation** — A trust relationship between two organizations' identity systems enabling cross-organization SSO.
- **Access recertification** — A periodic review process where managers confirm that users still require their assigned permissions.

---

## Examples / scenarios

**Scenario 1:** An employee transfers from the Finance department to Marketing. Three months later, an audit reveals the employee still has full access to the accounts payable system and payroll reports.
- **Answer:** Privilege creep. Role change access was added but old Finance access was never removed. Prevention: immediate access review on any role change, automated deprovisioning of old role permissions.

**Scenario 2:** A company's IT policy requires administrators to use a hardware YubiKey when accessing production servers. An auditor asks why the company chose hardware tokens over SMS codes for this purpose.
- **Answer:** Hardware tokens (FIDO2/WebAuthn) are phishing-resistant and the strongest MFA method. SMS codes are vulnerable to SIM swapping and interception — unacceptable for privileged access.

**Scenario 3:** A sysadmin is terminated involuntarily. HR plans to notify the employee at 5 PM on Friday and asks IT to disable accounts "sometime over the weekend."
- **Answer:** Accounts must be disabled **immediately** — before or simultaneously with notification — to prevent data exfiltration, sabotage, or unauthorized access during the gap.

**Scenario 4:** A university allows students to access a partner company's internship portal using their university credentials. The company does not create separate accounts for interns.
- **Answer:** Federation. The company trusts the university's IdP; interns authenticate with university credentials. Neither organization manages accounts for the other.

**Scenario 5:** A financial services firm uses a PAM solution where administrators must request production database credentials, use them within a two-hour window, and the password is automatically rotated after check-in.
- **Answer:** This describes **password vaulting** combined with **JIT access** — two core PAM capabilities that eliminate standing privileges and ensure credentials are never reused.

---

## Mini quiz

<details>
<summary><strong>Question 1:</strong> A user is assigned to a new team but keeps all their previous project access. Six months later they have access to five different systems they no longer need. What is this called, and what principle does it violate?</summary>

**Answer:** This is **privilege creep** — the gradual accumulation of excess permissions through role changes that are never cleaned up. It violates the **principle of least privilege**, which requires that users hold only the minimum access necessary for their current role.
</details>

<details>
<summary><strong>Question 2:</strong> An employee logs into their corporate IdP once in the morning and then accesses email, CRM, and HR systems throughout the day without re-authenticating. What is this capability called, and which protocol is most commonly used in enterprise environments to implement it?</summary>

**Answer:** This is **Single Sign-On (SSO)**. In enterprise environments, **SAML** (Security Assertion Markup Language) is the most commonly used protocol — the IdP issues a signed XML assertion after authentication, which Service Providers accept without requiring a separate login.
</details>

<details>
<summary><strong>Question 3:</strong> Why is a password combined with a security question NOT considered MFA?</summary>

**Answer:** MFA requires factors from **different categories**. A password and a security question are both "something you know" (knowledge factors). True MFA combines factors from at least two different categories — e.g., knowledge + possession (password + hardware token).
</details>

<details>
<summary><strong>Question 4:</strong> A company implements a PAM solution that records every command an administrator types during a privileged session. What two security goals does this primarily serve?</summary>

**Answer:** **Accountability** (creates an audit trail attributing every action to a specific admin) and **deterrence** (admins who know sessions are recorded are less likely to abuse access). Session recordings also support forensic investigations if suspicious activity is detected.
</details>

<details>
<summary><strong>Question 5:</strong> What is MFA fatigue and which MFA method is specifically vulnerable to it?</summary>

**Answer:** MFA fatigue occurs when attackers repeatedly send **push notification** MFA requests, hoping the user will eventually tap "Approve" out of frustration or habit — without verifying the request is legitimate. This is unique to push-based MFA; TOTP codes and hardware tokens are not vulnerable to this attack.
</details>

### CompTIA-style practice questions

<details>
<summary><strong>Question 6:</strong> A security administrator is reviewing access logs and finds that a developer has read access to the production customer database, write access to the billing system, and admin rights to the source code repository — all from different projects over the past two years. Which term BEST describes this situation?<br>A. Separation of duties violation<br>B. Privilege creep<br>C. Federated identity misuse<br>D. Insider threat</summary>

**Correct Answer: B. Privilege creep**

The developer accumulated access across multiple projects over time, and none of it was removed when the projects ended. This is privilege creep — excess permissions building up through unreviewed role and project changes.

- A: Separation of duties means no single person controls an entire critical process; the scenario describes accumulated access, not control of a complete process.
- C: Federated identity relates to cross-organization SSO trust; not applicable here.
- D: Insider threat describes malicious use of access; the scenario doesn't indicate intent — this is an access management failure.
</details>

<details>
<summary><strong>Question 7:</strong> A company wants to allow employees of its acquisition to access internal HR and benefits systems without creating new accounts in the parent company's Active Directory. Which solution BEST meets this requirement?<br>A. Provisioning new accounts for all acquisition employees in the parent company's AD<br>B. Requiring acquisition employees to use VPN before accessing any internal systems<br>C. Establishing a federation trust between the two organizations' identity providers<br>D. Implementing SSO using TOTP-based authentication for all users</summary>

**Correct Answer: C. Establishing a federation trust between the two organizations' identity providers**

Federation allows the parent company to trust the acquisition's IdP, enabling employees to authenticate with their existing credentials — no duplicate accounts required.

- A: Creating new accounts is exactly what federation avoids; it also creates an ongoing management burden.
- B: VPN controls network access but doesn't solve the identity/account problem.
- D: TOTP is an MFA method; SSO alone doesn't solve cross-organization identity management.
</details>

<details>
<summary><strong>Question 8:</strong> During a security review, an auditor recommends that the company require database administrators to request credentials from a secure vault, use them within a defined window, and have the password automatically rotated after use. Which PAM capability does this describe?<br>A. Session recording<br>B. Just-in-Time access combined with password vaulting<br>C. Role-based access control<br>D. Biometric authentication for privileged accounts</summary>

**Correct Answer: B. Just-in-Time access combined with password vaulting**

The workflow described — request → time-limited use → automatic rotation — is the combination of JIT access (temporary grant) and password vaulting (credential never permanently known, rotated after use). Together they eliminate standing privileges.

- A: Session recording captures what admins do during a session; it doesn't manage credential issuance or rotation.
- C: RBAC assigns permissions based on roles; it doesn't describe a credential checkout/rotation workflow.
- D: Biometrics are an MFA factor; the scenario is specifically about privileged credential management.
</details>

---

## Related objectives

- [**4.6**]({{ '/secplus/objectives/4-6/' | relative_url }}) — IAM implementation details (directory services, identity federation, PAM tools in practice) extend the concepts introduced here.
- [**4.7**]({{ '/secplus/objectives/4-7/' | relative_url }}) — Automation and orchestration enable automated provisioning/deprovisioning workflows tied to HR systems.
- [**2.2**]({{ '/secplus/objectives/2-2/' | relative_url }}) — Improperly managed identities (default credentials, overprivileged accounts) are a primary threat vector.
- [**1.2**]({{ '/secplus/objectives/1-2/' | relative_url }}) — Security controls framework — least privilege and separation of duties are foundational administrative controls.

---

## Navigation

**Domain 4.0: Security Operations**

| Objective | Title | Status |
|---|---|---|
| [4.1]({{ '/secplus/objectives/4-1/' | relative_url }}) | Given a scenario, apply common security techniques to computing resources. | done |
| [4.2]({{ '/secplus/objectives/4-2/' | relative_url }}) | Explain the security implications of proper hardware, software, and data asset management. | done |
| [4.3]({{ '/secplus/objectives/4-3/' | relative_url }}) | Explain various activities associated with vulnerability management. | done |
| [4.4]({{ '/secplus/objectives/4-4/' | relative_url }}) | Explain security alerting and monitoring concepts and tools. | done |
| **4.5** | Given a scenario, modify enterprise capabilities to enhance security. (current) | done |
| [4.6]({{ '/secplus/objectives/4-6/' | relative_url }}) | Given a scenario, implement and maintain identity and access management. | done |
| [4.7]({{ '/secplus/objectives/4-7/' | relative_url }}) | Explain the importance of automation and orchestration related to secure operations. | done |
| [4.8]({{ '/secplus/objectives/4-8/' | relative_url }}) | Explain appropriate incident response activities. | done |
| [4.9]({{ '/secplus/objectives/4-9/' | relative_url }}) | Given a scenario, use data sources to support an investigation. | done |

[← Previous: Objective 4.4]({{ '/secplus/objectives/4-4/' | relative_url }}) | [Back to Dashboard]({{ '/secplus/' | relative_url }}) | [Next: Objective 4.6 →]({{ '/secplus/objectives/4-6/' | relative_url }})
