---
layout: objective
title: "Security+ 4.1 — Given a scenario, apply common security techniques to computing resources."
objective_id: "4.1"
domain: "4.0 Security Operations"
status: "done"
tags:
  - secplus701
permalink: /secplus/objectives/4-1/
---

# Security+ 4.1 — Given a scenario, apply common security techniques to computing resources.

Status: <span class="status-badge done">done</span>

## Exam objective
Given a scenario, apply common security techniques to computing resources.

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

This objective covers implementing security on computing resources: hardening systems through secure baselines, securing wireless networks with modern protocols, and managing mobile devices across various ownership models. The exam presents scenarios and asks which technique, protocol, or control is most appropriate — recognizing the right tool for the right context is the key skill.

---

### Secure Baselines

**Definition:** A secure baseline is a standard hardened configuration applied consistently to a class of systems in order to reduce their attack surface.

**Purpose:**
- Achieve consistent security posture across all systems
- Meet compliance requirements (CIS Benchmarks, DISA STIGs)
- Reduce vulnerabilities before deployment

**Core hardening activities:**
- Disable unnecessary services and open ports
- Remove or rename default accounts; change default credentials
- Apply least privilege (minimal permissions)
- Enable logging and auditing
- Apply all current security patches

**Platform-specific baselines:**

**Windows Server:**
- Disable SMBv1 (vulnerable to EternalBlue/WannaCry)
- Enable Windows Defender and Windows Firewall
- Disable the Guest account
- Enforce strong password policies via Group Policy

**Linux:**
- Enable SELinux or AppArmor (mandatory access control)
- Disable root SSH login (`PermitRootLogin no`)
- Configure iptables / firewalld
- Remove unused packages; set correct file permissions (chmod)

**Network Devices (Routers/Switches):**
- Change all default credentials immediately after deployment
- Disable unused interfaces
- Enable SSH; disable Telnet (plaintext)
- Configure ACLs to restrict management access
- Forward logs to a syslog server

**Mobile Devices:**
- Require device encryption
- Enforce screen lock (PIN/biometric)
- Disable USB debugging
- Enable remote wipe capability
- Prohibit jailbreaking/rooting via MDM policy

> **Exam tip:** "Reduce attack surface" → **secure baseline / hardening**. The first action when deploying any new system should be applying a secure baseline before connecting it to the network.

---

### Wireless Security

**Wireless security protocols (evolution):**

| Protocol | Encryption | Status | Key detail |
|---|---|---|---|
| **WEP** | RC4 (broken) | ❌ Deprecated | Crackable in minutes; never use |
| **WPA** | TKIP | ❌ Deprecated | Improvement over WEP but still vulnerable |
| **WPA2** | AES | ✅ Minimum acceptable | Two modes: Personal (PSK) and Enterprise (802.1X) |
| **WPA3** | AES-256 (Enterprise) / SAE | ✅ Best current standard | Forward secrecy; resistant to brute-force |

**WPA2 modes:**
- **Personal (PSK):** Shared passphrase — suitable for home / small office
- **Enterprise (802.1X):** Per-user authentication via RADIUS — required for corporate environments

**WPA3 improvements over WPA2:**
- SAE (Simultaneous Authentication of Equals) replaces PSK — prevents offline dictionary attacks
- Forward secrecy — past traffic remains safe even if the password is later compromised
- 192-bit encryption suite for Enterprise mode

> **Exam tip:** Corporate networks should use **WPA2/WPA3-Enterprise** with a **RADIUS server** — never WPA2-Personal, which shares a single passphrase among all users.

**Enterprise wireless components (802.1X):**

| Role | Component | Function |
|---|---|---|
| **Supplicant** | Client device | Requests network access |
| **Authenticator** | Wireless access point | Forwards authentication requests to RADIUS |
| **Authentication server** | RADIUS server | Validates credentials and grants/denies access |

**EAP methods:**

| Method | Certificates required | Notes |
|---|---|---|
| **EAP-TLS** | Client + Server | Most secure; mutual authentication; complex to deploy |
| **EAP-TTLS** | Server only | Client authenticates with password inside secure tunnel |
| **PEAP** | Server only | Microsoft implementation; common in Windows environments |
| **EAP-FAST** | None (PAC) | Cisco proprietary; faster deployment; uses Protected Access Credential |

> **Exam tip:** "Most secure EAP method" → **EAP-TLS** (certificates on both sides). "Easiest to deploy" → **PEAP or EAP-TTLS** (only server needs a certificate).

**Common wireless attacks:**

