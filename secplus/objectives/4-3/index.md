---
layout: objective
title: "4.3 Activities Associated with Vulnerability Management"
objective_id: "4.3"
domain: "4.0 Security Operations"
status: "done"
tags:
  - secplus701
permalink: /objectives/4-3/
---

## Overview

Vulnerability management is a continuous cycle of identifying, analyzing, prioritizing, remediating, and validating security weaknesses. This objective covers the complete vulnerability lifecycle from discovery through verification of fixes. Effective vulnerability management reduces the attack surface and prevents exploitation of known weaknesses.

### Identification Methods

**Vulnerability Scanning:**
- Automated tools probe systems, networks, and applications for known vulnerabilities
- Compares current state against database of known vulnerabilities (CVE database)
- **Tools:** Nessus, OpenVAS, Qualys, Rapid7 InsightVM
- **Types:**
  - **Authenticated scans** - Uses credentials to access systems, finds more vulnerabilities (patch levels, misconfigurations)
  - **Unauthenticated scans** - External perspective, finds network-level vulnerabilities, safer but less comprehensive
  - **Agent-based** - Software installed on endpoints reports vulnerabilities continuously
  - **Agentless** - Scans over network without installing software, easier deployment
- **Frequency:** Weekly minimum for critical systems, monthly for lower-risk assets
- **Limitations:** Only finds known vulnerabilities with signatures, generates false positives

**Application Security Testing:**
- **Static Analysis (SAST)** - Examines source code without execution
  - Finds: Buffer overflows, SQL injection, XSS, hardcoded credentials, insecure crypto
  - When: During development ("shift left")
  - Pros: Finds code-level issues early, pinpoints exact line of code
  - Cons: Many false positives, can't find runtime/configuration issues
- **Dynamic Analysis (DAST)** - Tests running application
  - Finds: Authentication flaws, session management issues, API vulnerabilities
  - When: Pre-production and production
  - Pros: Finds runtime issues, tests actual deployed configuration
  - Cons: Can't see source code, may miss complex code paths
- **Package Monitoring** - Tracks third-party libraries and dependencies
  - Identifies vulnerable versions of libraries (Log4j, OpenSSL, etc.)
  - Tools: OWASP Dependency-Check, Snyk, WhiteSource
  - Critical: Modern apps use hundreds of dependencies

**Threat Feeds:**
- Continuous streams of threat intelligence from security researchers, vendors, and organizations
- **Types:**
  - **Open-source intelligence (OSINT)** - Free public feeds (CVE database, NVD, MITRE ATT&CK)
  - **Proprietary/third-party** - Commercial feeds with curated, analyzed data (FireEye, CrowdStrike, Mandiant)
  - **Information-sharing organizations** - Industry groups sharing threats (FS-ISAC for financial, H-ISAC for healthcare)
  - **Dark web** - Monitoring underground forums for leaked credentials, exploit discussions
- **Use cases:** Proactive vulnerability identification, threat hunting, prioritization based on active exploitation

**Penetration Testing:**
- Simulated real-world attacks to identify exploitable vulnerabilities
- Goes beyond vulnerability scans - demonstrates actual exploitability and impact
- **Types:**
  - **Known environment (White box)** - Testers have full system knowledge and credentials
  - **Partially known environment (Gray box)** - Limited information provided
  - **Unknown environment (Black box)** - No prior knowledge, simulates external attacker
- **Scope:** Network infrastructure, web applications, wireless, social engineering, physical security
- **Output:** Detailed report showing attack paths, exploited vulnerabilities, business impact
- **Frequency:** Annually minimum, after major changes, before critical deployments

**Responsible Disclosure Programs:**
- Framework for security researchers to report vulnerabilities ethically
- **Bug Bounty Programs** - Monetary rewards for finding and reporting vulnerabilities
  - Platforms: HackerOne, Bugcrowd, Synack
  - Benefits: Crowdsourced security testing, pay per valid finding
  - Scope: Define what's in/out of scope, acceptable testing methods
- **Coordinated Vulnerability Disclosure** - Researcher reports to vendor privately, allows time to patch before public disclosure
- **Requirements:** Clear reporting process, response SLA, legal safe harbor for researchers

**System/Process Audits:**
- Comprehensive reviews of security controls, policies, and procedures
- Ensures adherence to baselines, compliance frameworks, best practices
- Identifies configuration drift, policy violations, undocumented changes

### Analysis

**Confirmation:**
- Verify vulnerabilities are real, not false positives
- **False Positive** - Scanner reports vulnerability that doesn't actually exist
  - Common causes: Outdated signatures, version detection errors, environmental factors
  - Impact: Wasted time investigating non-issues, alert fatigue
- **False Negative** - Scanner misses real vulnerability
  - More dangerous than false positives
  - Causes: Zero-day vulnerabilities, custom applications, encrypted traffic

**Prioritization:**
- Not all vulnerabilities are equal - prioritize based on risk
- **Factors to consider:**
  - Severity (CVSS score)
  - Asset criticality (production vs development, customer-facing vs internal)
  - Exploitability (is exploit code publicly available?)
  - Threat intelligence (is it being actively exploited in the wild?)
  - Compensating controls (are other protections in place?)
  - Regulatory requirements (HIPAA, PCI DSS mandates)

