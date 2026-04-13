---
layout: objective
title: "Security+ 3.2 — Given a scenario, apply security principles to secure enterprise infrastructure."
objective_id: "3.2"
domain: "3.0 Security Architecture"
status: "done"
tags:
  - secplus701
permalink: /secplus/objectives/3-2/
---

# Security+ 3.2 — Given a scenario, apply security principles to secure enterprise infrastructure.

Status: <span class="status-badge done">done</span>

## Exam objective
Given a scenario, apply security principles to secure enterprise infrastructure.

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

Securing enterprise infrastructure requires applying layered security controls across network devices, implementing proper segmentation, configuring fail-safe modes, and enforcing access policies. This objective focuses on the practical application of security tools (firewalls, IDS/IPS, VPNs, network appliances) and design principles (device placement, security zones, fail modes) in real-world scenarios.

---

### Firewall types and capabilities

| Firewall Type | Layer | Capability | Use Case |
|---|---|---|---|
| **Packet Filtering** | Layer 3-4 | Inspects packet headers (IP, port) | Basic perimeter security |
| **Stateful** | Layer 4 | Tracks connection state; allows return traffic | Most common enterprise firewall |
| **Proxy** | Layer 5 or 7 | Makes connections on behalf of clients | Content inspection, caching |
| **Kernel Proxy** | All layers | Minimal performance impact, full inspection | High-performance environments |
| **Next Generation (NGFW)** | Layer 7 | Application-aware, deep packet inspection, IPS | Modern threat prevention |
| **Unified Threat Management (UTM)** | Multiple | Combines firewall, IPS, AV, filtering in one device | Small-medium business consolidation |
| **Web Application Firewall (WAF)** | Layer 7 | HTTP/HTTPS traffic inspection; prevents SQLi, XSS | Web application protection |

**Layer-based distinction:**
- **Layer 4 Firewall** — operates at transport layer (TCP/UDP ports).
- **Layer 7 Firewall** — operates at application layer (inspects content, protocol behavior).

**NGFW vs. UTM:**
- NGFW uses a **single engine** for all functions; faster, more integrated.
- UTM uses **separate engines** for each function; can be a single point of failure.

**WAF placement:**
- **Inline** — actively blocks attacks in real time.
- **Out-of-band** — monitors mirrored traffic for detection only.

---

### Access Control Lists (ACLs)

ACLs define which traffic is permitted or denied based on rules.

**ACL rules contain:**
- Type of traffic (protocol)
- Source address/network
- Destination address/network
- Action (permit/deny)

**Key configuration principles:**
- Rules are processed **top-down** — first match wins.
- Place **most specific rules at the top**, generic rules at the bottom.
- End with **implicit deny** (or explicit "deny all" if not supported).
- **Log deny actions** for security monitoring and incident response.

**Hardware vs. Software firewalls:**
- **Hardware firewall** — dedicated network appliance protecting entire network/subnet.
- **Software firewall** — runs on individual hosts (host-based) for per-device protection.

---

### Intrusion Detection and Prevention

| Feature | IDS | IPS |
|---|---|---|
| **Action** | Detects and alerts | Detects, alerts, and blocks |
| **Deployment** | Out-of-band (passive monitoring) | Inline (active protection) |
| **Risk** | No traffic disruption | False positives can block legitimate traffic |
| **Use case** | Threat visibility, forensics | Active threat prevention |

**IDS types:**
- **Network IDS (NIDS)** — monitors network traffic.
- **Host IDS (HIDS)** — monitors single endpoint activity.
- **Wireless IDS (WIDS)** — detects wireless DoS and rogue APs.

**Detection methods:**
- **Signature-based** — matches known attack patterns (low false positives, misses new attacks).
  - Pattern-matching (NIDS, WIDS)
  - Stateful-matching against known baseline (HIDS)
- **Anomaly-based** — compares traffic against normal baseline (detects unknown attacks, higher false positives).
  - Statistical, protocol, traffic, rule/heuristic, application-based