| Attack | Description |
|---|---|
| **Evil twin** | Rogue AP mimics a legitimate network to capture credentials |
| **Rogue AP** | Unauthorized access point installed on the corporate network |
| **Deauthentication attack** | Forces clients to disconnect; often precedes an evil twin attack |
| **WPS brute force** | Exploits the 8-digit WPS PIN to recover the WPA passphrase |

**Wireless hardening best practices:**
- Use WPA3 (WPA2 minimum)
- Change default SSID and admin credentials
- **Disable WPS** — vulnerable to brute force regardless of WPA version
- Isolate guest networks on a separate VLAN
- MAC filtering: weak alone (MACs are easily spoofed), acceptable as a defense-in-depth layer
- SSID hiding: security through obscurity only — SSIDs are trivially discoverable

---

### Mobile Security

**Mobile Device Management (MDM):** Centralized platform that enforces policy, manages configuration, and enables remote control of mobile devices.

**MDM capabilities:**

| Capability | Description |
|---|---|
| **Policy enforcement** | Password complexity, encryption requirements, screen lock |
| **App management** | Whitelist/blacklist applications |
| **Remote wipe** | Erase device data if lost or stolen |
| **Location tracking** | GPS-based device location |
| **Compliance monitoring** | Alert if device becomes non-compliant (e.g., jailbroken) |

**Mobile Application Management (MAM):** Manages specific applications rather than the entire device — useful when the organization does not own the device.

**Deployment models:**

| Model | Ownership | Key characteristic |
|---|---|---|
| **BYOD** (Bring Your Own Device) | Employee | Lowest cost; highest privacy concern; requires containerization |
| **COPE** (Corporate-Owned, Personally Enabled) | Company | Full control; employee permitted personal use |
| **CYOD** (Choose Your Own Device) | Company | Employee selects from an approved list |

> **Exam tip:** **BYOD** requires **containerization** to separate work and personal data — the organization can selectively wipe only the work container without touching personal data.

**Mobile security controls:**

| Control | Description |
|---|---|
| **Containerization** | Isolated encrypted workspace for work apps/data; selective wipe possible |
| **Context-aware authentication** | Requires additional authentication based on location, time, or network |
| **Geofencing** | Triggers actions (block access, alert) when device enters or exits a defined geographic boundary |
| **Remote wipe** | Full wipe (company-owned) or selective wipe (BYOD work container only) |
| **Push notifications** | Security event alerts sent to devices (e.g., suspicious login warning) |

**Mobile threats:**

| Threat | Description |
|---|---|
| **Jailbreaking (iOS) / Rooting (Android)** | Removes OS security controls; MDM should detect and block access |
| **Sideloading** | Installing apps from outside the official store; bypasses vendor security review |
| **App-based threats** | Malicious apps, excessive permissions, data exfiltration |
| **Network attacks** | MITM on public/open Wi-Fi |
| **Physical theft** | Device stolen; remote wipe is the key mitigation |

---

### Key distinctions to know for the exam

| Comparison | Distinction |
|---|---|
| **WPA2 Personal vs. Enterprise** | Personal uses a shared passphrase; Enterprise uses per-user RADIUS authentication |
| **WPA2 vs. WPA3** | WPA3 adds SAE (brute-force protection) and forward secrecy; WPA2 is still acceptable minimum |
| **EAP-TLS vs. PEAP** | EAP-TLS requires client and server certificates (most secure); PEAP requires only a server certificate |
| **MDM vs. MAM** | MDM manages the entire device; MAM manages specific apps only |
| **BYOD vs. COPE** | BYOD is employee-owned (privacy concern, use containerization); COPE is company-owned (full control) |
| **Full wipe vs. selective wipe** | Full wipe erases everything (company-owned); selective wipe removes only work data (BYOD) |
| **Containerization vs. virtualization** | Containerization isolates apps/data on the same OS; virtualization runs separate OS instances |

---

### Common exam traps

**Trap: WPA2-Personal is acceptable for a corporate environment.**
Reality: WPA2-Personal shares a single passphrase among all users — if it leaks, everyone is compromised. Corporate environments require WPA2/WPA3-Enterprise with RADIUS for per-user authentication.

**Trap: MAC filtering provides strong wireless security.**
Reality: MAC addresses are trivially spoofed by an attacker who monitors traffic to learn a valid MAC. MAC filtering is a weak, easily bypassed control — use it only as part of defense-in-depth, never as a primary control.

**Trap: Disabling SSID broadcast meaningfully improves security.**
Reality: Hidden SSIDs are discovered in seconds by any wireless scanner. This is security through obscurity and provides negligible protection.