**Common Vulnerability Scoring System (CVSS):**
- Standard for assessing vulnerability severity
- **Score range:** 0.0 to 10.0
- **Severity ratings:**
  - 0.0: None
  - 0.1-3.9: Low
  - 4.0-6.9: Medium  
  - 7.0-8.9: High
  - 9.0-10.0: Critical
- **CVSS v3.1 metrics:**
  - **Base metrics** - Intrinsic characteristics (exploitability, impact)
  - **Temporal metrics** - Change over time (exploit code maturity, remediation level)
  - **Environmental metrics** - Organization-specific factors (business impact, controls)
- **Limitation:** Doesn't account for organizational context, threat intelligence, or compensating controls

**Common Vulnerability Enumeration (CVE):**
- Standardized identifier for publicly known vulnerabilities
- **Format:** CVE-YEAR-NUMBER (e.g., CVE-2017-0144 for EternalBlue)
- Maintained by MITRE, funded by US government
- **Provides:** Unique ID, description, references, related information
- **Benefits:** Universal language for discussing vulnerabilities, enables tool interoperability

**Vulnerability Classification:**
- Categorize by type: Network, web application, OS, database, third-party software
- Helps assign to appropriate remediation teams

**Exposure Factor:**
- Percentage of asset value lost if vulnerability exploited
- Used in risk calculations: SLE (Single Loss Expectancy) = Asset Value × Exposure Factor

**Environmental Variables:**
- Organization-specific factors affecting vulnerability risk
- Examples: Internet-facing vs internal, data sensitivity, redundancy, monitoring

**Industry/Organizational Impact:**
- Consider sector-specific threats (financial sector targeted for fraud, healthcare for PHI)
- Compliance requirements (PCI DSS prioritizes cardholder data systems)

**Risk Tolerance:**
- Organization's willingness to accept risk
- High tolerance: May accept medium-severity vulnerabilities with compensating controls
- Low tolerance: Patch even low-severity findings immediately

### Vulnerability Response and Remediation

**Patching:**
- Primary remediation method - apply vendor-provided fixes
- **Process:** Test patches in non-production → Schedule maintenance window → Deploy → Verify
- **Challenges:** Legacy systems without patches, operational downtime requirements, compatibility issues
- **Patch management tools:** WSUS (Windows), SCCM, Jamf (macOS), apt/yum (Linux)

**Insurance:**
- Cybersecurity insurance as risk transfer mechanism
- Covers: Breach response costs, legal fees, customer notification, business interruption, ransom payments
- Requires: Security controls in place, incident response plan, regular backups
- **Limitation:** Doesn't prevent incidents, only mitigates financial impact

**Segmentation:**
- Isolate vulnerable systems to limit blast radius
- If can't patch immediately, segment from critical assets
- **Methods:** VLANs, firewalls, air-gapping

**Compensating Controls:**
- Alternative measures when primary control (patching) not feasible
- **Examples:**
  - Can't patch legacy system → Deploy WAF to filter malicious traffic
  - EOL OS → Enhanced monitoring, network isolation, application whitelisting
  - Vulnerable service needed → Restrict access with firewall rules, require VPN
- Must provide equivalent protection level
- Document in risk register for audit purposes

**Exceptions and Exemptions:**
- **Exception** - Temporary deviation from security policy
  - Business justification required
  - Expiration date set
  - Compensating controls mandatory
  - Regular review to reassess
- **Exemption** - Permanent waiver
  - Reserved for legacy systems with no alternative
  - Executive approval required
  - Documented risk acceptance
  - Annual recertification

### Validation of Remediation

**Rescanning:**
- Run vulnerability scans again after patching/remediation
- **Purpose:**
  - Confirm vulnerabilities remediated
  - Detect new vulnerabilities introduced by patches
  - Identify systems where patches failed
- **Best practices:**
  - Use same scanner and credentials as initial scan
  - Wait 24-48 hours after patching for updates to propagate
  - Scan representative sample first, then full environment

**Audit:**
- **Configuration auditing** - Verify security settings unchanged
- **Patch auditing** - Confirm patches deployed to all intended systems
- **Compliance auditing** - Ensure remediation meets regulatory requirements
- **Automated tools:** Security configuration management tools, compliance scanners

**Verification:**
- Final validation that systems secure and functional
- **Methods:**
  - **Penetration testing** - Attempt to exploit previously vulnerable systems
  - **User acceptance testing** - Verify applications work correctly after patching
  - **Functional testing** - Ensure no adverse impact on system performance
  - **External audit** - Independent verification for compliance

### Reporting

**Internal Reporting:**
- Communicate vulnerability findings within organization
- **Audiences:**
  - **Technical teams** - Detailed technical data, remediation steps, CVE IDs, CVSS scores
  - **Management** - Executive summary, risk ratings, business impact, remediation timelines
  - **Board** - High-level trends, comparison to industry, major risks, investment needs
- **Frequency:** Weekly scans, monthly trend reports, quarterly executive briefings

**External Reporting:**
- Share vulnerability information outside organization when appropriate
- **Scenarios:**
  - Vendor notification of product vulnerabilities
  - Regulatory reporting (some frameworks require vulnerability disclosure)
  - Information sharing with ISACs
  - CVE database submissions for newly discovered vulnerabilities
- **Confidentiality:** Share only non-sensitive details, protect organizational specifics

---

## Key Distinctions

