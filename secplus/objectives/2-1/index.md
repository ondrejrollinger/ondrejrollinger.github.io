---
layout: default
title: "Security+ 2.1 — Compare and contrast common threat actors and motivations."
objective_id: "2.1"
domain: "2.0 Threats, Vulnerabilities, and Mitigations"
status: "done"
tags:
  - secplus701
permalink: /secplus/objectives/2-1/
---

# Security+ 2.1 — Compare and contrast common threat actors and motivations.

Status: <span class="status-badge done">done</span>

## Exam objective
Compare and contrast common threat actors and motivations.

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

Threat actors are the people or groups behind cyberattacks. The exam tests your ability to match actor **type** to its typical **attributes** (skill, resources, internal/external) and **motivation**. Knowing these pairings lets you quickly eliminate distractors in scenario questions.

---

### Threat actor types and attributes

| Actor Type | Internal / External | Skill Level | Resources | Primary Motivation | Key Phrase |
|---|---|---|---|---|---|
| **Unskilled attacker (script kiddie)** | External | Low | Minimal | Notoriety / disruption | Uses pre-built tools |
| **Hacktivist** | External | Low–Medium | Limited | Ideology / political | Website defacement, DDoS |
| **Organized crime** | External | High | Well-funded | **Financial gain** | Ransomware, identity theft |
| **Nation-state / APT** | External | Very high | Government-backed | **Strategic / espionage** | Long-term stealth |
| **Insider threat** | **Internal** | Varies | Privileged access | Varies (revenge, gain, negligence) | Trusted access = hard to detect |
| **Shadow IT** | Internal | Low–Medium | Company resources | Convenience | Unauthorized systems / apps |

> **Mnemonic: UOHNIS** — Unskilled, Organized crime, Hacktivist, Nation-state, Insider, Shadow IT

---

### Threat actor motivations

| Motivation | Description | Typical Actor |
|---|---|---|
| **Data exfiltration** | Unauthorized transfer of sensitive data | Nation-state, organized crime, insider |
| **Financial gain** | Ransomware, banking trojans, fraud | Organized crime |
| **Blackmail** | Threaten to release compromising info | Organized crime |
| **Espionage** | Steal classified or competitive intel | Nation-state |
| **Service disruption** | Take systems / services offline | Hacktivist, nation-state |
| **Philosophical / political** | Ideological cause — hacktivism | Hacktivist |
| **Revenge** | Retaliate against a perceived wrong | Insider threat |
| **Disruption / chaos** | Cause widespread harm without a clear goal | Unskilled attacker |
| **War** | Cyber operations as acts of warfare | Nation-state |
| **Ethical** | Improve security (authorized hackers only) | Penetration testers |

> **Exam tip:** CompTIA distinguishes **intent** (what they want to achieve) from **motivation** (why they do it). Intent = objective; motivation = driving force.

---

### Deep dive: key actor types

#### Nation-state actors and APTs

- **Advanced Persistent Threat (APT):** Long-term, stealthy intrusion — the attacker stays undetected to exfiltrate data or monitor activity over time.
- Nation-state actors use: custom malware, zero-day exploits, supply-chain attacks.
- **False flag attack:** Designed to look like it came from a different actor to mislead attribution investigators.

#### Insider threats

- Can be **malicious** (intentional sabotage, data theft) or **negligent** (accidental, unaware of best practices).
- Mitigations: zero-trust architecture, robust access controls, regular audits, security awareness training.
- Hard to detect because the actor already has legitimate credentials and authorized access.

#### Shadow IT

- Systems, devices, or apps deployed **without IT department knowledge or approval**.
- Common cause: official security posture is too restrictive for daily workflows.
- **BYOD (Bring Your Own Device)** is a closely related concept — personal devices used for work purposes.
- Risk: bypasses security controls; creates an unmonitored attack surface.

---

### Key distinctions to know for the exam

| Comparison | Distinction |
|---|---|
| **Hacktivist vs. organized crime** | Hacktivist = ideology-driven, not financial; organized crime = money-motivated. |
| **Nation-state vs. APT** | APT describes the *technique* (long-term, stealthy); nation-state describes the *actor*. Most APTs are nation-state-sponsored. |
| **Insider threat vs. shadow IT** | Insider threat = the *person* posing a risk; shadow IT = the *unauthorized system*. |
| **Intent vs. motivation** | Intent = specific objective; motivation = underlying driving force. |
| **False flag vs. standard attack** | False flag deliberately misattributes the source to mislead investigators. |
| **Malicious vs. negligent insider** | Malicious = deliberate harm; negligent = accidental risk due to poor security practices. |

---

### Common exam traps

**Trap: Assuming all insider threats are malicious.**
Reality: Many insider incidents are caused by negligence or poor security awareness — no harmful intent required.