**When to use:**
- Use **IDS** for visibility without risk of blocking legitimate traffic.
- Use **IPS** when active blocking is required and tuning reduces false positives.

---

### Network appliances

| Appliance | Purpose |
|---|---|
| **Load Balancer** | Distributes traffic across multiple servers; provides redundancy, health checks |
| **Application Delivery Controller (ADC)** | Advanced load balancing with SSL offload, caching, compression |
| **Proxy Server** | Intermediary for client requests; caching, filtering, anonymity, DDoS protection |
| **Sensors** | Monitor network traffic; detect anomalies, security breaches, performance issues |
| **Jump Server / Jump Box** | Secure gateway for admins to access devices in different security zones |

**Jump server benefits:**
- Single point of admin access (reduces attack surface)
- Centralized logging and auditing
- Simplifies access control to sensitive zones
- Houses admin tools and scripts

---

### Port security and 802.1X

**Port security** restricts network switch ports to specific MAC addresses.

| Mechanism | Description |
|---|---|
| **MAC address filtering** | Associate specific MACs with switch ports; prevent unauthorized devices |
| **Sticky MAC** | Automatically learns and saves first connected MAC address |
| **CAM table** | Stores MAC-to-port mappings; vulnerable to MAC flooding attacks |

**Limitations:**
- Vulnerable to **MAC spoofing** — attacker clones authorized MAC address.

**802.1X authentication** provides stronger port-based access control.

**802.1X components:**
- **Supplicant** — client device requesting access.
- **Authenticator** — network switch/AP enforcing policy.
- **Authentication Server** — RADIUS server validating credentials.

**EAP variants:**

| Variant | Authentication Method | Use Case |
|---|---|---|
| **EAP-MD5** | Password-based, one-way | Weak; avoid in production |
| **EAP-TLS** | Certificate on client and server; mutual auth | Most secure; enterprise |
| **EAP-TTLS** | Server cert; client uses password | Common for user auth |
| **EAP-FAST** | Protected access credential (PAC) | Cisco environments |
| **PEAP** | Server cert + Active Directory password | Windows enterprise |
| **LEAP** | Cisco proprietary | Legacy Cisco-only |

**RADIUS vs. TACACS+:**
- **RADIUS** — cross-platform, combines authentication and authorization.
- **TACACS+** — Cisco proprietary, separates AAA functions, more granular control.

---

### VPN types and configurations

**VPN deployment models:**

| Type | Purpose | Example |
|---|---|---|
| **Site-to-Site** | Connects two physical locations over internet | Branch office to HQ |
| **Client-to-Site** | Remote user connects to corporate network | Employee working from home |
| **Clientless** | Browser-based VPN; no software installation | Contractor limited access |

**Tunnel modes:**
- **Full Tunnel** — all traffic routed through VPN; high security, limits local access.
- **Split Tunnel** — only corporate traffic through VPN; better performance, less secure.

**IPSec modes:**
- **Transport Mode** — encrypts payload, uses original IP header; client-to-site VPNs.
- **Tunnel Mode** — encrypts entire packet, adds new IP header; site-to-site VPNs.

**IPSec components:**
- **Authentication Header (AH)** — integrity and authentication (no encryption).
- **Encapsulating Security Payload (ESP)** — confidentiality, integrity, encryption, replay protection.

**TLS/DTLS:**
- **TLS** — TCP-based; used in HTTPS and clientless VPNs; slower but reliable.
- **DTLS** — UDP-based; faster; used where performance matters (VoIP, video).

---

### SD-WAN and SASE

**Software-Defined WAN (SD-WAN):**
- Virtualizes WAN management, intelligently routes traffic across multiple transports (MPLS, cellular, broadband).
- Benefits: agility, centralized control, cloud integration, cost reduction.
- Use case: Multi-branch enterprises moving to cloud services (IaaS, PaaS, SaaS).