### False Positive vs False Negative
- **False Positive**: Scanner reports vulnerability that doesn't exist (annoying, wastes time)
- **False Negative**: Scanner misses real vulnerability (dangerous, leaves systems exposed)

### SAST vs DAST
- **SAST**: Analyzes source code, finds code-level issues, early in SDLC, many false positives
- **DAST**: Tests running app, finds runtime issues, later in SDLC, can't see code

### Exception vs Exemption  
- **Exception**: Temporary deviation with expiration date and compensating controls
- **Exemption**: Permanent waiver requiring executive approval and documented risk acceptance

### Authenticated vs Unauthenticated Scanning
- **Authenticated**: Uses credentials, sees more vulnerabilities, finds missing patches
- **Unauthenticated**: External view, safer, only finds network-level issues

### Penetration Testing vs Vulnerability Scanning
- **Vulnerability Scanning**: Automated, identifies known vulnerabilities, broad coverage, frequent
- **Penetration Testing**: Manual, demonstrates exploitability, validates impact, less frequent

---

## Common Exam Traps

1. **Trap:** Thinking CVSS score alone determines patching priority
   - **Reality:** CVSS is one input; also consider asset criticality, exploitability, threat intel, compensating controls

2. **Trap:** Believing vulnerability scans find all vulnerabilities
   - **Reality:** Only detect known vulnerabilities with signatures; zero-days and custom app vulnerabilities require other methods

3. **Trap:** Assuming penetration tests replace vulnerability scans
   - **Reality:** Complementary - scans provide broad coverage, pen tests validate exploitability; need both

4. **Trap:** Confusing bug bounty with responsible disclosure
   - **Reality:** Bug bounty pays researchers; responsible disclosure is voluntary coordinated reporting process

5. **Trap:** Thinking patch deployment equals remediation completion
   - **Reality:** Must rescan to verify patches applied successfully and didn't introduce new issues

6. **Trap:** Believing compensating controls are inferior to patching
   - **Reality:** Sometimes necessary when patching not feasible; can provide equivalent protection if properly implemented

7. **Trap:** Assuming all exceptions become exemptions
   - **Reality:** Exceptions are temporary with expiration dates; exemptions are permanent and rarely granted

---

## Exam Tips

1. **CVSS ranges:** Memorize the severity levels (None 0.0, Low 0.1-3.9, Medium 4.0-6.9, High 7.0-8.9, Critical 9.0-10.0)

2. **CVE format:** CVE-YEAR-NUMBER (e.g., CVE-2017-0144) - know the structure

3. **Scan frequency:** Critical systems weekly minimum, normal systems monthly, after major changes

4. **SAST early, DAST later:** Static analysis during development, dynamic analysis before production

5. **Validation required:** Always rescan after remediation to confirm effectiveness

6. **Compensating controls need documentation:** Must document why patching not feasible and how alternative provides equivalent protection

7. **Threat feeds prioritize:** Use threat intelligence to prioritize actively exploited vulnerabilities over theoretical ones

8. **Exceptions expire:** Temporary exceptions have expiration dates and require compensating controls

9. **Authenticated scans better:** When possible, use authenticated scans for more comprehensive vulnerability detection

10. **Bug bounty scope critical:** Always define clear scope, rules of engagement, and legal protections for researchers

---

## Key Terms

- **Vulnerability Management** - Continuous process of identifying, analyzing, prioritizing, remediating, and validating security weaknesses
- **CVSS (Common Vulnerability Scoring System)** - Standard for rating vulnerability severity on 0-10 scale
- **CVE (Common Vulnerabilities and Exposures)** - Standardized identifier for publicly known vulnerabilities
- **SAST (Static Application Security Testing)** - Source code analysis without execution
- **DAST (Dynamic Application Security Testing)** - Testing running applications for vulnerabilities
- **Penetration Testing** - Simulated attacks to validate exploitability of vulnerabilities
- **Threat Feed** - Continuous stream of threat intelligence about vulnerabilities and exploits
- **Bug Bounty** - Reward program paying researchers for vulnerability discoveries
- **Responsible Disclosure** - Ethical process for reporting vulnerabilities to vendors privately
- **False Positive** - Incorrectly identified vulnerability that doesn't actually exist
- **False Negative** - Real vulnerability missed by scanner
- **Authenticated Scan** - Vulnerability scan using credentials to access systems deeply
- **Unauthenticated Scan** - External vulnerability scan without credentials
- **OSINT (Open-Source Intelligence)** - Publicly available threat intelligence
- **Compensating Control** - Alternative security measure when primary control not feasible
- **Exception** - Temporary deviation from security policy with expiration date
- **Exemption** - Permanent waiver of security requirement
- **Exposure Factor** - Percentage of asset value lost if vulnerability exploited
- **Patch Management** - Process of testing, deploying, and verifying software updates
- **Segmentation** - Network isolation to limit blast radius of vulnerable systems
- **SCAP (Security Content Automation Protocol)** - Standard for vulnerability management automation
- **Remediation** - Process of fixing identified vulnerabilities
- **Validation** - Confirming remediation was successful through rescanning and testing
- **Risk Tolerance** - Organization's willingness to accept security risk

---

## Example Scenarios

### Scenario 1: CVSS Prioritization Challenge
**Situation:** Vulnerability scan identifies 500 vulnerabilities across organization. CISO wants top 10 prioritized for immediate remediation. Security team has:
- 50 Critical (CVSS 9.0+) vulnerabilities
- 150 High (CVSS 7.0-8.9)
- 200 Medium (CVSS 4.0-6.9)
- 100 Low (CVSS 0.1-3.9)

