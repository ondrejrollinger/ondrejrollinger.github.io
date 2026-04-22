---
layout: objective
title: "Security+ 5.6 — Given a scenario, implement security awareness practices."
objective_id: "5.6"
domain: "5.0 Security Program Management and Oversight"
status: "done"
tags:
  - secplus701
permalink: /secplus/objectives/5-6/
---

# Security+ 5.6 — Given a scenario, implement security awareness practices.

Status: <span class="status-badge done">done</span>

## Exam objective
Given a scenario, implement security awareness practices.

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

Security awareness programs educate users about threats and safe practices to create a human layer of defence. The exam tests your ability to select appropriate training methods, interpret phishing simulation metrics, recognize anomalous behaviour indicators, and describe the components of a healthy security culture.

---

### Security awareness training

Training must reach all employees at the right level of depth, delivered through the right channel.

**Audience and content by role:**

| Audience | Key topics |
|---|---|
| **All employees** | Phishing recognition, password security, physical security, incident reporting, acceptable use |
| **Developers** | Secure coding, OWASP Top 10 |
| **Administrators** | Privileged access management, system hardening |
| **Executives** | Business email compromise, targeted (spear phishing) attacks |
| **Finance** | Wire fraud, invoice scams |
| **HR** | W-2 phishing, employee data protection |

**Training frequency:**

| Trigger | Frequency |
|---|---|
| New hire | Day 1 / Week 1 orientation |
| All staff refresher | Annually |
| Phishing simulations | Quarterly (or monthly) |
| Incident-driven | After incidents or when new threats emerge |

**Training delivery methods:**

| Method | Format | Best for |
|---|---|---|
| **Computer-based training (CBT)** | Online modules, videos, quizzes | Large organizations; scalable, trackable, self-paced |
| **Instructor-led training** | Classroom or virtual (Zoom, Teams) | Technical training; small groups; Q&A and demonstration |
| **Microlearning** | Short lessons (3–5 min) via email, Slack, intranet | Busy employees; continuous low-friction reinforcement |
| **Gamification** | Points, badges, leaderboards | Increasing participation; phishing simulation engagement |

> **Exam tip:** The exam may describe a scenario and ask you to choose the delivery method. CBT = scalable/trackable; instructor-led = interactive/costly; microlearning = brief/continuous; gamification = engaging/motivating.

---

### Phishing simulations

Phishing simulations measure user susceptibility and deliver just-in-time training to those who fail.

**Simulation lifecycle:**

| Phase | Key activity |
|---|---|
| **Planning** | Define goals (baseline vs. improvement), frequency, scope, and difficulty |
| **Template selection** | Choose scenario type (generic delivery notice, IT alert, executive request) and difficulty level |
| **Execution** | Send simulated email with tracking link; record user actions |
| **Measurement** | Track opens, clicks, credential entry, and reports |
| **Just-in-time training** | Redirect users who click to an education page immediately |
| **Reporting** | Publish campaign metrics; compare to prior campaigns; adjust difficulty |

**User actions and their meaning:**

| Action | Interpretation |
|---|---|
| Deleted without action | Pass — correct response |
| Reported as phishing | Pass — ideal response |
| Opened only | Neutral — engagement without risk |
| Clicked link | Failure — susceptible |
| Entered credentials | Critical failure — high risk |

**Sample metrics showing improvement over time:**

| Campaign | Click rate | Report rate |
|---|---|---|
| Q1 (baseline) | 25% | 5% |
| Q2 (post-training) | 15% | 9% |
| Q3 | 10% | 14% |
| Q4 | 7% | 18% |

> **Exam tip:** A high click rate on the *first* simulation is expected — it establishes a baseline. The programme is evaluated on *improvement over time*, not the initial number.

**Phishing reporting mechanisms:**

| Method | Description |
|---|---|
| **Email button** | "Report Phishing" plugin in Outlook / Gmail — lowest friction |
| **Email forward** | Forward to `phishing@company.com` |
| **IT portal** | Web form for reporting suspicious emails |
| **Phone** | Direct call to IT helpdesk |

