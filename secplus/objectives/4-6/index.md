---
layout: objective
title: "Security+ 4.6 — Given a scenario, implement and maintain identity and access management."
objective_id: "4.6"
domain: "4.0 Security Operations"
status: "done"
tags:
  - secplus701
permalink: /secplus/objectives/4-6/
---

# Security+ 4.6 — Given a scenario, implement and maintain identity and access management.

Status: <span class="status-badge done">done</span>

## Exam objective
Given a scenario, implement and maintain identity and access management.

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

Resilience and recovery ensure business operations continue during and after disruptions. This includes backup strategies, disaster recovery planning, high availability systems, and business continuity management.

---

### Backup Strategies

#### Backup types

| Backup type | What is copied | Restore requires | Backup speed | Storage use | Typical frequency |
|---|---|---|---|---|---|
| **Full** | All data | Single backup | Slowest | Most | Weekly / monthly |
| **Incremental** | Data changed since last backup (any type) | Last full + all incrementals | Fastest | Least | Daily / multiple times per day |
| **Differential** | Data changed since last **full** backup | Last full + last differential | Slower than incremental | More than incremental | Daily |

**Exam tip:** Incremental = **fastest backup, slowest restore**. Differential = **slower backup, faster restore** than incremental. Full = **slowest backup, fastest restore**. If a question asks which restores fastest — full wins; if it asks which backs up fastest — incremental wins.

**Backup schedule comparison:**

```
Sunday: Full backup (all data)

--- Differential schedule ---
Mon–Sat: Differential (all changes since Sunday)

Restore on Friday = Full (Sun) + Differential (Fri) = 2 backups

--- Incremental schedule ---
Mon–Sat: Incremental (changes since previous day)

Restore on Friday = Full (Sun) + Mon + Tue + Wed + Thu + Fri = 6 backups
```

#### Backup locations

| Location | Storage | Pros | Cons | Best use |
|---|---|---|---|---|
| **On-site** | Same building / datacenter | Fast backup and restore | Vulnerable to same disasters (fire, flood) | Quick recovery for minor incidents |
| **Off-site** | Different geographic location | Protected from local disasters | Slower restore (transport or network transfer) | Disaster recovery |
| **Cloud** | AWS S3, Azure Blob, Google Cloud | Scalable, distributed, cost-effective | Requires internet; ongoing subscription costs | Long-term retention, DR |

**Exam tip:** The **3-2-1 rule** — **3** copies of data, on **2** different media types, with **1** stored off-site. This is the standard backup best practice and a frequent exam scenario anchor.

#### Backup media

| Media | Pros | Cons | Best use |
|---|---|---|---|
| **Disk (HDD / NAS / SAN)** | Fast backup and restore; random access | More expensive per GB than tape | Recent backups; quick recovery |
| **Tape (LTO)** | Cheap per GB; durable (30+ year lifespan) | Sequential access (slow); requires tape drive | Long-term archival |
| **Cloud storage** | No hardware to maintain; unlimited scale | Ongoing costs; egress fees | Off-site backup; disaster recovery |

#### Backup security and testing

- **Encryption:** Encrypt backups at rest and in transit.
- **Access control:** Limit who can delete or modify backups.
- **Immutability (WORM):** Write-once-read-many storage prevents ransomware from encrypting backup copies.
- **Air gap:** Physically disconnect backup media from the network.
- **Testing frequency:** At minimum quarterly — restore test data, verify integrity, and document actual recovery time vs. RTO target.

**Exam tip:** Untested backups are not backups. A common exam trap is assuming backups work without testing. Test quarterly and document actual vs. target recovery times.

---

### Disaster Recovery

#### Disaster types

- **Natural:** Hurricane, earthquake, flood, fire
- **Technical:** Hardware failure, power outage, network failure
- **Human-caused:** Cyberattack, sabotage, terrorism
- **Pandemic:** Workforce unavailable

#### Recovery objectives

