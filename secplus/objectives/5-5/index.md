---
layout: objective
title: "5.5 Types of Policies"
objective_id: "5.5"
domain: "5.0 Security Program Management and Oversight"
status: "done"
tags: ["policies", "procedures", "standards", "guidelines"]
permalink: /objectives/5-5/
---

## Overview

Security policies provide the framework for an organization's security program. This includes various policy types, standards, procedures, and guidelines that guide security decisions and actions.

---

## Policy Hierarchy

**Hierarchy (top to bottom):**

### 1. Policies
- **Level:** High-level, strategic
- **Defines:** WHAT must be done
- **Example:** "All systems must use encryption for sensitive data"
- **Audience:** Entire organization
- **Approval:** Executive management, board
- **Frequency:** Review annually, update as needed

### 2. Standards
- **Level:** Mid-level, tactical
- **Defines:** HOW policy will be implemented (specific requirements)
- **Example:** "Use AES-256 encryption for data at rest"
- **Audience:** IT staff, administrators
- **Approval:** CISO, IT management
- **Frequency:** Review semi-annually

### 3. Procedures
- **Level:** Detailed, operational
- **Defines:** Step-by-step instructions
- **Example:** "Step 1: Open BitLocker control panel, Step 2: Select drive..."
- **Audience:** Specific roles (admins, users)
- **Approval:** Department managers
- **Frequency:** Update as technology changes

### 4. Guidelines
- **Level:** Recommendations (not mandatory)
- **Defines:** Best practices, suggestions
- **Example:** "Consider using a password manager for convenience"
- **Compliance:** Optional (encouraged but not required)

**Example hierarchy:**
```
Policy: "Protect confidential data"
  ↓
Standard: "Encrypt all laptops with BitLocker or FileVault"
  ↓
Procedure: "How to enable BitLocker on Windows 10"
  ↓
Guideline: "Consider disabling sleep mode during encryption"
```

---

## Common Security Policies

**Acceptable Use Policy (AUP):**
- **Purpose:** Define acceptable use of company resources
- **Covers:**
  - Internet usage (no personal shopping during work hours)
  - Email usage (no sending confidential data to personal email)
  - Software installation (only approved software)
  - Device usage (no jailbreaking company phones)
- **Consequences:** Disciplinary action for violations
- **User requirement:** Sign acknowledgement annually

**Data Classification Policy:**
- **Purpose:** Define data sensitivity levels and handling requirements
- **Classification levels:**
  - **Public:** No harm if disclosed (marketing materials)
  - **Internal:** Low harm if disclosed (employee directory)
  - **Confidential:** Moderate harm (internal strategies)
  - **Restricted/Sensitive:** High harm (customer PII, trade secrets)
- **Requirements per level:**
  ```
  Public: No special controls
  Internal: Access control (employees only)
  Confidential: Encryption, access logging
  Restricted: Encryption, MFA, DLP, audit trail
  ```

