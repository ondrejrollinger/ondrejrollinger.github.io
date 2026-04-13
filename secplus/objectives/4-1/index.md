---
layout: objective
title: "4.1 Apply Common Security Techniques to Computing Resources"
objective_id: "4.1"
domain: "4.0 Security Operations"
status: "done"
tags:
  - secplus701
permalink: /objectives/4-1/
---

## Overview

Securing computing resources requires a layered approach combining baseline establishment, system hardening, mobile device management, wireless security, and application security. This objective covers practical security techniques applied across workstations, servers, mobile devices, wireless infrastructure, and applications.

{% assign objective_slug = page.slug %}
{% if objective_slug == nil or objective_slug == ‘’ or objective_slug == ‘index’ %}
  {% assign url_parts = page.url | split: ‘/’ %}
  {% assign objective_slug = url_parts | last %}
  {% if objective_slug == ‘’ %}
    {% assign objective_slug = url_parts | slice: -2, 1 | first %}
  {% endif %}
{% endif %}
{% assign objective_id = objective_slug | replace: ‘-’, ‘.’ %}
{% include official_scope_pdf.html objective_id=objective_id %}

---

## My notes

### Secure Baselines

**Baseline** = A reference configuration representing the minimum security requirements for a system

**Three phases:**
1. **Establish** - Define security requirements based on industry standards (CIS Benchmarks, NIST guidelines), regulatory requirements, and organizational policies
2. **Deploy** - Implement baseline configurations across systems using automation tools (Group Policy, configuration management)
3. **Maintain** - Regularly review and update baselines, verify compliance through auditing, remediate deviations

**Why baselines matter:**
- Ensure consistent security posture across all systems
- Simplify compliance auditing and reporting
- Provide a known-good state for comparison when investigating incidents
- Reduce attack surface by disabling unnecessary services and features

### Hardening Targets

**Hardening** = Reducing attack surface by removing unnecessary services, closing ports, restricting permissions, and applying security configurations

**Target systems:**
- **Mobile devices** - Enforce encryption, disable debugging modes, restrict app installations, implement remote wipe
- **Workstations** - Disable unnecessary services, enable host-based firewalls, implement application whitelisting, enforce screen locks
- **Switches** - Disable unused ports, implement port security (MAC filtering), enable DHCP snooping, configure VLANs
- **Routers** - Change default credentials, disable unused interfaces, implement ACLs, enable logging
- **Cloud infrastructure** - Implement least privilege IAM policies, enable encryption at rest/transit, configure security groups, enable logging (CloudTrail, Azure Monitor)
- **Servers** - Minimize installed software, patch regularly, implement host-based IPS, configure file integrity monitoring
- **ICS/SCADA** - Air-gap from corporate networks when possible, implement vendor-approved patches carefully, use network segmentation, restrict physical access
- **Embedded systems** - Update firmware regularly, disable unnecessary protocols, implement secure boot, restrict physical interfaces
- **RTOS (Real-Time Operating System)** - Minimize code footprint, implement input validation, use memory protection, conduct security testing
- **IoT devices** - Change default credentials immediately, segment from main network, disable UPnP, update firmware regularly

### Wireless Security

**Installation considerations:**
- **Site surveys** - Physical walkthrough to identify optimal access point placement, sources of interference, coverage gaps, and potential unauthorized APs
- **Heat maps** - Visual representation of wireless signal strength across facility showing coverage areas, dead zones, and signal overlap

**Wireless security settings:**
- **WPA3 (Wi-Fi Protected Access 3)** - Latest wireless security standard with enhanced encryption (192-bit in Enterprise mode), protection against offline dictionary attacks (SAE - Simultaneous Authentication of Equals), forward secrecy
- **AAA/RADIUS** - Authentication, Authorization, Accounting using Remote Authentication Dial-In User Service for centralized credential management
- **Cryptographic protocols** - AES-256 encryption (WPA3), GCMP-256 (Galois/Counter Mode Protocol) for Enterprise
- **Authentication protocols** - 802.1X with EAP variants (see below)