**Analysis approach:**
1. **Filter by exploitability** - Check threat feeds for active exploitation
2. **Consider asset criticality** - Internet-facing production systems before internal dev systems
3. **Check for compensating controls** - Systems behind WAF lower priority than unprotected
4. **Regulatory requirements** - PCI DSS systems get priority
5. **Patch availability** - Prioritize vulnerabilities with available patches

**Top 10 criteria:**
- Internet-facing + Critical CVSS + Active exploitation = Immediate (within 24 hours)
- Production database + High CVSS + Public exploit = Urgent (within 1 week)
- Internal workstation + Critical CVSS + No known exploitation = Important (within 1 month)

**Lesson:** CVSS score alone insufficient - combine with threat intelligence, asset value, and environmental context

### Scenario 2: Legacy System Exception Management
**Situation:** Manufacturing company has SCADA system running Windows XP controlling production line. System cannot be upgraded (vendor no longer supports, would void warranty on $2M equipment). Vulnerabilities: 45 Critical, 120 High.

**Proper exception process:**
1. **Document business justification** - Equipment warranty, safety certification, operational necessity
2. **Risk assessment** - Quantify impact of compromise (production shutdown = $500k/day loss)
3. **Compensating controls:**
   - Network segmentation - Air-gap from corporate network
   - Strict firewall rules - Only allow specific IPs/ports
   - Enhanced monitoring - IDS monitoring all traffic
   - Physical security - Lock SCADA room, video surveillance
   - Jump box access - Hardened intermediary for remote access
4. **Exception approval** - CISO approval, documented risk acceptance by business owner
5. **Annual review** - Reassess yearly for alternatives (new vendor support, replacement equipment)

**Key documentation:**
- Exception form with business justification
- Risk assessment showing residual risk with compensating controls
- Approval signatures (CISO, business owner, compliance officer)
- Compensating control verification evidence
- Review schedule and criteria for exception termination

**Lesson:** Exceptions require thorough documentation, strong compensating controls, and regular reassessment

### Scenario 3: False Positive Reduction
**Situation:** Security team overwhelmed with 2000+ vulnerability findings per weekly scan. 60% are false positives. Team spending 80 hours/week validating false positives instead of remediating real issues.

**Root causes identified:**
- Scanner using outdated vulnerability signatures
- Version detection errors (banner grabbing inaccurate)
- Environmental false positives (scanner flagging expected configurations)

**Remediation approach:**
1. **Update scanner** - Ensure latest vulnerability database and detection signatures
2. **Tune scanner configuration:**
   - Enable authenticated scanning (more accurate version detection)
   - Adjust sensitivity for known environmental factors
   - Whitelist known-good configurations
3. **Baseline established systems** - Mark validated clean systems as baseline for comparison
4. **Implement validation workflow:**
   - Tier 1: Automated validation against known false positives list
   - Tier 2: Technical validation by security analysts
   - Tier 3: Only confirmed vulnerabilities assigned to remediation teams
5. **Track false positive patterns** - Document recurring false positives and create suppression rules

**Results after tuning:**
- False positive rate reduced to 15%
- Validation time reduced from 80 to 15 hours/week
- Remediation teams focus on confirmed vulnerabilities
- Scan credibility improved (teams trust findings)

**Lesson:** Scanner tuning and validation workflows essential to manage false positives and maintain team effectiveness

### Scenario 4: Third-Party Library Vulnerability (Log4Shell)
**Situation:** December 2021 - Log4Shell (CVE-2021-44228) disclosed. CVSS 10.0 Critical vulnerability in Log4j library. Actively exploited worldwide within hours. Organization runs 200+ applications, many using Java.

**Response timeline:**

**Hour 0-4 (Emergency Response):**
- Emergency change control meeting convened
- Security team identifies all applications using Log4j (dependency scanning tools)
- 47 applications confirmed vulnerable

**Hour 4-24 (Triage):**
- **Immediate**: Internet-facing applications - Emergency patching outside maintenance window
- **Urgent**: Internal applications with sensitive data access
- **Normal**: Internal applications with low data sensitivity
- **Monitoring**: Enhanced IDS rules deployed to detect exploitation attempts

**Day 1-3 (Remediation):**
- Patch available applications (32 applications patched)
- **15 applications** - Vendor patch not yet available:
  - Compensating control: WAF rules deployed to block exploit patterns
  - Network segmentation: Restrict access to trusted IPs only
  - Enhanced monitoring: Alert on any Log4j exploitation indicators

**Week 1-2 (Validation):**
- Rescan all applications to confirm successful patching
- Penetration testing to validate WAF rules blocking exploits
- Review logs for any exploitation attempts (none detected)

**Week 2-4 (Lessons Learned):**
- Implement Software Bill of Materials (SBOM) for all applications
- Automated dependency checking in CI/CD pipeline
- Quarterly third-party library vulnerability reviews

**Lesson:** Zero-day vulnerabilities with active exploitation require emergency response, multiple remediation strategies, and comprehensive validation

### Scenario 5: Bug Bounty Program Launch
**Situation:** E-commerce company launching public bug bounty program to crowdsource vulnerability discovery.

**Program design:**