**Secure Access Service Edge (SASE):**
- Cloud-delivered service combining network security and WAN capabilities.
- Components: Firewalls, VPN, Zero Trust Network Access (ZTNA), Cloud Access Security Broker (CASB).
- Delivered via common policy platform from cloud providers (AWS VPC, Azure Virtual WAN, Google Cloud Interconnect).

---

### Infrastructure considerations

**Device placement:**
- Routers at network edge filter traffic before entering internal network.
- Switches placed for easy segment connectivity.
- Access points strategically positioned for coverage without interference.

**Security zones and screened subnets:**
- **Security zones** isolate devices with similar security requirements.
- **Screened subnet** (formerly DMZ) — buffer zone hosting public-facing services (web, email); protects internal network.

**Attack surface:**
- All points where unauthorized access or data extraction can occur.
- Reduce by disabling unnecessary services, closing unused ports, applying least privilege.

**Connectivity considerations:**
- **Wired (Ethernet)** — stability, speed, limited mobility.
- **Wireless (Wi-Fi)** — flexibility, mobility, higher security risk (interference, eavesdropping).

**Device attributes:**
- **Active** — takes action on traffic (IPS, firewall).
- **Passive** — observes only (IDS, network tap).
- **Inline** — in the data path; can block traffic.
- **Tap/Monitor** — out-of-band; cannot disrupt traffic.

**Failure modes:**
- **Fail-open** — allows all traffic on device failure; maintains connectivity, reduces security.
- **Fail-closed** — blocks all traffic on device failure; prioritizes security over availability.

**Choosing fail mode:**
- Critical security segments: **fail-closed**.
- High-availability segments where downtime is unacceptable: **fail-open** with monitoring.

---

### Selecting infrastructure controls

**Key principles:**
- **Least Privilege** — grant minimum necessary access.
- **Defense in Depth** — multiple layers so one failure does not compromise system.
- **Risk-Based Approach** — prioritize controls by threat likelihood and impact.
- **Lifecycle Management** — regularly review, update, retire controls.
- **Open Design Principle** — transparent controls enable rigorous testing and accountability.

**Methodology:**
1. **Assess current state** — inventory infrastructure, vulnerabilities, existing controls.
2. **Gap analysis** — identify discrepancies between current and desired security posture.
3. **Set clear objectives** — define goals (data protection, compliance, uptime).
4. **Benchmarking** — compare against industry best practices.
5. **Cost-benefit analysis** — balance security level with resource constraints.
6. **Stakeholder involvement** — align with business operations.
7. **Monitoring and feedback** — continuously adapt to evolving threats.

**Best practices:**
- Conduct regular risk assessments.
- Align with established frameworks (NIST, ISO).
- Customize frameworks to organizational risk profile.
- Engage stakeholders and provide ongoing training.

---

### Key distinctions to know for the exam

| Comparison | Distinction |
|---|---|---|
| **IDS vs. IPS** | IDS = passive (detects/alerts); IPS = active (detects/blocks) |
| **NGFW vs. UTM** | NGFW = single engine; UTM = multiple engines (single point of failure) |
| **Layer 4 vs. Layer 7 Firewall** | Layer 4 = ports/protocols; Layer 7 = application content |
| **Full Tunnel vs. Split Tunnel** | Full = all traffic via VPN (secure); Split = only corporate traffic (faster) |
| **Transport vs. Tunnel Mode** | Transport = original IP header; Tunnel = new IP header encapsulates packet |
| **AH vs. ESP** | AH = integrity only; ESP = integrity + encryption |
| **Fail-Open vs. Fail-Closed** | Fail-open = availability priority; Fail-closed = security priority |
| **Active vs. Passive Device** | Active = takes action (IPS); Passive = observes (IDS) |
| **Inline vs. Tap** | Inline = in data path (can block); Tap = out-of-band (monitor only) |

---

### Common exam traps

**Trap: Thinking IDS and IPS are interchangeable.**
Reality: IDS is passive and cannot block. IPS is inline and actively blocks. Deploying IDS when blocking is needed = wrong answer.