**EAP (Extensible Authentication Protocol) variants:**
- **EAP-MD5** - Simple password-based, one-way authentication only, NOT RECOMMENDED (vulnerable to dictionary attacks)
- **EAP-TLS** - Most secure, requires certificates on both client and server, mutual authentication
- **EAP-TTLS** - Certificate on server only, client uses password, creates TLS tunnel
- **EAP-FAST** - Cisco proprietary, uses Protected Access Credential (PAC) instead of certificates
- **PEAP (Protected EAP)** - Similar to EAP-TTLS, Microsoft/Cisco/RSA collaboration, uses server certificate and Active Directory authentication
- **LEAP** - Cisco proprietary, legacy only, vulnerable to dictionary attacks, should NOT be used

### Mobile Solutions

**Mobile Device Management (MDM):**
- Centralized platform to manage, monitor, and secure mobile devices
- **Capabilities:** Remote configuration, app deployment, policy enforcement, remote lock/wipe, inventory tracking, compliance reporting
- **Use cases:** Enforce encryption, prevent jailbreaking/rooting, control app installations, implement containerization (separate work/personal data)

**Deployment models:**
- **BYOD (Bring Your Own Device)** - Employees use personal devices for work
  - Pros: Cost savings, employee satisfaction, device familiarity
  - Cons: Limited security control, privacy concerns, compatibility challenges, support complexity
- **COPE (Corporate-Owned, Personally Enabled)** - Company provides devices, employees can use for personal tasks
  - Pros: Full security control, standardized hardware, MDM enforcement
  - Cons: Higher initial cost, employee privacy concerns, may need to carry two devices
- **CYOD (Choose Your Own Device)** - Employees select from company-approved device list
  - Pros: Balance of choice and control, standardized support, better security than BYOD
  - Cons: Higher cost than BYOD, limited device selection

**Connection methods:**
- **Cellular** - Most secure for sensitive data, encrypted by carrier, not susceptible to local network attacks
- **Wi-Fi** - Vulnerable on open networks, require WPA3 and VPN for security, prefer known/trusted networks
- **Bluetooth** - Short-range, vulnerable to bluejacking/bluesnarfing, should be non-discoverable when not pairing, use encryption for sensitive transfers

### Application Security

**Input validation:**
- Verify all input data matches expected format, type, length, and range
- Whitelist acceptable inputs rather than blacklist malicious patterns
- Validate on both client-side (user experience) and server-side (security)
- Prevents SQL injection, XSS, buffer overflows, command injection

**Secure cookies:**
- **Secure flag** - Cookie only transmitted over HTTPS, prevents interception on unencrypted connections
- **HttpOnly flag** - Cookie inaccessible to JavaScript, prevents XSS attacks from stealing session tokens
- **SameSite attribute** - Controls cross-site cookie sending (Strict/Lax/None), prevents CSRF attacks
- **Expiration** - Set appropriate expiration times, use session cookies for sensitive operations

**Static code analysis (SAST):**
- Examines source code without executing it
- Identifies vulnerabilities: buffer overflows, SQL injection, XSS, hardcoded credentials, insecure crypto
- Performed early in development cycle (shift left)
- Tools: SonarQube, Checkmarx, Fortify

**Dynamic code analysis (DAST):**
- Tests running application through black-box testing
- Simulates attacks against web applications and APIs
- Identifies runtime vulnerabilities: authentication flaws, session management issues, configuration errors
- Tools: OWASP ZAP, Burp Suite

**Code signing:**
- Digital signature applied to executables and scripts
- Verifies publisher identity and code integrity
- Prevents tampering after release
- Does NOT guarantee code is vulnerability-free, only that it hasn't been modified since signing

### Sandboxing

**Sandboxing** = Isolated environment where untested or untrusted code can run without affecting the host system

**Use cases:**
- Test suspicious files or applications safely
- Run legacy applications with known vulnerabilities
- Analyze malware behavior
- Browser isolation for high-risk web browsing
- Mobile app containerization

**Implementation methods:**
- **Virtual machines** - Complete OS isolation, highest security but resource-intensive
- **Containers** - Lightweight isolation, shared kernel, good balance of security and performance
- **Application-level** - Java sandbox, browser sandbox (iframe sandbox attribute)
- **Hardware-based** - Intel VT-x, AMD-V for virtualization support

### Monitoring

**Continuous monitoring** ensures security controls remain effective and detects anomalies