When a user reports a suspicious email, the security team reviews it, blocks the sender or domain if confirmed malicious, and deletes it from all inboxes. Users who report — even incorrectly — should receive positive feedback to reinforce the behaviour.

---

### Anomalous behaviour recognition

Training users to notice and report unusual activity is central to both insider threat detection and phishing defence.

**Email red flags:**

| Indicator | Example |
|---|---|
| Urgency / threats | "Act now or account will be closed"; "Failure to comply = termination" |
| Sender mismatch | CEO emailing from a Gmail address instead of corporate domain |
| Generic greeting | "Dear Customer" rather than the recipient's name |
| Suspicious link | Hover reveals URL different from the display text |
| Unexpected attachment | `Invoice.exe`, `Resume.pdf.scr` |
| Sensitive info request | "Reply with your password to verify your account" |

**Insider threat behavioural indicators:**

| Indicator | Description |
|---|---|
| Disgruntlement | Recent disciplinary action; expressed frustration with organisation |
| Financial stress | Discussing money problems; lifestyle inconsistent with salary |
| Access anomalies | Accessing data outside role scope |
| After-hours activity | Unusual late-night or weekend logins |
| Large data downloads | Bulk copying of company data |
| Removable media use | Frequent USB activity; potential exfiltration |
| Policy violations | Repeatedly bypassing security controls |

> **Exam tip:** Employees should be trained to report insider threat concerns to HR or the security team — not to confront the individual directly.

**Risky end-user behaviours to address in training:**

| Behaviour | Risk |
|---|---|
| Weak or reused passwords | Single breach exposes multiple accounts |
| Writing down passwords | Physical access = credential theft |
| Sharing credentials | "Use my login while I'm away" breaks accountability |
| Public Wi-Fi without VPN | Eavesdropping / man-in-the-middle |
| Tailgating / piggybacking | Unauthorised physical access |
| Leaving devices unattended | Theft; device loss = data loss |
| Social media oversharing | Reveals unannounced projects, travel, org structure |

---

### Reporting and programme metrics

**No-blame culture** is the foundation of effective incident reporting. Users who fear punishment will not report mistakes — and early reporting contains incidents before they escalate.

| Metric category | Example metric | Target |
|---|---|---|
| **Training completion** | % of staff completing annual training | 100% |
| **Assessment scores** | Average quiz score | ≥ 80% |
| **Phishing click rate** | % clicking simulated phishing link | < 10% |
| **Reporting rate** | % of simulations proactively reported | Increasing over time |
| **Incident report volume** | User-submitted reports per month | Increasing = programme working |
| **Mean time to report** | Time from incident to user report | < 4 hours |

**Security culture health indicators:**

| Positive sign | Negative sign |
|---|---|
| High and increasing reporting rate | Low reporting (fear of blame) |
| Engaged questions during training | Repeat offenders on phishing simulations |
| Volunteers for security champion role | Low training completion rates |
| Declining phishing click rate | Policy violations ignored without consequence |

---

### Programme development lifecycle

1. **Assess** — Run a baseline phishing simulation; survey employees; review incident history to identify gaps.
2. **Define objectives** — Set measurable goals (e.g., click rate < 10%; 100% completion within 30 days of hire).
3. **Develop content** — Create general awareness modules, role-specific content, and microlearning cadence.
4. **Implement** — Roll out training, phishing simulations, and a reporting mechanism.
5. **Measure** — Track completion rate, click rate, reporting rate, and quiz scores quarterly.
6. **Improve** — Update content for emerging threats; adjust simulation difficulty; recognise security champions.

---

### Key distinctions to know for the exam