| Metric | Measures | Determined by | Example |
|---|---|---|---|
| **RPO** (Recovery Point Objective) | Maximum acceptable **data loss** (time) | Backup frequency | RPO = 4 h → must back up every ≤ 4 hours |
| **RTO** (Recovery Time Objective) | Maximum acceptable **downtime** | Recovery strategy (hot/warm/cold site) | RTO = 8 h → must restore within 8 hours |
| **MTBF** (Mean Time Between Failures) | Average operating time before a failure | Hardware reliability planning | MTBF = 100,000 h ≈ 11 years |
| **MTTR** (Mean Time To Repair) | Average time to repair and restore after failure | Recovery efficiency measurement | MTTR = 4 hours |

**Exam tip:** RPO = **data loss** → drives backup frequency. RTO = **downtime** → drives recovery site choice. These are commonly swapped on the exam — commit the distinction to memory.

**RPO / RTO worked example:**
```
Critical database:
- Revenue impact: $50k/hour
- Data sensitivity: high (customer orders)

Decision:
- RPO = 1 hour → back up every 30 minutes
- RTO = 4 hours → hot site with real-time replication
- Cost: $100k/year
- Justification: a 4-hour outage costs $200k; hot site prevents that loss
```

#### Recovery sites

| Site type | Readiness | RTO | Cost | Best use |
|---|---|---|---|---|
| **Hot site** | Immediate (real-time replication) | Minutes to hours | Highest | Mission-critical systems; zero-downtime tolerance |
| **Warm site** | Hours (restore from backups) | Hours to days | Medium | Important but not mission-critical |
| **Cold site** | Days to weeks (install hardware, restore data) | Days to weeks | Lowest | Non-critical systems; budget-constrained environments |
| **Mobile site** | Hours to days (transport and setup) | Variable | Medium | Temporary recovery; remote locations |

**Exam tip:** Match site type to RTO. If a scenario demands near-instant recovery → **hot site**. If cost is the primary constraint and long downtime is tolerable → **cold site**. Warm site sits in between.

#### Failover and replication

| Concept | Definition | Key detail |
|---|---|---|
| **Failover** | Switch to backup system when primary fails | Can be automatic (system-initiated) or manual (admin-initiated) |
| **Failback** | Return to primary system after it is recovered | Requires primary to be fully restored and tested before switching back |
| **Synchronous replication** | Real-time copy; zero data loss | Slower; requires low-latency link |
| **Asynchronous replication** | Delayed copy; minimal data loss | Faster; tolerates higher latency |

---

### High Availability and Redundancy

#### Availability tiers

| Uptime % | Common name | Annual downtime |
|---|---|---|
| 99% | Two nines | 3.65 days |
| 99.9% | Three nines | 8.76 hours |
| 99.99% | Four nines | 52.56 minutes |
| 99.999% | Five nines | 5.26 minutes |

**Exam tip:** "Five nines" (99.999%) is the gold standard for mission-critical systems. Know that higher availability requires exponentially more investment in redundancy.

#### Redundancy types

| Type | Examples |
|---|---|
| **Hardware redundancy** | Redundant power supplies; RAID arrays; redundant NICs; UPS (battery backup) |
| **Geographic redundancy** | Multiple datacenters in different cities/regions (e.g., AWS availability zones) |
| **Network redundancy** | Multiple ISPs; redundant switches and routers; diverse routing paths |

#### Clustering and load balancing

| Concept | Definition | Detail |
|---|---|---|
| **Active-Active cluster** | All nodes handle traffic simultaneously | Load balanced; all nodes must be sized for full load |
| **Active-Passive cluster** | One node active; others on standby | Automatic failover; standby nodes are idle during normal operation |
| **Round-robin load balancing** | Rotate requests sequentially through servers | Simple; ignores server load |
| **Least-connections load balancing** | Route to server with fewest active connections | More efficient than round-robin for variable workloads |
| **Geographic load balancing** | Route users to nearest server | Reduces latency; provides regional redundancy |

**Exam tip:** **Single Point of Failure (SPOF)** — any component whose failure stops the entire system. High availability design means eliminating all SPOFs through redundancy. Common SPOFs: single power supply, single ISP connection, single server.

---

### Business Continuity

#### DRP vs. BCP

| Plan | Focus | Scope |
|---|---|---|
| **DRP** (Disaster Recovery Plan) | IT systems recovery | Technology: servers, data, applications |
| **BCP** (Business Continuity Plan) | Entire business operations | People, processes, and technology |