**What to monitor:**
- System performance (CPU, memory, disk, network utilization)
- Security events (failed logins, privilege escalations, policy violations)
- Application behavior (response times, error rates, unusual API calls)
- Network traffic (bandwidth usage, connection patterns, protocol anomalies)
- Configuration changes (file modifications, registry changes, permission updates)

**Monitoring approaches:**
- **Agent-based** - Software installed on endpoints collects and reports data (more detailed, requires maintenance)
- **Agentless** - Uses existing protocols (SNMP, WMI, SSH) to query systems (easier deployment, less granular)
- **Log aggregation** - Centralize logs from all sources into SIEM for correlation and analysis

---

## Key Distinctions

### BYOD vs COPE vs CYOD
- **BYOD**: Employee owns, lowest cost, least control, privacy concerns
- **COPE**: Company owns, highest cost, most control, standardized security
- **CYOD**: Hybrid approach, moderate cost, balanced control, limited choice

### EAP-TLS vs EAP-TTLS vs PEAP
- **EAP-TLS**: Certificates on BOTH client and server, most secure, complex deployment
- **EAP-TTLS**: Certificate on server only, client uses password, simpler than EAP-TLS
- **PEAP**: Similar to EAP-TTLS, Microsoft/Cisco standard, uses MSCHAPv2 typically

### Static vs Dynamic Code Analysis
- **Static (SAST)**: Analyzes source code, finds coding errors, early in SDLC, many false positives
- **Dynamic (DAST)**: Tests running app, finds runtime issues, later in SDLC, misses code-level flaws

### WPA2 vs WPA3
- **WPA2**: AES encryption, PSK vulnerable to offline attacks, 802.11i standard
- **WPA3**: SAE (Dragonfly) replaces PSK, forward secrecy, 192-bit security (Enterprise), stronger protection

### Baseline vs Hardening
- **Baseline**: Minimum security configuration standard applied to all similar systems
- **Hardening**: Process of implementing baseline + additional security measures to reduce attack surface

---

## Common Exam Traps

1. **Trap:** Assuming WPA3 eliminates need for RADIUS/802.1X
   - **Reality:** WPA3-Enterprise still uses 802.1X with RADIUS for enterprise authentication; WPA3-Personal uses SAE instead of PSK

2. **Trap:** Thinking BYOD is always cheaper than COPE
   - **Reality:** Hidden costs in BYOD include MDM licensing, increased support complexity, security tools, and potential data breach costs

3. **Trap:** Believing code signing guarantees secure code
   - **Reality:** Code signing only verifies publisher identity and detects tampering; signed code can still contain vulnerabilities

4. **Trap:** Confusing static analysis with runtime testing
   - **Reality:** SAST analyzes source code without execution; DAST tests running applications

5. **Trap:** Assuming baselines are "set and forget"
   - **Reality:** Baselines must be regularly reviewed and updated as threats evolve and new vulnerabilities emerge

6. **Trap:** Thinking all EAP methods provide equal security
   - **Reality:** EAP-MD5 and LEAP are insecure; EAP-TLS is most secure but complex; PEAP and EAP-TTLS balance security and usability

7. **Trap:** Believing sandboxing provides complete security
   - **Reality:** Sandbox escapes are possible; sandboxing is one layer in defense-in-depth

---

## Exam Tips

1. **Site surveys before deployment:** Always conduct site surveys and create heat maps BEFORE deploying wireless access points to ensure proper coverage and identify interference

2. **WPA3 for new deployments:** For scenario questions about new wireless networks, recommend WPA3; for legacy compatibility, WPA2-Enterprise with 802.1X

3. **COPE for maximum control:** When security control is the priority (healthcare, finance, government), recommend COPE deployment model

4. **EAP-TLS when possible:** If certificates can be managed, EAP-TLS provides strongest wireless authentication; PEAP is acceptable alternative when client certificates are impractical

5. **Input validation at both layers:** Always validate input on both client (user experience) AND server (security) - client-side only is NOT sufficient

6. **Hardening ICS/SCADA carefully:** ICS/SCADA systems require careful patching during planned maintenance windows - availability often outweighs applying immediate patches

7. **Baseline before hardening:** Establish a secure baseline FIRST, then apply additional hardening as needed; baselines ensure consistency across similar systems

