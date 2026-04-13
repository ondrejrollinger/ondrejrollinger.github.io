---
layout: objective
title: "4.6 Identity and Access Management"
objective_id: "4.6"
domain: "4.0 Security Operations"
status: "done"
tags:
  - secplus701
permalink: /objectives/4-4/
---

## Overview

Identity and Access Management (IAM) ensures the right individuals have access to the right resources at the right times for the right reasons. This objective covers the complete user lifecycle from provisioning through deprovisioning, authentication methods including Single Sign-On (SSO) and Multi-Factor Authentication (MFA), access control models that determine permissions, and privileged access management for administrative accounts.

Effective IAM is foundational to security - it prevents unauthorized access, enables accountability through auditing, and supports compliance with regulatory requirements. Understanding IAM concepts and implementation is essential for the Security+ exam and securing modern enterprises.

---

## Provisioning and Deprovisioning

### Provisioning

**Definition:** Process of creating user accounts and granting initial access to systems and resources.

**Provisioning workflow:**
1. **Request:** User submits access request or HR initiates for new employee
2. **Approval:** Manager approves access based on job role
3. **Account creation:** IT creates accounts in relevant systems (AD, email, applications)
4. **Access assignment:** Grant permissions based on role/job function
5. **Notification:** User receives credentials and access instructions
6. **Documentation:** Record what access was granted and why

**Automated vs Manual Provisioning:**

**Manual provisioning:**
- IT staff manually creates each account
- **Disadvantages:** Slow (days/weeks), error-prone, inconsistent, doesn't scale
- **Use case:** Small organizations (<50 users), one-off special access

**Automated provisioning:**
- Integrated with HR system (HRIS)
- New employee in HR system → Automatic account creation
- **Advantages:** Fast (minutes/hours), consistent, scales, reduces errors
- **Tools:** Microsoft Identity Manager, Okta, Azure AD, SailPoint

**Just-in-Time (JIT) Provisioning:**
- Account created on first login attempt (not pre-created)
- Common with SSO/SAML: User logs into SSO, account auto-created in target application
- **Advantages:** Reduces unused accounts, ensures accounts created only when needed
- **Use case:** SaaS applications, federated access

**Role-based Provisioning:**
- Access granted based on job role/title
- HR assigns role (e.g., "Sales Representative") → Automatic access to CRM, email, file shares
- **Advantages:** Consistent access for same role, easier auditing, reduces errors
- **Requires:** Well-defined roles with documented access requirements

### Deprovisioning

**Definition:** Process of removing user access when no longer needed (termination, role change, contractor end date).

**Why critical:**
- **Security risk:** Former employees with active accounts = unauthorized access
- **Compliance:** Regulations require timely access removal (SOX, HIPAA)
- **Licensing costs:** Unused accounts still consume licenses

**Deprovisioning workflow:**
1. **Trigger:** HR system indicates termination/role change
2. **Immediate actions:**
   - Disable account (prevents login)
   - Revoke VPN/remote access
   - Collect physical assets (laptop, badge, keys)
3. **Access removal:**
   - Email access forwarded to manager (30 days)
   - Shared drive access removed
   - Application access revoked
   - MFA tokens disabled
4. **Data transfer:**
   - User's files transferred to manager
   - Email mailbox converted to shared mailbox or archived
5. **Account deletion:**
   - After retention period (typically 90 days), account deleted
6. **Audit trail:** Document when account disabled/deleted and by whom

**Deprovisioning timelines:**

**Immediate (within 1 hour):**
- Terminations (voluntary or involuntary)
- Security incidents (compromised account)
- Contractors upon project completion

**Same day:**
- Role changes (moving between departments)
- Leave of absence

**Scheduled:**
- Interns/temporary workers (known end date)
- Contractors (contract expiration)