**Password Policy:**
- **Requirements:**
  - Minimum length (12-16 characters)
  - Complexity (uppercase, lowercase, numbers, symbols)
  - Expiration (90 days, or no expiration if using MFA)
  - History (can't reuse last 5 passwords)
  - Account lockout (5 failed attempts = 30 min lockout)
- **Exceptions:** Service accounts (longer, complex, stored in vault)

**Information Security Policy:**
- **Purpose:** Overarching security policy (umbrella policy)
- **Covers:**
  - Security program goals
  - Roles and responsibilities
  - Compliance requirements
  - Incident response
  - Risk management
- **Scope:** All employees, contractors, partners

**Bring Your Own Device (BYOD) Policy:**
- **Purpose:** Govern use of personal devices for work
- **Requirements:**
  - MDM enrollment mandatory
  - Device encryption
  - Screen lock (PIN/biometric)
  - Prohibited: Jailbroken/rooted devices
  - Company rights: Remote wipe if device lost/stolen
- **User consent:** Agree to monitoring, wipe capability

**Remote Access Policy:**
- **Purpose:** Secure remote connections
- **Requirements:**
  - VPN required for remote access
  - MFA for VPN authentication
  - Approved devices only (managed endpoints)
  - Prohibited: Public Wi-Fi without VPN
  - Logging: All remote sessions logged

**Incident Response Policy:**
- **Purpose:** Define incident handling procedures
- **Defines:**
  - What constitutes an incident
  - Reporting procedures (who to contact, how quickly)
  - Response team roles
  - Communication protocols
  - Escalation criteria

**Business Continuity Policy:**
- **Purpose:** Ensure business operations continue during disruption
- **Defines:**
  - Critical business functions
  - Recovery objectives (RTO, RPO)
  - Backup requirements
  - Disaster recovery procedures
  - Testing frequency (annual)

**Disaster Recovery Policy:**
- **Purpose:** Restore IT systems after disaster
- **Defines:**
  - Recovery priorities (which systems first)
  - Backup locations (on-site, off-site, cloud)
  - Recovery procedures
  - Alternate site plans (hot, warm, cold)

**Software Development Lifecycle (SDLC) Policy:**
- **Purpose:** Secure software development
- **Requirements:**
  - Security requirements phase (threat modeling)
  - Code review (peer review before merge)
  - Security testing (SAST, DAST)
  - Change management (approval before production)

**Change Management Policy:**
- **Purpose:** Control system modifications
- **Defines:**
  - Change approval process
  - Testing requirements (dev → staging → production)
  - Rollback procedures
  - Emergency change process
  - Documentation requirements

---

## User Behavior and Training

**Security Awareness Policy:**
- **Purpose:** Ensure users understand security responsibilities
- **Requirements:**
  - Annual security awareness training (mandatory)
  - Phishing simulation (quarterly)
  - New hire orientation (security basics)
  - Role-specific training (developers, admins)
- **Topics:**
  - Password security
  - Phishing recognition
  - Social engineering
  - Physical security
  - Incident reporting

**Clean Desk Policy:**
- **Purpose:** Prevent unauthorized information access
- **Requirements:**
  - Lock computer when away (Windows+L)
  - Secure documents in locked drawer overnight
  - Shred confidential papers (don't trash)
  - No passwords on sticky notes
  - Visitor area restrictions

**Onboarding/Offboarding Policy:**

**Onboarding:**
```
Day 1:
- Sign acceptable use policy
- Security awareness training
- Issue credentials (username, password)
- Provision accounts (email, systems access)
- Issue equipment (laptop, phone)
- Badge access (building entry)
```

**Offboarding:**
```
Termination day:
- Disable accounts immediately
- Revoke access (VPN, badges, systems)
- Retrieve equipment (laptop, phone, badge)
- Transfer data ownership (email, files to manager)
- Exit interview (return of property confirmation)

30 days post-termination:
- Delete accounts (after retention period)
```

**Code of Conduct/Ethics Policy:**
- **Purpose:** Define expected professional behavior
- **Covers:**
  - Conflicts of interest (disclosure requirements)
  - Gifts and entertainment (limits)
  - Confidentiality (protect company/customer data)
  - Harassment (zero tolerance)
  - Reporting violations (whistleblower protection)

---

## Credential and Account Management

**Credential Management Policy:**

**Password requirements:**
- Length, complexity, expiration (covered in Password Policy)
- Storage: Password manager or vault (not plain text)
- Transmission: Encrypted channels only (no email/SMS)
- Sharing: Prohibited (except via secure vault)

**Account types:**

**User accounts:**
- Standard privileges (least privilege)
- Unique per person (no shared accounts)
- Named accounts (john.doe, not user1)

**Service accounts:**
- Application/service use (not human login)
- Long, complex passwords
- Stored in password vault
- No expiration (breaks services)
- Documented ownership (who manages)

**Privileged/Admin accounts:**
- Separate from user accounts (john.doe-admin)
- Used only when needed (not daily use)
- MFA required
- Session recording
- Regular access reviews

**Guest accounts:**
- Limited access (specific resources only)
- Time-limited (auto-expire after period)
- Sponsored (employee vouches for guest)
- Monitoring (enhanced logging)

**Shared accounts:**
- Discouraged (prefer unique accounts)
- If necessary: Vault for password, audit logging
- Example: Local admin account (for break-glass emergency)

**Account lifecycle:**
```
Creation:
- Manager request (approval workflow)
- Provisioning (IT creates account)
- Notification (user receives credentials)

Maintenance:
- Access reviews (quarterly for privileged, annually for standard)
- Password changes (if no MFA: 90 days)
- Role changes (update access when user changes roles)

Termination:
- Immediate disable (when employment ends)
- Data transfer (to manager)
- Deletion (after retention period, 30-90 days)
```

---

## Organizational Policies

**Data Retention Policy:**
- **Purpose:** Define how long data kept
- **Legal requirements:**
  - Email: 7 years (SOX for public companies)
  - Medical records: 6 years (HIPAA)
  - Tax records: 7 years (IRS)
- **Security consideration:** Less data = less breach risk
- **Balance:** Legal retention vs minimization

**Data Destruction Policy:**
- **Purpose:** Secure data disposal
- **Methods:** (covered in 4.2 Asset Management)
  - Overwriting (HDDs)
  - Degaussing (magnetic media)
  - Physical destruction (shredding)
  - Cryptographic erasure (delete key)
- **Requirements:**
  - Certificate of destruction
  - Asset decommissioning tracking

**Separation of Duties Policy:**
- **Purpose:** No single person controls entire critical process
- **Examples:**
  - Person who approves invoice ≠ person who pays
  - Code developer ≠ code approver
  - Backup administrator ≠ restore requester
- **Implementation:** Role-based access control (RBAC)

**Job Rotation Policy:**
- **Purpose:** Detect fraud, reduce insider threat
- **Method:** Employees rotate roles periodically
- **Benefit:** Multiple people know each process, fraud harder to hide
- **Frequency:** Annually or semi-annually

**Mandatory Vacation Policy:**
- **Purpose:** Detect fraud (requires someone else to handle duties)
- **Requirement:** Minimum consecutive days (e.g., 5 days)
- **Financial sector:** Common in banks (detect embezzlement)

**Least Privilege Policy:**
- **Principle:** Users have minimum access needed
- **Implementation:**
  - Role-based access control
  - Regular access reviews
  - Remove access when no longer needed
- **Reduces:** Insider threat, lateral movement

**Background Check Policy:**
- **Purpose:** Verify employee trustworthiness
- **Checks:**
  - Criminal background (felony convictions)
  - Employment verification (past jobs)
  - Education verification (degree claims)
  - Credit check (financial sector, positions with monetary access)
- **Timing:** Before hire, periodic re-checks for sensitive roles

**Non-Disclosure Agreement (NDA):**
- **Purpose:** Protect confidential information
- **Signed:** Before employee accesses sensitive data
- **Covers:** Trade secrets, customer data, internal strategies
- **Duration:** Often survives employment (5 years post-termination)

**Social Media Policy:**
- **Purpose:** Govern employee social media use
- **Covers:**
  - Prohibited: Posting confidential company info
  - Prohibited: Disparaging company/customers
  - Disclosure: Identify as employee if posting about company
  - Personal: Personal views don't represent company
- **Balance:** Free speech vs company protection

---

## Key Distinctions

**Policy vs Standard:**
- Policy: What must be done (high-level)
- Standard: How it's done (specific requirements)

**Standard vs Procedure:**
- Standard: Requirements (AES-256 encryption)
- Procedure: Step-by-step (how to enable AES-256)

**Guideline vs Policy:**
- Guideline: Recommended (optional)
- Policy: Required (mandatory)

**AUP vs Code of Conduct:**
- AUP: Technology resource usage
- Code of Conduct: Professional behavior/ethics

**Onboarding vs Offboarding:**
- Onboarding: Grant access when hired
- Offboarding: Revoke access when terminated

---

## Common Exam Traps

1. **Trap:** Thinking policies and procedures are the same
   - **Reality:** Policy = what, procedure = how (step-by-step)

2. **Trap:** Believing guidelines are mandatory
   - **Reality:** Guidelines are recommendations (not required)

3. **Trap:** Assuming all accounts need password expiration
   - **Reality:** Service accounts often no expiration (breaks automation)

4. **Trap:** Thinking shared accounts are never allowed
   - **Reality:** Sometimes necessary (with enhanced monitoring)

5. **Trap:** Believing data retention is always "longer is better"
   - **Reality:** Balance legal requirements with minimization (less data = less risk)

---

## Exam Tips

1. **Policy hierarchy:** Policy → Standard → Procedure → Guideline
2. **AUP defines** acceptable use of company resources
3. **Password policy** includes length, complexity, expiration, history
4. **Clean desk policy** requires locking screens, securing documents
5. **Offboarding** = immediate account disable, delayed deletion
6. **Service accounts** = long passwords, no expiration, vault storage
7. **Separation of duties** prevents single person controlling critical process
8. **Mandatory vacation** detects fraud (someone else handles duties)
9. **Least privilege** = minimum access needed
10. **Guidelines are optional**, policies are mandatory

---

## Quick Navigation
- [← Previous: 5.4 Compliance & Audit](../5-4/)
- [→ Next: 5.6 Security Awareness](../5-6/)
- [↑ Back to Domain 5](../)