8. **Agentless for minimal impact:** In environments where installing agents is problematic (legacy systems, IoT), agentless monitoring is preferred

9. **Sandbox untrusted code:** When testing suspicious files, running legacy apps, or analyzing malware, always use sandboxing to prevent host system compromise

10. **MDM for all mobile models:** Regardless of deployment model (BYOD/COPE/CYOD), MDM is essential for policy enforcement and device management

---

## Key Terms

- **Baseline** - Reference configuration representing minimum security requirements for a system type
- **Hardening** - Process of reducing attack surface by removing unnecessary services, closing ports, and applying security configurations
- **Site survey** - Physical assessment to determine optimal wireless access point placement and identify sources of interference
- **Heat map** - Visual representation of wireless signal strength showing coverage areas and dead zones
- **WPA3** - Latest Wi-Fi security standard with enhanced encryption and protection against offline attacks
- **SAE (Simultaneous Authentication of Equals)** - WPA3 handshake replacing vulnerable PSK, resistant to offline dictionary attacks
- **802.1X** - Port-based network access control standard requiring authentication before network access
- **EAP (Extensible Authentication Protocol)** - Framework for multiple authentication methods used with 802.1X
- **RADIUS (Remote Authentication Dial-In User Service)** - Centralized authentication server for AAA services
- **MDM (Mobile Device Management)** - Centralized platform to manage, monitor, and secure mobile devices
- **BYOD (Bring Your Own Device)** - Deployment model where employees use personal devices for work
- **COPE (Corporate-Owned, Personally Enabled)** - Deployment model where company provides devices employees can use personally
- **CYOD (Choose Your Own Device)** - Deployment model where employees select from company-approved device list
- **Input validation** - Verifying all input data matches expected format, type, length, and range before processing
- **Secure cookie** - Cookie with Secure, HttpOnly, and SameSite attributes to prevent interception and XSS/CSRF attacks
- **SAST (Static Application Security Testing)** - Analyzing source code without execution to identify vulnerabilities
- **DAST (Dynamic Application Security Testing)** - Testing running applications through simulated attacks to find runtime vulnerabilities
- **Code signing** - Digital signature applied to code to verify publisher identity and detect tampering
- **Sandboxing** - Isolated environment where untested code runs without affecting host system
- **Agent-based monitoring** - Software installed on endpoints to collect and report security data
- **Agentless monitoring** - Using existing protocols to query systems without installing additional software
- **ICS (Industrial Control Systems)** - Operational technology systems controlling industrial processes
- **SCADA (Supervisory Control and Data Acquisition)** - Systems monitoring and controlling industrial equipment
- **RTOS (Real-Time Operating System)** - OS designed for time-critical applications requiring guaranteed response times
- **Containerization** - Separating work and personal data on mobile devices into isolated containers
- **Jailbreaking/Rooting** - Removing manufacturer restrictions to gain elevated privileges on mobile devices
- **Remote wipe** - MDM capability to erase all data from lost or stolen device remotely
- **UPnP (Universal Plug and Play)** - Protocol allowing devices to discover each other, often exploited on IoT devices

---

## Example Scenarios

### Scenario 1: Wireless Network Deployment
**Situation:** Company is deploying new wireless network across 3-story office building. Security team must ensure secure implementation.

**Analysis:**
- Conduct physical site survey of all three floors
- Create heat maps showing coverage areas and dead zones
- Place access points to eliminate coverage gaps while minimizing overlap
- Identify sources of interference (microwaves, Bluetooth devices, neighboring networks)
- Configure WPA3-Enterprise with 802.1X authentication
- Implement RADIUS server for centralized credential management
- Use EAP-TLS for highest security (requires certificate deployment) or PEAP as acceptable alternative
- Segment wireless network from wired corporate network using VLANs
- Deploy wireless IDS to detect rogue access points

**Key point:** Site survey and heat maps BEFORE deployment ensure proper coverage; WPA3-Enterprise with 802.1X provides enterprise-grade security

### Scenario 2: Mobile Device Deployment
**Situation:** Healthcare organization needs mobile device strategy for doctors and nurses accessing patient records. HIPAA compliance required.