**Trap: MDM only applies to company-owned devices.**
Reality: MDM can manage BYOD devices with the user's consent. Containerization allows the organization to enforce policy on work data without full control of the personal device.

**Trap: Jailbreaking/rooting a device is just a user preference.**
Reality: Jailbreaking or rooting removes the OS security model entirely — MDM should detect this and block corporate access immediately.

**Trap: WPS is fine if WPA2 is enabled.**
Reality: WPS uses an 8-digit PIN that can be brute-forced regardless of WPA2 strength. Always disable WPS.

---

### Exam tips

1. "Reduce attack surface on a new system" → **secure baseline / hardening**
2. "Strongest current wireless protocol" → **WPA3**; minimum acceptable → **WPA2**
3. "Corporate wireless requires per-user authentication" → **WPA2/WPA3-Enterprise + RADIUS (802.1X)**
4. "Most secure EAP method" → **EAP-TLS** (certificates on both client and server)
5. "Separate work and personal data on a personal device" → **containerization**
6. "Device lost or stolen — BYOD employee" → **selective wipe** (work data only)
7. "Device lost or stolen — company-owned" → **full wipe**
8. "Block access based on location" → **geofencing**
9. "App installed outside official store" → **sideloading** (security risk)
10. "Always disable this wireless feature" → **WPS**

---

## Key terms

- **Secure baseline** — A standard hardened configuration applied to a system type to reduce attack surface before deployment.
- **Hardening** — The process of reducing vulnerabilities by disabling unnecessary services, removing defaults, and applying least privilege.
- **WEP (Wired Equivalent Privacy)** — Deprecated, broken wireless encryption; never use.
- **WPA2** — Wireless security standard using AES encryption; minimum acceptable for modern deployments.
- **WPA3** — Current best wireless standard; adds SAE and forward secrecy.
- **SAE (Simultaneous Authentication of Equals)** — WPA3 mechanism replacing PSK; protects against offline brute-force attacks.
- **802.1X** — Port-based network access control framework used by WPA2/WPA3-Enterprise for RADIUS authentication.
- **RADIUS** — Authentication server used in enterprise wireless environments; validates per-user credentials.
- **EAP-TLS** — Most secure EAP method; requires digital certificates on both client and server (mutual authentication).
- **PEAP** — Protected EAP; requires only a server certificate; client authenticates with a password inside an encrypted tunnel.
- **MDM (Mobile Device Management)** — Centralized platform for enforcing policy, managing apps, and remotely controlling mobile devices.
- **MAM (Mobile Application Management)** — Management of specific applications on a device rather than the entire device.
- **BYOD (Bring Your Own Device)** — Policy allowing employees to use personal devices for work.
- **COPE (Corporate-Owned, Personally Enabled)** — Company-owned device that employees are permitted to use personally.
- **Containerization** — Isolating work apps and data in an encrypted workspace on a device, enabling selective wipe.
- **Geofencing** — Triggering security actions when a device enters or exits a defined geographic boundary.
- **Remote wipe** — Erasing data on a lost or stolen device; full (entire device) or selective (work container only).
- **Sideloading** — Installing mobile apps from outside the official app store, bypassing vendor security review.
- **WPS (Wi-Fi Protected Setup)** — Wireless enrollment feature vulnerable to brute-force PIN attacks; should always be disabled.
- **Evil twin** — A rogue access point configured to mimic a legitimate network in order to intercept credentials.

---

## Examples / scenarios

**Scenario 1:** A company is deploying 200 new Windows Server instances. The security team wants to ensure a consistent, hardened configuration before any server goes live. What should they apply?
- **Answer:** Secure baseline. The team should apply a hardening standard (e.g., CIS Benchmark or DISA STIG) — disabling unnecessary services, removing default accounts, enabling logging, and patching before deployment.

**Scenario 2:** An employee connects their personal laptop to the corporate Wi-Fi using the shared passphrase they overheard in the break room. They now have full network access identical to any employee.
- **Answer:** This is the risk of WPA2-Personal. The solution is WPA2/WPA3-Enterprise (802.1X), where each user authenticates individually via RADIUS — a leaked passphrase affects only one credential, not the entire network.

**Scenario 3:** A security analyst sees a new access point in the wireless survey with the same SSID as the corporate network but a much stronger signal near the reception area. Employees are connecting to it and their credentials are being captured.
- **Answer:** Evil twin attack. The attacker placed a rogue AP mimicking the legitimate SSID. Mitigation: WPA2/WPA3-Enterprise (the fake AP cannot present a valid RADIUS certificate), wireless intrusion detection, and rogue AP monitoring.