**Exam tip:** BCP is the **broader** plan; DRP is a **subset** of BCP focused specifically on IT systems. If a scenario asks about keeping the whole organization running — BCP. If it asks about restoring IT systems — DRP.

#### Business Impact Analysis (BIA)

The BIA is the foundation of any BCP. It identifies what matters most and how long the business can survive without it.

1. Identify critical business functions (payroll, customer support, manufacturing)
2. Determine the impact of downtime (revenue loss, regulatory penalty, reputational damage)
3. Calculate **MTD** (Maximum Tolerable Downtime) per function
4. Prioritize recovery order (most critical functions first)

#### Continuity strategies

| Strategy | Description |
|---|---|
| **Work from home** | Remote work capabilities for workforce continuity |
| **Alternate work site** | Backup office location if primary is unavailable |
| **Cross-training** | Employees capable of covering multiple roles |
| **Succession planning** | Designated backups for key personnel |

#### BCP testing types

| Test type | Method | Scope | Frequency |
|---|---|---|---|
| **Tabletop exercise** | Discussion-based walkthrough; key personnel talk through a scenario | Low; no systems involved | Quarterly |
| **Simulation** | Simulated disaster; team actively responds using procedures | Medium; may involve technology | Annually |
| **Full interruption test** | Actual failover to backup systems | High; fully disruptive and expensive | Rarely |

**Exam tip:** Tabletop exercises are the **least disruptive** and most common. Full interruption tests are the **most realistic** but rare due to cost and risk. The exam may ask which test type is appropriate given operational constraints.

---

### Key distinctions to know for the exam

| Comparison | Distinction |
|---|---|
| **RPO vs. RTO** | RPO = how much data loss is acceptable (drives backup frequency); RTO = how long downtime is acceptable (drives recovery site selection) |
| **Hot site vs. cold site** | Hot site = fully ready, near-instant failover, most expensive; Cold site = empty facility, days to set up, cheapest |
| **Full vs. incremental backup** | Full = all data, slowest backup, fastest restore; Incremental = changed data only, fastest backup, slowest restore |
| **DRP vs. BCP** | DRP = IT systems recovery; BCP = entire organization continuity (broader) |
| **Failover vs. failback** | Failover = switch to backup system; Failback = return to primary after recovery |
| **Active-Active vs. Active-Passive** | Active-Active = all nodes serve traffic (load balanced); Active-Passive = one node active, others on standby |
| **Synchronous vs. asynchronous replication** | Synchronous = real-time, zero data loss, slower; Asynchronous = delayed, minimal data loss, faster |

---

### Common exam traps

**Trap:** Thinking RPO and RTO measure the same thing.
Reality: RPO measures acceptable data loss and determines backup frequency. RTO measures acceptable downtime and determines recovery strategy. They are independent variables.

**Trap:** Assuming that having backups guarantees successful recovery.
Reality: Backups must be tested regularly (minimum quarterly). Organizations frequently discover backup failures only during an actual disaster when it is too late.

**Trap:** Believing on-site backup alone is sufficient.
Reality: On-site backups are destroyed in the same disaster (fire, flood) as the primary system. The 3-2-1 rule requires at least one off-site copy.

**Trap:** Assuming the incremental backup is always the best choice.
Reality: Incremental backups have the fastest backup time and smallest storage footprint, but the slowest restore time — restoring requires the last full plus every subsequent incremental. The best choice depends on RPO and RTO requirements.

**Trap:** Thinking a hot site is always required for disaster recovery.
Reality: Hot, warm, and cold sites are cost/RTO trade-offs. If an organization can tolerate days of downtime and has budget constraints, a cold site is entirely appropriate.

**Trap:** Confusing DRP with BCP.
Reality: DRP is focused on restoring IT systems. BCP covers the entire organization — people, processes, communications, and alternate operations — and is broader in scope.

---

### Exam tips

1. **RPO = data loss** — determines how frequently you must back up
2. **RTO = downtime** — determines which recovery site tier you need
3. **3-2-1 rule:** 3 copies, 2 media types, 1 off-site
4. **Hot site = immediate** failover (real-time replication; highest cost)
5. **Cold site = days/weeks** to recover (empty facility; lowest cost)
6. **Full backup** = slowest backup, fastest restore
7. **Incremental backup** = fastest backup, slowest restore
8. **Test backups quarterly** — verify before disaster, not during
9. **BCP = entire business**; DRP = IT systems only
10. **High availability** measured in uptime % — 99.999% (five nines) = 5.26 min/year downtime
11. **WORM / immutable storage** is the key ransomware-resistant backup control
12. **Tabletop** = lowest disruption test; **full interruption** = highest fidelity test