**Analysis:**
- Recommend COPE model for maximum security control
- Deploy MDM solution to enforce security policies
- Required MDM policies: full-device encryption, complex passcodes, automatic screen lock (2 minutes), remote wipe capability, prohibit jailbreaking/rooting
- Containerize work data to separate from personal apps
- Restrict app installations to approved medical applications only
- Enforce VPN for all network connections
- Enable geo-fencing to wipe device if it leaves hospital premises
- Implement certificate-based authentication for accessing EHR systems
- Regular compliance audits through MDM reporting

**Key point:** COPE model with strict MDM policies ensures HIPAA compliance; containerization protects patient data even on personally-enabled devices

### Scenario 3: Application Security Implementation
**Situation:** Web application handles sensitive financial data. Security team must implement defense-in-depth for application layer.

**Analysis:**
- Implement input validation on ALL user inputs (forms, APIs, URL parameters)
- Validate on both client-side (user experience) and server-side (security)
- Use whitelist approach: define acceptable input patterns rather than blocking malicious ones
- Configure secure cookies: Secure flag (HTTPS only), HttpOnly (prevent XSS), SameSite=Strict (prevent CSRF)
- Implement SAST in development pipeline to catch coding errors early
- Run DAST before production deployment to test runtime vulnerabilities
- Sign all production code to ensure integrity and verify publisher
- Deploy WAF to provide additional layer of protection against injection attacks
- Sandbox third-party JavaScript libraries to limit damage if compromised
- Implement CSP (Content Security Policy) headers to prevent XSS

**Key point:** Defense-in-depth: input validation + secure cookies + code analysis + signing + WAF provides layered protection

### Scenario 4: ICS/SCADA Hardening
**Situation:** Manufacturing plant operates critical SCADA systems controlling production line. Systems cannot tolerate downtime.

**Analysis:**
- Air-gap SCADA network from corporate network (no direct internet connectivity)
- If connectivity required, use unidirectional gateway (data can flow out for monitoring, nothing flows in)
- Implement network segmentation using separate VLANs for different control zones
- Change ALL default credentials on SCADA devices immediately
- Disable unnecessary services and protocols on HMI (Human-Machine Interface) systems
- Patch systems only during planned maintenance windows after testing in isolated environment
- Implement strict physical access controls to SCADA equipment rooms
- Use jump servers for remote access - never allow direct connections
- Deploy passive network monitoring (no inline devices that could impact availability)
- Maintain detailed asset inventory with firmware versions
- Establish vendor-approved baseline configurations

**Key point:** Availability is priority for ICS/SCADA; air-gapping and segmentation provide security without impacting operations

### Scenario 5: Baseline and Hardening
**Situation:** Organization has 500 Windows workstations with inconsistent security configurations. Need to establish security baseline.

**Analysis:**
- Develop baseline using CIS Benchmark for Windows 10/11
- Key baseline elements: password policy (12+ characters, 90-day expiration), screen lock (5 minutes idle), BitLocker encryption, Windows Defender enabled, automatic updates
- Additional hardening: disable unnecessary services (Remote Registry, Print Spooler if not needed), enable Windows Firewall with strict rules, implement AppLocker to whitelist approved applications
- Deploy baseline via Group Policy Objects (GPO) for automated enforcement
- Use SCCM or Intune for configuration management and compliance monitoring
- Schedule monthly compliance scans to identify deviations
- Automated remediation where possible, manual review for exceptions
- Update baseline quarterly to address new threats
- Document all exceptions with business justification and compensating controls

**Key point:** Baselines ensure consistency; automated deployment and monitoring maintain compliance; regular updates adapt to evolving threats

---

## Mini Quiz

### Question 1
You are implementing wireless authentication for a corporate network. The network has a mix of company-owned laptops and personal employee devices. The security policy requires the strongest possible authentication while maintaining compatibility with both managed and unmanaged devices. Certificate deployment to all employee personal devices is not feasible.

Which EAP method best meets these requirements?

<details>
<summary>Show Answer</summary>

**Answer: PEAP (Protected Extensible Authentication Protocol)**

**Explanation:**
PEAP provides strong authentication while only requiring certificates on the RADIUS server, not on client devices. This makes it ideal for environments with mixed managed/unmanaged devices where deploying client certificates is impractical.