| Comparison | Distinction |
|---|---|
| **Training vs. awareness** | Training = formal education (courses, modules); awareness = ongoing reminders (tips, posters, weekly emails) |
| **Phishing test vs. phishing training** | Test = measures susceptibility (click rate); training = education delivered after clicking (just-in-time) |
| **CBT vs. instructor-led** | CBT = scalable, self-paced, trackable; instructor-led = interactive, Q&A, expensive to schedule |
| **General vs. role-specific** | General = all employees (phishing, passwords); role-specific = targeted content (developers = secure coding; finance = wire fraud) |
| **Baseline click rate vs. goal click rate** | High baseline is expected; success is measured by improvement trend, not the starting number |
| **No-blame culture vs. punishment** | No-blame encourages reporting and early containment; punishment suppresses reporting and worsens outcomes |

---

### Common exam traps

**Trap:** Phishing simulations should result in disciplinary action for users who click.
Reality: Simulations are training opportunities. Punishing users suppresses reporting and creates a culture of fear — the opposite of what the programme needs.

**Trap:** Annual training is sufficient to maintain a secure workforce.
Reality: Annual training is required, but awareness must be continuous — phishing simulations, microlearning tips, and timely communications about new threats are all necessary.

**Trap:** All training should be computer-based for consistency.
Reality: Effective programmes mix delivery methods. CBT handles scale; instructor-led handles depth; microlearning handles continuous reinforcement; gamification handles engagement.

**Trap:** A 25% phishing click rate means the programme has failed.
Reality: The first simulation establishes a baseline. A downward trend over subsequent campaigns is the measure of success.

**Trap:** Cybersecurity awareness is the IT department's responsibility.
Reality: Security is a shared, organisation-wide responsibility. Awareness programmes exist precisely to distribute that responsibility to all employees.

---

### Exam tips

1. **Just-in-time training** redirects users to an education page *immediately* after they click a simulated phishing link.
2. **No-blame culture** increases reporting rates — users report early, incidents get contained faster.
3. **Microlearning** = short (3–5 min), frequent lessons; used for continuous awareness, not initial training.
4. **Gamification** adds points, badges, and leaderboards to increase training engagement.
5. **Role-specific training** targets high-risk groups: developers (secure coding), executives (spear phishing), finance (wire fraud).
6. **Annual training** is the minimum required; phishing simulations should be quarterly or monthly.
7. **Reporting mechanisms** must be easy — a one-click button in the email client is ideal.
8. **Metrics to know:** completion rate, click rate, reporting rate, quiz score, mean time to report.
9. **Baseline simulation** measures current susceptibility *before* training begins — do not evaluate it against the target.
10. **Security champions** are volunteer employees who promote awareness within their teams — a sign of a healthy security culture.

---

### Key terms

- **Security awareness programme** — A structured initiative to educate employees on threats and expected security behaviours.
- **Computer-based training (CBT)** — Self-paced, online training modules that can be tracked and scaled across large populations.
- **Microlearning** — Short (3–5 minute) lessons delivered frequently (weekly emails, Slack messages) for continuous reinforcement.
- **Gamification** — Use of points, badges, and leaderboards to increase engagement with training activities.
- **Phishing simulation** — A controlled test in which the security team sends fake phishing emails to measure user susceptibility.
- **Just-in-time training** — Immediate education delivered at the moment a user fails a phishing simulation (e.g., clicks the link).
- **Click rate** — The percentage of users who click a link in a simulated phishing email; the primary susceptibility metric.
- **Reporting rate** — The percentage of users who correctly report a simulated (or real) phishing email; indicates programme maturity.
- **No-blame culture** — An organisational posture that encourages reporting mistakes without fear of punishment, improving detection and response times.
- **Security champion** — An employee who voluntarily promotes security awareness within their team or department.
- **Insider threat** — A security risk originating from individuals within the organisation (employees, contractors, former staff).
- **Anomalous behaviour** — Unusual activity that may indicate compromise or malicious intent (e.g., after-hours logins, bulk data downloads).
- **Role-specific training** — Targeted security education delivered to groups with elevated risk profiles (developers, executives, finance, HR).

---