**Scope definition (CRITICAL):**
- **In scope:**
  - Main website (www.company.com)
  - Mobile apps (iOS/Android)
  - Public APIs
- **Out of scope:**
  - Third-party services (payment processor)
  - Physical security testing
  - Social engineering of employees
  - DoS attacks

**Rules of engagement:**
- Test only on designated test environment when possible
- Don't access/modify customer data
- Don't perform actions that degrade service
- Report vulnerabilities within 24 hours of discovery
- Allow 90 days for remediation before public disclosure

**Reward structure:**
- Critical (CVSS 9.0-10.0): $5,000-$10,000
- High (CVSS 7.0-8.9): $1,000-$5,000  
- Medium (CVSS 4.0-6.9): $250-$1,000
- Low (CVSS 0.1-3.9): $50-$250

**First 6 months results:**
- 150 vulnerability submissions
- 45 valid vulnerabilities (30% valid rate)
- 105 duplicates/false positives/out of scope
- 12 Critical findings (SQL injection, RCE, authentication bypass)
- Total paid: $75,000
- Cost of penetration testing alternative: $150,000+ annually

**Challenges encountered:**
- Duplicate submissions (first reporter gets reward)
- Report quality varies (some lack details, others excellent)
- Volume management (triage team needed)
- Researcher communication (timely updates required)

**Lesson:** Bug bounty programs cost-effective but require clear scope, fast triage, good communication, and fair reward structure

---

## Mini Quiz

### Question 1
A security analyst is reviewing vulnerability scan results and finds a vulnerability with CVSS 9.8 (Critical) on an internal development server. The server is not internet-facing, is behind multiple firewalls, and only accessible from developer workstations. Threat intelligence shows no active exploitation of this vulnerability.

What should be the analyst's NEXT step?

<details>
<summary>Show Answer</summary>

**Answer: Verify the vulnerability is not a false positive**

**Explanation:**
Before prioritizing remediation, the analyst should confirm the vulnerability is real. High CVSS scores don't guarantee the vulnerability actually exists on the system.

**Why this is correct:**
- Vulnerability scanners generate false positives, especially with version detection
- Confirming saves wasted effort remediating non-existent issues
- Internal dev server has lower immediate risk than internet-facing production

**Verification methods:**
- Check if exact vulnerable version is installed (not just banner)
- Manual testing to confirm exploitability
- Review system configuration for mitigating factors

**After confirmation, prioritization factors:**
- CVSS: 9.8 Critical (very severe)
- Asset criticality: Development server (lower than production)
- Exposure: Internal only, multiple network barriers (lower risk)
- Threat intelligence: No active exploitation (lower urgency)
- Appropriate timeline: 30 days (not emergency but should address)

**Why other approaches premature:**
- Immediately emergency patching: Wasteful if false positive
- Requesting exception: Haven't confirmed vulnerability exists yet
- Creating compensating controls: Unnecessary if vulnerability isn't real

The key principle: Always validate before acting, especially for findings on non-critical systems with high CVSS scores.
</details>

### Question 2
An organization has 500 web applications. The security team wants to implement vulnerability testing that identifies runtime issues like broken authentication and session management flaws, but the applications are written in many different languages making source code review impractical.

Which testing method is MOST appropriate?

<details>
<summary>Show Answer</summary>

**Answer: Dynamic Application Security Testing (DAST)**

**Explanation:**

**Why DAST is correct:**
- **Language agnostic** - Tests running application regardless of programming language
- **Finds runtime issues** - Specifically designed to detect authentication, session management, configuration vulnerabilities
- **Black-box approach** - Doesn't require source code access
- **Scales** - Can test 500 applications without needing language-specific tools

**Finds exactly the requested vulnerabilities:**
- Broken authentication
- Session management flaws  
- Configuration errors
- API security issues
- Authorization bypass

**Why other methods insufficient:**

**SAST (Static Analysis):**
- Requires source code in each language
- Need different tools for Java, Python, C#, Ruby, etc.
- Doesn't find runtime/configuration issues
- Impractical for 500 apps in multiple languages

**Penetration Testing:**
- Manual, doesn't scale to 500 applications
- Too expensive and time-consuming
- Best as validation, not primary testing method

**Vulnerability Scanning:**
- Finds infrastructure vulnerabilities, not application logic flaws
- Misses custom application vulnerabilities
- Doesn't test authentication/session management deeply

**Best practice combination:**
- DAST for all 500 applications (primary method)
- SAST for critical applications where source code available
- Penetration testing for highest-risk applications (annual)

This tests understanding that DAST is the right tool for large-scale application testing without source code access.
</details>

### Question 3
A financial services company discovers a critical vulnerability (CVSS 9.5) on their main transaction processing system. The vendor has released a patch, but the patch requires system downtime for 4 hours. The system processes $50M in transactions daily and cannot be taken offline during business hours without significant business impact.

What is the BEST approach?

<details>
<summary>Show Answer</summary>

**Answer: Implement compensating controls immediately while scheduling patching during next maintenance window**

**Explanation:**

**Why this is correct:**
This balances security (addressing critical vulnerability) with business continuity (avoiding unplanned downtime).

**Immediate actions (within 24 hours):**
1. **Implement compensating controls:**
   - Deploy WAF rules to filter known attack patterns
   - Enhanced monitoring with IDS alerts for exploitation attempts
   - Restrict network access to minimum required IPs
   - Increase logging verbosity for forensic capability
