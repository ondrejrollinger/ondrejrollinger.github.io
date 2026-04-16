---
layout: objective
title: "4.5 Identity and Access Management"
objective_id: "4.5"
domain: "4.0 Security Operations"
status: "done"
tags: ["IAM", "authentication", "authorization", "privileged-access"]
permalink: /objectives/4-5/
---

## Overview

Identity and Access Management (IAM) ensures the right users have appropriate access to resources. This includes provisioning/deprovisioning accounts, managing privileged access, and implementing least privilege principles.

---

## Provisioning and Deprovisioning

**User lifecycle:**

**On boarding (provisioning):**
1. HR creates employee record
2. IT creates user account (Active Directory, cloud IAM)
3. Assign to groups (determines access)
4. Provision email, apps, file shares
5. Issue credentials (temporary password, require change)
6. Training (acceptable use policy, security awareness)

**Role changes:**
- Promotion: Add new access (but remove old if no longer needed)
- Lateral move: Different department = different access requirements
- **Key principle:** Review and remove unnecessary access (privilege creep prevention)

**Off-boarding (deprovisioning):**
1. HR initiates termination process
2. IT disables account immediately (before employee notified if involuntary)
3. Revoke access badges, VPN, remote access
4. Transfer data ownership (email, files to manager)
5. Delete account after retention period (30-90 days)
6. Retrieve company property (laptop, phone, access cards)

**Automated provisioning:**
- **Identity Provider (IdP):** Centralized user directory (Azure AD, Okta)
- **Integration:** HR system → IdP → Applications
- **Just-in-Time (JIT) provisioning:** Account created when user first accesses app
- **Benefits:** Faster onboarding, consistent access, reduced errors

**Deprovisioning best practices:**
- **Immediate disable:** Don't delay (security risk)
- **Automated:** Trigger from HR system (termination date)
- **Checklist:** Ensure all access revoked (account, VPN, badges, apps)
- **Delayed deletion:** Keep account disabled but not deleted (data retention, investigations)

---

## Permission Auditing and Recertification

**Access reviews:**

**Purpose:** Validate users still need their assigned permissions

**Frequency:**
- **High-privilege accounts:** Quarterly
- **Standard accounts:** Annually  
- **After role changes:** Immediately

**Process:**
1. Generate access report (who has access to what)
2. Send to managers for review
3. Managers certify (approve or revoke)
4. IT implements changes (remove uncertified access)
5. Document review (compliance evidence)

**Privilege creep:**
- **Definition:** Accumulating permissions over time
- **Cause:** Role changes, project assignments, never removing old access
- **Risk:** Excessive permissions violate least privilege
- **Prevention:** Regular access reviews, automated deprovisioning

**Separation of duties:**
- **Definition:** No single person controls entire critical process
- **Example:** Person who approves invoice ≠ person who pays invoice
- **Implementation:** Mutually exclusive roles in IAM system
- **Purpose:** Prevent fraud, reduce insider threat

---

## Privileged Access Management (PAM)

**Privileged accounts:**
- Administrator/root accounts
- Service accounts (run applications with elevated rights)
- Emergency accounts (break-glass for disaster recovery)

**PAM solutions:**

**Privileged Account Management:**
- **Password vaulting:** Store privileged passwords in secure vault
- **Check-out/check-in:** Admin requests password, uses, returns
- **Automatic rotation:** Password changes after each use
- **Examples:** CyberArk, BeyondTrust, Thycotic

**Privileged Session Management:**
- **Session recording:** Record all admin actions (video/keystroke logging)
- **Real-time monitoring:** Watch privileged sessions live
- **Alerting:** Suspicious commands trigger alerts
- **Purpose:** Accountability, audit trail, detect abuse

**Just-in-Time (JIT) Access:**
- **Concept:** Grant admin rights only when needed, for limited time
- **Example:** Developer requests production access for 2 hours to troubleshoot
- **Benefits:** Reduces standing privileges (smaller attack surface)
- **Implementation:** Automated workflow approves, grants, revokes

**Least privilege:**
- **Definition:** Minimum permissions necessary to perform job
- **Application:** Users, processes, applications
- **Implementation:**
  - Start with no access, add as needed (deny by default)
  - Regular reviews to remove excess
  - Time-limited elevated access (JIT)

---

## Multi-Factor Authentication (MFA)

**Authentication factors:**
- **Something you know:** Password, PIN
- **Something you have:** Smart card, phone, hardware token
- **Something you are:** Biometric (fingerprint, face, iris)
- **Somewhere you are:** Location (GPS, network)
- **Something you do:** Behavioral (typing pattern, gait)

**MFA = Two or more DIFFERENT factors**
- Password + security questions = NOT MFA (both knowledge factors)
- Password + SMS code = MFA (knowledge + possession)
- Password + fingerprint = MFA (knowledge + biometric)

**MFA methods:**

**SMS/Email codes:**
- **Pro:** Easy to implement, users familiar
- **Con:** Vulnerable to interception (SIM swap, man-in-the-middle)
- **Use:** Better than password-only, but not strongest

**Authenticator apps (TOTP):**
- **Examples:** Google Authenticator, Microsoft Authenticator, Authy
- **Method:** Time-based one-time password (changes every 30 seconds)
- **Pro:** Not interceptable (code generated locally)
- **Con:** Requires app installation