- **Why not EAP-TLS:** Requires certificates on both server AND clients - not feasible for personal devices per the scenario
- **Why not EAP-TTLS:** Similar to PEAP but less common in Windows environments; PEAP is typically preferred
- **Why not EAP-FAST:** Cisco proprietary and uses PAC instead of server certificates - less secure than certificate-based methods
- **Why not EAP-MD5:** Only provides one-way authentication and is vulnerable to dictionary attacks - should never be used

PEAP creates a TLS tunnel using the server certificate, then authenticates the user with credentials (typically MSCHAPv2). The TLS tunnel protects credentials from interception, providing strong security without requiring client certificate management.
</details>

### Question 2
A financial services company is deciding on a mobile device deployment model. Requirements include: full control over device security configurations, ability to remotely wipe all data, enforcement of encryption, and prevention of jailbreaking. Cost is a secondary concern compared to security and compliance.

Which deployment model should be recommended?

<details>
<summary>Show Answer</summary>

**Answer: COPE (Corporate-Owned, Personally Enabled)**

**Explanation:**
COPE provides the maximum level of control over device security while allowing employees to use devices for personal tasks. Since the company owns the devices, they have full authority to enforce security policies without privacy concerns that limit BYOD.

- **Why not BYOD:** Offers least control - employees may resist aggressive security policies on personal devices, privacy laws may limit data wiping capabilities
- **Why not CYOD:** Provides moderate control but still faces some BYOD challenges since employee has ownership
- **COPE advantages:** Company owns device so can enforce any policy, implement full-device encryption, prevent jailbreaking through MDM, remotely wipe without privacy concerns, standardize hardware for easier management

For highly regulated industries like financial services, COPE is the standard because it eliminates the conflict between employee privacy rights and corporate security requirements.
</details>

### Question 3
During application development, the security team wants to identify vulnerabilities as early as possible in the SDLC. They need to detect issues like hardcoded credentials, buffer overflows, and SQL injection vulnerabilities in the source code before the application is compiled and deployed.

Which security testing method should be implemented?

<details>
<summary>Show Answer</summary>

**Answer: Static Application Security Testing (SAST)**

**Explanation:**
SAST analyzes source code without executing it, allowing detection of vulnerabilities during the development phase ("shift left" in the SDLC). This catches issues before they make it to production.

- **Why SAST specifically:** Can detect hardcoded credentials, buffer overflows, and SQL injection by examining code patterns and data flows
- **Why not DAST:** Tests running applications (black-box approach) - happens later in SDLC and can't see source code issues like hardcoded credentials
- **Why not penetration testing:** Manual testing conducted on deployed applications - too late to catch issues "early in SDLC"
- **Why not code signing:** Verifies integrity but doesn't identify vulnerabilities

Best practice: Use both SAST early in development and DAST before production deployment for comprehensive coverage. SAST finds code-level issues, DAST finds runtime configuration and deployment issues.
</details>

### Question 4
A company is hardening Windows servers in their data center. The baseline configuration includes disabling unnecessary services. However, one critical business application requires the Print Spooler service, which has known vulnerabilities.

What is the BEST approach to address this situation?

<details>
<summary>Show Answer</summary>

**Answer: Document an exception to the baseline with business justification and implement compensating controls**

**Explanation:**
When a service required by business applications conflicts with security baselines, the proper approach is to document a formal exception with:

1. **Business justification** - Why the exception is necessary (critical application dependency)
2. **Risk assessment** - What vulnerabilities are introduced (Print Spooler exploits)
3. **Compensating controls** - Additional measures to mitigate risk:
   - Network segmentation - isolate affected server
   - Enhanced monitoring - alert on Print Spooler exploitation attempts
   - Strict access controls - limit who can access the service
   - Regular patching - apply security updates promptly
   - Host-based IPS - detect and block exploitation attempts

- **Why not disable the service:** Would break the critical business application
- **Why not ignore the security issue:** Violates security baseline without documentation and risk acceptance
- **Why not replace the application:** May not be feasible due to cost, time, or lack of alternatives

This approach balances security requirements with business needs while maintaining accountability through documented exceptions and risk mitigation through compensating controls.
</details>

### Question 5
An organization is deploying IoT sensors throughout their facility. These sensors have default credentials, no automatic update mechanism, and limited computing resources. They will monitor temperature and humidity in the data center.