2. **Schedule emergency maintenance window:**
   - Weekend or overnight when transaction volume lowest
   - Communicate to business stakeholders
   - Prepare rollback plan

**Why this approach:**
- **Addresses urgency**: Critical vulnerability needs immediate response
- **Maintains availability**: $50M/day revenue protected
- **Reduces risk**: Compensating controls provide protection until patching
- **Follows change management**: Scheduled window allows proper testing

**Why other options inadequate:**

**Immediate emergency patching (unscheduled):**
- 4-hour downtime = ~$8M revenue loss
- Insufficient time for testing patch
- Could introduce new issues
- Business impact unacceptable

**Request exemption:**
- Exemptions for permanent situations (legacy systems)
- Vendor provides patch - exemption inappropriate
- Critical CVSS 9.5 too severe to exempt

**Wait for regular maintenance (weeks away):**
- Leaves critical vulnerability exposed too long
- CVSS 9.5 + financial data = unacceptable risk
- Need compensating controls at minimum

**Accept the risk:**
- Not appropriate for CVSS 9.5 critical finding
- Financial services regulatory requirements
- Fiduciary duty to protect customer funds

**Follow-up within 7 days:**
- Test patch in dev/staging environment
- Deploy patch during scheduled maintenance window
- Rescan to validate remediation
- Remove compensating controls after validation

This tests understanding that compensating controls allow balancing security urgency with operational requirements while planning proper remediation.
</details>

### Question 4
A security team receives 15 different reports of the same SQL injection vulnerability from their bug bounty program within 2 hours. All submissions include proof of concept and detailed steps to reproduce.

How should the team handle these submissions?

<details>
<summary>Show Answer</summary>

**Answer: Award the first valid submission, close others as duplicates, and immediately begin remediation**

**Explanation:**

**Proper bug bounty handling:**

1. **Determine first reporter:**
   - Review submission timestamps
   - First complete, valid report wins
   - Subsequent reports closed as duplicates

2. **Award structure:**
   - **First reporter**: Full reward based on severity (SQL injection typically High-Critical)
   - **Duplicate reporters**: Notify submissions are duplicates, no reward
   - **Communication**: Thank all researchers, explain duplicate policy

3. **Immediate remediation:**
   - SQL injection is typically CVSS 8.0+ (High to Critical)
   - Begin fixing immediately
   - Update all researchers on fix progress

4. **Response timeline communication:**
   - Acknowledge receipt to first reporter within 24 hours
   - Provide remediation timeline (e.g., "fix within 7 days")
   - Keep researcher updated on progress
   - Notify when fixed and validated

**Why this approach:**

**Rewards first discovery:**
- Incentivizes quick reporting
- Fair to researcher who found it first
- Standard bug bounty practice

**Prevents duplicate payments:**
- Organization shouldn't pay 15× for same vulnerability
- Clear policy prevents disputes
- Resources allocated to remediation, not payments

**Maintains researcher relationships:**
- Professional communication even to duplicate submitters
- Thank all for participation
- Encourages future submissions

**Why other approaches wrong:**

**Paying all 15 researchers:**
- Financially unsustainable ($75k instead of $5k)
- Doesn't incentivize speed
- Creates perverse incentive to share vulnerabilities

**Averaging reward among all:**
- Unfair to first reporter
- Complex to administer
- Not standard practice

**Paying none until remediation complete:**
- Violates trust with researchers
- May delay reporting in future
- Standard practice pays within 30 days of validation

**Not communicating with duplicate reporters:**
- Damages program reputation
- Researchers don't know their status
- May submit elsewhere or publicly disclose

**Key policy elements for bug bounty:**
- Clear "first to report" rule in program terms
- Fast triage (validate within 24-48 hours)
- Communication with all submitters
- Defined payment timeline
- Public status dashboard for submissions

This tests understanding of proper bug bounty program operation and researcher relationship management.
</details>

### Question 5
After deploying patches to remediate critical vulnerabilities, the security team rescans and finds 12 out of 100 patched systems still show the vulnerabilities. Investigation reveals the patches were successfully deployed to all systems.

What is the MOST likely cause?

<details>
<summary>Show Answer</summary>

**Answer: Systems require reboot to complete patch installation**

**Explanation:**

**Why this is most likely:**
Many patches, especially OS-level and kernel patches, require system restart to take effect:
- Windows updates typically require reboot
- Linux kernel patches need reboot
- Some application updates need service restart
- Files locked during normal operation can only update during reboot

**Why scanner still detects vulnerability:**
- Scanner checks running version in memory
- Patched files on disk but old code still running
- After reboot, scanner will show vulnerability remediated

**Verification process:**
1. Check patch deployment logs - confirm successful installation
2. Verify reboot status of affected 12 systems
3. Schedule reboots during maintenance window
4. Rescan after reboots to confirm remediation

**Why other causes less likely:**

**Patches failed to install:**
- Investigation confirmed successful deployment
- Would show in patch management logs if failed
- 88% success rate unlikely with failed installs

**False positive from scanner:**
- Unlikely to affect exactly 12 systems consistently
- Same vulnerability on different systems
- Scanner correctly detected before patching

**Vulnerability still present in latest patch:**
- Vendor wouldn't release ineffective patch
- Other 88 systems successfully remediated
- Would affect all 100 systems, not just 12