**Trap: Assuming UTM is always better because it consolidates functions.**
Reality: UTM is a single point of failure. If the UTM fails, all security functions fail. NGFW with integrated functions in a single engine is more resilient.

**Trap: Believing split tunnel VPNs are insecure and should never be used.**
Reality: Split tunnel trades some security for better performance. Acceptable when balanced with endpoint protection and for non-critical remote access.

**Trap: Thinking Layer 7 firewalls are always better than Layer 4.**
Reality: Layer 7 provides deeper inspection but at higher performance cost. Layer 4 is sufficient for basic traffic filtering and faster.

**Trap: Assuming fail-closed is always the right choice.**
Reality: For high-availability systems (e.g., hospital networks, financial trading), fail-open may be required to maintain critical operations during a device failure.

---

### Exam tips

1. Questions about IDS/IPS deployment will test whether you understand **inline (IPS) vs. out-of-band (IDS)** positioning.
2. When asked about VPN for remote workers, **client-to-site** is the answer. Site-to-site connects facilities, not individuals.
3. **ACL rule order** questions always test top-down processing — most specific first, deny-all last.
4. For questions about WAF, remember it **only protects web applications** (HTTP/HTTPS). It does not filter network-layer traffic.
5. **Fail mode** questions will present a scenario requiring you to choose based on whether availability or security is the priority.
6. **802.1X with EAP-TLS** is the most secure wired/wireless access control — requires certificates on both client and server.

---

## Key terms

- **Firewall** — Network security device controlling inbound and outbound traffic based on rules.
- **Stateful Firewall** — Tracks connection state; automatically allows return traffic for established connections.
- **Next Generation Firewall (NGFW)** — Application-aware firewall with integrated IPS, deep packet inspection.
- **Unified Threat Management (UTM)** — All-in-one security appliance combining firewall, IPS, AV, content filtering.
- **Web Application Firewall (WAF)** — Layer 7 firewall protecting web applications from SQLi, XSS, CSRF.
- **Access Control List (ACL)** — Rules defining permitted and denied traffic based on source, destination, protocol.
- **Intrusion Detection System (IDS)** — Passive security tool that detects and alerts on suspicious activity.
- **Intrusion Prevention System (IPS)** — Active security tool that detects and blocks malicious traffic inline.
- **Load Balancer** — Distributes traffic across multiple servers for performance and redundancy.
- **Proxy Server** — Intermediary handling requests on behalf of clients; provides caching and filtering.
- **Jump Server** — Secure gateway for administrative access to devices in different security zones.
- **Port Security** — Switch feature restricting access to specific ports based on MAC addresses.
- **802.1X** — Port-based network access control standard using RADIUS authentication.
- **EAP (Extensible Authentication Protocol)** — Framework for various authentication methods in 802.1X.
- **VPN (Virtual Private Network)** — Encrypted tunnel extending private network over public infrastructure.
- **Site-to-Site VPN** — Connects two physical locations over the internet.
- **Client-to-Site VPN** — Connects remote user to corporate network.
- **Full Tunnel** — All traffic routed through VPN; higher security, limited local access.
- **Split Tunnel** — Only corporate traffic through VPN; better performance, lower security.
- **IPSec** — Protocol suite providing encryption, authentication, and integrity for IP communications.
- **Transport Mode** — IPSec mode using original IP header; client-to-site VPNs.
- **Tunnel Mode** — IPSec mode adding new IP header; site-to-site VPNs.
- **SD-WAN** — Software-defined approach to WAN management with intelligent traffic routing.
- **SASE** — Cloud service combining network security and WAN capabilities.
- **Screened Subnet** — Isolated network segment hosting public-facing services (formerly DMZ).
- **Fail-Open** — Device failure mode allowing all traffic; prioritizes availability.
- **Fail-Closed** — Device failure mode blocking all traffic; prioritizes security.