**Common failures:**
- Orphaned accounts (employee left but account never disabled)
- Delayed deprovisioning (notification from HR delayed)
- Incomplete removal (account disabled in AD but not in all applications)
- No documented process (IT doesn't know employee left)

**Best practices:**
- Automated deprovisioning triggered by HR system
- Checklist for all systems where user had access
- Regular access reviews (quarterly) to identify orphaned accounts
- Exit interview includes account verification
- Grace period (90 days) before permanent deletion (allows recovery if mistake)

---

## Single Sign-On (SSO)

**Definition:** Authentication method allowing users to log in once and access multiple applications without re-entering credentials.

**How SSO works:**
1. User attempts to access Application A
2. Application redirects to SSO provider (Identity Provider - IdP)
3. User authenticates with SSO provider (username/password + MFA)
4. SSO provider generates authentication token
5. User redirected back to Application A with token
6. Application validates token, grants access
7. User attempts to access Application B
8. Application B checks for SSO token (already exists)
9. User automatically logged into Application B (no re-authentication)

**Benefits:**
- **User experience:** Single set of credentials, no repeated logins
- **Security:** Fewer passwords to manage and forget, stronger authentication feasible (MFA once vs every app)
- **IT efficiency:** Centralized user management, easier provisioning/deprovisioning
- **Audit/compliance:** Centralized logging of all access

**Risks:**
- **Single point of failure:** SSO provider down = can't access any applications
- **Credential compromise:** One compromised password = access to all applications (mitigated by MFA)
- **Credential theft high value target:** SSO credentials more valuable to attackers

### SSO Protocols

**LDAP (Lightweight Directory Access Protocol):**
- **Purpose:** Directory service for storing user information and credentials
- **Port:** 389 (unencrypted), 636 (LDAPS - LDAP over SSL)
- **How it works:**
  - Application queries LDAP directory for user authentication
  - LDAP returns user attributes (name, email, group memberships)
  - Application uses groups for authorization decisions
- **Data stored:** Username, password hash, email, department, manager, group memberships
- **Common LDAP servers:** Microsoft Active Directory, OpenLDAP, Apache Directory Server
- **Use cases:** 
  - Authentication for on-premises applications
  - Corporate directory (org chart, email addresses)
  - Network login (Windows domain)
- **LDAP vs LDAPS:**
  - LDAP (port 389): Unencrypted (passwords transmitted in clear text) - NEVER use for authentication
  - LDAPS (port 636): Encrypted with SSL/TLS - REQUIRED for secure authentication
  - StartTLS: Upgrade from 389 to encrypted (alternative to 636)

**OAuth 2.0 (Open Authorization):**
- **Purpose:** Authorization framework (NOT authentication protocol)
- **Use case:** Grant applications limited access to user data without sharing passwords
- **Common example:** "Login with Google" - app gets limited access to Google profile
- **How it works:**
  1. User clicks "Login with Google"
  2. Redirected to Google authorization page
  3. User approves: "Allow App X to access your name and email?"
  4. Google issues access token to App X
  5. App X uses token to request user data from Google API
  6. Google validates token, returns requested data
- **Key components:**
  - **Resource Owner:** User who owns the data
  - **Client:** Application requesting access
  - **Authorization Server:** Issues tokens (e.g., Google, Facebook, Microsoft)
  - **Resource Server:** Hosts protected data (e.g., Google APIs)
- **Token types:**
  - **Access token:** Short-lived (hours), grants access to resources
  - **Refresh token:** Long-lived (weeks/months), used to obtain new access tokens
- **Scopes:** Define what application can access (read email, view profile, post to timeline)
- **Important:** OAuth is authorization (what app can do), NOT authentication (who user is)
- **OAuth 2.0 vs 1.0:** 2.0 simpler, uses bearer tokens, widely adopted

**SAML (Security Assertion Markup Language):**
- **Purpose:** XML-based standard for exchanging authentication and authorization data between parties
- **Common use case:** Enterprise SSO, federated authentication
- **How SAML works:**
  1. User attempts to access Service Provider (SP) application (e.g., Salesforce)
  2. SP redirects user to Identity Provider (IdP) for authentication (e.g., Okta, Azure AD)
  3. User authenticates with IdP
  4. IdP generates SAML assertion (XML document) containing user identity and attributes
  5. User's browser receives SAML assertion
  6. Browser forwards assertion to SP
  7. SP validates assertion signature, grants access
- **SAML assertion contains:**
  - User identity (email, username)
  - Authentication method used
  - Attributes (department, role, groups)
  - Validity period (time-limited)
  - Digital signature (prevents tampering)
- **SAML components:**
  - **Identity Provider (IdP):** Authenticates users (Okta, Azure AD, ADFS)
  - **Service Provider (SP):** Applications trusting IdP (Salesforce, Office 365, Slack)
  - **Assertion:** XML containing authentication/authorization data
- **Advantages:**
  - Standard protocol (widely supported)
  - Secure (digitally signed assertions)
  - Works across security domains (on-prem and cloud)
- **SAML vs OAuth:**
  - SAML: Authentication AND authorization, XML-based, enterprise SSO
  - OAuth: Authorization only, JSON-based, API access delegation

**OpenID Connect (OIDC):**
- **Purpose:** Authentication layer on top of OAuth 2.0
- **Adds to OAuth:** ID token containing user identity information
- **Use case:** "Login with Google/Facebook/Microsoft"
- **Combines:** OAuth authorization + user authentication
- **ID Token (JWT):** Contains user identity, email, name, authentication time
- **Modern alternative to SAML:** Simpler, JSON-based, mobile-friendly

### Federation

**Definition:** Trust relationship between organizations allowing users from one organization to access resources in another using their home credentials.

**Federated SSO scenario:**
- Company A employees need access to Partner B's application
- Instead of creating accounts in Partner B's system:
  - Partner B trusts Company A's IdP
  - Company A employee logs in with Company A credentials
  - Company A IdP issues SAML assertion
  - Partner B accepts assertion, grants access
- **No account creation at Partner B** (Just-in-Time provisioning)

**Benefits:**
- Reduced account sprawl (fewer credentials to manage)
- Centralized access control (Company A controls own users)
- Better user experience (one set of credentials works everywhere)

**Common federation standards:**
- SAML 2.0 (enterprise)
- OAuth 2.0 + OIDC (consumer, mobile)
- WS-Federation (Microsoft ecosystem)

---

## Access Control Models

**Purpose:** Frameworks defining how access permissions are assigned and enforced.

### Mandatory Access Control (MAC)

**Definition:** Operating system enforces access controls based on classification labels. Users cannot change permissions.

**How it works:**
- Every subject (user, process) assigned **clearance level**
- Every object (file, database) assigned **classification label**
- OS enforces access rules:
  - **No read up:** User with Secret clearance can't read Top Secret file
  - **No write down:** User with Top Secret clearance can't write to Unclassified file (prevents data leakage)

**Classification levels (typical military):**
- Top Secret
- Secret
- Confidential
- Unclassified

**Advantages:**
- Highest security (centralized control)
- Prevents accidental or intentional unauthorized access
- Users can't bypass controls

**Disadvantages:**
- Inflexible (difficult to grant exceptions)
- Administrative overhead (labeling every object)
- Complex to implement and maintain

**Use cases:**
- Military and government systems
- Intelligence agencies
- Highly regulated industries (nuclear power, defense contractors)

**Examples:**
- SELinux (Security-Enhanced Linux)
- Trusted Solaris
- Windows Mandatory Integrity Control (MIC)

### Discretionary Access Control (DAC)

**Definition:** Owner of resource controls access permissions. Users can grant/modify access to objects they own.

**How it works:**
- File owner decides who can access file
- Permissions typically: Read, Write, Execute
- Owner can delegate permissions to other users/groups
- **Discretion:** Owner's discretion (choice) determines access

**Example (Windows file permissions):**
- User creates Document.docx
- User is owner, can grant:
  - Read: Finance group
  - Write: Manager
  - Full control: Admin group

**Advantages:**
- Flexible (owners control their own resources)
- Easy to implement
- Low administrative overhead

**Disadvantages:**
- Decentralized (inconsistent permissions)
- Users might grant excessive access
- Difficult to audit (permissions spread across many owners)
- Permissions can proliferate (permission creep)

**Use cases:**
- Most modern operating systems (Windows, Linux, macOS)
- File sharing
- Collaboration tools

**Examples:**
- Windows NTFS permissions
- Unix/Linux file permissions (chmod, chown)
- Cloud storage (Dropbox, Google Drive)

### Role-Based Access Control (RBAC)

**Definition:** Access permissions assigned to roles (job functions), users assigned to roles.

**How it works:**
1. Define roles based on job functions (Sales Rep, Accountant, HR Manager)
2. Assign permissions to each role (Sales Rep: access to CRM, price lists, customer data)
3. Assign users to roles (John Smith → Sales Rep)
4. User inherits all permissions from assigned roles

**Example:**
```
Role: Accountant
Permissions:
  - Read/Write: QuickBooks
  - Read: Payroll system
  - Write: Expense reports
  
Users in role:
  - Jane Doe
  - Bob Smith
  - Mary Johnson

Result: All three users have identical access (Accountant permissions)
```

**Advantages:**
- **Scalability:** Assign role once, applies to all users in role
- **Consistency:** All users with same role have same access
- **Easier auditing:** Review role permissions instead of individual user permissions
- **Supports separation of duties:** Create roles that don't conflict
- **Onboarding/offboarding:** Assign/remove role, access automatically granted/revoked

**Disadvantages:**
- Role explosion (too many granular roles becomes unmanageable)
- Users in multiple roles may have conflicting permissions
- Doesn't handle exceptions well (user needs temporary extra access)

**Use cases:**
- Enterprise applications (ERP, CRM, HRM)
- Cloud platforms (AWS IAM roles, Azure RBAC)
- Database access control

**Examples:**
- Microsoft Active Directory groups
- AWS IAM roles
- Salesforce profiles

### Rule-Based Access Control

**Definition:** Access decisions based on predefined rules (if-then statements).

**How it works:**
- Administrator creates rules (conditions and actions)
- System evaluates rules when access requested
- **Example rules:**
  - IF time between 9 AM - 5 PM THEN allow
  - IF user's IP from company network THEN allow
  - IF user authenticated with MFA THEN allow admin access

**Advantages:**
- Flexible (complex conditions supported)
- Dynamic (access changes based on conditions)
- Context-aware (location, time, device, risk score)

**Disadvantages:**
- Complex to configure
- Rule conflicts possible
- Performance impact (evaluating many rules)

**Use cases:**
- Firewall ACLs (if source IP = X, allow traffic)
- VPN access (if device compliant, allow)
- Adaptive authentication (if risk high, require MFA)

**Examples:**
- Firewall rules
- Network access control (NAC) policies
- Conditional access policies

### Attribute-Based Access Control (ABAC)

**Definition:** Access decisions based on attributes of user, resource, and environment.

**Attributes:**
- **User attributes:** Department, clearance, role, manager, location
- **Resource attributes:** Classification, owner, creation date, sensitivity
- **Environmental attributes:** Time of day, location, IP address, risk score, device type

**How it works:**
- Policies defined using attribute-based rules
- **Example policy:** "Allow access if (user.department = Finance) AND (document.classification = Financial) AND (time.hour >= 9 AND time.hour <= 17)"
- System evaluates all relevant attributes, grants/denies access

**Example scenario:**
- User: Alice (department=HR, clearance=Confidential, location=HQ)
- Resource: Employee_Salaries.xlsx (classification=Confidential, owner=HR)
- Environment: 2 PM on Monday, from company network
- Policy: Allow if (user.department = HR) AND (user.clearance >= document.classification) AND (access_time = business_hours) AND (location = company_network)
- **Result:** Access granted (all conditions met)

**Advantages:**
- **Most flexible:** Fine-grained access control
- **Context-aware:** Considers multiple factors
- **Dynamic:** Access changes as attributes change
- **Scales:** No role explosion (attributes define access)

**Disadvantages:**
- **Complex:** Difficult to design and implement
- **Performance:** Evaluating many attributes per request
- **Debugging:** Hard to troubleshoot "why was access denied?"

**Use cases:**
- Cloud environments (dynamic, diverse users)
- Healthcare (HIPAA requires need-to-know, context matters)
- Federal government (complex access requirements)

**Examples:**
- AWS IAM policies with conditions
- Azure Attribute-Based Access Control
- XACML (eXtensible Access Control Markup Language)

---

## Multi-Factor Authentication (MFA)

**Definition:** Authentication requiring two or more independent factors from different categories.

### Authentication Factors

**Something You Know:**
- Passwords, passphrases
- PINs
- Security questions
- **Weaknesses:** Forgotten, phished, shared, weak passwords, reused across sites

**Something You Have:**
- Hardware tokens (RSA SecurID)
- Smart cards
- Mobile devices (smartphone)
- Security keys (YubiKey, Titan Key)
- **Weaknesses:** Lost, stolen, borrowed, expensive (hardware tokens)

**Something You Are (Biometrics):**
- **Physiological:**
  - Fingerprint
  - Facial recognition
  - Iris/retina scan
  - Palm vein patterns
  - DNA
- **Behavioral:**
  - Voice recognition
  - Keystroke dynamics (typing patterns)
  - Gait analysis (how you walk)
  - Signature dynamics
- **Weaknesses:** Cannot be changed if compromised, false acceptance/rejection rates, privacy concerns, expensive hardware

**Somewhere You Are (Location-based):**
- GPS location
- IP address geolocation
- Proximity to Bluetooth beacon
- **Weaknesses:** Spoofable, privacy concerns, not precise

**Something You Do:**
- Gesture patterns (swipe pattern on phone)
- **Weaknesses:** Observation (shoulder surfing), limited patterns available

### MFA Implementations

**Hardware Tokens:**
- **TOTP (Time-based One-Time Password):** RSA SecurID generates 6-digit code every 30 seconds
- **HOTP (HMAC-based One-Time Password):** Counter-based code generation
- **Advantages:** Secure (offline), no phone needed
- **Disadvantages:** Expensive ($50-100/token), can be lost, battery dies

**Software Tokens (Authenticator Apps):**
- **Apps:** Google Authenticator, Microsoft Authenticator, Authy
- **How it works:**
  1. Scan QR code during enrollment (shares secret key)
  2. App generates 6-digit code every 30 seconds (TOTP algorithm)
  3. Enter code along with password
- **Advantages:** Free, works offline, multiple accounts in one app
- **Disadvantages:** Requires smartphone, vulnerable if phone compromised

**SMS/Voice Codes:**
- Service sends 6-digit code via SMS or voice call
- User enters code to authenticate
- **Advantages:** Universal (everyone has phone), easy to implement
- **Disadvantages:**
  - **SS7 attacks:** SMS interception on cellular network
  - **SIM swapping:** Attacker gets new SIM with victim's number
  - **Phishing:** User gives code to attacker
  - **NIST deprecates SMS for MFA** (still common but discouraged)

**Push Notifications:**
- **Apps:** Duo Mobile, Microsoft Authenticator
- **How it works:**
  1. User enters password
  2. Push notification sent to registered mobile device
  3. User approves/denies login request
- **Advantages:** User-friendly (tap to approve), harder to phish than codes
- **Disadvantages:** Requires internet connection, MFA fatigue (approve blindly)

**Security Keys (FIDO2/WebAuthn):**
- **Physical devices:** YubiKey, Google Titan Key
- **Protocols:** FIDO U2F, FIDO2, WebAuthn
- **How it works:**
  1. Insert key into USB port or tap NFC
  2. Press button on key
  3. Cryptographic challenge-response completes authentication
- **Advantages:**
  - **Phishing-resistant:** Cryptographic verification of site domain
  - **No shared secrets:** Private key never leaves device
  - **Fast:** Tap/press, no code entry
- **Disadvantages:** Cost ($20-50/key), requires USB/NFC support, can be lost (issue backup key)

**Biometric Authentication:**
- **Fingerprint scanners:** Most common (phones, laptops)
- **Facial recognition:** Windows Hello, iPhone Face ID
- **Iris scanners:** High security applications
- **Measurements:**
  - **False Acceptance Rate (FAR):** Unauthorized person incorrectly authenticated (lower better)
  - **False Rejection Rate (FRR):** Authorized person incorrectly rejected (lower better)
  - **Crossover Error Rate (CER):** Point where FAR = FRR (metric for biometric accuracy, lower better)
- **Advantages:** Convenient (always have your fingerprint), fast
- **Disadvantages:**
  - Cannot change if compromised
  - False positives/negatives
  - Presentation attacks (fake fingerprints, photos for facial recognition)
  - Privacy concerns

### MFA Best Practices

**What counts as MFA:**
✅ **True MFA (different factor categories):**
- Password + SMS code (know + have)
- Password + fingerprint (know + are)
- Smart card + PIN (have + know)
- Security key + password (have + know)

❌ **NOT MFA (same factor category):**
- Password + security question (both something you know)
- Two different passwords (both something you know)

**Recommendations:**
1. **Use phishing-resistant MFA:** Security keys (FIDO2) best, push notifications better than codes
2. **Avoid SMS:** Use authenticator apps or security keys instead
3. **Backup codes:** Provide offline codes in case primary MFA unavailable
4. **Adaptive/risk-based MFA:** Require MFA for high-risk activities (admin access, unusual location)
5. **User education:** Teach users to never approve unexpected MFA requests
6. **MFA fatigue attacks:** Limit MFA prompts (if denied 3 times, lock account temporarily)

---

## Privileged Access Management (PAM)

**Definition:** Managing and monitoring access for privileged accounts (administrators, root, service accounts).

**Why PAM needed:**
- Privileged accounts have elevated permissions (install software, modify system configs, access all data)
- **High-value targets:** Attackers seek admin credentials (complete system control)
- **Insider threats:** Admins can abuse access
- **Compliance:** Regulations require monitoring privileged access

### PAM Capabilities

**Credential Vaulting:**
- Store privileged credentials in encrypted vault
- Admins check out credentials when needed
- Automatic password rotation after use
- **Example workflow:**
  1. Admin needs to access production database
  2. Requests credentials from vault (approval workflow if required)
  3. Vault provides temporary credentials (valid 4 hours)
  4. After 4 hours, credentials automatically changed
- **Benefits:** No shared passwords, audit trail of who accessed what, credentials rotated frequently

**Session Recording:**
- Record all privileged user activity
- **What's recorded:** Keystrokes, commands, screenshots, video of session
- **Use cases:**
  - Audit compliance (prove admin didn't access sensitive data)
  - Incident investigation (what did attacker do with stolen admin account?)
  - Training (review junior admin's work)
- **Privacy considerations:** Notify admins of recording, limit to privileged actions only

**Just-in-Time (JIT) Privileged Access:**
- Grant admin rights only when needed, for limited time
- **Example:**
  - User normally has standard user rights
  - Needs to install software → Requests temporary admin rights
  - Approved for 1 hour
  - After 1 hour, reverted to standard user
- **Benefits:** Reduces standing privileges, limits exposure window, enforces least privilege

**Privileged Account Discovery:**
- Scan network for privileged accounts (local admin accounts, service accounts, root)
- Identify shadow IT (accounts not in inventory)
- **Goal:** Ensure all privileged accounts managed by PAM

**Privileged Behavior Analytics:**
- Baseline normal admin behavior
- Alert on anomalies (admin accessing unusual servers, running commands they never use)
- **Use case:** Detect compromised admin accounts

**Emergency Access (Break-Glass):**
- Emergency accounts for use when PAM system unavailable
- Stored in physical safe, requires two-person rule to access
- Automatically generates alert when used

### PAM Best Practices

1. **Eliminate shared accounts:** Each admin has individual account (accountability)
2. **Implement MFA:** Require MFA for all privileged access
3. **Principle of least privilege:** Grant minimum permissions needed
4. **Separate admin accounts:** Standard user account for email/browsing, separate admin account for administrative tasks
5. **Regular audits:** Review who has privileged access, remove unused accounts
6. **Password rotation:** Change privileged passwords frequently (daily/weekly via automation)
7. **Session monitoring:** Monitor and record privileged sessions
8. **Time-limited access:** JIT or expire access after set period

**Popular PAM solutions:**
- CyberArk
- BeyondTrust
- Thycotic (Delinea)
- HashiCorp Vault
- AWS Secrets Manager

---

## Password Policies

**Purpose:** Enforce password security requirements to prevent weak/compromised passwords.

**Common password policy settings:**

**Password Length:**
- **Minimum:** 8 characters (NIST recommends 8, but 12-16 better)
- **Maximum:** Often 128+ characters (no reason to limit)
- **Longer better:** 16-character simple password (e.g., "blueelephantdancing") more secure than 8-character complex password

**Password Complexity:**
- **Traditional requirements:**
  - Uppercase letter (A-Z)
  - Lowercase letter (a-z)
  - Number (0-9)
  - Special character (!@#$%^&*)
- **Problems with complexity:**
  - Leads to predictable patterns (Password1!, Summer2023!)
  - Users write down complex passwords
  - Doesn't prevent dictionary words or common passwords
- **NIST guidance (SP 800-63B):**
  - Length more important than complexity
  - Check against known breached password lists
  - Allow all printable characters (including spaces)

**Password History:**
- Remember last N passwords (typically 12-24)
- Prevents password reuse
- **Problem:** Users cycle through old passwords to get back to favorite

**Password Age:**
- **Minimum age:** 1 day (prevents rapid password changes to cycle through history)
- **Maximum age:** 60-90 days (forces regular password changes)
- **NIST recommendation:** Don't force expiration unless compromise suspected
  - Forced expiration leads to weak patterns (Password1 → Password2 → Password3)
  - Better: Monitor for compromised passwords, force change when detected

**Account Lockout:**
- Lock account after N failed login attempts (typically 3-5)
- **Lockout duration:**
  - Temporary: 15-30 minutes (auto-unlocks)
  - Permanent: Requires admin intervention
- **Considerations:**
  - Too aggressive: Denial-of-service (attacker locks out all users)
  - Too lenient: Brute force attacks succeed
- **Best practice:** Progressive delays (1st fail: instant, 2nd fail: 5 sec delay, 3rd fail: 30 sec delay, 5th fail: lockout)

**Password Requirements Evolution:**

**Old approach (Pre-NIST 800-63B):**
- 8 characters minimum
- Complex requirements (upper, lower, number, special)
- Change every 90 days
- Password history (12 passwords)
- **Result:** Weak patterns, written passwords, user frustration

**Modern approach (NIST 800-63B compliant):**
- 8+ characters minimum (12-16 recommended)
- Check against breached password lists (Have I Been Pwned API)
- No forced expiration (change only if compromised)
- Allow passphrases and spaces
- Require MFA for sensitive accounts
- **Result:** Longer, unique passwords that users actually remember

**Password managers:**
- Software that generates and stores complex passwords
- **Benefits:**
  - Unique password per site (breach of one site doesn't expose others)
  - Complex passwords (30+ random characters)
  - Convenient (auto-fill)
- **Examples:** 1Password, LastPass, Bitwarden, Dashlane
- **Enterprise:** Enterprises should provide password managers to employees

---

## Key Distinctions

### Provisioning vs Deprovisioning
- **Provisioning:** Creating accounts and granting access when user joins/changes role
- **Deprovisioning:** Removing access when user leaves/changes role - MUST be immediate for security

### Authentication vs Authorization
- **Authentication:** Verifying identity (who are you?) - username/password, MFA
- **Authorization:** Determining permissions (what can you do?) - access control models

### SSO vs Federation
- **SSO:** Single login for multiple applications within one organization
- **Federation:** Trust relationship between organizations allowing cross-organization SSO

### LDAP vs SAML vs OAuth
- **LDAP:** Directory service for storing users, authentication protocol (on-prem)
- **SAML:** XML-based authentication/authorization for enterprise SSO (cloud + on-prem)
- **OAuth:** JSON-based authorization for API access delegation (NOT authentication)

### RBAC vs ABAC
- **RBAC:** Access based on job role (Sales Rep, Manager, Admin)
- **ABAC:** Access based on multiple attributes (department, clearance, time, location, device)

### MAC vs DAC
- **MAC:** Operating system enforces access based on labels, users can't change permissions
- **DAC:** Resource owner controls permissions, users can grant access to their files

### MFA vs 2FA
- **2FA:** Exactly two factors required
- **MFA:** Two or more factors required (MFA includes 2FA)

### Something You Know vs Something You Have
- **Know:** Password, PIN, security question - can be forgotten or phished
- **Have:** Token, smart card, phone - can be lost or stolen but harder to duplicate

### PAM vs IAM
- **PAM:** Subset of IAM focused on privileged/administrative accounts
- **IAM:** Broader - all user access management (standard users + privileged)

---

## Common Exam Traps

1. **Trap:** Thinking password + security question is MFA
   - **Reality:** Both "something you know" - same factor, NOT MFA

2. **Trap:** Believing OAuth is authentication protocol
   - **Reality:** OAuth is authorization only (what app can do), not authentication (who user is)

3. **Trap:** Assuming LDAP is secure by default
   - **Reality:** LDAP (port 389) unencrypted; must use LDAPS (636) or StartTLS

4. **Trap:** Thinking deprovisioning can wait until next business day
   - **Reality:** Should be immediate (within 1 hour) for security, especially terminations

5. **Trap:** Believing biometrics alone provide strong authentication
   - **Reality:** Biometrics should be used with another factor (password, PIN) - "biometric + PIN" is MFA

6. **Trap:** Assuming SMS codes are secure MFA
   - **Reality:** SMS vulnerable to SIM swapping, SS7 attacks - NIST deprecates for sensitive applications

7. **Trap:** Thinking complex 8-character password more secure than 16-character simple password
   - **Reality:** Length trumps complexity - "blueelephantdancing" > "P@ssw0rd"

8. **Trap:** Believing forced 90-day password changes improve security
   - **Reality:** Leads to weak patterns (Password1 → Password2) - NIST recommends NO forced expiration unless compromised

---

## Exam Tips

1. **True MFA = different factor categories** - Password + security question is NOT MFA (both knowledge)

2. **Deprovisioning is immediate** - Terminated employees = disable within 1 hour, not next day

3. **LDAPS (636) not LDAP (389)** - Unencrypted LDAP transmits passwords in clear text

4. **OAuth ≠ Authentication** - OAuth authorizes (what app can do), SAML/OIDC authenticate (who you are)

5. **RBAC most common** - Assign permissions to roles, users to roles - exam loves RBAC scenarios

6. **MAC for government/military** - Highest security, labels enforced by OS, users can't override

7. **Biometrics measure: FAR, FRR, CER** - Crossover Error Rate (CER) where FAR=FRR is accuracy metric

8. **PAM for privileged accounts** - Credential vaulting, session recording, JIT access for admins

9. **Password length > complexity** - 16 characters simple > 8 characters complex

10. **Security keys most secure MFA** - FIDO2/WebAuthn phishing-resistant, better than SMS/codes

---

## Key Terms

- **IAM** - Identity and Access Management, ensuring right access to right resources
- **Provisioning** - Creating accounts and granting initial access
- **Deprovisioning** - Removing access when no longer needed
- **JIT (Just-in-Time)** - Granting access/permissions only when needed, for limited time
- **SSO** - Single Sign-On, one login for multiple applications
- **Federation** - Trust between organizations for cross-domain authentication
- **LDAP** - Lightweight Directory Access Protocol, directory service for users/authentication
- **LDAPS** - LDAP over SSL/TLS (port 636), encrypted version of LDAP
- **OAuth** - Open Authorization, framework for API access delegation
- **SAML** - Security Assertion Markup Language, XML-based authentication/authorization
- **OIDC** - OpenID Connect, authentication layer on OAuth 2.0
- **IdP** - Identity Provider, authenticates users in SSO/federation
- **MAC** - Mandatory Access Control, OS enforces labels, users can't override
- **DAC** - Discretionary Access Control, owner controls permissions
- **RBAC** - Role-Based Access Control, permissions assigned to roles
- **ABAC** - Attribute-Based Access Control, permissions based on multiple attributes
- **MFA** - Multi-Factor Authentication, requiring 2+ factors from different categories
- **2FA** - Two-Factor Authentication, exactly two factors
- **TOTP** - Time-based One-Time Password, 6-digit codes rotating every 30 seconds
- **HOTP** - HMAC-based One-Time Password, counter-based codes
- **Biometrics** - Authentication using physical/behavioral characteristics
- **FAR** - False Acceptance Rate, unauthorized person incorrectly authenticated
- **FRR** - False Rejection Rate, authorized person incorrectly rejected
- **CER** - Crossover Error Rate, point where FAR=FRR (biometric accuracy)
- **PAM** - Privileged Access Management, managing admin/root accounts
- **Credential Vaulting** - Storing privileged passwords in encrypted vault
- **Session Recording** - Recording privileged user activity for audit
- **Break-Glass** - Emergency access when normal systems unavailable
- **Password Policy** - Rules enforcing password security requirements
- **Account Lockout** - Locking account after failed login attempts
- **Password History** - Remembering previous passwords to prevent reuse

---

## Example Scenarios

### Scenario 1: Delayed Deprovisioning Leads to Data Breach
**Situation:** Software company with 500 employees. Former employee (software developer) terminated on Friday at 5 PM. HR submitted termination form, but IT team works Monday-Friday 9-5 (no weekend coverage). Account not disabled until Monday 9 AM when IT returned.

**Timeline:**

**Friday 5:00 PM:** Employee John terminated (voluntary resignation, gave 2 weeks notice)
**Friday 5:15 PM:** HR submits deprovisioning request via email to IT
**Friday 5:30 PM:** IT already left for weekend, email unread
**Friday 6:30 PM:** John's VPN access still active
**Friday 7:00 PM:** John connects via VPN from home
**Friday 7:15 PM - 11:00 PM:** John downloads entire source code repository (20,000 files, 15 GB)
**Friday 11:30 PM:** John copies customer database (50,000 customer records with PII)
**Saturday 2:00 AM:** John disconnects VPN
**Monday 9:00 AM:** IT sees deprovisioning request, disables account
**Monday 9:15 AM:** Too late - data already exfiltrated

**What John took:**
- Proprietary source code (company's main product)
- Customer database (names, emails, addresses, purchase history)
- Internal technical documentation
- API keys and credentials (hardcoded in source)

**Discovery (3 weeks later):**
- Competitor announces product with identical features
- Security team investigates, reviews VPN logs
- Discovers John's Friday night access
- Forensics confirm data download

**Impact:**
- **Trade secret theft:** Competitor using stolen code
- **Data breach:** 50,000 customers' PII exposed
- **Regulatory:** Must report breach to state AG, notify customers
- **Reputation:** Customer trust damaged
- **Financial:**
  - Legal action against John: $500k (civil suit)
  - Customer notifications: $50k
  - Credit monitoring for customers: $200k
  - Lost revenue from competitive product: $5M estimated
- **Total cost:** $5.75M+

**Root causes:**

**Process failures:**
1. **Deprovisioning not immediate:** 60-hour window of access
2. **No weekend IT coverage:** Critical security functions unavailable
3. **Manual email-based process:** Delays, no automation
4. **No separation:** Accounts not disabled before final day
5. **No monitoring:** VPN access outside business hours not flagged

**Technical failures:**
1. **No DLP:** Data exfiltration not detected/blocked
2. **No behavioral analytics:** Massive download not flagged as anomalous
3. **No privileged access controls:** Developer had full access to customer database (not need-to-know)
4. **Source code access:** All developers had access to entire codebase (not segmented)

**Proper deprovisioning process (implemented after incident):**

**Immediate actions (within 1 hour of termination):**
1. **AD account:** Disabled immediately (prevents all Windows logins)
2. **VPN access:** Revoked immediately
3. **Email:** Access revoked, forwarding to manager enabled
4. **MFA tokens:** Disabled
5. **Physical access:** Badge deactivated
6. **Remote access:** All active sessions terminated

**Same day:**
7. **Application access:** Salesforce, GitHub, AWS, Jira, Slack revoked
8. **Service accounts:** Any service accounts owned by user disabled/transferred
9. **API keys/tokens:** Revoked and regenerated
10. **Shared accounts:** Reset passwords for any shared accounts

**Within 3 days:**
11. **Data transfer:** User's files transferred to manager
12. **Email mailbox:** Converted to shared mailbox or archived
13. **Device collection:** Laptop, phone, hardware tokens collected

**After 90 days:**
14. **Account deletion:** AD account permanently deleted
15. **Audit:** Verify complete access removal

**Automation implemented:**

**Before (manual):**
- HR emails IT → IT manually disables each system → 60-hour delay

**After (automated):**
- HR marks employee "terminated" in HRIS
- HRIS triggers webhook to identity management system
- Identity management automatically:
  - Disables AD account (instantly blocks all Windows auth)
  - Revokes VPN access
  - Triggers revocation in all integrated SaaS apps
  - Sends notifications to IT, security, facilities
- **Timeline:** 5 minutes from HR action to complete access removal

**Technical controls added:**

**DLP implementation:**
- **Endpoint DLP:** Blocks USB, prevents large downloads to unauthorized destinations
- **Network DLP:** Monitors VPN for data exfiltration patterns
- **Action:** Alert + block when user downloads >1 GB in single session

**User behavior analytics (UEBA):**
- **Baseline:** Normal developer access patterns
- **Alert triggers:**
  - Access outside normal hours (developer usually works 9-5)
  - Downloading entire repository (usually only works on specific projects)
  - Accessing customer database (developer role doesn't need customer data)
- **Automated response:** Alert SOC immediately, optionally block session

**Least privilege enforcement:**
- **Before:** All developers had access to entire codebase
- **After:** Developers only access projects they actively work on
- **Before:** Developers could query customer database directly
- **After:** Customer data access requires specific approval, time-limited

**Separation of duties:**
- **2 weeks before final day:** Disable privileged access, transfer responsibilities
- **Final day:** Disable VPN, revoke application access
- **Policy:** No access to company systems after resignation date (even during notice period if handling sensitive data)

**Results after remediation:**
- Zero deprovisioning delays (automated)
- 15 attempted data exfiltrations detected by DLP (blocked)
- 3 employees flagged by UEBA for anomalous access (investigated, legitimate)
- Average deprovisioning time: 5 minutes (was 60 hours)

**Lessons learned:**
1. **Immediate deprovisioning is non-negotiable** - Cannot wait for next business day
2. **Automate deprovisioning** - Manual processes have delays and errors
3. **Integrate systems** - HRIS should trigger identity management automatically
4. **Monitor privileged users** - Developers have access to valuable IP
5. **DLP essential** - Detect and block data exfiltration before it leaves
6. **Least privilege** - Developers don't need access to entire codebase or customer data
7. **Audit regularly** - Quarterly access reviews find orphaned accounts

**Industry statistics:**
- 89% of former employees retain access to corporate apps after termination
- Average time to revoke access: 2.4 days
- 25% of data breaches involve privileged credential abuse
- Cost of delayed deprovisioning: Average $4.5M per incident

### Scenario 2: SSO Implementation with SAML Federation
**Situation:** Global manufacturing company (10,000 employees) uses 50+ cloud applications (Salesforce, Office 365, Workday, Slack, GitHub, etc.). Each application has separate username/password. Users complain about password fatigue (too many passwords to remember), IT flooded with password reset requests (500/week), security concerns about password reuse.

**Current state problems:**
- **Password fatigue:** Users reset passwords weekly
- **Password reuse:** 73% of users admit using same password across apps
- **Help desk burden:** 500 password reset tickets/week = 2 FTE just for resets
- **Security incidents:** 12 phishing compromises in 6 months (credentials stolen, attacker had access to all apps due to reuse)
- **Onboarding friction:** New employees spend entire first day setting up accounts
- **Compliance:** Auditors concerned about no centralized access control

**Decision:** Implement SSO with SAML federation using Okta as IdP

**Implementation (12-week project):**

**Week 1-2: Planning and architecture**
- Selected Okta (could be Azure AD, Ping Identity, OneLogin)
- Identified 50 applications to integrate
- Prioritized:
  - **Phase 1 (critical):** Office 365, Salesforce, Workday (top 3 by usage)
  - **Phase 2 (high):** Slack, GitHub, Zoom, ServiceNow (15 apps)
  - **Phase 3 (medium):** Remaining 32 apps
- Designed authentication flow
- Selected MFA provider (Okta Verify app)

**Week 3-4: Identity Provider setup**
- Deployed Okta tenant (cloud-based)
- Integrated with Active Directory (user import)
- Configured Okta as SAML IdP
- Set up MFA policies:
  - **MFA required for:** All users, all applications
  - **MFA methods:** Okta Verify push, Google Authenticator backup, SMS backup
- Configured password policies in Okta (users authenticate to Okta, not each app)

**Week 5-6: Phase 1 SAML integration**

**Office 365 integration:**
1. Configure Office 365 as SAML Service Provider
2. Exchange SAML metadata with Okta (certificates, endpoints)
3. Configure attribute mapping (email, name, groups)
4. Test with pilot group (10 users)
5. Verify:
   - User clicks Office 365 icon in Okta dashboard
   - Automatically logged into Office 365 (SSO successful)
   - Logout from Okta logs out of Office 365

**Salesforce integration:**
1. Enable SAML SSO in Salesforce
2. Upload Okta SAML metadata to Salesforce
3. Configure JIT provisioning (auto-create accounts on first login)
4. Map Okta groups to Salesforce profiles
5. Test with pilot

**Workday integration:**
1. Similar SAML configuration
2. Note: Workday also HR system (employee data source for Okta)
3. Two-way integration: Workday → Okta (user provisioning), Okta → Workday (SSO authentication)

**Week 7-8: Pilot testing**
- **Pilot users:** 100 early adopters from IT, Security, HR
- **Training:** 1-hour session on Okta dashboard, MFA enrollment
- **Feedback:**
  - ✅ "So much easier, one login for everything"
  - ✅ "Love push notifications, faster than typing codes"
  - ⚠️ "What happens if phone dies?" (distribute backup codes)
  - ⚠️ "Can't access Okta from old iPad" (browser compatibility fixed)

**Week 9-10: Phase 2 rollout (15 additional apps)**
- Integrated Slack, GitHub, Zoom, ServiceNow, Box, Confluence, Jira, etc.
- Staggered rollout: 5 apps/week
- Each app: Configure SAML, test, document, train

**Week 11-12: Organization-wide rollout**
- **Communication plan:**
  - Email announcement 2 weeks before
  - Video tutorials posted to intranet
  - FAQs published
  - Help desk trained on Okta support
  - Live Q&A sessions
- **Rollout by department:** Sales (week 11), Engineering (week 11), Finance/HR (week 12), all others (week 12)
- **Forced migration:** Old app passwords disabled after grace period

**SAML authentication flow (user perspective):**

**Before SSO:**
1. User goes to salesforce.com
2. Enters Salesforce username and password
3. Logged into Salesforce
4. User goes to office.com
5. Enters Office 365 username and password
6. Logged into Office 365
7. *(Repeat for 48 other apps)*

**After SSO:**
1. User goes to okta.company.com
2. Enters Okta username and password
3. Okta sends push notification to phone
4. User approves on phone (MFA)
5. Logged into Okta dashboard (shows all 50 apps)
6. User clicks Salesforce icon
7. **Automatically logged into Salesforce (SSO magic)**
8. User clicks Office 365 icon
9. **Automatically logged into Office 365**
10. *(One login = access to all 50 apps)*

**SAML authentication flow (technical):**
1. User accesses Salesforce
2. Salesforce detects user not authenticated
3. **Salesforce generates SAML AuthnRequest**, redirects user to Okta (IdP)
4. User authenticates with Okta (username + password + MFA)
5. **Okta generates SAML Response** (XML assertion)
6. SAML Response contains:
   - User identity (email: john.doe@company.com)
   - Attributes (name, department, groups)
   - Digital signature (prevents tampering)
   - Validity period (5 minutes)
7. User's browser posts SAML Response to Salesforce
8. **Salesforce validates SAML signature** (verifies Okta signed it)
9. Salesforce checks assertion validity period
10. Salesforce extracts user identity and attributes
11. Salesforce grants access (user logged in)
12. When user accesses another app (Office 365):
    - User already has Okta session cookie
    - Okta issues SAML assertion without re-authentication
    - SSO achieved

**Results (6 months post-implementation):**

**Security improvements:**
- **Password reuse eliminated:** Users have one strong Okta password
- **MFA enforcement:** 100% of logins protected by MFA
- **Centralized access control:** Disable Okta account = access removed from all 50 apps
- **Phishing resistance:** Even if password phished, attacker needs phone (MFA) and passes SAML signature validation
- **Incident reduction:** Phishing compromises dropped from 12/6 months to 1/6 months (92% reduction)

**User experience improvements:**
- **Password reset tickets:** 500/week → 50/week (90% reduction)
- **Help desk savings:** 2 FTE reassigned to other projects ($200k/year)
- **User satisfaction:** Survey shows 94% prefer SSO over individual logins
- **Onboarding time:** New employee setup from 4 hours to 30 minutes

**Operational benefits:**
- **Centralized provisioning:** New employee automatically gets access to all apps based on department/role
- **Deprovisioning:** Disable Okta account = instant removal from all apps
- **Audit/compliance:** Single dashboard shows all access, comprehensive logs
- **Application discovery:** Found 12 shadow IT apps users connected to Okta

**Costs:**
- **Okta licensing:** $8/user/month × 10,000 users = $80k/month = $960k/year
- **Implementation:** $200k (consultants, internal labor)
- **Total year 1:** $1.16M

**Savings:**
- **Help desk:** 2 FTE × $100k = $200k/year
- **Reduced security incidents:** 11 incidents prevented × $150k average = $1.65M/year
- **Productivity:** 5 min/day password recovery × 10,000 employees × $50/hour = $2.17M/year
- **Total savings:** $4.02M/year

**ROI: 346% first year**

**Challenges encountered:**

**Application compatibility:**
- 5 legacy apps didn't support SAML (10+ years old)
- **Solution:** Okta Secure Web Authentication (SWA) - automated password injection
- **How it works:** Okta stores app password, auto-fills login form (less secure than SAML but better than manual)

**User adoption:**
- 15% of users initially resistant (change aversion)
- **Solution:** Gamification - departments with highest adoption won prizes

**MFA fatigue:**
- Some users complained about approving every login
- **Solution:** Trusted device policy (remember device for 30 days, MFA every 30 days or new device)

**Lessons learned:**
1. **SSO dramatically improves security and UX** - Worth investment for organizations with 5+ applications
2. **Phased rollout essential** - Don't migrate all apps at once (pilot → critical apps → all apps)
3. **Change management critical** - User training and communication determine success
4. **MFA requirement non-negotiable** - SSO without MFA = single point of failure
5. **Application inventory first** - Can't integrate apps you don't know about (shadow IT discovery)
6. **Legacy app plan** - Not all apps support SAML (plan alternative like SWA or reverse proxy)
7. **Compliance value** - Centralized access control simplifies audits

### Scenario 3: RBAC vs ABAC Access Control Decision
**Situation:** Healthcare provider with 2,000 employees (doctors, nurses, administrators, billing staff, researchers) needs to implement access controls for electronic health records (EHR) system. Must comply with HIPAA (minimum necessary principle - only access data required for job function).

**Requirements:**
- Doctors should access their own patients' records
- Nurses should access patients on their assigned unit
- Billing staff should access billing information only
- Researchers should access de-identified data only
- Emergency access needed (ER doctor needs access to ANY patient)
- Audit every record access (who accessed what, when)

**Option 1: Role-Based Access Control (RBAC)**

**Implementation attempt:**
- Created roles:
  - Doctor
  - Nurse
  - Billing Specialist
  - Researcher
  - Administrator

**Doctor role permissions:**
- Access: All patient records in EHR (read/write)
- **Problem:** Doctor should only access their own patients, not all 50,000 patient records

**Attempted fix - Create more granular roles:**
- Cardiology Doctor
- Pediatrics Doctor
- Emergency Medicine Doctor
- ICU Nurse
- Medical-Surgical Nurse
- Billing - Insurance Claims
- Billing - Patient Statements
- Research - Cancer Study
- Research - Diabetes Study
- *(200 roles created...)*

**Result: Role explosion**
- 200+ roles created (unmanageable)
- Still doesn't solve context-based access (doctor on-call needs different access than doctor in clinic)
- Can't handle exceptions (covering for colleague)
- Breaking point: Doctor says "I'm covering for Dr. Smith today, need access to her patients"
  - Solution with RBAC: Grant temporary "Dr. Smith" role (but that gives access to more than just patients)

**Option 2: Attribute-Based Access Control (ABAC)**

**Implementation:**

**User attributes:**
- `user.role` = Doctor, Nurse, Billing, Researcher
- `user.department` = Cardiology, Pediatrics, Emergency, ICU
- `user.specialty` = Cardiology, Orthopedics, Oncology
- `user.employeeID` = unique identifier

**Resource attributes (patient records):**
- `record.patientID` = patient unique identifier
- `record.sensitivity` = Normal, VIP, Employee
- `record.assigned_physician` = doctor's employeeID
- `record.assigned_unit` = ICU, Medical-Surgical-3, Emergency
- `record.dataType` = demographics, diagnosis, billing, lab results

**Environmental attributes:**
- `time.hour` = current hour (0-23)
- `location.IP` = IP address
- `location.facility` = Main Hospital, Satellite Clinic A
- `access.reason` = treatment, billing, research, emergency

**Access policies (ABAC rules):**

**Policy 1: Doctor accessing assigned patients**
```
IF (user.role = Doctor) AND 
   (record.assigned_physician = user.employeeID)
THEN ALLOW access to demographics, diagnosis, treatment, lab results
```

**Policy 2: Nurse accessing patients on their unit**
```
IF (user.role = Nurse) AND 
   (record.assigned_unit = user.assigned_unit) AND
   (time.hour >= 6 AND time.hour <= 18) [shift hours]
THEN ALLOW access to demographics, vital signs, medication orders
```

**Policy 3: Emergency access**
```
IF (user.department = Emergency) AND 
   (access.reason = emergency)
THEN ALLOW access to demographics, allergies, active medications
   AND LOG as emergency access (higher scrutiny)
   AND NOTIFY patient's assigned physician
```

**Policy 4: Billing access**
```
IF (user.role = Billing) AND
   (record.dataType = billing) AND
   (location.facility = Main Hospital)
THEN ALLOW access to billing codes, insurance information
     DENY access to diagnosis, treatment notes
```

**Policy 5: Research access**
```
IF (user.role = Researcher) AND
   (record.patientID IS de-identified) AND
   (user.IRB_approval = True)
THEN ALLOW access to de-identified demographics, diagnosis
     DENY access to names, addresses, MRN
```

**Policy 6: VIP patient protection**
```
IF (record.sensitivity = VIP) AND
   (user.employeeID NOT IN record.approved_access_list)
THEN DENY access
     AND ALERT privacy officer
```

**Real-world scenarios handled by ABAC:**

**Scenario A: Doctor covering for colleague**
- Dr. Smith (employeeID 12345) is assigned to Patient Jones
- Dr. Johnson (employeeID 67890) covering for Dr. Smith today
- **Solution:** Temporarily add `record.assigned_physician = 67890` to Patient Jones records
- No role changes needed
- Automatically expires when coverage ends

**Scenario B: Night shift nurse**
- Nurse Thompson normally works ICU day shift (6 AM - 6 PM)
- Picks up night shift (6 PM - 6 AM)
- **Solution:** Attribute `user.current_shift = night` updated
- Policy allows ICU access if `user.assigned_unit = ICU` (regardless of shift time)
- No manual intervention needed

**Scenario C: Emergency room access**
- ER patient arrives unconscious, unknown to hospital
- ER doctor needs immediate access
- **Solution:** 
  - Doctor selects `access.reason = emergency`
  - ABAC grants access to critical info (allergies, medications, medical history)
  - Flags access as emergency (reviewed by privacy officer next day)
  - Assigned physician notified

**Scenario D: Researcher needs additional data**
- Cancer researcher approved by IRB to access diagnosis codes
- Needs to expand to lab results for new study phase
- **Solution:**
  - IRB updates researcher's `approved_data_types` attribute to include `lab_results`
  - No system reconfiguration needed
  - Audit trail shows attribute change and approver

**Results (ABAC implementation):**

**Security improvements:**
- **Minimum necessary access:** Each user gets only data needed for their specific job function
- **Context-aware:** Access changes based on time, location, reason
- **Granular control:** Can restrict to specific data types (billing sees billing only, not diagnosis)
- **VIP protection:** Automatic protection for sensitive patients

**Compliance:**
- **HIPAA compliant:** Minimum necessary principle enforced by policy
- **Audit trail:** Every access logged with context (who, what, when, why)
- **Privacy officer review:** Emergency accesses flagged for review
- **Regulatory audit:** Show policies to auditors, demonstrate enforcement

**Operational benefits:**
- **No role explosion:** 200+ roles → 5 base roles + attributes
- **Dynamic access:** Coverage, shift changes handled by attribute updates
- **Exception handling:** Emergency access, VIP patients, research approvals all policy-driven
- **Reduced manual work:** No IT tickets for "grant access to Dr. Smith's patients" (attribute update instead)

**Challenges:**

**Policy complexity:**
- 50+ ABAC policies defined (vs 200+ RBAC roles, still improvement)
- **Solution:** Policy templates for common scenarios

**Performance:**
- Evaluating attributes for every access request adds latency
- **Solution:** Cache attribute values, evaluate policy once per session

**Debugging:**
- "Why was I denied access?" harder to diagnose
- **Solution:** Policy decision logs explain which policy evaluated, which condition failed

**Initial deployment:**
- 6 months to design policies, identify attributes, test
- **But:** Easier to maintain long-term than RBAC role explosion

**Costs:**
- **ABAC-capable system:** $500k (vs $200k for RBAC-only system)
- **Implementation:** 6 months effort
- **Savings:** Reduced manual access management, fewer compliance violations

**Lessons learned:**
1. **ABAC better for complex, context-aware access requirements** - Healthcare, government, finance benefit most
2. **RBAC simpler for straightforward scenarios** - Small businesses, simple permission structures
3. **Hybrid approach common** - Base roles (RBAC) + attribute refinement (ABAC)
4. **Attribute quality critical** - Garbage in, garbage out (wrong `assigned_physician` = wrong access)
5. **Policy testing essential** - Test all scenarios before production
6. **User education needed** - Users must understand access.reason field (emergency vs routine)

**When to use RBAC vs ABAC:**

**Use RBAC when:**
- Simple permission structure (same access for everyone in role)
- Limited number of roles (<20)
- Context doesn't matter (time, location irrelevant)
- Small organization
- **Example:** Office with 50 employees, 5 roles (Admin, Manager, Sales, Support, Finance)

**Use ABAC when:**
- Complex, context-dependent access requirements
- Many conditional access scenarios
- Regulatory compliance requires minimum necessary access
- Dynamic environments (frequent exceptions, temporary access)
- **Example:** Healthcare (patient access), Government (classified data), Finance (trading restrictions)

**Hybrid RBAC+ABAC:**
- Start with RBAC for base permissions
- Add ABAC policies for refinement
- **Example:** User role = Doctor (RBAC: can access EHR) + assigned_physician attribute (ABAC: only assigned patients)

### Scenario 4: MFA Implementation and Phishing-Resistant Authentication
**Situation:** Financial services company with 500 employees experienced 5 account compromises in 3 months due to phishing attacks. Users received fake Office 365 login pages, entered credentials, attackers gained access. Current authentication: Username + password only (no MFA).

**Security team proposal:** Implement MFA to prevent credential theft

**Option 1: SMS codes (easiest, cheapest)**
- **How it works:** User enters password, receives 6-digit code via SMS
- **Deployment:** Collect phone numbers, configure MFA in Azure AD, user enrollment
- **Cost:** $0 (included in Azure AD licensing)
- **Timeline:** 1 week

**Pilot test (50 users, 2 weeks):**
- ✅ Users found it acceptable (familiar with SMS codes)
- ✅ IT support tickets minimal (< 5 tickets)
- ⚠️ 3 users had issues receiving SMS (carrier filtering, international numbers)
- ⚠️ Security team warned about SIM swapping attacks

**Attack test (with permission):**
- Security team hired pentester to attempt SIM swap attack
- **Process:**
  1. Pentester social engineered carrier (called AT&T pretending to be user)
  2. Claimed "lost phone, need SIM reactivated"
  3. Carrier transferred number to pentester's SIM card
  4. Pentester phished user credentials
  5. Received SMS MFA code on transferred number
  6. **Successfully logged in despite MFA**
- **Result:** SMS MFA bypassed in 30 minutes

**Option 2: Authenticator app codes (better security)**
- **How it works:** User enters password, opens authenticator app (Google Authenticator, Microsoft Authenticator), enters 6-digit TOTP code
- **Deployment:** Users install app, scan QR code during enrollment
- **Cost:** $0 (free apps)
- **Timeline:** 2 weeks

**Pilot test (100 users, 3 weeks):**
- ✅ More secure than SMS (no SIM swap risk)
- ✅ Works offline (codes generated locally)
- ✅ Multiple accounts in one app
- ⚠️ User friction: "Have to open app, find code, type 6 digits every time I login"
- ⚠️ Help desk tickets increased: "Lost phone with authenticator app, can't login"
  - Solution: Backup codes provided during enrollment

**Attack test:**
- Pentester sent phishing email with fake Office 365 login page
- **Page asked for:**
  - Username
  - Password
  - "Enter your authenticator code"
- User entered credentials + code
- **Pentester immediately used credentials + code to login**
  - TOTP codes valid for 30 seconds
  - If attacker acts quickly, code still works
- **Result:** Authenticator app MFA bypassed via real-time phishing

**Option 3: Push notifications (better UX, still vulnerable)**
- **How it works:** User enters password, receives push notification on phone ("Approve login to Office 365?"), taps Approve
- **Deployment:** Users install Microsoft Authenticator app, enable push notifications
- **Cost:** $0
- **Timeline:** 2 weeks

**Pilot test (200 users, 4 weeks):**
- ✅✅ Users LOVED it: "Just tap approve, so easy"
- ✅ Faster than typing codes
- ✅ Reduced login time by 10 seconds vs typing codes
- ⚠️ "MFA fatigue" observed:
  - Users tapping Approve without reading notification
  - Trained to just tap Approve whenever prompt appears

**Attack test:**
- Pentester phished user credentials
- Pentester attempted login with stolen credentials
- User received push notification: "Approve login attempt?"
- **Pentester simultaneously messaged user:** "IT here, please approve the MFA request we just sent for system update"
- User approved without thinking
- **Result:** Push notification MFA bypassed via social engineering

**MFA fatigue attack (real-world):**
- Attacker uses stolen credentials to repeatedly request MFA pushes
- User receives 10, 20, 50 push notifications
- User frustrated, eventually approves just to make notifications stop
- Attacker logs in

**Option 4: Security keys - FIDO2/WebAuthn (phishing-resistant)**
- **How it works:**
  1. User inserts YubiKey into USB port (or taps NFC)
  2. Website initiates WebAuthn challenge
  3. User enters password, presses button on YubiKey
  4. YubiKey performs cryptographic challenge-response
  5. **YubiKey verifies website domain** (can't be phished)
- **Deployment:** Purchase YubiKeys ($50/key × 2 per user = backup), enroll keys, distribute
- **Cost:** $50k (500 users × 2 keys × $50)
- **Timeline:** 6 weeks

**How FIDO2 prevents phishing:**
1. **Domain binding:** YubiKey stores domain (company.okta.com) during enrollment
2. Attacker creates phishing site (c0mpany.okta.com or company-okta.com)
3. User enters password on phishing site
4. Phishing site requests YubiKey authentication
5. **YubiKey checks domain: "This is c0mpany.okta.com, not company.okta.com"**
6. **YubiKey refuses to authenticate** (cryptographic challenge fails)
7. Even if user presses button, authentication fails
8. **Attacker cannot login** (doesn't have YubiKey + domain mismatch)

**Pilot test (100 users, 6 weeks):**
- ✅✅ Security team thrilled: "Actually phishing-resistant"
- ✅ Fast: Touch YubiKey, done (no codes to type)
- ✅ Works across all devices (USB-A, USB-C, NFC for phones)
- ⚠️ Users need to carry YubiKey (issued backup key for home, primary key for wallet/keychain)
- ⚠️ 2 users lost YubiKey (used backup key, requested replacement)
- ⚠️ Some legacy applications don't support FIDO2 (used push notification fallback)

**Attack test:**
- Pentester sent best phishing page (exact replica of Office 365 login)
- User entered credentials
- User inserted YubiKey and pressed button
- **YubiKey refused to authenticate** (domain mismatch)
- User saw error: "Security key cannot be used with this website"
- User reported phishing attempt to security team
- **Result:** FIDO2 MFA CANNOT be bypassed via phishing**

**Decision: Implement FIDO2 security keys**

**Rollout (12 weeks):**

**Week 1-2: Procurement**
- Ordered 1,000 YubiKey 5 NFC (2 per employee)
- $50 × 1,000 = $50k

**Week 3-4: IT enrollment**
- IT staff (50 employees) enrolled first
- Created enrollment documentation
- Tested all applications for FIDO2 support

**Week 5-8: Phase 1 (high-risk users)**
- Executives (20 users)
- Finance team (30 users)
- IT administrators (20 users)
- Users with access to sensitive data (100 users)
- Total: 170 users

**Week 9-12: Phase 2 (all users)**
- Remaining 330 users
- Department-by-department rollout

**User training:**
- 15-minute video: "What is a security key and why it matters"
- Step-by-step enrollment guide
- FAQ: "What if I lose my key?", "Do I need to carry it everywhere?", "What about my phone?"
- Office hours: IT staff available for help

**Challenges:**

**Application compatibility:**
- 90% of applications supported FIDO2 (Office 365, Salesforce, AWS, GitHub, Okta)
- 10% legacy apps didn't support FIDO2
- **Solution:** Fallback to push notification for legacy apps (still better than no MFA)

**User resistance:**
- "Another thing to carry"
- **Solution:** YubiKey 5 NFC fits on keychain, works with phone via NFC (don't need to remove from keychain)

**Lost/forgotten keys:**
- Users forgot key at home or lost it
- **Solution:** 
  - Backup codes (10 single-use codes for emergencies)
  - Help desk can remotely verify identity and issue temporary access
  - Backup YubiKey at home

**Results (12 months after full deployment):**

**Security outcomes:**
- **Phishing compromises:** 5 in 3 months before MFA → **0 in 12 months after FIDO2**
- **Credential stuffing blocked:** 47 attempts detected (stolen passwords from other breaches), all blocked by MFA requirement
- **Account takeover attempts:** 0 successful (was 5)
- **Help desk tickets:** "I think I was phished" reports up 300% (users more aware, reporting suspicious emails)

**User satisfaction:**
- Survey: 87% of users prefer YubiKey over previous password-only
- "Faster than typing password twice"
- "Peace of mind knowing account is secure"

**Operational:**
- **Lost keys:** 23 users lost YubiKey in 12 months (4.6% loss rate)
  - Used backup key
  - Replacement cost: $50 × 23 = $1,150
- **Help desk tickets:** Initial spike during rollout (week 5-8: 50 tickets), then stabilized (5-10/month)

**Cost-benefit:**

**Costs:**
- YubiKeys: $50k (1,000 keys)
- Replacement keys: $1,150/year
- IT labor (rollout): $25k
- **Total year 1:** $76k

**Prevented losses:**
- **Before MFA:** 5 compromises × 3 months = 20/year
- **Average incident cost:** $50k (forensics, remediation, regulatory reporting, customer notification)
- **Prevented:** 20 incidents × $50k = $1M/year

**ROI: 1,215% first year**

**Additional benefits:**
- **Cyber insurance premium reduction:** 15% discount for MFA implementation ($50k/year savings)
- **Compliance:** Satisfies regulatory requirements (FFIEC, NYDFS)
- **Customer trust:** Marketing highlights security measures

**Lessons learned:**
1. **Not all MFA is equal** - SMS < Codes < Push < FIDO2 for security
2. **Phishing-resistant MFA essential** - SMS and codes can be real-time phished
3. **User experience matters** - Security keys faster and easier than typing codes
4. **Budget for hardware** - Upfront cost justified by prevented breaches
5. **Phased rollout** - Start with high-risk users, learn lessons, expand
6. **Backup plan essential** - Lost key shouldn't lock out user
7. **Application compatibility** - Not all apps support FIDO2 (have fallback)
8. **User education critical** - Users must understand why new process important

**Industry adoption:**
- Google required security keys for all 85,000 employees (2017) - **zero account compromises since**
- Microsoft saw 100% reduction in account compromises after implementing phishing-resistant MFA
- NIST SP 800-63B recommends phishing-resistant authenticators for high-value accounts

### Scenario 5: Privileged Access Management (PAM) Implementation
**Situation:** Technology company (1,000 employees) with 50 employees having admin/root access (system administrators, DevOps, DBAs). Current state: Shared administrator passwords in Excel spreadsheet, no audit trail of who did what, no password rotation.

**Security audit findings:**

**Critical issues identified:**
1. **Shared credentials:** 12 different admin accounts, passwords shared via Excel file
   - Windows Domain Admin (shared by 15 IT staff)
   - Linux root (shared by 20 DevOps)
   - Database SA account (shared by 5 DBAs)
   - AWS root account (shared by 10 cloud admins)

2. **No accountability:** Can't determine who performed actions
   - Production database deleted - who did it? (5 people have password)
   - Firewall rule changed - by whom? (everyone uses "admin" account)

3. **Password never changed:** Some admin passwords unchanged for 3+ years
   - Windows Domain Admin password: "Password123" for 5 years
   - Database SA password: Known to 20+ people (current and former employees)

4. **No session recording:** No visibility into what admins do
   - Can't prove compliance for SOX audit
   - Can't investigate malicious insider activity

5. **Standing privileges:** Everyone with admin access has it 24/7
   - Developers have production admin access (don't need daily)
   - Not following least privilege

**Incident that triggered PAM project:**

**Friday 6 PM:**
- Production database server went down
- Investigation: Database tables dropped
- **Who did it?** 5 people have SA password, all deny responsibility
- **Forensics:** SQL Server logs show "SA" account dropped tables, but can't identify which person

**Recovery:**
- Restore from backup (3 hours downtime)
- Revenue loss: $500k (e-commerce site down Friday evening)
- Customer impact: 50,000 orders lost/delayed

**Root cause:**
- Disgruntled DBA (Jason) being terminated (last day Friday)
- Used shared SA password to drop tables
- **No evidence to prosecute:** Can't prove it was Jason (5 people have password)

**PAM solution implemented: CyberArk**

**Deployment (16-week project):**

**Week 1-4: Planning and infrastructure**
- Selected CyberArk Privileged Access Security
- Deployed CyberArk vault (encrypted credential storage)
- Identified all privileged accounts:
  - Windows Domain Admin (5 accounts)
  - Linux root (30 servers)
  - Database admin (SQL Server SA, Oracle SYS, MySQL root - 20 databases)
  - Cloud admin (AWS root, Azure Global Admin)
  - Network admin (switch/router/firewall admin accounts)
  - Application admin (SAP, Salesforce, custom apps)
  - **Total: 200+ privileged accounts discovered** (more than expected!)

**Week 5-8: Credential vaulting**
- Onboarded all accounts to CyberArk vault
- Changed all passwords to 32-character random (CyberArk generates)
- **Passwords now stored in vault, encrypted, no human knows them**

**Example workflow - Before PAM:**
1. Admin needs to access production database
2. Opens Excel spreadsheet: "Database_Passwords.xlsx"
3. Finds SA password: "DbAdmin2019!"
4. Logs into database
5. *(Password never expires, everyone knows it, no audit of who logged in when)*

**Example workflow - After PAM:**
1. Admin needs to access production database
2. Logs into CyberArk web portal
3. Searches for "Prod-DB-01 SA account"
4. Clicks "Connect"
5. **Request approval workflow:**
   - If non-business hours: Requires manager approval
   - If business hours + valid reason: Auto-approved
6. CyberArk launches RDP/SSH session using stored credentials
7. **Admin never sees password** (transparent connection)
8. After 4 hours, connection terminates automatically
9. **CyberArk automatically rotates password** (new random 32-character password)

**Week 9-12: Session recording**
- Enabled session recording for all privileged access
- **What's recorded:**
  - Full video of session (screen recording)
  - All keystrokes typed
  - All commands executed
  - Timestamps of all actions
- **Storage:** 90 days online, 1 year archived

**Week 13-16: Just-in-Time (JIT) access**
- Removed standing admin privileges
- **Developers:** No longer have permanent production admin access
- **Request process:**
  - Developer needs access for troubleshooting
  - Submits request: "Need admin on Prod-Web-01 to investigate memory leak"
  - Manager approves
  - CyberArk grants temporary admin rights (4 hours)
  - After 4 hours, rights automatically revoked
- **Benefits:** Reduced standing privileged accounts from 50 to 10 (80% reduction)

**Advanced features enabled:**

**Dual control (four-eyes):**
- For highest-risk actions (production database, financial systems)
- Requires two approvers
- Example: Accessing production database requires approval from both manager and security team

**Anomaly detection:**
- CyberArk baselines normal admin behavior
- **Alerts on:**
  - Admin accessing servers they never accessed before
  - Admin running commands unusual for their role
  - Access from unusual location/time
  - Rapid privilege escalation

**Password rotation:**
- Automatic rotation after every use
- Scheduled rotation: Every 30 days even if not used
- Rotation happens in seconds (CyberArk changes password via API)

**Emergency access (break-glass):**
- If CyberArk system unavailable, emergency accounts in physical safe
- Requires two executives to unlock safe
- Emergency access automatically generates alert to CISO

**Results (12 months after implementation):**

**Security improvements:**
- **No shared passwords:** Each admin has individual account, no sharing
- **Accountability:** Full audit trail of who accessed what, when, for how long
- **Password rotation:** Admin passwords changed after every use (vs 5 years before)
- **Reduced attack surface:** 50 standing admin accounts → 10 (80% reduction)
- **Session recording:** Complete forensic evidence of all admin actions

**Incident prevention:**
- **Malicious insider detected:**
  - 6 months after PAM deployment, another DBA (Sarah) being terminated
  - Morning of termination, Sarah requested access to production database
  - **CyberArk anomaly detection flagged:** "Sarah requesting DB access unusual for Friday morning"
  - Security team reviewed request, denied (terminated same day)
  - **PAM prevented repeat of original incident**

**Compliance benefits:**
- **SOX audit:** Auditors praised privileged access controls
  - Session recordings demonstrate no unauthorized access to financial systems
  - Segregation of duties enforced (developer can't have production admin + database admin simultaneously)
- **PCI DSS:** Requirement 7 (restrict access) and 8 (unique IDs) satisfied
- **Audit time reduced:** Comprehensive logs reduced audit from 2 weeks to 3 days

**Operational benefits:**
- **Password reset tickets:** Eliminated (admins no longer manage privileged passwords)
- **Onboarding/offboarding:** New admin? Add to CyberArk group. Admin leaves? Remove from group (instant access revocation across all systems)
- **Emergency access:** Break-glass procedure tested quarterly, worked every time

**User feedback:**
- **Initial resistance:** "Another system to learn, more clicks to access servers"
- **After 3 months:** "Actually easier - no more password spreadsheets, don't have to remember/change passwords"
- **Security team:** "Can actually investigate incidents now - session recordings are game-changer"

**Metrics:**

**Before PAM:**
- Privileged accounts: 200+
- Standing admin rights: 50 people
- Password rotation: Never (or every 3-5 years)
- Shared accounts: 12
- Audit capability: None (can't determine who did what)
- Incidents: 2/year (malicious insider actions)

**After PAM:**
- Privileged accounts: 200+ (same, but now managed)
- Standing admin rights: 10 people (80% reduction via JIT)
- Password rotation: After every use + every 30 days
- Shared accounts: 0 (all individual accounts)
- Audit capability: Complete (who, what, when, how long, recording)
- Incidents: 0/year (prevented 1 via anomaly detection)

**Costs:**
- **CyberArk licensing:** $500/year per privileged account × 200 = $100k/year
- **Infrastructure:** $50k (servers, storage for recordings)
- **Implementation:** $100k (consulting, internal labor)
- **Total year 1:** $250k

**ROI:**
- **Prevented incident:** $500k (original incident cost)
- **Prevented incident #2:** $500k (Sarah's attempted sabotage)
- **Reduced audit costs:** $50k/year (faster audits)
- **Eliminated password management overhead:** $30k/year (help desk time)
- **Total value:** $1.58M first year

**ROI: 532% first year**

**Lessons learned:**
1. **Shared passwords = no accountability** - Individual accounts essential for forensics
2. **PAM not just vaulting** - Session recording, JIT access, rotation equally important
3. **Discover all privileged accounts first** - Often 2-3× more than expected
4. **Start with highest-risk** - Production databases, domain admin, cloud root accounts
5. **User education critical** - Admins must understand why change necessary
6. **Emergency access essential** - Break-glass must work when PAM unavailable
7. **Integrate with ticketing** - Link access requests to change tickets (why admin needs access)

**Industry best practices:**
- **NIST SP 800-53 AC-2:** Privileged account management requirements
- **PCI DSS Requirement 8:** Unique IDs for privileged users
- **SOX:** Segregation of duties, audit trails for financial system access
- **CIS Controls:** Control 4 (Controlled Use of Administrative Privileges)

**Expansion roadmap:**
- **Year 2:** Integrate with SIEM (forward all PAM events)
- **Year 3:** Application-to-application password management (service account vaulting)
- **Year 4:** Extend to cloud (AWS Secrets Manager integration, Azure Key Vault)

---

## Mini Quiz

### Question 1
IT department received deprovisioning request for terminated employee Sarah at 5 PM Friday. IT team works Monday-Friday 9-5. Manager wants to wait until Monday to disable account "to avoid rushing and making mistakes."

What should security team recommend?

<details>
<summary>Show Answer</summary>

**Answer: Disable account immediately (within 1 hour), even if after hours - deprovisioning cannot wait**

**Explanation:**

**Why immediate deprovisioning essential:**
- **Security risk:** 60+ hours (Friday 5 PM - Monday 9 AM) of unnecessary access
- **Malicious insider:** Terminated employees high-risk for sabotage or data theft
- **Compliance violation:** SOX, HIPAA, PCI DSS require timely access removal
- **Window of opportunity:** Former employee can access systems remotely (VPN, cloud apps)

**What can happen in 60 hours:**
- Download entire customer database
- Delete production data
- Copy source code/trade secrets
- Create backdoor accounts
- Steal credentials for future access

**Proper procedure:**
1. **Immediate (within 1 hour):**
   - Disable AD account (blocks all Windows authentication)
   - Revoke VPN access
   - Disable MFA tokens
   - Deactivate physical access badge
2. **Same day:**
   - Revoke application access (SaaS, cloud)
   - Forward email to manager
   - Collect company devices
3. **Within 3 days:**
   - Transfer files to manager
   - Document all access removed
4. **After 90 days:**
   - Delete account permanently

**Why "wait until Monday" is wrong:**
- Prioritizes IT convenience over security
- Creates 60-hour vulnerability window
- Violates compliance requirements
- Standard operating procedure should handle after-hours deprovisioning

**Best practice:**
- **Automated deprovisioning:** HR marks "terminated" in HRIS → Automatic account disable (minutes)
- **On-call rotation:** IT security on-call can handle after-hours terminations
- **Emergency procedure:** Pre-documented checklist for immediate actions
</details>

### Question 2
Company implementing SSO. Users will authenticate to Okta (IdP) once, then access Salesforce, Office 365, and 20 other applications without re-entering credentials.

Security team concerned: "If attacker compromises Okta password, they get access to everything!"

What is BEST mitigation for this risk?

<details>
<summary>Show Answer</summary>

**Answer: Require MFA for Okta authentication (preferably phishing-resistant like FIDO2 security keys)**

**Explanation:**

**The SSO security trade-off:**
- **Pro:** Users have one strong password (not reusing weak passwords across apps)
- **Con:** One compromised credential = access to all apps (high-value target)

**MFA as compensating control:**
- **Without MFA:** Password alone unlocks all apps
- **With MFA:** Password + second factor required
- **Even if password phished, attacker still blocked by MFA**

**MFA strength hierarchy (best to worst):**

**1. FIDO2 Security Keys (BEST):**
- **Why best:** Phishing-resistant (domain binding prevents fake login pages)
- **Example:** YubiKey
- **Attack scenario:** Attacker phishes password → Sends fake Okta page → User inserts security key → Key refuses (domain mismatch) → **Attack fails**

**2. Push Notifications (GOOD):**
- **Why good:** Harder to phish than codes (user approves/denies)
- **Weakness:** MFA fatigue (user blindly approves), social engineering possible
- **Attack scenario:** Attacker gets password → Floods user with push requests → User approves to stop notifications → **Attack succeeds**

**3. Authenticator App Codes (ACCEPTABLE):**
- **Why acceptable:** Not vulnerable to SIM swap
- **Weakness:** Real-time phishing possible (attacker captures code within 30-second window)
- **Attack scenario:** Attacker gets password → Phishing page asks for code → User enters code → Attacker uses immediately → **Attack succeeds** (if fast)

**4. SMS Codes (WEAK):**
- **Why weak:** SIM swapping, SS7 attacks
- **Attack scenario:** Attacker gets password → SIM swap to get user's phone number → Receives SMS code → **Attack succeeds**
- **NIST deprecates SMS for sensitive applications**

**Additional mitigations:**

**Risk-based/Adaptive authentication:**
- **Low risk:** Known device, normal location, business hours → Password only
- **Medium risk:** New device or unusual location → Require MFA
- **High risk:** Foreign country or impossible travel → Block + require additional verification

**Session timeout:**
- Okta session expires after inactivity (15-30 minutes)
- Limits window even if session compromised

**Continuous authentication:**
- Monitor behavior after login (unusual access patterns)
- Challenge with step-up authentication if suspicious

**Application-specific MFA:**
- Critical apps (financial systems, admin portals) require MFA even with SSO
- Step-up authentication for sensitive operations

**Other controls (helpful but not sufficient alone):**
- Strong password policy (length, complexity, no reuse)
- Conditional access (block from unknown countries)
- User training (recognize phishing)
- **But none of these prevent credential theft like MFA does**

**Why other answers insufficient:**

**"Disable SSO":**
- Defeats purpose of SSO
- Back to password fatigue and reuse (worse security)

**"Require frequent password changes":**
- Users create weak patterns (Password1 → Password2)
- NIST recommends NO forced expiration
- Doesn't prevent phishing

**"Monitor for suspicious logins":**
- Detection, not prevention
- Attacker has already accessed apps by time you detect

**Best practice:**
- SSO + Phishing-resistant MFA (FIDO2) = Secure and convenient
- One login, two factors (password + security key)
- Protects against phishing, credential stuffing, password reuse
</details>

### Question 3
Hospital implementing access controls for electronic health records. Requirement: Doctors should only access their own patients' records, nurses should only access patients on their assigned unit, and access should be blocked outside normal shift hours.

Which access control model BEST meets these requirements?

<details>
<summary>Show Answer</summary>

**Answer: ABAC (Attribute-Based Access Control)**

**Explanation:**

**Why ABAC is best:**

**Requirements demand context-aware access:**
- "Their own patients" = Relationship-based (doctor-patient assignment)
- "Assigned unit" = Location-based (ICU vs Medical-Surgical)
- "Normal shift hours" = Time-based (day shift vs night shift)
- All three factors must be evaluated together

**ABAC attributes needed:**

**User attributes:**
- `user.role` = Doctor, Nurse
- `user.employee_id` = unique identifier
- `user.assigned_unit` = ICU, Medical-Surgical, Emergency
- `user.shift_hours` = 6-18 (day shift) or 18-6 (night shift)

**Resource attributes:**
- `record.patient_id` = patient identifier
- `record.assigned_physician` = doctor's employee_id
- `record.assigned_unit` = ICU, Medical-Surgical

**Environmental attributes:**
- `time.hour` = current hour (0-23)

**ABAC policy example:**
```
IF (user.role = Doctor) AND 
   (record.assigned_physician = user.employee_id)
THEN ALLOW access
```

```
IF (user.role = Nurse) AND 
   (record.assigned_unit = user.assigned_unit) AND
   (time.hour >= user.shift_start AND time.hour <= user.shift_end)
THEN ALLOW access
```

**Why other models fail:**

**RBAC (Role-Based Access Control):**
- Can define "Doctor" and "Nurse" roles ✓
- **Cannot enforce "their own patients"** ✗
  - All doctors would have access to all patient records
  - Can't differentiate Dr. Smith's patients from Dr. Jones's patients
- **Cannot enforce time restrictions** ✗
  - Roles don't consider time of day
  - Nurses would have 24/7 access (even off-shift)

**Workaround attempt:** Create roles like "Dr-Smith-Patients" and "ICU-Day-Shift-Nurse"
- **Result:** Role explosion (200+ roles)
- **Problem:** Doctor covering for colleague needs temporary role change
- **Unmanageable**

**MAC (Mandatory Access Control):**
- Based on classification labels (Top Secret, Secret, Confidential)
- **Cannot express patient-doctor relationship** ✗
- **Cannot incorporate time or location** ✗
- **Use case:** Military/government, not healthcare

**DAC (Discretionary Access Control):**
- Resource owner controls access
- **Who owns patient record?** Patient? Hospital? Doctor?
- **Cannot enforce organizational policy** (hospital decides access, not individuals)
- **Compliance risk:** Owners might grant excessive access
- **Not suitable for regulated healthcare**

**Rule-Based Access Control:**
- Similar to ABAC but less flexible
- Could work but ABAC is more comprehensive
- **ABAC is evolution of rule-based access control**

**Real-world ABAC scenario:**

**Scenario:** Dr. Johnson (Cardiologist) needs to access patient Mary's record

**ABAC evaluation:**
1. Check `user.role = Doctor` ✓
2. Check `record.assigned_physician = Dr-Johnson-ID` ✓
3. Check `user.department = Cardiology` ✓
4. Check `record.department = Cardiology` ✓
5. **Result:** Access GRANTED

**Scenario:** Nurse Williams (ICU, day shift) tries to access patient in Medical-Surgical unit

**ABAC evaluation:**
1. Check `user.role = Nurse` ✓
2. Check `record.assigned_unit (Med-Surg) = user.assigned_unit (ICU)` ✗
3. **Result:** Access DENIED

**Scenario:** Nurse Williams tries to access ICU patient at 8 PM (off shift)

**ABAC evaluation:**
1. Check `user.role = Nurse` ✓
2. Check `record.assigned_unit (ICU) = user.assigned_unit (ICU)` ✓
3. Check `time.hour (20) BETWEEN user.shift_start (6) AND user.shift_end (18)` ✗
4. **Result:** Access DENIED (outside shift hours)

**Emergency override:**
- ER doctor needs to access any patient
- **ABAC policy:** IF `user.department = Emergency` AND `access.reason = emergency` THEN ALLOW
- Logs emergency access for privacy officer review

**HIPAA compliance:**
- **Minimum necessary principle:** ABAC enforces (access only to assigned patients)
- **Audit controls:** Every access logged (who, what, when, why)
- **Access reviews:** Quarterly review of ABAC policies and access logs

**Why ABAC chosen by healthcare:**
- Veterans Affairs (VA): ABAC for patient records
- Kaiser Permanente: Attribute-based access
- Epic EMR: Supports ABAC policies
- **Reason:** Complex, context-dependent access requirements
</details>

### Question 4
Company requires all employees to use MFA. Currently using SMS codes. Security team wants to upgrade to more secure MFA.

Which option provides STRONGEST protection against phishing attacks?

<details>
<summary>Show Answer</summary>

**Answer: FIDO2 security keys (hardware tokens with WebAuthn/U2F)**

**Explanation:**

**Why FIDO2 security keys are strongest:**

**Phishing resistance through cryptographic domain binding:**
1. During enrollment, security key generates key pair for specific domain (e.g., company.okta.com)
2. Private key stored on hardware device (never leaves device)
3. Public key registered with website
4. When authenticating:
   - Website sends challenge
   - Security key checks: "Is this the same domain I enrolled with?"
   - If domain matches → Signs challenge with private key
   - If domain different (phishing site) → **Refuses to respond**

**Attack scenario:**
1. Attacker sends phishing email with link to fake-company-okta.com
2. User clicks link, enters password
3. Fake site requests security key authentication
4. **Security key examines domain: "fake-company-okta.com ≠ company.okta.com"**
5. **Security key refuses to authenticate**
6. User sees error: "Security key cannot be used with this website"
7. **User realizes it's phishing site**
8. Attack fails - attacker cannot login even with password

**Why SMS codes are weakest:**

**Vulnerable to:**
1. **SIM swapping:**
   - Attacker social engineers carrier ("I lost my phone, transfer number to new SIM")
   - Carrier transfers victim's number to attacker's SIM
   - Attacker receives all SMS including MFA codes
   - **Real-world:** Twitter CEO Jack Dorsey's account compromised via SIM swap

2. **SS7 attacks:**
   - Vulnerability in cellular network signaling protocol
   - Attackers can intercept SMS messages
   - Requires technical sophistication but known attack vector

3. **Real-time phishing:**
   - Phishing site captures password
   - Immediately prompts for SMS code
   - User enters code thinking it's for real site
   - Attacker receives code, uses within 60-second validity window
   - Attack succeeds

**Why authenticator app codes are better than SMS but still vulnerable:**

**TOTP (Time-Based One-Time Password) codes:**
- More secure than SMS (no SIM swap risk)
- Work offline (no cellular dependency)

**But still vulnerable to real-time phishing:**
1. User visits phishing site
2. Enters password + authenticator code
3. Attacker immediately uses credentials on real site (within 30-second code validity)
4. **Attack succeeds if attacker fast enough**

**Why push notifications are better but still vulnerable:**

**Push notification MFA:**
- User receives "Approve login?" push
- Tap to approve

**Vulnerabilities:**
1. **MFA fatigue:**
   - Attacker spams login attempts → 20+ push notifications
   - User approves just to stop notifications
   - Attack succeeds

2. **Social engineering:**
   - Attacker messages user: "IT here, approve the push we just sent"
   - User approves without thinking
   - Attack succeeds

3. **Prompt bombing:**
   - Attacker floods user with prompts at 2 AM
   - Sleepy user approves to silence phone
   - Attack succeeds

**FIDO2 security keys address all these:**
- ✅ No SIM swap risk (no phone needed)
- ✅ No real-time phishing (domain binding)
- ✅ No MFA fatigue (one button press, not 20 prompts)
- ✅ No social engineering (cryptographic validation, not user decision)

**MFA comparison table:**

| Method | SIM Swap | Real-Time Phishing | MFA Fatigue | User Convenience |
|--------|----------|-------------------|-------------|------------------|
| SMS | ✗ Vulnerable | ✗ Vulnerable | N/A | ✓ High |
| Authenticator App | ✓ Protected | ✗ Vulnerable | N/A | ✓ Medium |
| Push Notification | ✓ Protected | ⚠️ Social Eng | ✗ Vulnerable | ✓✓ High |
| FIDO2 Security Key | ✓ Protected | ✓ Protected | ✓ Protected | ✓ High |

**Real-world FIDO2 success:**
- **Google:** Required security keys for 85,000 employees → **Zero account compromises since 2017**
- **Microsoft:** Saw **100% reduction** in account takeovers after deploying phishing-resistant MFA
- **Cloudflare:** Issued security keys to all employees → No successful phishing attacks

**Implementation considerations:**

**FIDO2 advantages:**
- Phishing-resistant (primary benefit)
- Fast (touch button, done - no codes to type)
- Works across devices (USB, NFC for phones)
- Open standard (not vendor lock-in)

**FIDO2 challenges:**
- **Cost:** $20-50 per key, need 2 per user (primary + backup) = $40-100/user
- **Loss risk:** Users can lose keys (issue backup key)
- **Application support:** Not all legacy apps support FIDO2 (90%+ modern apps do)

**Migration path:**
1. **Phase 1:** SMS codes (current state) - Known weak
2. **Phase 2:** Authenticator app codes - Better than SMS
3. **Phase 3:** Push notifications - Good UX, still some risk
4. **Phase 4:** FIDO2 security keys - **Strongest protection**

**Best practice:**
- Deploy FIDO2 for high-risk users first (executives, finance, IT admins)
- Expand to all employees over time
- Keep push notifications as fallback for legacy apps
- Never use SMS for sensitive accounts

**Answer:** FIDO2 security keys provide strongest protection against phishing through cryptographic domain binding that cannot be bypassed by attackers.
</details>

### Question 5
IT admin needs to access production database to troubleshoot urgent issue. Currently, admin knows the "SA" password (shared by 5 DBAs). Security team proposes implementing PAM (Privileged Access Management).

What is PRIMARY benefit of PAM in this scenario?

<details>
<summary>Show Answer</summary>

**Answer: Individual accountability through unique credentials and session recording - can determine exactly who did what**

**Explanation:**

**Current problem (shared "SA" account):**
- 5 people know password
- All use same "SA" username
- **Database logs show:** "SA logged in at 2 PM, dropped table CUSTOMERS"
- **Investigation:** "Which of the 5 people did it?" - **Cannot determine**
- **No accountability** - Anyone can deny ("wasn't me!")

**PAM solution:**

**Individual accountability:**
1. **Unique credentials:** Each admin has individual account
   - Admin-John, Admin-Sarah, Admin-Mike (not shared "SA")
2. **Session recording:** Every action recorded
   - Who: Admin-John
   - What: Dropped table CUSTOMERS
   - When: 2024-01-15 14:32:15
   - How long: 5-minute session
   - Recording: Full video of session
3. **Audit trail:** Irrefutable evidence
   - Can prove John dropped table
   - Legal evidence for termination or prosecution

**Example incident with PAM:**

**Friday 2 PM:** Production database table dropped
**Investigation:**
1. Check PAM logs: "Admin-John accessed Prod-DB-01 at 13:58 using SA vault credentials"
2. Review session recording: Video shows John executing `DROP TABLE customers;`
3. **Clear evidence:** John responsible
4. **Outcome:** John terminated, legal action possible

**Why this is PRIMARY benefit:**

**Without accountability (shared account):**
- Admins can blame each other
- No evidence for HR/legal action
- Malicious admin goes unpunished
- **More likely to abuse:** If can't get caught, why not?

**With accountability (PAM):**
- Every action attributed to individual
- Session recordings are evidence
- Admins know they're being watched → **Deterrent effect**
- Malicious actions reduced

**Other PAM benefits (secondary):**

**Credential vaulting:**
- Passwords stored encrypted, not in Excel
- Automatic rotation after use
- **But:** Even with vaulting, shared accounts still lack accountability

**Just-in-Time access:**
- Grant admin rights only when needed
- Automatic expiration
- **But:** Doesn't help if can't determine who abused access

**Password rotation:**
- Passwords changed frequently
- **But:** Shared password = everyone gets new password, still shared

**Why other answers are incomplete:**

**"Eliminates need to remember passwords":**
- True but minor benefit
- Password managers can do this without PAM
- Not addressing core security issue (accountability)

**"Prevents password sharing":**
- Partially true (password in vault, can't be written down)
- But shared accounts can still exist
- **Accountability ensures each person has individual account**

**"Reduces password reset tickets":**
- True (admins don't manage privileged passwords)
- Operational benefit, not security benefit
- Misses primary security value

**Real-world compliance requirement:**

**SOX (Sarbanes-Oxley):**
- Requires individual accountability for financial system access
- Shared accounts = SOX violation
- Auditors specifically check: "Can you prove who accessed financial data?"
- **PAM session recordings demonstrate compliance**

**PCI DSS Requirement 8:**
- "Assign a unique ID to each person with computer access"
- Shared "SA" account violates this
- Individual PAM accounts satisfy requirement

**HIPAA:**
- Requires audit controls to track who accessed ePHI
- Shared accounts make audit trail meaningless
- Individual accountability required

**Example from scenario 5:**

**Before PAM:**
- Production database deleted
- 5 people have SA password
- **Investigation:** "Who did it?" - Unknown
- **Outcome:** Everyone denies, no evidence, no accountability

**After PAM:**
- Sarah requests production database access
- **CyberArk anomaly detection:** "Sarah usually doesn't access production on Fridays"
- Security team reviews request, sees Sarah being terminated today
- **Request denied** - Incident prevented
- **If allowed:** Session recorded, clear evidence if Sarah misbehaves

**Lesson:** Accountability is deterrent AND enables investigation when incidents occur.
</details>

---

## CompTIA-Style Practice Questions

### Question 1
IT department preparing to onboard 50 new employees starting Monday. Each employee needs accounts in Active Directory, Office 365, Salesforce, Workday, and 10 other applications. Manual account creation takes 2 hours per employee.

Which solution would BEST improve efficiency and consistency?

A. Create template user accounts and copy for each new employee  
B. Implement automated provisioning integrated with HR system  
C. Train additional IT staff to handle increased workload  
D. Use PowerShell scripts to batch-create accounts in each system

<details>
<summary>Show Answer</summary>

**Correct Answer: B**

**Explanation:**

**Why B is correct (automated provisioning with HR integration):**

**How it works:**
1. HR adds new employee to HRIS (Workday, BambooHR, etc.)
2. HRIS triggers webhook/API call to Identity Management system (Okta, Azure AD)
3. Identity Management system:
   - Creates AD account based on employee data (name, department, title)
   - Assigns to appropriate groups based on role/department
   - Provisions Office 365 mailbox
   - Creates Salesforce account with appropriate profile
   - Provisions all other integrated applications
4. **Timeline:** 5-15 minutes (vs 2 hours manual)
5. Employee receives welcome email with credentials

**Benefits:**
- **Speed:** 50 employees × 2 hours = 100 hours manual vs 5 hours automated
- **Consistency:** Every Sales Rep gets exact same access (role-based)
- **Accuracy:** No typos, forgotten applications, incorrect permissions
- **Scalability:** Handles 50 or 500 employees same effort
- **Single source of truth:** HR system drives access (terminated in HR = auto-disabled everywhere)
- **Audit trail:** Automatic documentation of who got what access when
- **Compliance:** Role-based access enforces least privilege

**Example workflow:**
```
HR adds: John Doe, Sales Representative, starts 2024-01-15
↓
Identity Management detects new employee (role=Sales Rep)
↓
Applies "Sales Representative" provisioning template:
  - AD account: jdoe, Sales group, Sales OU
  - O365: Mailbox, Sales Team site access
  - Salesforce: Sales User profile, assigned to sales pipeline
  - CRM access, price list access, customer database read-only
  - Deny: Financial systems, engineering tools, admin portals
↓
Total time: 10 minutes
↓
John receives email: "Welcome! Your accounts are ready"
```

**Why A is incorrect (template user accounts):**
- **Faster than manual but still manual:** Copy template, customize name/email, assign groups (30 min/user = 25 hours for 50)
- **Error-prone:** Forgot to update email address, name typos
- **Inconsistent:** Copied wrong template (sales template vs engineer template)
- **Doesn't scale:** 50 users manageable, 500 users not feasible
- **No integration:** Doesn't connect to HR (source of truth)
- **Maintenance nightmare:** Update template, all previous users don't get update

**Why C is incorrect (train more IT staff):**
- **Doesn't solve problem:** More people doing manual work (still slow, error-prone)
- **Expensive:** Hiring cost, training time, ongoing salary
- **Doesn't scale:** What if 200 employees next month? Hire 4× staff?
- **Temporary solution:** Only addresses current problem, not future
- **Still manual:** All disadvantages of manual process remain

**Why D is incorrect (PowerShell scripts):**
- **Better than pure manual but limited:**
  - Can batch-create AD accounts ✓
  - Can create O365 mailboxes ✓
  - **Cannot easily create Salesforce accounts** (different API)
  - **Cannot create Workday accounts** (different API)
  - Need separate script for each system (10+ scripts to maintain)
- **No HR integration:** Still manually run scripts when employee starts
- **No role-based logic:** Script creates accounts but doesn't know Sales Rep vs Engineer permissions
- **Maintenance burden:** Update script when access requirements change
- **Partial automation:** Only automates account creation, not access assignment

**Automated provisioning ROI:**

**Manual process:**
- 2 hours × 50 employees = 100 hours
- IT staff hourly rate: $50/hour
- Cost: 100 hours × $50 = $5,000 per onboarding batch

**Automated provisioning:**
- Initial setup: $50k (identity management system, integration)
- Per-employee time: 15 minutes review/approval
- 50 employees × 15 min = 12.5 hours
- Cost: 12.5 hours × $50 = $625 per batch
- **Savings:** $4,375 per batch
- **Break-even:** 11 batches (550 employees)
- **Ongoing:** Handles offboarding, role changes, access reviews automatically

**Additional benefits not in original calculation:**
- **Deprovisioning:** Automatic when employee marked terminated in HR
- **Role changes:** Promotion → New access automatically granted
- **Access reviews:** Quarterly review of all access (compliance)
- **Audit trail:** Who approved, when provisioned, what access granted

**Best practices:**
- **Start with critical systems:** AD, email, primary applications first
- **Role-based templates:** Define access by role (Sales, Engineering, Finance, etc.)
- **Approval workflows:** Manager approves before provisioning
- **Exceptions handled:** Custom access requests for non-standard needs
- **Audit and adjust:** Review provisioning accuracy quarterly

This tests understanding that automation + integration is superior to manual processes or partial automation.
</details>

### Question 2
Organization using SAML for SSO between Okta (IdP) and Salesforce (SP). User reports: "When I click Salesforce in Okta dashboard, I see 'Invalid SAML Response' error."

Which component is MOST likely misconfigured?

A. User's password in Okta  
B. Certificate used to sign SAML assertion  
C. User's browser cookie settings  
D. Network firewall blocking SAML traffic

<details>
<summary>Show Answer</summary>

**Correct Answer: B**

**Explanation:**

**"Invalid SAML Response" error meaning:**
- Salesforce received SAML assertion from Okta
- Salesforce attempted to validate digital signature
- **Signature validation failed** (most common cause)
- Salesforce rejected assertion, denied access

**SAML authentication flow:**
1. User clicks Salesforce in Okta
2. Okta generates SAML assertion (XML document)
3. **Okta signs assertion with private key**
4. Assertion sent to user's browser
5. Browser posts assertion to Salesforce
6. **Salesforce validates signature using Okta's public key**
7. If signature valid → Grant access
8. If signature invalid → "Invalid SAML Response"

**Certificate mismatch scenarios:**

**Scenario 1: Certificate expired**
- Okta's signing certificate valid 2022-2024
- Certificate expired 2024-12-31
- Okta still signs with expired certificate
- Salesforce rejects (certificate no longer valid)

**Scenario 2: Certificate rotated but not updated**
- Okta administrator rotated signing certificate (security best practice)
- New certificate generated
- **Forgot to update public key in Salesforce**
- Salesforce still has old public key
- Can't validate signatures made with new private key

**Scenario 3: Wrong certificate uploaded**
- Okta has multiple certificates (signing, encryption)
- Administrator uploaded encryption certificate to Salesforce instead of signing certificate
- Signature validation fails

**How to diagnose:**
1. Export certificate from Okta: `Settings → SAML → Download signing certificate`
2. Check certificate in Salesforce: `Setup → Identity → SSO Settings → SAML metadata`
3. Compare certificate thumbprints (SHA-256 hash)
4. If different → Mismatch found

**How to fix:**
1. Download current signing certificate from Okta
2. Upload to Salesforce: `Setup → Single Sign-On Settings → Edit`
3. Paste certificate in "Identity Provider Certificate" field
4. Save
5. Test: Click Salesforce in Okta → Should work now

**Why A is incorrect (user's password):**
- **User successfully authenticated to Okta** (password correct)
- Error occurs AFTER Okta authentication, DURING Salesforce validation
- If password wrong, user couldn't access Okta dashboard
- **Password doesn't affect SAML signature validation**

**Why C is incorrect (browser cookie settings):**
- SAML flow doesn't require cookies between IdP and SP
- Cookies used within each system (Okta session cookie, Salesforce session cookie)
- SAML assertion passed via POST (form submission), not cookies
- **Browser cookie issues would cause different error** ("Session expired", not "Invalid SAML Response")

**Why D is incorrect (firewall blocking SAML):**
- **If firewall blocked SAML, user would see timeout error** ("Cannot reach server", "Connection timed out")
- "Invalid SAML Response" means Salesforce RECEIVED and PROCESSED assertion
- Firewall doesn't selectively block SAML (blocks all HTTPS or allows all)
- SAML travels over standard HTTPS (port 443) - if firewall blocks, entire Salesforce inaccessible

**Other possible certificate-related issues:**

**Certificate trust chain:**
- Salesforce requires certificate signed by trusted CA
- Self-signed certificates may be rejected
- **Solution:** Use certificate from trusted CA (DigiCert, Let's Encrypt)

**Certificate algorithm mismatch:**
- Okta signs with SHA-256
- Salesforce configured to expect SHA-1
- **Solution:** Update Salesforce to accept SHA-256

**Multiple certificates (advanced):**
- Okta has 2 signing certificates during rotation (old and new)
- Salesforce needs both public keys during overlap period
- After rotation complete, remove old certificate

**Testing certificate configuration:**

**SAML Tracer browser extension:**
1. Install SAML Tracer (Firefox/Chrome)
2. Attempt login
3. View SAML assertion
4. Check certificate in assertion
5. Verify matches certificate in Salesforce

**Manual verification:**
1. Decode SAML assertion (Base64 decode)
2. View XML signature element
3. Compare X.509 certificate with Salesforce configuration

**Best practices:**

**Certificate rotation procedure:**
1. Generate new certificate in Okta (keep old active)
2. Upload new certificate to Salesforce (both certificates now trusted)
3. Wait 24 hours (ensure propagation)
4. Activate new certificate in Okta
5. Monitor for errors
6. After 1 week, remove old certificate from Salesforce

**Certificate expiration monitoring:**
- Set reminders: 90 days, 30 days, 7 days before expiration
- Automate rotation if possible
- Test certificate updates in non-production first

**Documentation:**
- Document which certificate used for which SP
- Track expiration dates in calendar
- Runbook for certificate rotation procedure

This tests understanding of SAML authentication process and most common configuration error (certificate mismatch).
</details>

### Question 3 (Multiple Select)
Organization implementing new access control system for 1,000 employees across Sales, Engineering, Finance, and HR departments. Requirements include: different access based on department and job level, context-aware restrictions (time/location), and compliance with least privilege principle.

Which THREE access control components should be implemented? (Choose THREE)

A. Mandatory Access Control (MAC) with classification labels  
B. Role-Based Access Control (RBAC) for department-level permissions  
C. Attribute-Based Access Control (ABAC) for context-aware restrictions  
D. Discretionary Access Control (DAC) allowing users to share files  
E. Multi-Factor Authentication (MFA) for all users  
F. Just-in-Time (JIT) access for temporary elevated permissions

<details>
<summary>Show Answer</summary>

**Correct Answers: B, C, E**

**Explanation:**

These three components together provide comprehensive, layered access control:

**B - RBAC for department-level permissions (CORRECT):**

**Why needed:**
- **Department-based access:** Sales needs CRM, Engineering needs code repos, Finance needs accounting system
- **Job level differences:** Manager vs individual contributor, senior vs junior
- **Scalability:** 1,000 employees × individual permissions = unmanageable; roles scale better

**Implementation:**
```
Roles defined:
- Sales Representative: CRM (read/write), price lists (read), customer database (read)
- Sales Manager: Sales Rep permissions + reports (read), commission data (read/write)
- Software Engineer: Code repos (read/write), issue tracker (read/write), production (read-only)
- Senior Engineer: Engineer permissions + production (read/write), architecture docs (read/write)
- Accountant: QuickBooks (read/write), financial reports (read), payroll (read)
- HR Specialist: HRIS (read/write), employee data (read), payroll (read-only)
```

**Benefits:**
- **Consistency:** All Sales Reps have identical access
- **Easy onboarding:** New Sales Rep → Assign role → Done
- **Audit-friendly:** Review role permissions, not 1,000 individual users
- **Supports least privilege:** Each role has minimum necessary permissions

**C - ABAC for context-aware restrictions (CORRECT):**

**Why needed:**
- **Requirement:** "Context-aware restrictions (time/location)"
- RBAC alone can't enforce "accountants can only access financials during business hours from office network"
- ABAC adds conditions to access decisions

**Implementation:**
```
ABAC policies:

Policy 1: Financial system access
IF (user.role = Accountant) AND 
   (time.hour >= 8 AND time.hour <= 17) AND
   (network.location = office)
THEN ALLOW access to QuickBooks

Policy 2: Remote access with MFA
IF (user.role = ANY) AND 
   (network.location = external) AND
   (mfa.verified = true)
THEN ALLOW limited access

Policy 3: Production system access
IF (user.role = Senior Engineer) AND
   (request.change_ticket_approved = true)
THEN ALLOW write access to production
ELSE ALLOW read-only access

Policy 4: HR data access
IF (user.role = HR Specialist) AND
   (user.employee_id = record.assigned_hr_rep)
THEN ALLOW access
```

**Benefits:**
- **Context-aware:** Time, location, device, risk level considered
- **Dynamic:** Access changes based on conditions (office vs remote)
- **Compliance:** Enforces "minimum necessary" access
- **Flexible:** Handle complex scenarios RBAC can't

**E - MFA for all users (CORRECT):**

**Why essential:**
- **Authentication ≠ Authorization:** RBAC/ABAC determine what user can do (authorization), MFA ensures user is who they claim (authentication)
- **Prevents credential theft:** Even if password phished, attacker blocked by MFA
- **Compliance:** Most regulations require MFA (PCI DSS, NYDFS, CMMC)
- **Least privilege foundation:** Can't enforce least privilege if can't verify identity

**Implementation:**
```
MFA requirements:
- All users: Authenticator app or security key
- High-risk users (executives, finance, IT admins): Security keys (phishing-resistant)
- Remote access: MFA required regardless of role
- Administrative access: Step-up authentication (MFA again for admin tasks)
```

**Integration with RBAC/ABAC:**
```
IF (user.role = Finance Manager) AND 
   (mfa.verified = true) AND
   (time.hour >= 8 AND time.hour <= 17)
THEN ALLOW financial reports access
```

**Why MFA complements access controls:**
- RBAC: "This role has these permissions"
- ABAC: "Under these conditions"
- **MFA: "And I've verified it's actually you requesting access"**

**Together (B + C + E) provide defense in depth:**
1. **MFA:** Authenticate user identity
2. **RBAC:** Assign base permissions by role
3. **ABAC:** Apply context-aware restrictions

**Why A is incorrect (MAC):**

**Mandatory Access Control:**
- Based on security labels (Top Secret, Secret, Confidential)
- OS enforces, users can't override
- **Use case:** Military, government, intelligence agencies
- **Not suited for:** Business with departments/roles (Sales, Engineering)

**Why requirement doesn't need MAC:**
- No mention of classified data or security clearances
- "Department and job level" = RBAC, not classification labels
- "Least privilege" achievable with RBAC + ABAC

**Why D is incorrect (DAC):**

**Discretionary Access Control:**
- File owner controls permissions
- Users can share files at their discretion
- **Problem:** Conflicts with "least privilege principle"
  - Sales Rep creates customer list
  - Shares with entire Sales department
  - Junior Sales Rep shares with external partner
  - Data leak

**Why requirement contradicts DAC:**
- "Compliance with least privilege" = Centralized control needed
- DAC gives control to users (discretionary)
- Organization needs to enforce policies (not user discretion)

**DAC appropriate for:**
- Collaborative environments (Google Drive, Dropbox)
- Personal file shares
- Small organizations (<50 employees)
- **Not for:** Regulated industries, large organizations, least privilege requirements

**Why F is incorrect (JIT access):**

**Just-in-Time access:**
- Grant elevated permissions temporarily
- Automatically expire after time limit
- **Valuable but not in top 3 for this scenario**

**Why not selected:**
- **Requirement doesn't mention temporary elevated access**
- JIT is enhancement to RBAC (grant role temporarily), not replacement
- **Use case:** Developer needs production access for 4 hours to debug
  - Covered by ABAC policy: `IF request.change_ticket_approved THEN grant access for 4 hours`

**JIT is complementary:**
- Could be added after RBAC/ABAC/MFA implemented
- Part of PAM (Privileged Access Management)
- **But:** Not foundational like RBAC/ABAC/MFA

**Architecture with B + C + E:**

```
User login attempt:
  ↓
[E] MFA Authentication (verify identity)
  ↓ Authentication successful
[B] RBAC Check (what is user's role? Sales Rep)
  ↓ Base permissions assigned
[C] ABAC Evaluation:
    - Time: 2 PM ✓ (business hours)
    - Location: Office network ✓
    - Device: Company laptop ✓
  ↓ All conditions met
ALLOW access to CRM system
```

**Real-world example:**

**User:** Jane, Sales Manager
**Time:** 3 PM Tuesday
**Location:** Coffee shop WiFi
**Action:** Access customer database

**Access decision:**
1. **MFA:** Jane enters password + approves push notification ✓
2. **RBAC:** Role = Sales Manager → Permitted to access customer database ✓
3. **ABAC evaluation:**
   - Time: 3 PM ✓ (business hours)
   - Location: External WiFi ⚠️ (not office network)
   - ABAC policy: "IF external network THEN read-only AND log access"
4. **Result:** ALLOW read-only access, log for audit

**Benefits of layered approach:**
- **MFA:** Ensures it's actually Jane
- **RBAC:** Jane has Sales Manager role (authorized)
- **ABAC:** External network = read-only (risk-appropriate)

**Compliance support:**

**SOX (Sarbanes-Oxley):**
- RBAC: Segregation of duties (Finance can't approve AND record transactions)
- ABAC: Enforce business hours access to financial systems
- MFA: Verify identity for financial system access

**HIPAA:**
- RBAC: Role-based access to ePHI (doctor, nurse, billing)
- ABAC: Minimum necessary (doctor sees only their patients)
- MFA: Protect against unauthorized access

**GDPR:**
- RBAC: Define data processor roles
- ABAC: Enforce purpose limitation (access only for legitimate purpose)
- MFA: Prevent unauthorized data access

This tests understanding that comprehensive access control requires multiple complementary components working together.
</details>

---

## Related Objectives

- **4.1 Security techniques** - NAC integrates with secure baseline configurations
- **4.5 Enterprise capabilities** - NAC, email security, DLP support IAM
- **4.8 Incident response** - PAM session recordings support forensic investigation
- **5.1 Governance and compliance** - IAM supports regulatory compliance (SOX, HIPAA, PCI DSS)
- **5.2 Risk management** - Access controls mitigate insider threat risks
- **5.3 Third-party risk** - Federation enables secure partner access
- **5.4 Security compliance** - IAM audit trails support compliance reporting

---

## Quick Navigation
- [← Previous: 4.5 Enterprise Capabilities](../4-5/)
- [→ Next: 4.7 Automation and Orchestration](../4-7/)
- [↑ Back to Domain 4: Security Operations](../)
- [⌂ Security+ Home](/)