**Scenario 4:** An employee's personal phone is enrolled in the company's MDM. The phone is lost. The employee is concerned about losing personal photos. What should the IT team do?
- **Answer:** Perform a **selective wipe** — remove only the work container (email, corporate apps, work data) while leaving the employee's personal data intact. A full wipe would be appropriate for a company-owned device.

**Scenario 5:** A hospital wants to block clinical staff from using any medical apps downloaded outside the official app store on their work phones, without managing employees' personal data.
- **Answer:** Deploy **MAM** (Mobile Application Management) with app whitelisting. MAM manages specific apps rather than the entire device, allowing the hospital to enforce app policy without full MDM control over personal data.

**Scenario 6:** A company's policy states that when an executive travels internationally, their phone must require an additional authentication factor beyond their normal PIN. What control implements this?
- **Answer:** **Context-aware authentication** — additional authentication is triggered based on contextual factors such as geographic location (outside the home country).

---

## Mini quiz

<details>
<summary><strong>Question 1:</strong> What is the difference between WPA2-Personal and WPA2-Enterprise, and why does it matter for corporate networks?</summary>

**Answer:** WPA2-Personal uses a single shared passphrase (PSK) for all users — if it leaks, every user is compromised and the passphrase must be changed everywhere. WPA2-Enterprise uses 802.1X with RADIUS, giving each user unique credentials. Corporations require Enterprise mode so that a compromised credential affects only one account, not the entire wireless infrastructure.
</details>

<details>
<summary><strong>Question 2:</strong> What is SAE and why does WPA3 use it instead of PSK?</summary>

**Answer:** SAE (Simultaneous Authentication of Equals) is a key exchange mechanism that replaces the Pre-Shared Key in WPA2-Personal. Unlike PSK, SAE is resistant to offline dictionary attacks — an attacker who captures the handshake cannot run a brute-force attack against it. SAE also provides forward secrecy, meaning past sessions cannot be decrypted even if the password is later compromised.
</details>

<details>
<summary><strong>Question 3:</strong> What is containerization in the mobile context and what problem does it solve?</summary>

**Answer:** Containerization creates an isolated, encrypted workspace on the device that holds all work apps and data, completely separated from personal data. It solves the BYOD privacy problem — the organization can selectively wipe the work container if the device is lost or the employee leaves, without touching the user's personal photos, messages, or apps.
</details>

<details>
<summary><strong>Question 4:</strong> Why should WPS be disabled even on networks using WPA2?</summary>

**Answer:** WPS uses an 8-digit PIN for device enrollment. The PIN is validated in two halves, reducing the effective keyspace to ~11,000 combinations — trivially brute-forceable. Once the WPS PIN is cracked, the WPA2 passphrase is exposed. WPS is vulnerable regardless of WPA2 strength, so it should always be disabled.
</details>

<details>
<summary><strong>Question 5:</strong> What is the difference between MDM and MAM, and when would you choose each?</summary>

**Answer:** MDM (Mobile Device Management) controls the entire device — policies, apps, remote wipe, location. MAM (Mobile Application Management) controls only specific applications. Choose MDM for company-owned devices where full control is appropriate. Choose MAM for BYOD scenarios where employees consent to app-level management but not full device control, preserving personal privacy.
</details>

### CompTIA-style practice questions

<details>
<summary><strong>Question 6:</strong> A security engineer is deploying wireless for a 500-person office. Management requires that each employee authenticate with their domain credentials and that a lost password not expose the entire wireless network. Which solution BEST meets these requirements?<br>A. WPA2-Personal with a complex shared passphrase<br>B. WPA3-Personal with SAE<br>C. WPA2-Enterprise with RADIUS and EAP-TLS<br>D. WEP with MAC filtering</summary>

**Correct Answer: C. WPA2-Enterprise with RADIUS and EAP-TLS**

Per-user domain credential authentication requires 802.1X with a RADIUS server. EAP-TLS provides mutual authentication via certificates, and each user has individual credentials — a compromised password does not affect other users.

