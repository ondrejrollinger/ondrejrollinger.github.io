---
layout: objective
title: "Security+ 2.2 — Explain common threat vectors and attack surfaces."
objective_id: "2.2"
domain: "2.0 Threats, Vulnerabilities, and Mitigations"
status: "done"
tags:
  - secplus701
permalink: /secplus/objectives/2-2/
---

# Security+ 2.2 — Explain common threat vectors and attack surfaces.

Status: <span class="status-badge done">done</span>

## Exam objective
Explain common threat vectors and attack surfaces.

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

A **threat vector** is *how* an attacker gets in — the pathway or method to deliver an attack. An **attack surface** is *where* they can potentially get in — all exploitable entry points on a system or network. This objective also covers social engineering, which exploits the human attack surface.

---

### Threat vector vs. attack surface

| Concept | Definition | Key question |
|---|---|---|
| **Threat vector** | Method or pathway used to deliver the attack | *How* does the attacker get in? |
| **Attack surface** | All points where unauthorized entry or data extraction is possible | *Where* can the attacker get in? |

Reducing the attack surface: restrict access, remove unnecessary software, disable unused protocols.

---

### Common threat vectors

| Vector | Description | Example Attack |
|---|---|---|
| **Messages (email/SMS/IM)** | Malicious content delivered via messaging | Phishing email with malicious link |
| **Images** | Malicious code embedded in image files | Steganography-based malware delivery |
| **Files** | Malicious documents disguised as legitimate files | Macro-infected Word doc as attachment |
| **Voice calls (vishing)** | Tricks victim into revealing info over phone | Fake tech support call |
| **Removable devices** | Infected USB drives or removable media | Baiting — USB left in parking lot |
| **Unsecured networks** | Wireless, wired, or Bluetooth without proper controls | Evil twin Wi-Fi, BlueBorne exploit |

---

### Social engineering: motivational triggers

Social engineers exploit **human psychology** rather than technical vulnerabilities.

| Trigger | How it's used | Key phrase |
|---|---|---|
| **Authority** | Impersonating boss, IT admin, government | "I'm from corporate IT…" |
| **Urgency** | Creates panic, shortcuts critical thinking | "Your account will be deleted in 1 hour" |
| **Social proof** | Peer pressure — everyone else complied | "All other managers have already done this" |
| **Scarcity** | Fear of missing out drives hasty decisions | "Only 2 spots left" |
| **Likability** | Builds rapport — people comply with people they like | Attacker acts friendly, finds common ground |
| **Fear** | Threat of negative consequences | "If you don't comply, you'll be audited" |

---

### Impersonation techniques

- **Brand impersonation:** Pretends to represent a legitimate company using logos, language, domain look-alikes.
- **Typosquatting (URL hijacking):** Registers a domain with a common typo (e.g., `gooogle.com`) to capture misdirected traffic.
- **Watering hole attack:** Compromises a trusted website the target is known to visit; malware infects victims on browsing.

### Pretexting

Creates a fabricated but credible scenario to coax the victim into providing information.
Mitigation: train employees not to fill in missing information for callers — require them to prove their identity.

---

### Phishing attack types

| Type | Target | Channel | Defining Feature |
|---|---|---|---|
| **Phishing** | General / mass | Email | Broad, untargeted; impersonates trusted source |
| **Spear phishing** | Specific person / group | Email | Personalized; higher success rate |
| **Whaling** | C-suite executives | Email | Spear phishing aimed at executives |
| **BEC (Business Email Compromise)** | Business employees | Email | Uses a **compromised real account** |
| **Vishing** | General | Phone / voice | Voice-based phishing |
| **Smishing** | General | SMS text | Text message phishing |

**Phishing red flags:**
- Urgency — "Respond immediately or your account will be suspended"
- Unusual requests — asking for passwords, card numbers, credentials
- Mismatched URLs — hover reveals a different URL than the displayed text
- Strange sending address — display name matches but actual address doesn't
- Poor grammar / spelling — broken English, excessive typos

