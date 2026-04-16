---
layout: objective
title: "4.1 Security Techniques for Computing Resources"
objective_id: "4.1"
domain: "4.0 Security Operations"
status: "done"
tags: ["secure-baselines", "wireless-security", "mobile-security", "hardening"]
permalink: /objectives/4-1/
---

## Overview

Security techniques for computing resources focus on implementing secure configurations, protecting wireless networks, and managing mobile devices. This objective covers secure baselines, wireless security protocols, and mobile device management (MDM) strategies.

---

## Secure Baselines

**Definition:** Standard secure configuration applied to systems to reduce attack surface.

**Purpose:**
- Consistent security across all systems
- Reduce vulnerabilities through hardening
- Meet compliance requirements (CIS benchmarks, DISA STIGs)

**Key hardening activities:**
- Disable unnecessary services and ports
- Remove default accounts and passwords
- Apply least privilege (minimal permissions)
- Enable logging and auditing
- Install security updates

**Platform-specific baselines:**

**Windows Server:**
- Disable SMBv1 (vulnerable to EternalBlue)
- Enable Windows Defender
- Configure Windows Firewall
- Disable Guest account
- Enforce strong password policies

**Linux:**
- SELinux/AppArmor enabled (mandatory access control)
- Disable root SSH login
- Configure iptables/firewalld
- Remove unused packages
- File permissions properly set (chmod)

**Network Devices (Routers/Switches):**
- Change default credentials
- Disable unused interfaces
- Enable SSH (disable Telnet)
- Configure ACLs (Access Control Lists)
- Enable logging to syslog server

**Mobile Devices:**
- Require device encryption
- Enforce screen lock (PIN/biometric)
- Disable USB debugging
- Remote wipe capability
- Prohibit jailbreaking/rooting

---

## Wireless Security

**Wireless vulnerabilities:**
- Open networks (no encryption)
- Weak encryption (WEP, WPA)
- Default SSIDs and passwords
- Rogue access points

**Wireless security protocols (evolution):**

**WEP (Wired Equivalent Privacy) - DEPRECATED:**
- ❌ Broken encryption (crackable in minutes)
- ❌ Do NOT use

**WPA (Wi-Fi Protected Access):**
- Uses TKIP (Temporal Key Integrity Protocol)
- Better than WEP but still vulnerable
- ❌ Deprecated

**WPA2:**
- Uses AES encryption (strong)
- Two modes:
  - **Personal (PSK):** Shared password, suitable for home/small office
  - **Enterprise (802.1X):** RADIUS authentication, suitable for corporations
- ✅ Minimum acceptable standard

**WPA3:**
- Improved encryption (192-bit for Enterprise)
- Protection against brute force (SAE - Simultaneous Authentication of Equals)
- Forward secrecy (past traffic safe even if password compromised)
- ✅ Best current standard

**Enterprise wireless security (WPA2/WPA3-Enterprise):**

**Components:**
1. **Supplicant:** Client device requesting access
2. **Authenticator:** Access point (forwards auth requests)
3. **Authentication server:** RADIUS server (validates credentials)

**EAP methods (Extensible Authentication Protocol):**

**EAP-TLS (Transport Layer Security):**
- Requires digital certificates (client + server)
- Most secure (mutual authentication)
- Complex to deploy (certificate management)

**EAP-TTLS (Tunneled TLS):**
- Server certificate required, client uses password
- Easier than EAP-TLS
- Secure tunnel protects password

**PEAP (Protected EAP):**
- Similar to EAP-TTLS
- Microsoft implementation
- Common in Windows environments

**EAP-FAST:**
- Cisco proprietary
- Uses PAC (Protected Access Credential) instead of certificates
- Faster deployment than certificate-based methods

**Wireless security best practices:**
- Use WPA3 (or WPA2 minimum)
- Change default SSID and admin password
- Disable WPS (Wi-Fi Protected Setup - vulnerable)
- Enable MAC filtering (not strong security, but defense in depth)
- Guest network isolation (separate VLAN)
- Disable SSID broadcast (security through obscurity - minimal benefit)

**Common wireless attacks:**
- **Evil twin:** Fake access point mimicking legitimate one
- **Rogue AP:** Unauthorized access point on network
- **Deauthentication attack:** Forcing clients to disconnect
- **WPS brute force:** Cracking WPS PIN

---

## Mobile Security

**Mobile device management (MDM):**

**Definition:** Centralized management of mobile devices (smartphones, tablets).

