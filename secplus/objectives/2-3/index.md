---
layout: objective
title: "Security+ 2.3 — Explain various types of vulnerabilities."
objective_id: "2.3"
domain: "2.0 Threats, Vulnerabilities, and Mitigations"
status: "done"
tags:
  - secplus701
permalink: /secplus/objectives/2-3/
---

# Security+ 2.3 — Explain various types of vulnerabilities.

Status: <span class="status-badge done">done</span>

## Exam objective
Explain various types of vulnerabilities.

{% include official_scope_pdf.html objective_id=page.objective_id %}

---

## My notes

### Overview

Vulnerabilities are weaknesses that can be exploited to compromise confidentiality, integrity, or availability. This objective covers a broad taxonomy — from application and OS flaws to hardware, cloud, and supply-chain vulnerabilities. The exam emphasizes recognizing vulnerability *types* from scenario descriptions.

---

### Application vulnerabilities

#### Memory and injection vulnerabilities

| Vulnerability | Description | Exam keyword |
|---|---|---|
| **Memory injection** | Injecting malicious code into a running process's memory space | DLL injection, shellcode |
| **Buffer overflow** | Writing more data than a buffer can hold, overwriting adjacent memory | Classic C/C++ flaw; enables arbitrary code execution |
| **Race condition** | Two processes access the same resource simultaneously; outcome depends on timing | Time-of-check/time-of-use (TOCTOU) attack |
| **SQL injection (SQLi)** | Inserting malicious SQL into input fields to manipulate a database | `' OR 1=1 --`; input validation failure |
| **Cross-site scripting (XSS)** | Injecting malicious scripts into web pages viewed by other users | Stored vs. reflected XSS |
| **Cross-site request forgery (CSRF)** | Tricks authenticated user's browser into sending an unauthorized request | Forged requests riding valid session |
| **Directory traversal** | Uses `../` sequences to access files outside the web root | Access to `/etc/passwd` or `C:\Windows\` |

#### Other application vulnerabilities

- **Malicious update:** Attacker compromises the software update mechanism (update server, signed package) to push malware.
- **OS vulnerability:** Weaknesses in operating system code exploitable without user interaction (e.g., SMB vulnerabilities like EternalBlue/WannaCry).

---

### Hardware vulnerabilities

| Type | Description | Example |
|---|---|---|
| **Firmware vulnerabilities** | Bugs in low-level device firmware; difficult to patch; persist across OS reinstalls | Router / IoT firmware bugs |
| **End-of-life (EOL)** | Vendor no longer provides security patches | Windows XP, legacy medical devices |
| **Legacy systems** | Old systems still in production, no longer receiving updates | Industrial control systems, ATMs |
| **BIOS/UEFI vulnerabilities** | Compromise at boot level, below the OS — allows rootkit persistence | Bootkits surviving OS reinstalls |

> **Exam tip:** EOL and legacy systems require **compensating controls** (network segmentation, enhanced monitoring) since patching is not possible.

---

### Virtualization vulnerabilities

| Vulnerability | Description |
|---|---|
| **VM escape** | Attacker breaks out of a virtual machine and gains access to the hypervisor or other VMs on the same host |
| **Resource reuse** | Sensitive data (memory, storage) from one VM is not properly cleared before being reused by another VM |

> **Exam tip:** VM escape is the highest severity virtualization vulnerability — it compromises the hypervisor itself.

---

### Cloud-specific vulnerabilities

| Vulnerability | Description |
|---|---|
| **Shared tenancy** | Multiple organizations share physical infrastructure; misconfiguration can expose one tenant's data to another |
| **Inadequate access management** | Overly permissive IAM roles / policies in cloud environments |
| **Insecure APIs** | Cloud services are API-driven; improperly secured APIs are a primary cloud attack surface |
| **Misconfigured storage** | Publicly exposed S3 buckets or Azure Blob containers leaking sensitive data |
| **Single point of failure** | Reliance on a single cloud region or provider without redundancy |

---

### Supply chain vulnerabilities

The supply chain includes hardware manufacturers, software vendors, and managed service providers (MSPs).

| Type | Description | Example |
|---|---|---|
| **Hardware supply chain** | Malicious components inserted during manufacturing | Tampered network cards or chips |
| **Software supply chain** | Malicious code injected into legitimate software during development or distribution | SolarWinds SUNBURST attack |
| **Managed service provider (MSP)** | Attackers compromise an MSP to pivot into all of that MSP's clients | Kaseya VSA attack |

> **Exam tip:** Supply chain attacks are especially dangerous because the attack arrives via **trusted** channels — software updates, legitimate hardware, trusted vendors.

---

### Cryptographic vulnerabilities

| Vulnerability | Description |
|---|---|
| **Weak algorithms** | Use of MD5, SHA-1, DES, RC4 — algorithms with known collision/break techniques |
| **Short key lengths** | Keys too short to resist brute force (e.g., 56-bit DES, 512-bit RSA) |
| **Improper certificate management** | Expired certs, self-signed certs in production, failure to revoke compromised certs |
| **Downgrade attack** | Forces connection to use older, weaker protocol versions (e.g., POODLE forces SSL 3.0) |

---

### Misconfiguration vulnerabilities

- **Default credentials:** Factory default usernames/passwords left unchanged (e.g., `admin/admin`).
- **Open ports / unnecessary services:** Unused services increase attack surface.
- **Weak permissions:** Over-privileged accounts or world-readable files.
- **Missing patches:** Known vulnerabilities left unpatched.
- **Insecure defaults:** Security features disabled by default (e.g., unencrypted protocols).

> **Exam tip:** Misconfiguration is consistently one of the most common sources of real-world breaches. Always harden systems by removing defaults.

---

### Mobile device vulnerabilities

| Vulnerability | Description |
|---|---|
| **Sideloading** | Installing apps from outside the official app store; bypasses vendor security review |
| **Jailbreaking (iOS) / Rooting (Android)** | Removes OS restrictions; eliminates built-in security controls |
| **Outdated OS / unpatched firmware** | Many mobile devices receive updates infrequently or never |
| **Insecure Wi-Fi** | Mobile devices connecting to rogue or open Wi-Fi networks |

---

### Zero-day vulnerabilities

- **Zero-day:** A vulnerability that is *unknown to the vendor* — no patch exists.
- Called "zero-day" because the vendor has had **zero days** to address it.
- Particularly dangerous because standard patch management cannot defend against it.
- Defenses: behavior-based detection (EDR/XDR), network segmentation, defense-in-depth.

> **Zero-day vs. unpatched vulnerability:** A zero-day has no patch available. An unpatched vulnerability *has* a patch — the organization just hasn't applied it yet.

---

### Key distinctions to know for the exam

| Comparison | Distinction |
|---|---|
| **Buffer overflow vs. SQL injection** | Buffer overflow attacks memory directly; SQLi targets database query logic via input fields. |
| **XSS vs. CSRF** | XSS injects script into a page served to other users; CSRF tricks a user's browser into making unauthorized requests. |
| **EOL vs. legacy** | EOL = vendor no longer supports it (no patches coming); legacy = old technology still in use (may or may not be EOL). |
| **VM escape vs. resource reuse** | VM escape = attacker breaks hypervisor boundary; resource reuse = leftover data leaks between VMs. |
| **Zero-day vs. unpatched** | Zero-day = no patch exists yet; unpatched = patch exists but wasn't applied. |
| **Sideloading vs. jailbreaking** | Sideloading = installing apps outside app store; jailbreaking = removing OS-level security restrictions entirely. |

---

### Common exam traps

**Trap: Assuming "zero-day" means the attack just happened.**
Reality: Zero-day refers to the vendor having zero days to fix it — the vulnerability is unknown to them. The attack timing is unrelated.

**Trap: Thinking legacy systems can be fully protected by patching.**
Reality: Legacy systems often *cannot* be patched — they need compensating controls like network segmentation and enhanced monitoring.

**Trap: Confusing XSS and CSRF.**
Reality: XSS injects malicious script into a webpage affecting *other users*. CSRF hijacks an *authenticated user's session* to make unauthorized requests on their behalf.

**Trap: Treating supply chain attacks as simple malware.**
Reality: Supply chain attacks exploit the *trust* in legitimate channels — the compromised component arrives via a trusted update or vendor, bypassing standard defenses.

---

### Exam tips

1. "Unknown to the vendor, no patch exists" → **zero-day**.
2. "Old system, vendor no longer supports it" → **EOL / legacy** → needs **compensating controls**.
3. "Broke out of VM to access hypervisor" → **VM escape**.
4. "Installed app from outside the app store" → **sideloading**.
5. "Input field was used to manipulate the database" → **SQL injection**.
6. "Malicious code injected through a trusted software update" → **supply chain** / malicious update.
7. Default credentials unchanged on a newly deployed device → **misconfiguration**.

---

## Key terms

- **Vulnerability** — A weakness in a system, application, or process that can be exploited to compromise security.
- **Buffer overflow** — Writing data beyond a buffer's capacity, overwriting adjacent memory and potentially enabling code execution.
- **SQL injection (SQLi)** — Inserting malicious SQL via input fields to manipulate or extract database data.
- **XSS (Cross-site scripting)** — Injecting malicious client-side scripts into web pages viewed by other users.
- **CSRF (Cross-site request forgery)** — Tricks an authenticated user's browser into sending unauthorized requests.
- **Race condition / TOCTOU** — Exploits timing between resource check and use; two processes compete for the same resource.
- **Zero-day** — Vulnerability unknown to the vendor; no patch exists.
- **VM escape** — Breaking out of a virtual machine to access the hypervisor or other VMs.
- **EOL (End-of-life)** — Vendor no longer provides security patches for a system or application.
- **Sideloading** — Installing mobile apps outside the official app store.
- **Supply chain attack** — Compromising software or hardware through trusted vendor or update channels.
- **Firmware vulnerability** — Security flaw in low-level device code; persists across OS reinstalls.
- **Misconfiguration** — Insecure default settings, open ports, or weak permissions left unaddressed.

---

## Examples / scenarios

**Scenario 1:** A developer discovers that a competitor's update server was compromised. The latest version of the competitor's security software now contains a backdoor that was silently pushed to 18,000 customers.
- **Answer:** Supply chain attack (malicious update). The trusted update mechanism was weaponized.

**Scenario 2:** A penetration tester submits `' OR '1'='1` into a login form and gains access to the admin panel without credentials.
- **Answer:** SQL injection. Input validation was not in place; malicious SQL manipulated the query logic.

**Scenario 3:** A hospital uses an MRI machine running Windows XP Embedded — the vendor has not issued updates since 2014. The hospital cannot replace the device.
- **Answer:** EOL / legacy system vulnerability. The system needs compensating controls: network segmentation, monitoring, restricted access.

**Scenario 4:** A cloud customer's files are accessible to other tenants because a storage bucket was configured as publicly readable by default.
- **Answer:** Cloud misconfiguration vulnerability (insecure defaults / open storage).

**Scenario 5:** Researchers discover an attacker has been running malware on a server for three months by exploiting a vulnerability that was only reported to the vendor last week.
- **Answer:** Zero-day. The vendor had no time (zero days) to patch before active exploitation began.

---

## Mini quiz

<details>
<summary><strong>Question 1:</strong> What is a zero-day vulnerability and why is it especially dangerous?</summary>

**Answer:** A zero-day is a vulnerability unknown to the vendor, meaning no patch is available. It's dangerous because standard patch management cannot address it — the only defenses are behavioral detection, network segmentation, and defense-in-depth.
</details>

<details>
<summary><strong>Question 2:</strong> What is VM escape and why is it critical?</summary>

**Answer:** VM escape occurs when an attacker breaks out of a virtual machine's isolation and gains access to the hypervisor or other VMs on the same physical host. It's critical because it defeats the fundamental security model of virtualization — isolation between tenants.
</details>

<details>
<summary><strong>Question 3:</strong> How does XSS differ from CSRF?</summary>

**Answer:** XSS injects malicious scripts into a webpage that are then executed by *other users* who view that page. CSRF tricks an *already-authenticated* user's browser into sending unauthorized requests to a site they're logged into, exploiting their active session.
</details>

<details>
<summary><strong>Question 4:</strong> What security risks does sideloading mobile apps introduce?</summary>

**Answer:** Apps installed outside the official app store bypass the vendor's security review process, meaning they may contain malware, spyware, or backdoors that would normally be caught before publication.
</details>

<details>
<summary><strong>Question 5:</strong> Why are supply chain attacks particularly dangerous?</summary>

**Answer:** They arrive via trusted channels — legitimate software updates, hardware from reputable vendors, or services from trusted MSPs. Defenders have little reason to suspect malicious content from a trusted source, and standard defenses (URL filtering, email scanning) don't apply.
</details>

### CompTIA-style practice questions

<details>
<summary><strong>Question 6:</strong> A security analyst discovers that a web application allows an attacker to retrieve the contents of `/etc/passwd` by submitting the URL `https://example.com/view?file=../../etc/passwd`. Which vulnerability type does this represent?<br>A. SQL injection<br>B. Buffer overflow<br>C. Directory traversal<br>D. Cross-site scripting</summary>