What are the MOST important hardening steps for these devices? (Select the THREE best answers)

<details>
<summary>Show Answer</summary>

**Answer: Change default credentials, segment IoT devices onto isolated VLAN, disable UPnP**

**Explanation:**

**Essential hardening steps for IoT devices:**

1. **Change default credentials** - CRITICAL first step; default credentials are publicly known and primary IoT attack vector
2. **Network segmentation** - Isolate IoT devices on separate VLAN with strict firewall rules; prevents compromised sensor from accessing corporate network
3. **Disable UPnP** - Universal Plug and Play is commonly exploited on IoT devices; disabling reduces attack surface

**Why these three:**
- Address the most common IoT vulnerabilities (default creds, network access, UPnP exploitation)
- Feasible even on resource-constrained devices
- Don't require manufacturer cooperation (unlike firmware updates)

**Other important measures (but not as critical):**
- Update firmware if possible (but scenario states "no automatic update mechanism")
- Implement strong authentication (may not be supported by basic sensors)
- Enable encryption (may exceed device capabilities)
- Regular security scanning (good practice but secondary to the fundamentals)

The key principle: Since IoT devices often can't be hardened at the device level, focus on changing defaults and controlling their network access.
</details>

---

## CompTIA-Style Practice Questions

### Question 1
A security administrator is configuring a new wireless network for a small office. The network will serve 15 employees who need to access corporate resources from their personal smartphones and laptops. The administrator wants to implement the strongest security while minimizing certificate management overhead. The organization already operates a Windows domain with Active Directory.

Which combination of technologies would BEST meet these requirements?

A. WPA2-PSK with a strong pre-shared key rotated monthly  
B. WPA3-Personal with SAE and complex passphrase  
C. WPA2-Enterprise with 802.1X using PEAP and Active Directory authentication  
D. WPA3-Enterprise with 802.1X using EAP-TLS and client certificates

<details>
<summary>Show Answer</summary>

**Correct Answer: C**

**Explanation:**

**Why C is correct:**
- WPA2-Enterprise provides strong security suitable for business use
- 802.1X with PEAP leverages existing Active Directory infrastructure (no additional user database)
- PEAP only requires server certificate (minimizes certificate management - key requirement)
- Each user authenticated individually (better than shared PSK)
- Active Directory integration means users use existing domain credentials

**Why A is incorrect:**
- WPA2-PSK uses shared key - if one employee leaves, must change key on all devices
- No individual user authentication or accountability
- PSK is vulnerable to offline dictionary attacks if captured
- Not enterprise-grade security

**Why B is incorrect:**
- WPA3-Personal still uses a shared passphrase (SAE instead of PSK, but still shared)
- No individual user authentication
- Better than WPA2-PSK but doesn't meet "strongest security" for enterprise use

**Why D is incorrect:**
- While most secure option, requires client certificates on all personal devices
- Question specifies "minimizing certificate management overhead"
- EAP-TLS requires deploying and managing certificates on 15+ personal devices
- Not practical for BYOD scenario

**Key takeaway:** PEAP balances strong security with practical certificate management - perfect for organizations with Active Directory who don't want to manage client certificates.
</details>

### Question 2
A healthcare organization is implementing a mobile device strategy for 200 physicians and nurses who need access to electronic health records (EHR). The organization must comply with HIPAA requirements for data protection. The IT team has identified the following requirements:

- Full encryption of all data on devices
- Ability to remotely wipe devices if lost or stolen
- Separation of personal and work data
- Prevention of unauthorized app installations
- Centralized management and compliance reporting

The organization wants to balance security with user satisfaction. Budget allows for device purchase if necessary. Which deployment model should the security team recommend?

A. BYOD with comprehensive MDM and containerization  
B. COPE with MDM enforcing security policies and allowing limited personal use  
C. CYOD offering choice between three approved device models  
D. Company-issued devices with no personal use allowed

<details>
<summary>Show Answer</summary>

**Correct Answer: B**

**Explanation:**

**Why B is correct:**
- COPE gives organization full control since they own devices (critical for HIPAA)
- Can enforce ALL required policies without privacy concerns:
  - Full-device encryption (meets HIPAA encryption requirements)
  - Remote wipe without legal issues (organization owns data and device)
  - Complete control over app installations
  - Strongest MDM policy enforcement