**Systems have different vulnerability:**
- Scanner identified same CVE
- Investigation confirmed same vulnerability
- Patches targeted correct issue

**Best practices to prevent this:**
1. **Patch deployment process includes:**
   - Deploy patches
   - Reboot systems (scheduled)
   - Verify services running
   - Rescan 24-48 hours after reboot
2. **Patch documentation notes:**
   - Which patches require reboot
   - Maintenance window planning
   - Verification checklist
3. **Automated remediation:**
   - Some tools schedule automatic reboot
   - Staged rollout (test group → production)
   - Monitoring for successful completion

**Communication:**
- Inform stakeholders reboot required
- Schedule maintenance windows
- Balance security urgency with availability requirements

This tests understanding that patch deployment is a multi-step process and vulnerability persistence often indicates incomplete deployment (missing reboot) rather than patch failure.
</details>

---

## CompTIA-Style Practice Questions

### Question 1
A security analyst is reviewing the organization's vulnerability management process. Currently, vulnerability scans run monthly, and high-severity findings are remediated within 30 days. A recent audit identified several systems compromised through vulnerabilities that were known and had patches available for over 90 days.

Which change to the vulnerability management process would MOST effectively prevent future compromises?

A. Increase scan frequency to weekly for all systems  
B. Reduce remediation SLA for high-severity findings to 7 days  
C. Implement continuous monitoring with automated patching  
D. Require monthly scanning reports to be reviewed by executive team

<details>
<summary>Show Answer</summary>

**Correct Answer: C**

**Explanation:**

**Why C is correct:**
The problem is that vulnerabilities existed for 90+ days despite monthly scanning and 30-day remediation SLA. This indicates:
- Monthly scans only catch issues 0-30 days after introduction
- 30-day remediation window too long (allows 60-day exposure total)
- Systems compromised during this exposure window

**Continuous monitoring with automated patching addresses:**
- **Immediate detection** - Identifies vulnerabilities as soon as systems vulnerable or patches released
- **Automated remediation** - Deploys patches automatically within hours/days, not weeks
- **Consistent application** - Removes human delay factors
- **Validates deployment** - Confirms patches successfully applied

This reduces exposure window from 60 days (monthly scan + 30-day remediation) to <7 days.

**Why A is insufficient:**
- Weekly scanning improves detection (30 days → 7 days)
- Still has 30-day remediation window
- Total exposure: ~37 days (still allows compromise)
- Doesn't address remediation delay (root cause)

**Why B is incomplete:**
- Reduces remediation time (30 days → 7 days)
- Still has monthly detection delay (up to 30 days)
- Total exposure: ~37 days
- Doesn't address detection delay

**Why D is ineffective:**
- Executive review doesn't reduce exposure time
- Governance without operational improvement
- May increase awareness but doesn't prevent compromise
- Root cause is process timing, not oversight

**Best practice implementation:**
1. Automated patch management for critical systems
2. Testing in development before production deployment
3. Staged rollout (pilot → full deployment)
4. Rollback capability for problematic patches
5. Exceptions for systems requiring manual testing

**Real-world considerations:**
- Not all patches can be automated (legacy systems, vendor testing requirements)
- Balance automation with testing and stability
- Some high-risk systems need manual review
- Continuous monitoring provides data for prioritization

This tests understanding that vulnerability management effectiveness depends on both detection speed AND remediation speed, and that automation addresses both factors.
</details>

### Question 2
A penetration tester discovered a vulnerability during an assessment that is not in any CVE database and has no CVSS score assigned. The vulnerability allows remote code execution on the organization's web application server. The tester reported it through the responsible disclosure program.

What should the security team do FIRST?

A. Assign a CVSS score based on the CVSS calculator and remediate  
B. Submit the vulnerability to MITRE for CVE assignment  
C. Verify the vulnerability is real by reproducing the steps in a test environment  
D. Implement a web application firewall to block the exploitation

<details>
<summary>Show Answer</summary>

**Correct Answer: C**

**Explanation:**

**Why C is correct:**
Before taking any remediation action, the team must confirm the vulnerability actually exists:

**Verification process:**
1. Review penetration tester's report and proof of concept
2. Reproduce the vulnerability in test/development environment
3. Confirm it works on production-like configuration
4. Document the exploitation steps and impact

**Why verification first:**
- Penetration testers can make mistakes (false positives)
- Understanding exact exploitation mechanism guides remediation
- Testing in safe environment prevents production disruption
- Confirms scope and impact of vulnerability
- Zero-day findings need careful validation

**After verification, proceed to:**
1. Assess severity and business impact
2. Develop remediation plan
3. Implement fix and compensating controls
4. Validate fix effectiveness
5. Consider CVE assignment for documentation

**Why A is premature:**
- Assigning CVSS before confirming vulnerability exists wastes effort
- Need to understand exploitation details to accurately score
- Verification informs accurate CVSS assessment
- After verification, yes - score and remediate

**Why B is not first priority:**
- CVE assignment useful for documentation but not urgent
- Remediation more important than bureaucratic process
- Can submit for CVE after fixing vulnerability
- MITRE CVE assignment can take weeks/months
- Internal tracking doesn't require external CVE

**Why D jumps ahead:**
- WAF might not block this specific vulnerability
- Don't know attack vector without verification
- Compensating control without understanding vulnerability is guesswork
- WAF is appropriate AFTER verification while developing fix