**Correct Answer: C. Directory traversal**

The `../` sequences navigate outside the web root directory to access system files — the defining characteristic of a directory traversal attack.

- A: SQL injection targets database queries through input fields; no SQL is involved here.
- B: buffer overflow involves writing past memory boundaries; this is a file path manipulation.
- D: XSS injects client-side scripts into pages viewed by other users; this is a server-side file access issue.
</details>

<details>
<summary><strong>Question 7:</strong> A manufacturing company runs a proprietary industrial control system that the vendor stopped supporting in 2019. The system cannot be patched. Which action BEST reduces risk?<br>A. Upgrade to the latest Windows version<br>B. Implement network segmentation and enhanced monitoring as compensating controls<br>C. Disable antivirus to improve performance<br>D. Apply the vendor's latest firmware update</summary>

**Correct Answer: B. Implement network segmentation and enhanced monitoring as compensating controls**

When a system is EOL and cannot be patched or replaced, compensating controls — especially isolation via network segmentation and increased monitoring — are the appropriate response.

- A: the ICS runs proprietary software; upgrading the OS would likely break the system.
- C: disabling antivirus increases risk, not decreases it.
- D: the vendor stopped support in 2019; no updates are available.
</details>

<details>
<summary><strong>Question 8 (Multi-select):</strong> A security team is reviewing vulnerability categories after a breach. Which TWO of the following represent supply chain vulnerabilities? (Select TWO.)<br>A. An attacker exploits a buffer overflow in a web application<br>B. Malicious code is inserted into a legitimate software package before it is distributed to customers<br>C. A managed service provider's remote management tool is compromised, giving attackers access to all MSP clients<br>D. An employee installs an unauthorized app on their work laptop<br>E. A zero-day exploit targets an unpatched OS</summary>