**Hardware tokens:**
- **Examples:** YubiKey, RSA SecurID
- **Types:**
  - **FIDO2/WebAuthn:** Cryptographic challenge-response
  - **TOTP generator:** Displays rotating codes
- **Pro:** Most secure (physical device required)
- **Con:** Cost, can be lost

**Push notifications:**
- **Method:** App sends approval request to registered device
- **User:** Taps "Approve" or "Deny"
- **Pro:** User-friendly, fast
- **Con:** Users may approve without reading (MFA fatigue)

**Biometric:**
- **Types:** Fingerprint, facial recognition, iris scan
- **Pro:** Convenient (can't forget or lose)
- **Con:** Can't change if compromised, false accept/reject rates

**Where to require MFA:**
- VPN access (remote users)
- Privileged accounts (administrators)
- Cloud applications (email, file storage)
- Financial systems
- After suspicious activity (impossible travel detected)

**MFA bypass/fallback:**
- **Backup codes:** One-time use codes if primary MFA unavailable
- **Admin reset:** Helpdesk can reset MFA (requires identity verification)
- **Hardware token:** Backup to software token

---

## Single Sign-On (SSO)

**Definition:** Authenticate once, access multiple applications

**Components:**

**Identity Provider (IdP):**
- Central authentication service
- Examples: Azure AD, Okta, Auth0
- Stores user credentials and attributes

**Service Provider (SP):**
- Application relying on IdP for authentication
- Examples: Salesforce, Office 365, custom apps
- Trusts IdP's authentication decision

**SSO protocols:**

**SAML (Security Assertion Markup Language):**
- XML-based standard
- Enterprise SSO (common in corporations)
- Web browser SSO

**OAuth 2.0:**
- Authorization framework (not authentication)
- Delegates access ("Allow app X to access your Google Drive")
- Used by Google, Facebook, GitHub

**OpenID Connect (OIDC):**
- Authentication layer on top of OAuth 2.0
- Modern SSO protocol
- Returns ID token (user identity)

**SSO flow example (SAML):**
1. User accesses application (Service Provider)
2. SP redirects to IdP for authentication
3. User logs in at IdP (username + password + MFA)
4. IdP sends SAML assertion back to SP
5. SP validates assertion, grants access
6. User accesses application without re-authenticating

**SSO benefits:**
- **User experience:** Single login for all apps
- **Security:** Centralized credential management, MFA enforcement
- **Productivity:** Fewer password resets

**SSO risks:**
- **Single point of failure:** Compromise IdP = access to all apps
- **Mitigation:** Strong IdP security, MFA, conditional access

---

## Federation

**Definition:** Trust relationship between organizations for authentication

**Use case:** Partner companies share resources without creating separate accounts

**Example:**
- Company A trusts Company B's IdP
- Company B employees access Company A's resources
- Company A doesn't create accounts for Company B users
- Authentication handled by Company B's IdP

**Federation protocols:**
- **SAML:** Enterprise federation
- **OAuth/OIDC:** Modern federation
- **Shibboleth:** Academic/research institutions

**Federated identity management:**
- Each organization manages own users
- Trust established through metadata exchange
- Cross-organization SSO

---

## Key Distinctions

**Provisioning vs Deprovisioning:**
- Provisioning: Create account, assign access (on-boarding)
- Deprovisioning: Disable/delete account, revoke access (off-boarding)

**Authentication vs Authorization:**
- Authentication: Verify identity (who are you?)
- Authorization: Verify permissions (what can you access?)

**MFA vs 2FA:**
- 2FA: Two factors specifically (subset of MFA)
- MFA: Two or more factors

**SSO vs Federation:**
- SSO: Single login for multiple apps (same organization)
- Federation: Trust between organizations (cross-organization SSO)

**PAM vs IAM:**
- IAM: General identity/access management (all users)
- PAM: Specifically for privileged accounts (admins)

---

## Common Exam Traps

1. **Trap:** Thinking password + security question = MFA
   - **Reality:** Both knowledge factors, not MFA (need different factor types)

2. **Trap:** Believing SSO reduces security
   - **Reality:** SSO can improve security (centralized MFA, better monitoring)

3. **Trap:** Assuming deprovisioning means immediate account deletion
   - **Reality:** Disable immediately, delete after retention period

4. **Trap:** Thinking least privilege means no access
   - **Reality:** Minimum access needed, not zero access

5. **Trap:** Believing all MFA methods equally secure
   - **Reality:** Hardware tokens > Authenticator apps > SMS

---

## Exam Tips

1. **MFA requires different factor types** (password + password ≠ MFA)
2. **Deprovisioning = immediate disable** (don't wait for employee's last day)
3. **Least privilege = minimum necessary access** (not zero access)
4. **Privilege creep = accumulating excess permissions over time**
5. **PAM manages privileged accounts** (password vaulting, session recording)
6. **SSO = authenticate once**, access multiple apps
7. **SAML = enterprise SSO protocol** (XML-based)
8. **Federation = trust between organizations**
9. **JIT = Just-in-Time access** (temporary elevated privileges)
10. **Separation of duties prevents fraud** (no single person controls entire process)

---

## Quick Navigation
- [← Previous: 4.4 Alerting & Monitoring](../4-4/)
- [→ Next: 4.6 Resilience and Recovery](../4-6/)
- [↑ Back to Domain 4](../)