- A: WPA2-Personal shares a single passphrase among all users; a leak requires changing it everywhere.
- B: WPA3-Personal still uses a shared passphrase (SAE protects the handshake but doesn't give per-user auth).
- D: WEP is deprecated and broken; MAC filtering provides no meaningful security on its own.
</details>

<details>
<summary><strong>Question 7:</strong> A user reports their company-issued laptop was stolen at an airport. The laptop contains sensitive customer data. Which action should the IT team take FIRST?<br>A. Notify local law enforcement and file a report<br>B. Issue the employee a new laptop<br>C. Perform a remote wipe via MDM<br>D. Reset the employee's domain password</summary>

**Correct Answer: C. Perform a remote wipe via MDM**

The immediate priority is protecting the sensitive data on the stolen device. A remote full wipe via MDM destroys all data before an attacker can access it. The other actions are appropriate follow-up steps but do not address the data exposure risk.

- A: Filing a report is appropriate but does not protect the data on the device.
- B: Issuing a new laptop is a business continuity step, not a security response.
- D: Resetting the domain password is useful but the data already on the device is still accessible without network connectivity.
</details>

<details>
<summary><strong>Question 8:</strong> An organization enforces a BYOD policy. An employee leaves the company. The employee's personal device contains both corporate email and personal family photos. Which action BEST protects corporate data while respecting the employee's privacy?<br>A. Perform a full wipe of the device<br>B. Perform a selective wipe of the corporate container<br>C. Disable the employee's MDM enrollment and take no further action<br>D. Request the employee return the device</summary>

**Correct Answer: B. Perform a selective wipe of the corporate container**

Containerization in a BYOD context allows the organization to remove only the work container — email, corporate apps, and work data — leaving personal data untouched. This is the designed purpose of containerization for BYOD offboarding.

- A: A full wipe destroys personal data on an employee-owned device — legally and ethically problematic.
- C: Simply removing MDM enrollment without wiping the work container may leave corporate data accessible on the device.
- D: The device is employee-owned; the organization has no right to take it.
</details>

<details>
<summary><strong>Question 9 (Multi-select):</strong> A network administrator is hardening a new wireless deployment. Which TWO actions provide the MOST security improvement? (Select TWO.)<br>A. Disable SSID broadcast<br>B. Enable MAC address filtering<br>C. Disable WPS<br>D. Migrate from WPA2-Personal to WPA2-Enterprise<br>E. Reduce the Wi-Fi transmit power</summary>

**Correct Answers: C and D**

Disabling WPS eliminates a well-known brute-force vulnerability. Migrating to Enterprise mode eliminates the shared passphrase risk and introduces per-user RADIUS authentication — the two highest-impact improvements.

- A: SSID hiding is security through obscurity; SSIDs are trivially discoverable with any wireless scanner.
- B: MAC filtering is easily bypassed by spoofing a captured valid MAC address.
- E: Reducing transmit power may slightly limit coverage but does not address authentication or encryption weaknesses.
</details>

---

## Related objectives

- [**3.1**]({{ '/secplus/objectives/3-1/' | relative_url }}) — Security architecture covers wireless networks and mobile as infrastructure components.
- [**4.2**]({{ '/secplus/objectives/4-2/' | relative_url }}) — Asset management includes tracking and controlling mobile device inventory.
- [**4.6**]({{ '/secplus/objectives/4-6/' | relative_url }}) — Identity and access management covers 802.1X, RADIUS, and per-user authentication.
- [**2.3**]({{ '/secplus/objectives/2-3/' | relative_url }}) — Vulnerability types include wireless vulnerabilities, mobile threats, and misconfiguration.

---

## Navigation

**Domain 4.0: Security Operations**

| Objective | Title | Status |
|---|---|---|
| **4.1** | Given a scenario, apply common security techniques to computing resources. (current) | done |
| [4.2]({{ '/secplus/objectives/4-2/' | relative_url }}) | Explain the security implications of proper hardware, software, and data asset management. | done |
| [4.3]({{ '/secplus/objectives/4-3/' | relative_url }}) | Explain various activities associated with vulnerability management. | done |
| [4.4]({{ '/secplus/objectives/4-4/' | relative_url }}) | Explain security alerting and monitoring concepts and tools. | done |
| [4.5]({{ '/secplus/objectives/4-5/' | relative_url }}) | Given a scenario, modify enterprise capabilities to enhance security. | done |
| [4.6]({{ '/secplus/objectives/4-6/' | relative_url }}) | Given a scenario, implement and maintain identity and access management. | done |
| [4.7]({{ '/secplus/objectives/4-7/' | relative_url }}) | Explain the importance of automation and orchestration related to secure operations. | done |
| [4.8]({{ '/secplus/objectives/4-8/' | relative_url }}) | Explain appropriate incident response activities. | done |
| [4.9]({{ '/secplus/objectives/4-9/' | relative_url }}) | Given a scenario, use data sources to support an investigation. | done |

[← Previous: Domain 3]({{ '/secplus/objectives/3-4/' | relative_url }}) | [Back to Dashboard]({{ '/secplus/' | relative_url }}) | [Next: Objective 4.2 →]({{ '/secplus/objectives/4-2/' | relative_url }})