**Correct Answers: B and C**

Supply chain attacks involve compromising trusted third-party vendors, software packages, or service providers.

- B: inserting malware into a software package before distribution is a classic software supply chain attack.
- C: compromising an MSP to pivot into its clients is a supply chain / MSP attack (e.g., Kaseya VSA).
- A: a buffer overflow targets the application directly, not the supply chain.
- D: unauthorized app installation is shadow IT / sideloading.
- E: zero-day is a vulnerability type, not a supply chain issue.
</details>

---

## Related objectives

- [**2.4**]({{ '/secplus/objectives/2-4/' | relative_url }}) — Indicators of malicious activity are the observable signs that these vulnerabilities have been exploited.
- [**2.5**]({{ '/secplus/objectives/2-5/' | relative_url }}) — Mitigation techniques directly address the vulnerability types covered here.
- [**1.4**]({{ '/secplus/objectives/1-4/' | relative_url }}) — Cryptographic solutions address cryptographic vulnerabilities.
- [**4.3**]({{ '/secplus/objectives/4-3/' | relative_url }}) — Vulnerability management is the operational process for finding and remediating these vulnerability types.

---

## Navigation

**Domain 2.0: Threats, Vulnerabilities, and Mitigations**

| Objective | Title | Status |
|---|---|---|
| [2.1]({{ '/secplus/objectives/2-1/' | relative_url }}) | Compare and contrast common threat actors and motivations. | done |
| [2.2]({{ '/secplus/objectives/2-2/' | relative_url }}) | Explain common threat vectors and attack surfaces. | done |
| **2.3** | Explain various types of vulnerabilities. (current) | done |
| [2.4]({{ '/secplus/objectives/2-4/' | relative_url }}) | Given a scenario, analyze indicators of malicious activity. | done |
| [2.5]({{ '/secplus/objectives/2-5/' | relative_url }}) | Explain the purpose of mitigation techniques used to secure the enterprise. | done |

[← Previous: Objective 2.2]({{ '/secplus/objectives/2-2/' | relative_url }}) | [Back to Dashboard]({{ '/secplus/' | relative_url }}) | [Next: Objective 2.4 →]({{ '/secplus/objectives/2-4/' | relative_url }})