---

## Key terms

- **Backup** — A copy of data stored separately from the primary system for recovery purposes.
- **Full backup** — A complete copy of all data; slowest to create, fastest to restore.
- **Incremental backup** — Copies only data changed since the last backup of any type; fastest to create, slowest to restore.
- **Differential backup** — Copies all data changed since the last full backup; restoration requires only the last full + last differential.
- **3-2-1 rule** — Best-practice backup strategy: 3 copies of data, on 2 different media types, with 1 stored off-site.
- **WORM (Write-Once-Read-Many)** — Immutable storage that prevents modification or deletion; key control against ransomware targeting backups.
- **RPO (Recovery Point Objective)** — The maximum acceptable amount of data loss measured in time; drives backup frequency.
- **RTO (Recovery Time Objective)** — The maximum acceptable duration of downtime; drives recovery site and strategy selection.
- **MTBF (Mean Time Between Failures)** — Average operating time between hardware failures; a reliability metric.
- **MTTR (Mean Time To Repair)** — Average time to restore a system after failure; a recovery efficiency metric.
- **Hot site** — A fully equipped, operational duplicate datacenter with real-time data replication; enables near-immediate failover.
- **Warm site** — Partially equipped facility with hardware in place; requires hours to restore from backup before operations resume.
- **Cold site** — An empty facility with power and network; requires days to weeks to install hardware and restore data.
- **Failover** — The automatic or manual switch to a backup system when the primary fails.
- **Failback** — The process of returning operations to the primary system after it has been restored and tested.
- **High availability (HA)** — Design approach that minimizes downtime through redundancy, clustering, and load balancing.
- **SPOF (Single Point of Failure)** — Any component whose failure halts the entire system; eliminated through redundancy.
- **Active-Active cluster** — All cluster nodes serve traffic simultaneously; provides load balancing and redundancy.
- **Active-Passive cluster** — One node handles all traffic; others remain on standby and activate only on failover.
- **BCP (Business Continuity Plan)** — A comprehensive plan to maintain all business operations (people, processes, technology) during and after a disruption.
- **DRP (Disaster Recovery Plan)** — A subset of the BCP focused specifically on restoring IT systems and data after a disaster.
- **BIA (Business Impact Analysis)** — Analysis that identifies critical business functions, quantifies downtime impact, and establishes recovery priorities.
- **MTD (Maximum Tolerable Downtime)** — The longest period a business function can be unavailable before causing irreversible harm.
- **Tabletop exercise** — A discussion-based BCP/DRP test where participants walk through a simulated scenario without activating real systems.

---

## Examples / scenarios

**Scenario 1:** A company's primary datacenter is destroyed by a fire on Friday at noon. Their last successful backup was taken Thursday at 11 PM. Their RPO is 4 hours and RTO is 8 hours. Was the RPO met?
- **Answer:** No. The data loss is approximately 13 hours (11 PM Thursday to noon Friday), which exceeds the 4-hour RPO. The backup frequency was insufficient for the defined RPO.

**Scenario 2:** An organization backs up every Sunday (full) and runs incremental backups Monday through Saturday. A ransomware attack destroys all data on Friday afternoon. What is required to restore?
- **Answer:** The Sunday full backup plus every incremental from Monday through Friday — six backup sets in total. This is the primary drawback of incremental strategies: restore complexity grows throughout the week.

**Scenario 3:** A hospital's electronic health record system must be restored within 2 hours of any outage and can tolerate no more than 15 minutes of data loss. Which recovery site type should they use?
- **Answer:** Hot site with synchronous replication. A 15-minute RPO and 2-hour RTO demand real-time data replication and an immediately operational alternate site. Warm or cold sites cannot meet these targets.