**Trap: Treating APT and nation-state as identical.**
Reality: APT is a *technique* (long-term persistence and stealth). Nation-states are the most common sponsors, but organized crime can also execute APT-style campaigns.

**Trap: Thinking script kiddies can't cause real damage.**
Reality: Even low-skill actors using off-the-shelf DDoS tools can take down services. Low skill ≠ low impact.

**Trap: Classifying shadow IT as an external threat.**
Reality: Shadow IT originates inside the organization — it is an internal threat, even when there is no malicious intent.

**Trap: Assuming hacktivists are completely resource-starved.**
Reality: Groups like Anonymous have coordinated large-scale attacks. Resources are *limited*, not zero.

---

### Exam tips

1. When a scenario describes **long-term, stealthy intrusion with no financial demand** → think APT / nation-state (espionage).
2. When motivation is **ideological or political** → think hacktivist (not financial).
3. When an employee is involved, check whether the scenario signals **malicious insider** or **negligent insider** — look for intent cues.
4. **"False flag"** is a specific exam term — memorize it as an attack designed to misattribute the source.
5. For any actor, ask: internal or external? Skill level? Motivation? These three axes resolve most questions.
6. **Organized crime = money**. Every time. If the question involves ransomware or identity theft, organized crime is likely the answer.

---

## Key terms

- **Threat actor** — Any entity that poses a risk to an organization by attempting unauthorized actions.
- **APT (Advanced Persistent Threat)** — Prolonged, targeted intrusion where the attacker remains undetected while exfiltrating data or monitoring systems.
- **Hacktivist** — Attacker motivated by ideology or political cause rather than financial gain.
- **Organized crime** — Well-structured cybercriminal groups motivated primarily by financial gain.
- **Nation-state actor** — Government-sponsored attacker with advanced skills and significant resources.
- **Insider threat** — Threat originating from within the organization, either malicious or negligent.
- **Shadow IT** — IT systems or applications deployed without explicit organizational approval.
- **BYOD (Bring Your Own Device)** — Policy/practice of employees using personal devices for work.
- **False flag attack** — Attack orchestrated to appear to originate from a different source.
- **Script kiddie (unskilled attacker)** — Low-skill attacker who relies on pre-made tools and exploits created by others.
- **Doxing** — Public release of private information about an individual or organization; a hacktivist technique.
- **Intent** — The specific objective a threat actor aims to achieve through an attack.
- **Motivation** — The underlying reason driving a threat actor's behavior.

---

## Examples / scenarios

**Scenario 1:** A threat group has been inside a defense contractor's network for 18 months, slowly exfiltrating classified R&D files. No ransomware was deployed and no systems were damaged.
- **Answer:** Nation-state actor / APT. Indicators: long-term stealth, strategic target, espionage motivation, no financial demand.

**Scenario 2:** A disgruntled employee uses still-active credentials to delete production database records the week after being terminated.
- **Answer:** Malicious insider threat. Motivation: revenge. Key indicator: legitimate internal access used for deliberate harm.

**Scenario 3:** A finance employee installs a personal cloud storage app on their work laptop to share files more easily, bypassing the company's approved tools.
- **Answer:** Shadow IT / negligent insider. No malicious intent, but creates an unmonitored data-exfiltration risk.

**Scenario 4:** A cyberattack targets a power utility. Forensics suggest Russian origins, but all command-and-control infrastructure is routed through Chinese servers with Chinese-language strings.
- **Answer:** False flag attack. The apparent origin is deliberately designed to mislead attribution.

**Scenario 5:** A group defaces a major bank's website and posts manifestos against corporate greed, then shares the screenshots on social media.
- **Answer:** Hacktivist. Motivation is philosophical/political; technique is website defacement.

---

## Mini quiz

<details>
<summary><strong>Question 1:</strong> What distinguishes an APT from a standard cyberattack?</summary>

**Answer:** An APT involves prolonged, stealthy access — the attacker remains undetected for an extended period (months or years) to steal data or monitor activity, rather than causing immediate, visible damage. Standard attacks are often opportunistic and short-lived.
</details>

<details>
<summary><strong>Question 2:</strong> What is the primary motivation of organized crime threat actors?</summary>

**Answer:** Financial gain — through ransomware, identity theft, fraud, data breaches, and banking trojans. Unlike nation-states or hacktivists, organized crime groups are not driven by ideology or strategic national objectives.
</details>

<details>
<summary><strong>Question 3:</strong> How does shadow IT differ from a malicious insider threat?</summary>

**Answer:** Shadow IT is the *thing* — unauthorized IT systems or apps deployed inside the organization. A malicious insider is the *person* — someone who deliberately misuses access to harm the org. An employee deploying shadow IT could be negligent but not necessarily malicious.
</details>