### Examples / scenarios

**Scenario 1:** A company runs its first phishing simulation and finds that 28% of employees clicked the link. Leadership wants to fire the employees who clicked.
- **Answer:** This is a misuse of phishing simulations. The 28% is a *baseline* — it reflects the state before training, not after. The correct response is to use the results to prioritise training, adopt just-in-time education for those who clicked, and track improvement in subsequent campaigns. Punishment discourages reporting.

**Scenario 2:** A security team needs to train 5,000 employees across 12 countries on password security. Scheduling live sessions is impractical.
- **Answer:** Computer-based training (CBT) is the appropriate delivery method. It is scalable, self-paced, available across time zones, and provides trackable completion data for compliance purposes.

**Scenario 3:** After completing a phishing simulation, a user receives an immediate pop-up explaining what indicators they missed and how to recognise phishing in the future.
- **Answer:** This is just-in-time training — education delivered at the exact moment of failure to maximise relevance and retention.

**Scenario 4:** A security analyst notices that one employee consistently downloads large volumes of files at 11 PM, has recently complained about being passed over for promotion, and has been accessing project files outside their normal role.
- **Answer:** These are insider threat behavioural indicators — after-hours activity, disgruntlement, and access anomalies. Employees trained in anomalous behaviour recognition should report such observations to HR or the security team.

**Scenario 5:** A CISO wants to reduce friction for employees reporting suspicious emails and increase the reporting rate.
- **Answer:** Implement a one-click "Report Phishing" button integrated into the email client (Outlook or Gmail). This is the lowest-friction reporting mechanism and consistently improves reporting rates.

---

### Mini quiz

<details>
<summary><strong>Question 1:</strong> What is the purpose of just-in-time training in a phishing simulation programme?</summary>

**Answer:** Just-in-time training delivers immediate education to a user at the moment they fail a simulated phishing test (e.g., click a link). Rather than waiting for scheduled training, the user is redirected to a page explaining what they missed and how to spot the threat in future. Timing maximises relevance and retention.
</details>

<details>
<summary><strong>Question 2:</strong> Why is a no-blame culture important for a security awareness programme?</summary>

**Answer:** When employees fear punishment for reporting mistakes, they hide incidents — allowing breaches to escalate undetected. A no-blame culture encourages early reporting, enabling the security team to contain incidents faster. Recognition for reporting (rather than discipline for clicking) is the correct posture.
</details>

<details>
<summary><strong>Question 3:</strong> How does microlearning differ from computer-based training?</summary>

**Answer:** CBT is a formal, structured module (often 30–60 minutes) completed at a scheduled time. Microlearning consists of very short (3–5 minute) lessons pushed frequently through low-friction channels like email or Slack. CBT is used for initial training; microlearning maintains continuous awareness between formal sessions.
</details>

<details>
<summary><strong>Question 4:</strong> A phishing simulation campaign shows a 22% click rate in Q1 and a 9% click rate in Q3. How should this be interpreted?</summary>

**Answer:** The programme is working. The Q1 rate is a baseline (high rates are expected before training begins). The downward trend — from 22% to 9% — demonstrates measurable improvement in user susceptibility. The target is typically below 10%, so Q3 is approaching or meeting that goal.
</details>

### CompTIA-style practice questions

<details>
<summary><strong>Question 5:</strong> A security manager wants to provide targeted training to employees in the software development team to address application security risks. Which training content is MOST appropriate for this group?<br>A. Password hygiene and phishing recognition<br>B. Wire fraud and invoice scam awareness<br>C. Secure coding practices and OWASP Top 10<br>D. W-2 phishing and employee data protection</summary>

**Correct Answer: C. Secure coding practices and OWASP Top 10**

Developers require role-specific training focused on the security risks they can directly influence — secure coding and common web application vulnerabilities (OWASP Top 10).

- A: Password hygiene and phishing are general awareness topics appropriate for all employees, not role-specific to developers.
- B: Wire fraud and invoice scams are targeted at finance teams.
- D: W-2 phishing and employee data protection are targeted at HR teams.
</details>