- Allowing limited personal use maintains user satisfaction (requirement stated)
- No conflict between employee privacy rights and security requirements
- Meets "balance security with user satisfaction" goal

**Why A is incorrect:**
- BYOD faces privacy law challenges - employees may resist full-device wipe
- Cannot fully prevent personal app installations without user pushback
- Compliance reporting may be limited by employee privacy rights
- Higher risk of non-compliance with HIPAA
- Hidden costs often exceed initial budget savings

**Why C is incorrect:**
- Employee still owns device (same privacy issues as BYOD, just with approved models)
- Cannot enforce strongest policies without employee consent
- Doesn't provide the control level needed for HIPAA compliance

**Why D is incorrect:**
- Meets security requirements but fails "user satisfaction" goal
- Physicians/nurses will carry two devices (personal and work)
- Likely to cause resistance and workarounds
- Not necessary when COPE can achieve security while allowing personal use

**Key insight:** For regulated industries (healthcare, finance, government), COPE is typically the best balance - maximum security control with reasonable user experience. The organization ownership eliminates privacy conflicts that limit BYOD effectiveness.
</details>

### Question 3 (Multiple Select)
A development team is implementing security testing for a new web application that processes credit card payments. The security architect wants comprehensive vulnerability detection throughout the development lifecycle. 

Which THREE testing methods should be implemented to achieve the most thorough security coverage? (Choose THREE)

A. Static application security testing (SAST) during code development  
B. Dynamic application security testing (DAST) before production deployment  
C. Penetration testing by external security firm after deployment  
D. Code signing of all production releases  
E. Web application firewall (WAF) deployment  
F. Security code reviews by peer developers

<details>
<summary>Show Answer</summary>

**Correct Answers: A, B, C**

**Explanation:**

These three methods provide comprehensive coverage across different phases and perspectives:

**A - SAST during development (CORRECT):**
- Analyzes source code early in SDLC ("shift left")
- Detects: hardcoded credentials, injection flaws, buffer overflows, insecure crypto
- Catches issues before they reach production
- Complements other methods by seeing code-level vulnerabilities

**B - DAST before production (CORRECT):**
- Tests running application in pre-production environment
- Detects: authentication/session flaws, runtime configuration issues, API vulnerabilities
- Finds issues SAST misses (deployment/configuration problems)
- Black-box approach simulates attacker perspective

**C - Penetration testing after deployment (CORRECT):**
- Manual testing by skilled professionals
- Finds: business logic flaws, complex attack chains, real-world exploitability
- Validates that automated tools didn't miss critical issues
- Tests production environment and configuration

**Why D is incorrect (but still good practice):**
- Code signing verifies integrity and publisher identity
- Does NOT detect vulnerabilities or test security
- Prevents tampering but doesn't improve security coverage

**Why E is incorrect (but still good practice):**
- WAF is a compensating control, not a testing method
- Protects against attacks but doesn't identify vulnerabilities
- Deployment tool, not a testing tool

**Why F is incorrect (good but not best three):**
- Manual code reviews are valuable but time-intensive
- Less comprehensive than automated SAST
- Better as supplement to SAST, not replacement

**Best practice combination:**
1. SAST (early, finds code issues)
2. DAST (middle, finds runtime issues)
3. Penetration testing (late, validates with human expertise)

This covers the entire SDLC and provides automated + manual testing perspectives.
</details>

---

## Related Objectives

- **1.2 Summarize fundamental security concepts** - Zero trust, defense in depth, deception technologies
- **2.5 Mitigation techniques** - Hardening, encryption, patching, segmentation
- **3.2 Apply security principles to secure enterprise infrastructure** - Port security, 802.1X, firewall types
- **4.2 Security implications of asset management** - Asset tracking during device lifecycle
- **4.5 Modify enterprise capabilities to enhance security** - Firewalls, IDS/IPS, DLP, EDR/XDR implementation

---

## Quick Navigation
- [← Previous: 3.4 Resilience and Recovery](../3-4/)
- [→ Next: 4.2 Asset Management](../4-2/)
- [↑ Back to Domain 4: Security Operations](../)
- [⌂ Security+ Home](/)