**Scenario 4:** A security auditor finds that a company keeps all backups on the same SAN as production data in the same building. What rule is being violated and what is the primary risk?
- **Answer:** The 3-2-1 backup rule is violated — all copies are on the same media type and the same location. A single disaster (fire, flood, ransomware encrypting the SAN) would destroy both production data and all backups simultaneously.

**Scenario 5:** An organization conducts quarterly meetings where IT leadership and department heads discuss what they would do if the headquarters building became inaccessible for a week. No systems are actually activated. What type of test is this?
- **Answer:** Tabletop exercise. It is discussion-based, involves key stakeholders reviewing the scenario verbally, and does not disrupt live systems — the hallmark of a tabletop test.

---

## Mini quiz

<details>
<summary><strong>Question 1:</strong> What is the difference between RPO and RTO, and what does each determine in practice?</summary>

**Answer:** RPO (Recovery Point Objective) is the maximum acceptable amount of **data loss** measured in time. It determines **backup frequency** — if your RPO is 1 hour, you must back up at least every hour. RTO (Recovery Time Objective) is the maximum acceptable duration of **downtime** after a disaster. It determines **recovery strategy** — a 2-hour RTO requires a hot site; a 2-week RTO may permit a cold site.
</details>

<details>
<summary><strong>Question 2:</strong> A company runs a full backup every Sunday and incremental backups Monday–Saturday. Restoration is needed on Thursday. What is required?</summary>

**Answer:** The Sunday full backup plus Monday's, Tuesday's, and Wednesday's incremental backups — four backup sets in total. Each incremental must be restored in sequence. This is why incremental backup restore is slower than differential: differentials only ever require the last full + the most recent differential (two sets), regardless of how many days have passed.
</details>

<details>
<summary><strong>Question 3:</strong> Why is WORM (immutable) storage important for backups?</summary>

**Answer:** Ransomware often targets and encrypts backup files in addition to production data. WORM storage prevents any modification or deletion of written data, meaning ransomware cannot overwrite or encrypt the backup copies. This preserves a clean recovery point even if the primary environment is fully compromised.
</details>

<details>
<summary><strong>Question 4:</strong> What is the difference between a tabletop exercise and a full interruption test?</summary>

**Answer:** A tabletop exercise is a discussion-based walkthrough — key personnel talk through a simulated scenario without activating any real systems. It is low-risk and conducted frequently (quarterly). A full interruption test actually fails over to the backup environment, proving the plan works end-to-end. It is the highest-fidelity test but is disruptive, expensive, and conducted rarely.
</details>

<details>
<summary><strong>Question 5:</strong> What is a Single Point of Failure (SPOF) and how is it eliminated?</summary>

**Answer:** A SPOF is any component whose failure would halt the entire system — for example, a single power supply, single ISP connection, or single database server. SPOFs are eliminated through redundancy: duplicate components, diverse network paths, clustered servers, and geographic distribution so no single failure can bring down the whole system.
</details>

### CompTIA-style practice questions

<details>
<summary><strong>Question 6:</strong> An organization's financial reporting system has a defined RPO of 1 hour and an RTO of 4 hours. A power surge destroys the primary server at 2:00 PM. The last backup completed at 12:45 PM. Which statement BEST describes the situation?<br>A. Both RPO and RTO have been violated because the system is not yet restored<br>B. The RPO has been met but the RTO is still being evaluated<br>C. The RPO has been violated; 75 minutes of data may be lost, exceeding the 1-hour limit<br>D. The RTO has been violated because the system has been down for more than 1 hour</summary>

**Correct Answer: C. The RPO has been violated; 75 minutes of data may be lost, exceeding the 1-hour limit**

The last backup was 75 minutes before the failure (12:45 PM to 2:00 PM). The RPO is 60 minutes, so up to 75 minutes of data could be lost — a violation. RTO measures downtime from failure to restoration; that clock is still running and has not yet been violated or confirmed. A and D misidentify which metric applies.

- A: RTO cannot be assessed yet — it depends on when restoration completes, not when the failure occurred.
- B: The RPO *has* been violated (75 min loss > 60 min RPO).
- D: RTO is measured from failure to restoration; 4 hours have not elapsed yet.
</details>