<details>
<summary><strong>Question 6:</strong> A security analyst reviews phishing simulation data from the past year. The click rate has dropped from 30% to 8%, and the reporting rate has risen from 4% to 19%. What do these trends BEST indicate?<br>A. The simulations are too easy and need to be more difficult<br>B. The security awareness programme is achieving its objectives<br>C. Employees are sharing simulation details with each other<br>D. The reporting mechanism is malfunctioning and must be reviewed</summary>

**Correct Answer: B. The security awareness programme is achieving its objectives**

A falling click rate and a rising reporting rate are the two primary indicators that a phishing awareness programme is working. Users are becoming more resistant to phishing and more willing to report suspicious messages.

- A: difficulty adjustment is a programme refinement tool, not what these metrics indicate.
- C: nothing in the data suggests collusion; improved recognition is the more logical explanation.
- D: an increasing reporting rate indicates the mechanism is working correctly, not malfunctioning.
</details>

<details>
<summary><strong>Question 7 (Multi-select):</strong> A CISO is designing a new security awareness programme. Which TWO delivery methods would BEST support both initial training completeness and ongoing reinforcement across a large, distributed workforce? (Select TWO.)<br>A. Annual instructor-led classroom sessions<br>B. Computer-based training modules<br>C. Quarterly tabletop exercises for all staff<br>D. Weekly microlearning messages<br>E. Monthly one-on-one security consultations</summary>

**Correct Answers: B and D**

CBT provides scalable, trackable initial training accessible to a distributed workforce. Microlearning delivers frequent, low-friction reinforcement between formal training cycles. Together they address both completeness and continuity.

- A: instructor-led sessions are valuable but impractical for large distributed organisations; cost and scheduling are prohibitive.
- C: tabletop exercises are typically scoped to incident response teams, not all staff.
- E: one-on-one consultations are not scalable to a large workforce.
</details>

---

### Related objectives

- [**5.1**]({{ '/secplus/objectives/5-1/' | relative_url }}) — Security governance provides the policy and accountability framework that security awareness programmes operate within.
- [**5.2**]({{ '/secplus/objectives/5-2/' | relative_url }}) — Risk management informs which threats training should prioritise based on likelihood and impact.
- [**5.5**]({{ '/secplus/objectives/5-5/' | relative_url }}) — Audits and assessments may evaluate training completion rates and phishing simulation metrics as part of a security programme review.
- [**2.1**]({{ '/secplus/objectives/2-1/' | relative_url }}) — Threat actors and motivations inform the scenarios used in phishing simulations and insider threat training.
- [**5.3**]({{ '/secplus/objectives/5-3/' | relative_url }}) — Third-party risk management extends awareness requirements to vendors and contractors who access company systems.

---

## Navigation

**Domain 5.0: Security Program Management and Oversight**

| Objective | Title | Status |
|---|---|---|
| [5.1]({{ '/secplus/objectives/5-1/' | relative_url }}) | Summarize elements of effective security governance. | done |
| [5.2]({{ '/secplus/objectives/5-2/' | relative_url }}) | Explain elements of the risk management process. | done |
| [5.3]({{ '/secplus/objectives/5-3/' | relative_url }}) | Explain the processes associated with third-party risk assessment and management. | done |
| [5.4]({{ '/secplus/objectives/5-4/' | relative_url }}) | Summarize elements of effective security compliance. | done |
| [5.5]({{ '/secplus/objectives/5-5/' | relative_url }}) | Explain types and purposes of audits and assessments. | done |
| **5.6** | Given a scenario, implement security awareness practices. (current) | done |

[← Previous: Objective 5.5]({{ '/secplus/objectives/5-5/' | relative_url }}) | [Back to Dashboard]({{ '/secplus/' | relative_url }}) | [Next: Dashboard →]({{ '/secplus/' | relative_url }})