**Proper sequence:**
1. **Verify** - Confirm vulnerability real (FIRST - this question)
2. **Assess** - Score severity, identify impact
3. **Protect** - Implement compensating controls (WAF, monitoring)
4. **Remediate** - Develop and deploy fix
5. **Validate** - Confirm fix works
6. **Document** - Consider CVE assignment

**Zero-day vulnerability handling:**
- Extra care with verification (new vulnerability type)
- Document thoroughly for future reference
- Consider responsible disclosure timeline
- Thank researcher, award appropriate bounty
- Monitor threat intelligence for similar vulnerabilities

**Communication:**
- Acknowledge researcher's report within 24 hours
- Provide timeline for verification and fix
- Keep researcher updated on progress
- Coordinate public disclosure after fix deployed

This tests understanding that vulnerability verification comes before all other actions, especially for zero-day vulnerabilities from external researchers.
</details>

### Question 3 (Multiple Select)
An organization is implementing a comprehensive vulnerability management program. The program must address applications, infrastructure, and third-party components while supporting compliance requirements.

Which THREE activities are essential components of this program? (Choose THREE)

A. Monthly penetration testing of all systems  
B. Automated vulnerability scanning with risk-based prioritization  
C. Defined remediation SLAs based on vulnerability severity  
D. Annual security awareness training for all employees  
E. Validation of remediation through rescanning and testing  
F. Implementation of zero-trust architecture

<details>
<summary>Show Answer</summary>

**Correct Answers: B, C, E**

**Explanation:**

These three form the core vulnerability management lifecycle:

**B - Automated scanning with risk-based prioritization (CORRECT):**
- **Automated scanning** provides continuous identification:
  - Infrastructure vulnerabilities (OS, network devices)
  - Application vulnerabilities (web apps, APIs)
  - Third-party components (libraries, dependencies)
- **Risk-based prioritization** ensures efficient remediation:
  - CVSS score
  - Asset criticality
  - Exploitability
  - Threat intelligence
  - Compensating controls
- Addresses "applications, infrastructure, third-party components" requirement
- Supports compliance (regular scanning mandated by PCI DSS, HIPAA)

**C - Defined remediation SLAs based on severity (CORRECT):**
- Ensures timely response to vulnerabilities
- **Typical SLAs:**
  - Critical (CVSS 9.0-10.0): 7-14 days
  - High (CVSS 7.0-8.9): 30 days
  - Medium (CVSS 4.0-6.9): 90 days
  - Low (CVSS 0.1-3.9): 180 days or risk accept
- Compliance frameworks require defined remediation timelines
- Provides accountability and measurable metrics
- Balances security urgency with operational reality

**E - Validation through rescanning and testing (CORRECT):**
- Confirms remediation was successful:
  - Rescanning verifies vulnerability no longer detected
  - Testing confirms system functionality maintained
  - Penetration testing validates not still exploitable
- Essential for compliance (must prove fixes effective)
- Detects failed patches and new vulnerabilities introduced
- Closes vulnerability management loop
- Without validation, organization doesn't know if secure

**Together these form complete cycle:**
1. Identify (B - Automated scanning)
2. Prioritize (B - Risk-based)
3. Remediate (C - Within SLAs)
4. Validate (E - Rescan and test)
5. Repeat (Continuous process)

**Why A is incorrect:**
- **Monthly penetration testing of ALL systems:**
  - Too expensive and time-consuming
  - Penetration testing complements, doesn't replace scanning
  - Annual pen testing typical, not monthly
  - Targeted pen testing on critical systems sufficient
- Good practice: Annual pen testing + quarterly for critical systems

**Why D is incorrect:**
- **Security awareness training:**
  - Important for overall security program
  - Not specific to vulnerability management
  - Addresses human risk, not technical vulnerabilities
  - Different domain (security awareness vs vulnerability management)
- Training reduces social engineering, not system vulnerabilities

**Why F is incorrect:**
- **Zero-trust architecture:**
  - Security architecture principle
  - Not vulnerability management activity
  - Complementary to vulnerability management but different domain
  - Reduces blast radius but doesn't identify/fix vulnerabilities
- Zero-trust helps limit damage if system compromised, doesn't prevent compromise

**Comprehensive program includes:**
- Core: B + C + E (vulnerability management cycle)
- Supporting: Threat intelligence feeds, exception process, metrics/reporting
- Complementary: Pen testing (annual), architecture reviews, training

This tests understanding of the essential vulnerability management cycle: identify → prioritize → remediate → validate, versus activities that support security but aren't core vulnerability management.
</details>

---

## Related Objectives

- **2.3 Explain various types of vulnerabilities** - Categories of vulnerabilities that this process identifies
- **2.4 Analyze indicators of malicious activity** - Exploitation of vulnerabilities creates IoCs
- **2.5 Mitigation techniques** - Patching, segmentation, compensating controls
- **4.1 Security techniques** - Hardening reduces vulnerabilities
- **4.4 Security alerting and monitoring** - Detection of vulnerability exploitation

---

## Quick Navigation
- [← Previous: 4.2 Asset Management](../4-2/)
- [→ Next: 4.4 Security Alerting and Monitoring](../4-4/)
- [↑ Back to Domain 4: Security Operations](../)
- [⌂ Security+ Home](/)