---

## Examples / scenarios

**Scenario 1:** A company needs to protect its e-commerce website from SQL injection and cross-site scripting attacks. The security team is evaluating firewall options.
- **Answer:** Deploy a **Web Application Firewall (WAF)** inline to inspect HTTP/HTTPS traffic and block layer 7 web attacks. A traditional firewall operates at layers 3-4 and cannot inspect application-layer attack patterns.

**Scenario 2:** The network team is deploying an IPS to protect the internal network. During testing, the IPS blocks several legitimate applications, causing business disruption.
- **Answer:** This is a **false positive** issue. Tune the IPS signatures to reduce false positives, create exceptions for known-good traffic, and consider starting in IDS mode (alert-only) until tuning is complete. IPS inline placement means false positives directly impact availability.

**Scenario 3:** A remote employee using a VPN cannot access local network printers at home while connected to the corporate network.
- **Answer:** The VPN is configured in **full tunnel mode** — all traffic including local LAN traffic is routed through the VPN to corporate. Change to **split tunnel** to allow local traffic direct access while corporate traffic uses the VPN.

**Scenario 4:** A hospital's critical patient monitoring system requires 24/7 connectivity. The security team is configuring a new IPS to protect this segment and must choose a failure mode.
- **Answer:** Configure **fail-open** mode. In healthcare, availability of life-critical systems takes priority over security during a device failure. Implement compensating controls (monitoring, alerts) to detect if the IPS fails.

**Scenario 5:** An organization uses 802.1X authentication for wired network access. They need the most secure EAP method that prevents man-in-the-middle attacks.
- **Answer:** Deploy **EAP-TLS** — requires digital certificates on both client and server, providing mutual authentication. This is the most secure EAP variant. EAP-TTLS and PEAP are less secure (server cert only), and EAP-MD5 provides no encryption.

---

## Mini quiz

<details>
<summary><strong>Question 1:</strong> What is the functional difference between an IDS and an IPS, and how does deployment differ?</summary>

**Answer:** IDS detects and alerts on suspicious activity but takes no action — it is deployed **out-of-band** (passive monitoring). IPS detects and actively blocks malicious traffic — it is deployed **inline** in the data path. IDS provides visibility without disruption risk; IPS provides active protection but false positives can block legitimate traffic.
</details>

<details>
<summary><strong>Question 2:</strong> An organization needs to connect remote offices with secure communication. Should they use client-to-site or site-to-site VPN?</summary>

**Answer:** **Site-to-site VPN** connects two physical locations (offices, data centers). Client-to-site VPN connects individual remote users to the corporate network. The scenario describes connecting offices, so site-to-site is correct.
</details>

<details>
<summary><strong>Question 3:</strong> What is the purpose of a screened subnet, and what type of services should be placed there?</summary>

**Answer:** A screened subnet (formerly DMZ) is an isolated network segment between the internet and internal network. It hosts **public-facing services** — web servers, email servers, FTP — that must be accessible from the internet. If these are compromised, the internal network remains protected by the inner firewall.
</details>

<details>
<summary><strong>Question 4:</strong> Why do ACL rules need to be ordered from most specific to most generic?</summary>

**Answer:** ACLs are processed top-down, and the first matching rule is applied. If generic rules (e.g., "allow all from 10.0.0.0/8") are placed before specific rules (e.g., "deny 10.0.5.100"), the specific rules will never be evaluated. Most specific first ensures fine-grained control is applied before broader rules.
</details>

<details>
<summary><strong>Question 5:</strong> When should a security device be configured to fail-open vs. fail-closed?</summary>

**Answer:** **Fail-closed** when security is the priority — critical data segments, financial systems, classified environments. **Fail-open** when availability is paramount — life-critical systems (hospital monitors), high-uptime services (e-commerce during peak sales). The choice depends on whether the organization can tolerate downtime or security degradation during a device failure.
</details>

### CompTIA-style practice questions