<details>
<summary><strong>Question 7:</strong> A company needs a disaster recovery site that can be operational within 2 hours of a declared disaster but wants to minimize ongoing costs. The existing production environment uses real-time database replication. Which recovery site type BEST meets these requirements?<br>A. Hot site<br>B. Warm site<br>C. Cold site<br>D. Mobile site</summary>

**Correct Answer: B. Warm site**

A warm site has hardware pre-installed and ready; restoration from backup typically takes hours — consistent with a 2-hour target in favorable conditions. It costs less than a hot site because it does not maintain real-time replication. Note: the question states the company *uses* real-time replication on production — that does not mean the DR site must replicate in real time. A hot site would also meet the RTO but is more expensive than required. Cold site and mobile site cannot meet a 2-hour RTO.

- A: Hot site would meet the requirement but costs more; the question asks to minimize cost.
- C: Cold site requires days to weeks to become operational.
- D: Mobile sites require transport and setup time, typically hours to days.
</details>

<details>
<summary><strong>Question 8 (Multi-select):</strong> A security team is reviewing a company's backup strategy after a ransomware incident destroyed both production data and all on-site backups. Which TWO controls, if implemented, would MOST directly have prevented total data loss? (Select TWO.)<br>A. Increasing the backup frequency from weekly to daily<br>B. Storing at least one backup copy off-site or in cloud storage<br>C. Implementing WORM (immutable) storage for backup copies<br>D. Switching from full backups to incremental backups<br>E. Conducting quarterly tabletop exercises</summary>

**Correct Answers: B and C**

Ransomware destroyed on-site backups alongside production — two controls directly address this:

- B: Off-site or cloud storage ensures a copy exists outside the blast radius of a local attack or disaster, satisfying the "1 off-site" component of the 3-2-1 rule.
- C: WORM/immutable storage prevents ransomware from overwriting or encrypting backup files, preserving a clean copy even if the backup server is compromised.

- A: Daily backups reduce RPO but do not prevent ransomware from encrypting them.
- D: Switching backup type does not affect ransomware resilience.
- E: Tabletop exercises test response plans but do not protect backup data.
</details>

---

## Related objectives

- [**4.3**]({{ '/secplus/objectives/4-3/' | relative_url }}) — Vulnerability management feeds into understanding what risks drive RPO/RTO requirements.
- [**4.8**]({{ '/secplus/objectives/4-8/' | relative_url }}) — Incident response relies on the backup and recovery capabilities defined here.
- [**5.1**]({{ '/secplus/objectives/5-1/' | relative_url }}) — Risk management frameworks inform BIA and BCP prioritization decisions.
- [**5.4**]({{ '/secplus/objectives/5-4/' | relative_url }}) — Data privacy regulations impose RPO/RTO-like requirements on certain data categories.

---

## Navigation

**Domain 4.0: Security Operations**

| Objective | Title | Status |
|---|---|---|
| [4.1]({{ '/secplus/objectives/4-1/' | relative_url }}) | Given a scenario, apply common security techniques to computing resources. | done |
| [4.2]({{ '/secplus/objectives/4-2/' | relative_url }}) | Explain the security implications of proper hardware, software, and data asset management. | done |
| [4.3]({{ '/secplus/objectives/4-3/' | relative_url }}) | Explain various activities associated with vulnerability management. | done |
| [4.4]({{ '/secplus/objectives/4-4/' | relative_url }}) | Explain security alerting and monitoring concepts and tools. | done |
| [4.5]({{ '/secplus/objectives/4-5/' | relative_url }}) | Given a scenario, modify enterprise capabilities to enhance security. | done |
| **4.6** | Given a scenario, implement and maintain identity and access management. (current) | done |
| [4.7]({{ '/secplus/objectives/4-7/' | relative_url }}) | Explain the importance of automation and orchestration related to secure operations. | done |
| [4.8]({{ '/secplus/objectives/4-8/' | relative_url }}) | Explain appropriate incident response activities. | done |
| [4.9]({{ '/secplus/objectives/4-9/' | relative_url }}) | Given a scenario, use data sources to support an investigation. | done |

[← Previous: Objective 4.5]({{ '/secplus/objectives/4-5/' | relative_url }}) | [Back to Dashboard]({{ '/secplus/' | relative_url }}) | [Next: Objective 4.7 →]({{ '/secplus/objectives/4-7/' | relative_url }})