<details>
<summary><strong>Question 4:</strong> Name three techniques hacktivists commonly use.</summary>

**Answer:** Website defacement, DDoS attacks, doxing (releasing private information publicly), and leaking sensitive data to the public.
</details>

<details>
<summary><strong>Question 5:</strong> Why are insider threats particularly difficult to detect?</summary>

**Answer:** Insiders already have legitimate credentials and authorized access. Their activities often appear as normal user behavior, making it harder for security tools to distinguish malicious actions from routine work. Standard perimeter defenses don't apply when the threat is already inside.
</details>

### CompTIA-style practice questions

<details>
<summary><strong>Question 6:</strong> A cybersecurity analyst discovers that an attacker has been present inside the corporate network for 14 months, slowly copying sensitive R&D files to an external server. No systems were damaged and no ransom was demanded. Which type of threat actor BEST describes this attacker?<br>A. Script kiddie<br>B. Hacktivist<br>C. Nation-state / APT<br>D. Organized crime</summary>

**Correct Answer: C. Nation-state / APT**

Long-term stealth, no financial demand, and targeted theft of R&D data are classic APT / nation-state indicators consistent with espionage.

- A is wrong: script kiddies lack the skill for a 14-month undetected operation.
- B is wrong: hacktivists are ideologically motivated and typically publicize their actions.
- D is wrong: organized crime would likely deploy ransomware or monetize the access quickly.
</details>

<details>
<summary><strong>Question 7:</strong> An employee installs a personal file-sharing application on a corporate laptop to make collaboration easier. The IT team was never informed. Which term BEST describes this situation?<br>A. Insider threat<br>B. Shadow IT<br>C. BYOD violation<br>D. Data exfiltration</summary>

**Correct Answer: B. Shadow IT**

Shadow IT is the use of IT systems or services without explicit organizational approval. The employee had no malicious intent — convenience drove the behavior.

- A: while there is insider risk, shadow IT is the precise term for the unauthorized system/application.
- C: BYOD refers to personal *devices*, not applications installed on corporate hardware.
- D: no evidence that data was actually stolen; the risk exists but the act hasn't occurred.
</details>

<details>
<summary><strong>Question 8 (Multi-select):</strong> Which TWO characteristics BEST describe a nation-state threat actor? (Select TWO.)<br>A. Primarily motivated by financial gain<br>B. Possesses advanced technical skills and extensive government-level resources<br>C. Typically uses only publicly available hacking tools<br>D. May conduct false flag attacks to conceal attribution<br>E. Targets organizations primarily through website defacement</summary>

**Correct Answers: B and D**

Nation-state actors are characterized by high sophistication with government backing (B) and use of deception techniques like false flag attacks to misattribute the source (D).

- A: financial gain is organized crime's primary driver, not nation-states.
- C: nation-states develop custom malware and zero-days, not just public tools.
- E: website defacement is a hacktivist technique.
</details>

---

## Related objectives

- [**2.2**]({{ '/secplus/objectives/2-2/' | relative_url }}) — Threat vectors are the specific methods these actors use to attack systems.
- [**2.4**]({{ '/secplus/objectives/2-4/' | relative_url }}) — Indicators of malicious activity help identify which actor type may be responsible.
- [**1.2**]({{ '/secplus/objectives/1-2/' | relative_url }}) — Deception technologies (honeypots) are used to study and detect threat actor behavior.
- [**5.1**]({{ '/secplus/objectives/5-1/' | relative_url }}) — Security governance frameworks address insider threats through policy and access controls.

---

## Navigation

**Domain 2.0: Threats, Vulnerabilities, and Mitigations**

| Objective | Title | Status |
|---|---|---|
| **2.1 (current)** | Compare and contrast common threat actors and motivations. | <span class="status-badge done">done</span> |
| [2.2]({{ '/secplus/objectives/2-2/' | relative_url }}) | Explain common threat vectors and attack surfaces. | <span class="status-badge done">done</span> |
| [2.3]({{ '/secplus/objectives/2-3/' | relative_url }}) | Explain various types of vulnerabilities. | <span class="status-badge done">done</span> |
| [2.4]({{ '/secplus/objectives/2-4/' | relative_url }}) | Given a scenario, analyze indicators of malicious activity. | <span class="status-badge done">done</span> |
| [2.5]({{ '/secplus/objectives/2-5/' | relative_url }}) | Explain the purpose of mitigation techniques used to secure the enterprise. | <span class="status-badge done">done</span> |

[← Back to Dashboard]({{ '/secplus/' | relative_url }}) | [Next: Objective 2-2 →]({{ '/secplus/objectives/2-2/' | relative_url }})