<details>
<summary><strong>Question 6:</strong> A security administrator is configuring network access control for a corporate office. Employees use company-issued laptops with certificates. Which authentication method provides the MOST secure wired network access?<br>A. EAP-MD5 with password authentication<br>B. MAC address filtering on switch ports<br>C. 802.1X with EAP-TLS<br>D. Static IP address assignment</summary>

**Correct Answer: C. 802.1X with EAP-TLS**

EAP-TLS requires certificates on both client and server, providing mutual authentication and encrypted credentials — the most secure 802.1X method. EAP-MD5 (A) uses weak password authentication and no encryption. MAC filtering (B) is easily spoofed. Static IP (D) provides no authentication.
</details>

<details>
<summary><strong>Question 7:</strong> An IPS is deployed inline to protect the internal network. After deployment, users report that a critical business application is unavailable. Investigation shows the IPS is blocking the application's traffic. What is the MOST likely cause?<br>A. The IPS is configured in fail-open mode<br>B. The IPS generated a false positive and blocked legitimate traffic<br>C. The application is using an encrypted connection<br>D. The IPS is deployed out-of-band</summary>

**Correct Answer: B. The IPS generated a false positive and blocked legitimate traffic**

IPS inline deployment means it can block traffic. A false positive occurs when legitimate traffic matches a malicious signature and is incorrectly blocked. Fail-open (A) would allow all traffic, not block it. Encryption (C) would prevent inspection but not cause blocking. Out-of-band (D) means the IPS cannot block — it would only alert.
</details>

<details>
<summary><strong>Question 8 (Multi-select):</strong> A company is implementing network segmentation. Which TWO design decisions provide the BEST security improvement? (Choose TWO)<br>A. Place all servers in a single flat network for easy management<br>B. Create a screened subnet for public-facing web servers<br>C. Use VLANs to separate guest Wi-Fi from corporate network<br>D. Disable all firewall rules to improve performance<br>E. Connect all IoT devices directly to the corporate VLAN</summary>

**Correct Answers: B. Create a screened subnet for public-facing web servers and C. Use VLANs to separate guest Wi-Fi from corporate network**

Both are fundamental segmentation best practices. Screened subnets (B) isolate internet-facing services. VLAN segmentation (C) prevents untrusted guest traffic from accessing corporate resources. Flat network (A) eliminates segmentation benefits. Disabling firewalls (D) removes protection. IoT on corporate VLAN (E) increases risk.
</details>

---

## Related objectives

- [**1.1**]({{ '/secplus/objectives/1-1/' | relative_url }}) — Security controls framework categorizes the infrastructure controls applied here.
- [**2.5**]({{ '/secplus/objectives/2-5/' | relative_url }}) — Mitigation techniques include many of the infrastructure controls covered in this objective.
- [**3.1**]({{ '/secplus/objectives/3-1/' | relative_url }}) — Architecture models determine which infrastructure security principles apply.
- [**4.1**]({{ '/secplus/objectives/4-1/' | relative_url }}) — Applying security techniques to computing resources builds on infrastructure security principles.

---

## Navigation

**Domain 3.0: Security Architecture**

| Objective | Title | Status |
|---|---|---|
| [3.1]({{ '/secplus/objectives/3-1/' | relative_url }}) | Compare and contrast security implications of different architecture models. | done |
| **3.2** | Given a scenario, apply security principles to secure enterprise infrastructure. (current) | done |
| [3.3]({{ '/secplus/objectives/3-3/' | relative_url }}) | Compare and contrast concepts and strategies to protect data. | done |
| [3.4]({{ '/secplus/objectives/3-4/' | relative_url }}) | Explain the importance of resilience and recovery in security architecture. | done |

[← Previous: Objective 3.1]({{ '/secplus/objectives/3-1/' | relative_url }}) | [Back to Dashboard]({{ '/secplus/' | relative_url }}) | [Next: Objective 3.3 →]({{ '/secplus/objectives/3-3/' | relative_url }})