**MDM capabilities:**
- Remote device enrollment
- Policy enforcement (password requirements, encryption)
- App management (whitelist/blacklist apps)
- Remote wipe (if device lost/stolen)
- Location tracking
- Compliance monitoring

**Mobile Application Management (MAM):**
- Manage specific apps (not entire device)
- App containerization (separate work/personal data)
- Distribute internal apps
- App-level policies (prevent copy/paste from work apps)

**Deployment models:**

**BYOD (Bring Your Own Device):**
- Employees use personal devices for work
- **Pros:** Cost savings, employee satisfaction
- **Cons:** Security risk, data leakage, privacy concerns
- **Security:** MDM/MAM required, containerization separates work/personal

**COPE (Corporate-Owned, Personally Enabled):**
- Company owns device, employee can use personally
- **Pros:** Full control, better security
- **Cons:** Cost, employee may resist personal use restrictions

**CYOD (Choose Your Own Device):**
- Employee selects from approved device list, company purchases
- **Pros:** Balance between BYOD and COPE
- **Cons:** Still requires device management

**Mobile security controls:**

**Containerization:**
- Separate work apps/data from personal
- Encrypted container for work data
- Wipe work container without affecting personal data

**Context-aware authentication:**
- Additional auth required for sensitive actions
- Factors: Location (GPS), time, network (corporate WiFi)
- Example: Require extra auth if accessing from outside country

**Geofencing:**
- Define geographic boundaries
- Trigger actions when device enters/exits area
- Example: Block access when device leaves corporate campus

**Push notifications:**
- Alert users to security events
- Example: "Suspicious login detected, was this you?"

**Remote wipe:**
- **Full wipe:** Entire device erased (for company-owned)
- **Selective wipe:** Only work data removed (for BYOD)

**Mobile threats:**
- **Jailbreaking/Rooting:** Removes OS security controls
- **Sideloading:** Installing apps from untrusted sources
- **App-based threats:** Malicious apps, excessive permissions
- **Network attacks:** Man-in-the-middle on public WiFi
- **Physical theft:** Device stolen

---

## Key Distinctions

**WPA2 vs WPA3:**
- WPA2: AES encryption, vulnerable to KRACK attack
- WPA3: Improved encryption, SAE authentication, forward secrecy

**EAP-TLS vs PEAP:**
- EAP-TLS: Requires client certificates (most secure)
- PEAP: Client uses password (easier to deploy)

**MDM vs MAM:**
- MDM: Manages entire device
- MAM: Manages specific apps only

**BYOD vs COPE:**
- BYOD: Employee-owned, personal use primary
- COPE: Company-owned, work use primary

**Containerization vs Virtualization:**
- Containerization: Separate app/data spaces on same OS
- Virtualization: Separate OS instances

---

## Common Exam Traps

1. **Trap:** Thinking WPA2-Personal is sufficient for corporate networks
   - **Reality:** Enterprises should use WPA2/WPA3-Enterprise with RADIUS

2. **Trap:** Believing MAC filtering provides strong wireless security
   - **Reality:** MAC addresses easily spoofed, use for defense in depth only

3. **Trap:** Assuming disabling SSID broadcast significantly improves security
   - **Reality:** SSIDs easily discovered, security through obscurity is weak

4. **Trap:** Thinking MDM is only for company-owned devices
   - **Reality:** MDM can manage BYOD devices (with consent)

5. **Trap:** Believing jailbroken/rooted devices are just user preference
   - **Reality:** Major security risk, should be blocked by MDM

---

## Exam Tips

1. **WPA3 is strongest wireless encryption** (WPA2 minimum acceptable)
2. **Enterprise wireless requires RADIUS** (802.1X authentication)
3. **EAP-TLS most secure** (requires certificates on client and server)
4. **Secure baselines reduce attack surface** (disable unnecessary services)
5. **MDM enables remote wipe** (critical for lost/stolen devices)
6. **Containerization separates work/personal data** (best for BYOD)
7. **Geofencing triggers location-based actions** (e.g., block access outside region)
8. **WPS should be disabled** (vulnerable to brute force)
9. **Jailbreaking/rooting removes security controls** (should be detected and blocked)
10. **Guest networks should be isolated** (separate VLAN from corporate)

---

## Related Objectives

- **3.1 Security architecture:** Wireless networks as part of infrastructure
- **4.2 Asset management:** Tracking mobile devices
- **4.6 Identity and access management:** 802.1X and RADIUS authentication

---

## Quick Navigation
- [→ Next: 4.2 Asset Management](../4-2/)
- [↑ Back to Domain 4](../)
- [⌂ Home](/)