---

### Frauds, scams, and influence campaigns

- **Identity fraud:** Uses victim's credit card or personal info to make purchases.
- **Identity theft:** Fully assumes the victim's identity to open new accounts.
- **Invoice scam:** Tricks target into paying a fake invoice for goods never ordered.
- **Misinformation:** False information spread *without* harmful intent (the spreader believes it's true).
- **Disinformation:** Deliberately fabricated false information created *with intent to deceive*.

---

### Other social engineering attacks

| Attack | Description | Defense |
|---|---|---|
| **Diversion theft** | Creates distraction to steal valuables or information | Situational awareness |
| **Hoax** | False alarm / threat spread to cause panic; often pairs with phishing | Critical thinking, fact-checking |
| **Shoulder surfing** | Looks over victim's shoulder to capture credentials; can use cameras | Privacy screen filters |
| **Dumpster diving** | Searches discarded documents for sensitive data | Clean desk policy, cross-cut shredding |
| **Eavesdropping** | Intercepts private conversations (physical or network) | Encryption, secure meeting rooms |
| **Baiting** | Leaves malware-infected USB for victim to find | Train users: never plug in found devices |
| **Tailgating** | Follows authorized person through secured door *without their knowledge* | Access control vestibules |
| **Piggybacking** | Gets authorized employee to *knowingly* badge them in | Enforce one-person-per-badge policy |

> **Tailgating vs. piggybacking:** **Tail**gating = victim doesn't **know**; **Pig**gybacking = victim is **persuaded** (knowingly swipes badge).

---

### Bluetooth attack vectors

| Attack | Description | Key Feature |
|---|---|---|
| **BlueBorne** | Exploits Bluetooth vulnerabilities for device takeover, malware spread, or on-path attacks | **No user interaction required** |
| **BlueSmack** | DoS attack via crafted L2CAP Bluetooth packet | Overwhelms and crashes Bluetooth devices |

---

### Key distinctions to know for the exam

| Comparison | Distinction |
|---|---|
| **Tailgating vs. piggybacking** | Tailgating = victim unaware; piggybacking = victim knowingly allows it. |
| **Phishing vs. spear phishing** | Phishing = mass/untargeted; spear phishing = targeted individual or group. |
| **Whaling vs. BEC** | Whaling uses a fake/spoofed email targeting executives; BEC uses a *real compromised account*. |
| **Misinformation vs. disinformation** | Misinformation = false but spread without harmful intent; disinformation = deliberately fabricated to deceive. |
| **Vishing vs. smishing** | Vishing = voice / phone; smishing = SMS / text. |
| **Watering hole vs. phishing** | Watering hole = compromised trusted website; phishing = fake email luring victim to act. |

---

### Common exam traps

**Trap: Confusing tailgating and piggybacking.**
Reality: The difference is consent — tailgating is done without the authorized user's knowledge; piggybacking involves the authorized user being convinced to help.

**Trap: Thinking whaling is separate from spear phishing.**
Reality: Whaling *is* spear phishing — it's specifically aimed at high-value executive targets.

**Trap: Confusing misinformation with disinformation.**
Reality: Disinformation requires intent to deceive. Misinformation can be spread by someone who genuinely believes it's true.

**Trap: Assuming BlueBorne requires the victim to pair a device or click something.**
Reality: BlueBorne requires *no user interaction* — proximity to a vulnerable Bluetooth device is sufficient.

---

### Exam tips

1. USB in parking lot → **baiting**.
2. Employee followed through door without noticing → **tailgating**.
3. Employee knowingly holds door or swipes badge for someone → **piggybacking**.
4. Highly targeted email to a CEO → **whaling**.
5. Legitimate internal email account used to request wire transfer → **BEC**.
6. Trusted website compromised to infect regular visitors → **watering hole**.
7. Questions about reducing attack surface → restrict access, remove unnecessary software, disable unused protocols.

---

## Key terms

- **Threat vector** — The method or pathway used to deliver a malicious payload or gain unauthorized access.
- **Attack surface** — All points where an unauthorized user could attempt to enter or extract data.
- **Phishing** — Mass email attack impersonating a trusted source to steal credentials or deliver malware.
- **Spear phishing** — Targeted phishing aimed at a specific individual or group.
- **Whaling** — Spear phishing targeting C-level executives.
- **Vishing** — Voice phishing using phone calls.
- **Smishing** — SMS / text message phishing.
- **BEC (Business Email Compromise)** — Uses a compromised legitimate business email account to authorize fraud.
- **Pretexting** — Creating a fabricated scenario to manipulate a target into revealing information.
- **Typosquatting** — Registering a domain with a common typo to capture misdirected traffic.
- **Watering hole attack** — Compromising a trusted website frequented by the target.
- **Baiting** — Leaving malware-infected media for a victim to find and use.
- **Tailgating** — Following an authorized person into a secured area without their knowledge.
- **Piggybacking** — Gaining physical access by convincing an authorized person to let you in.
- **Misinformation** — False information spread without harmful intent.
- **Disinformation** — Deliberately created and spread false information intended to deceive.
- **BlueBorne** — Bluetooth vulnerability set enabling device takeover with no user interaction.

---

## Examples / scenarios

**Scenario 1:** A CFO receives an email from what appears to be the CEO's actual email address, asking for an urgent wire transfer to a new vendor. Investigation shows the CEO's mailbox was compromised last week.
- **Answer:** Business Email Compromise (BEC) — a legitimate internal account was used.

**Scenario 2:** A security researcher finds that a popular infosec blog has been compromised and is now serving malware to visitors who are typically security professionals.
- **Answer:** Watering hole attack — the attacker chose a trusted site known to be visited by the intended targets.

**Scenario 3:** An employee finds a USB drive labeled "Payroll_2024.xlsx" in the company parking garage and plugs it in out of curiosity, infecting their workstation.
- **Answer:** Baiting — the attacker deliberately planted the device to exploit curiosity.

**Scenario 4:** An attacker calls a helpdesk claiming to be a new manager who locked himself out on his first day and provides just enough plausible detail to sound credible.
- **Answer:** Pretexting with vishing — fabricated scenario delivered by voice call.

**Scenario 5:** A foreign-funded social media campaign spreads false voting location information in a key electoral district.
- **Answer:** Disinformation (influence campaign) — deliberately false information designed to deceive.

---

## Mini quiz

<details>
<summary><strong>Question 1:</strong> What is the difference between a threat vector and an attack surface?</summary>

**Answer:** A threat vector is the *method* used to attack (the "how"). An attack surface is the sum of all *points* an attacker could potentially exploit (the "where"). Reducing the attack surface shrinks the number of viable threat vectors.
</details>

<details>
<summary><strong>Question 2:</strong> What are the six motivational triggers social engineers exploit?</summary>

**Answer:** Authority, Urgency, Scarcity, Social proof, Fear, and Likability.
</details>

<details>
<summary><strong>Question 3:</strong> How does a watering hole attack work?</summary>

**Answer:** The attacker identifies a trusted website frequented by the target, compromises that site and injects malware, then waits for targets to visit. The victims are infected simply by browsing to a website they already trusted.
</details>

<details>
<summary><strong>Question 4:</strong> What distinguishes BEC from whaling?</summary>

**Answer:** Whaling uses a fake or spoofed email targeting executives. BEC uses a *real compromised internal email account* — making it much harder to detect because the email genuinely originates from inside the organization.
</details>

<details>
<summary><strong>Question 5:</strong> What makes BlueBorne especially dangerous?</summary>

**Answer:** BlueBorne requires no user interaction — the attacker only needs to be within Bluetooth range of a vulnerable device. There is no link to click, no pairing to accept, no notification given to the victim.
</details>

### CompTIA-style practice questions

<details>
<summary><strong>Question 6:</strong> A CFO receives a highly personalized email — containing her assistant's name and details of an active project — requesting approval of a vendor payment. The email is sent from the CEO's actual corporate email address, which was compromised the previous week. Which attack type BEST describes this?<br>A. Phishing<br>B. Whaling<br>C. Business Email Compromise (BEC)<br>D. Spear phishing</summary>

**Correct Answer: C. Business Email Compromise (BEC)**

The email originates from a *real, compromised* internal account — that is the defining characteristic of BEC.

- A: phishing is broad and untargeted, sent from external fake addresses.
- B: whaling targets executives but uses a fake/spoofed address, not a compromised real account.
- D: spear phishing is targeted but uses an external fake address, not a compromised real one.
</details>

<details>
<summary><strong>Question 7:</strong> An employee holds the secure door open after an individual in business attire explains they forgot their badge. The employee recognizes the person from a previous meeting. What physical social engineering technique does this represent?<br>A. Tailgating<br>B. Piggybacking<br>C. Impersonation<br>D. Baiting</summary>

**Correct Answer: B. Piggybacking**

Piggybacking occurs when an unauthorized person convinces an authorized user to *knowingly* grant them physical access.

- A: tailgating means the victim is *unaware* — they did not knowingly let the person in.
- C: impersonation describes the pretense used; piggybacking is the physical access technique itself.
- D: baiting involves malicious media, not physical entry.
</details>

<details>
<summary><strong>Question 8 (Multi-select):</strong> A security trainer is creating phishing awareness content. Which TWO items are reliable phishing indicators to teach employees? (Select TWO.)<br>A. The email arrives outside of business hours<br>B. The link text in the email does not match the actual URL shown on hover<br>C. The email creates extreme urgency demanding immediate action<br>D. The email comes from a known corporate domain<br>E. The email contains a PDF attachment</summary>

**Correct Answers: B and C**

Mismatched URLs (B) and artificial urgency (C) are two of the most consistently tested phishing indicators on CompTIA exams.

- A: time of arrival is not a reliable phishing indicator.
- D: phishing emails routinely spoof or compromise corporate domains.
- E: legitimate business emails frequently contain PDF attachments; this alone is not a red flag.
</details>

---

## Related objectives

- [**2.1**]({{ '/secplus/objectives/2-1/' | relative_url }}) — Threat actors use these vectors to carry out their attacks.
- [**2.4**]({{ '/secplus/objectives/2-4/' | relative_url }}) — Analyzing indicators of malicious activity often begins by identifying which vector was used.
- [**2.5**]({{ '/secplus/objectives/2-5/' | relative_url }}) — Mitigation techniques directly reduce the attack surface and defend against specific vectors.
- [**5.6**]({{ '/secplus/objectives/5-6/' | relative_url }}) — Security awareness training is the primary defense against social engineering vectors.

---

## Navigation

**Domain 2.0: Threats, Vulnerabilities, and Mitigations**

| Objective | Title | Status |
|---|---|---|
| [2.1]({{ '/secplus/objectives/2-1/' | relative_url }}) | Compare and contrast common threat actors and motivations. | done |
| **2.2** | Explain common threat vectors and attack surfaces. (current) | done |
| [2.3]({{ '/secplus/objectives/2-3/' | relative_url }}) | Explain various types of vulnerabilities. | done |
| [2.4]({{ '/secplus/objectives/2-4/' | relative_url }}) | Given a scenario, analyze indicators of malicious activity. | done |
| [2.5]({{ '/secplus/objectives/2-5/' | relative_url }}) | Explain the purpose of mitigation techniques used to secure the enterprise. | done |

[← Previous: Objective 2.1]({{ '/secplus/objectives/2-1/' | relative_url }}) | [Back to Dashboard]({{ '/secplus/' | relative_url }}) | [Next: Objective 2.3 →]({{ '/secplus/objectives/2-3/' | relative_url }})
