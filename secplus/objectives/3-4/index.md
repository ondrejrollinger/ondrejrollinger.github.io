-----

layout: default
title: “Security+ 3.4 — Explain the importance of resilience and recovery in security architecture.”
objective_id: “3.4”
domain: “3.0 Security Architecture”
status: “done”
tags:

- secplus701
  permalink: /secplus/objectives/3-4/

-----

# Security+ 3.4 — Explain the importance of resilience and recovery in security architecture.

Status: <span class="status-badge done">done</span>

## Exam objective

Explain the importance of resilience and recovery in security architecture.

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

-----

## My notes

### Overview

Resilience ensures systems can withstand disruptions and continue operating. Recovery ensures systems can be restored after failures. Together, they form the foundation of business continuity and disaster recovery planning. This objective covers high availability mechanisms, backup site strategies, capacity planning, testing methodologies, backup approaches, recovery techniques, and power infrastructure.

-----

### High availability

**High availability** — systems designed to remain operational with minimal downtime, typically measured as a percentage of uptime.

|Uptime Target             |Annual Downtime|Description                           |
|--------------------------|---------------|--------------------------------------|
|**99%** (“two nines”)     |3.65 days      |Basic availability                    |
|**99.9%** (“three nines”) |8.76 hours     |Standard enterprise                   |
|**99.99%** (“four nines”) |52.56 minutes  |High availability                     |
|**99.999%** (“five nines”)|5.26 minutes   |Mission-critical                      |
|**99.9999%** (“six nines”)|31.5 seconds   |Ultra-critical (financial, healthcare)|

**Load balancing vs. clustering:**

|Mechanism         |Description                                   |Purpose                               |Failure Behavior                    |
|------------------|----------------------------------------------|--------------------------------------|------------------------------------|
|**Load Balancing**|Distributes workload across multiple servers  |Optimize performance, prevent overload|Redirects traffic to healthy servers|
|**Clustering**    |Multiple systems acting as single logical unit|High availability, failover           |Cluster takes over if primary fails |

**Load balancing:**

- Distributes incoming requests across server pool
- Performs health checks to detect failed servers
- Types: Round-robin, least connections, weighted distribution
- Can be hardware (F5, Citrix) or software (HAProxy, NGINX)

**Clustering:**

- Active-active: All nodes handle requests simultaneously
- Active-passive: Standby nodes activate only on primary failure
- Combines with load balancing for comprehensive HA solution
- Shared storage ensures data consistency across cluster

-----

### Site considerations

Organizations maintain backup sites to recover operations if primary site is unavailable.

**Site types:**

|Site Type      |Ready Time             |Cost         |Infrastructure                        |Use Case                                     |
|---------------|-----------------------|-------------|--------------------------------------|---------------------------------------------|
|**Hot Site**   |Immediate - minutes    |Very high    |Fully equipped, live data replication |Mission-critical; cannot tolerate downtime   |
|**Warm Site**  |Hours to days          |Moderate     |Partially equipped, periodic data sync|Important services; can tolerate brief outage|
|**Cold Site**  |Weeks to months        |Low          |Empty building, no equipment          |Non-critical; long recovery acceptable       |
|**Mobile Site**|Varies (portable units)|Moderate-high|Deployable trailers/tents             |Rapid deployment, temporary needs            |

**Hot site:**

- Duplicate of production environment
- Real-time or near-real-time data synchronization
- Staff can switch over immediately
- Expensive to maintain (double infrastructure cost)
- **Example:** Financial trading firms requiring continuous operation

**Warm site:**

- Basic infrastructure in place (power, HVAC, network connectivity)
- Equipment may need installation and configuration
- Data restored from recent backups
- Balanced cost vs. recovery time
- **Example:** E-commerce during non-peak seasons

**Cold site:**

- Just physical space with utilities
- Organization brings equipment and restores data
- Longest recovery time
- Minimal ongoing cost
- **Example:** Archival systems with long RTO tolerance

**Geographic dispersion:**

- Sites located in different geographic regions to avoid correlated failures (natural disasters, power grid issues)
- Minimum distance recommendations: 50-100 miles (avoid regional disasters like hurricanes)
- Considerations: Latency for data replication, regulatory data sovereignty requirements

-----

### Platform diversity and multi-cloud

**Platform diversity** — using different technologies to prevent single points of failure.

**Benefits:**

- Reduces risk if a specific vendor, OS, or platform has a vulnerability or outage
- Different operating systems (Linux, Windows, proprietary RTOS)
- Different hypervisors (VMware, Hyper-V, KVM)
- Different cloud providers (AWS, Azure, GCP)

**Multi-cloud systems:**

- Distribute workloads across multiple cloud providers
- Mitigates vendor lock-in
- Provides resilience against provider-specific outages
- Enables cost optimization (use cheapest provider for each workload)

**Challenges:**

- Increased complexity in management and monitoring
- Inconsistent security policies across platforms
- Data synchronization and consistency
- Staff training on multiple platforms

-----

### Continuity of operations

**Continuity of Operations Plan (COOP)** — ensures organization can recover from disruptive events.

**Business Continuity Plan (BC):**

- Broader scope covering all organizational functions
- Addresses technical and non-technical disruptions
- Includes preventative measures and recovery steps
- Covers threats: Natural disasters, cyberattacks, supply chain disruptions, pandemics

**Disaster Recovery Plan (DRP):**

- Subset of BC focused specifically on IT systems and data
- Technical recovery procedures for infrastructure and applications
- Faster recovery focus after specific disasters (fire, flood, hurricane, ransomware)

**Key metrics:**

|Metric                               |Definition                                                         |Example                                                             |
|-------------------------------------|-------------------------------------------------------------------|--------------------------------------------------------------------|
|**RPO (Recovery Point Objective)**   |Maximum acceptable data loss (time between last backup and failure)|RPO = 1 hour means backups every hour; can lose up to 1 hour of data|
|**RTO (Recovery Time Objective)**    |Maximum acceptable downtime (time to restore operations)           |RTO = 4 hours means system must be back online within 4 hours       |
|**MTTR (Mean Time To Repair)**       |Average time to fix a failed component                             |MTTR = 2 hours means typical repair takes 2 hours                   |
|**MTBF (Mean Time Between Failures)**|Average time between system failures                               |MTBF = 10,000 hours means failure every ~417 days                   |

**RPO vs. RTO distinction:**

- **RPO** = How much data can you afford to lose? (drives backup frequency)
- **RTO** = How quickly must you recover? (drives site selection: hot/warm/cold)

-----

### Capacity planning

Ensures resources can handle current and future demand without over-provisioning.

**Capacity planning dimensions:**

|Dimension         |Considerations                                                                              |
|------------------|--------------------------------------------------------------------------------------------|
|**People**        |Staffing levels for normal operations and emergency response; training and skill development|
|**Technology**    |Server capacity, storage, network bandwidth, processing power                               |
|**Infrastructure**|Physical space (data center, office), power capacity, cooling requirements                  |

**Key principles:**

- Plan for peak load, not average load
- Include headroom for growth (typically 20-30% over current max)
- Account for failover scenarios (can remaining systems handle full load?)
- Regular capacity reviews aligned with business growth projections

**Scaling strategies:**

- **Vertical scaling (scale up)** — add resources to existing systems (more CPU, RAM)
- **Horizontal scaling (scale out)** — add more systems to distribute load

-----

### Testing methodologies

Regular testing validates that resilience and recovery plans actually work.

|Test Type              |Description                                  |Disruption Level  |Frequency                  |
|-----------------------|---------------------------------------------|------------------|---------------------------|
|**Tabletop Exercise**  |Discussion-based walkthrough of scenario     |None (theoretical)|Quarterly                  |
|**Failover Test**      |Switch to backup systems in controlled manner|Planned, minimal  |Semi-annually              |
|**Simulation**         |Virtual environment mimicking real disaster  |None (simulated)  |Annually                   |
|**Parallel Processing**|Run primary and backup concurrently          |None              |Ongoing or annual full test|

**Tabletop exercises:**

- Scenario-based discussion among stakeholders (no actual resource deployment)
- Identifies gaps in response plans
- Low cost, promotes team building
- **Example scenario:** “Hurricane hits primary data center; walk through recovery steps”

**Failover tests:**

- Controlled transition from primary to backup
- Validates disaster recovery procedures work as documented
- Can identify issues in failover process before real emergency
- Requires more resources and time than tabletop
- **Best practice:** Schedule during maintenance window with stakeholder notification

**Simulations:**

- Computer-generated representation of real scenario
- Hands-on practice in virtual environment
- Tests incident responders and system administrators in real-time
- Provides performance feedback

**Parallel processing:**

- Runs primary and secondary systems simultaneously
- Secondary system processes same data as primary
- Validates secondary can handle load
- Tests ability to handle multiple failure scenarios
- Can be used for both resilience testing and recovery testing

-----

### Backup strategies

Backups are copies of data created to protect against loss, corruption, or ransomware.

**Backup locations:**

|Type       |Description                                     |Pros                              |Cons                             |
|-----------|------------------------------------------------|----------------------------------|---------------------------------|
|**Onsite** |Stored at same physical location as primary data|Fast restore, low cost            |Vulnerable to site-wide disasters|
|**Offsite**|Stored at geographically separate location      |Protected from localized disasters|Slower restore, higher cost      |

**Best practice:** Follow **3-2-1 rule** — 3 copies of data, on 2 different media types, with 1 offsite.

**Backup frequency:**

- Determined by RPO — if RPO is 4 hours, backups every 4 hours
- Critical systems: Continuous or hourly backups
- Standard systems: Daily or weekly backups
- Archival data: Monthly or quarterly backups

**Backup encryption:**

- Protects backup data from unauthorized access
- Encrypt data at rest (on backup media)
- Encrypt data in transit (during backup transfer)
- Secure key management critical — losing keys means losing backup access

**Snapshots:**

- Point-in-time copies capturing consistent state
- Record only changes since previous snapshot (incremental)
- Fast to create, space-efficient
- **Use case:** Database servers, file servers, virtual machines
- **Limitation:** Not a substitute for full backups; dependent on base image

-----

### Recovery techniques

**Replication:**

- Real-time or near-real-time data copying to secondary location
- Ensures seamless data continuity
- **Synchronous replication** — writes committed to both primary and secondary simultaneously (no data loss, but slower)
- **Asynchronous replication** — writes committed to primary first, then secondary later (faster, but potential data loss = lag time)
- **Use case:** High-availability databases, disaster recovery

**Journaling:**

- Maintains detailed log of all data changes over time
- Enables granular recovery to specific point in time
- Provides audit trail for compliance
- **Use case:** Financial systems, databases requiring point-in-time recovery

**Recovery process:**

1. **Select appropriate backup** — most recent full backup + incremental/differential
1. **Initiate recovery** — restore data to target system
1. **Data validation** — verify integrity (checksums, test critical records)
1. **Testing** — confirm applications work with restored data
1. **Documentation** — record recovery steps, time taken, issues encountered
1. **Notification** — inform stakeholders when system is operational

-----

### Power infrastructure

Uninterrupted power is critical for continuous operations.

**Power components:**

|Component                             |Purpose                                                       |Runtime                       |Cost    |
|--------------------------------------|--------------------------------------------------------------|------------------------------|--------|
|**UPS (Uninterruptible Power Supply)**|Bridge power during brief outages, line conditioning          |10-60 minutes                 |Moderate|
|**Generator**                         |Long-term power during extended grid outages                  |Hours to days (fuel-dependent)|High    |
|**PDC (Power Distribution Center)**   |Central hub for power distribution, monitoring, load balancing|N/A (distribution)            |High    |

**UPS:**

- Battery backup maintains power during short failures
- Line conditioning protects against voltage spikes and sags
- Provides time to gracefully shut down systems or start generator
- Types:
  - **Standby (offline)** — switches to battery when power fails
  - **Line-interactive** — continuously monitors and adjusts voltage
  - **Online (double-conversion)** — always runs on battery (cleanest power)

**Generators:**

- Convert mechanical energy to electrical energy
- Backup power during extended grid outages
- Require startup time (10-30 seconds)
- Fuel types: Diesel, natural gas, propane
- Require regular testing and maintenance

**Power Distribution Centers (PDC):**

- Centralized power management
- Circuit protection and monitoring
- Load balancing across power sources
- Integrates UPS and generators for seamless transitions

**Data center best practices:**

- Redundant power supplies (N+1 or 2N configuration)
- UPS provides immediate backup (10-15 minutes)
- Generator starts within that window for extended power
- Rack-mounted UPS for individual servers
- PDU (Power Distribution Units) manage load balancing

-----

### Key distinctions to know for the exam

| Comparison | Distinction |
|—|—|—|
| **Load Balancing vs. Clustering** | Load balancing = distributes requests for performance; Clustering = failover for availability |
| **Hot vs. Warm vs. Cold Site** | Hot = immediate (expensive); Warm = hours-days (moderate); Cold = weeks-months (cheap) |
| **RPO vs. RTO** | RPO = acceptable data loss (drives backup frequency); RTO = acceptable downtime (drives recovery speed) |
| **Onsite vs. Offsite Backup** | Onsite = fast restore, vulnerable to disasters; Offsite = protected, slower restore |
| **Synchronous vs. Asynchronous Replication** | Synchronous = no data loss, slower; Asynchronous = faster, potential data loss |
| **Snapshot vs. Full Backup** | Snapshot = incremental point-in-time; Full backup = complete copy |
| **UPS vs. Generator** | UPS = short-term (minutes), immediate; Generator = long-term (hours-days), startup delay |
| **Tabletop vs. Failover Test** | Tabletop = discussion-based, no disruption; Failover = actual system switch, controlled disruption |
| **BC vs. DR** | BC = all organizational functions; DR = IT systems recovery |

-----

### Common exam traps

**Trap: Thinking hot sites eliminate the need for backups.**
Reality: Hot sites provide site redundancy, but backups protect against logical corruption (ransomware, accidental deletion). Both are needed.

**Trap: Confusing RPO with RTO.**
Reality: RPO = data loss tolerance (time between backups). RTO = downtime tolerance (recovery speed). RPO drives backup frequency; RTO drives site selection.

**Trap: Assuming snapshots replace full backups.**
Reality: Snapshots are dependent on a base image. If the base is corrupted or lost, all snapshots are unusable. Snapshots complement backups but don’t replace them.

**Trap: Believing clustering and load balancing are the same.**
Reality: Load balancing optimizes performance by distributing requests. Clustering provides failover for availability. They serve different purposes and are often used together.

**Trap: Thinking UPS provides long-term power.**
Reality: UPS provides 10-60 minutes — enough to start a generator or gracefully shut down. For extended outages, generators are required.

-----

### Exam tips

1. **Site selection** questions will give you an RTO and budget constraint — match the site type to the requirement. Short RTO = hot site; long RTO = cold site.
1. Questions about **RPO** always relate to backup frequency. If RPO is 2 hours, backups must occur every 2 hours maximum.
1. For **failover testing**, remember it causes planned disruption — done during maintenance windows with stakeholder notification.
1. **Replication** questions test synchronous vs. asynchronous — synchronous = zero data loss (but slower); asynchronous = faster (but lag = potential data loss).
1. **Power infrastructure** questions emphasize the UPS → Generator handoff. UPS provides immediate power; generator provides extended power after startup.
1. When asked about **3-2-1 backup rule**, remember: 3 copies, 2 media types, 1 offsite. This appears on the exam.

-----

## Key terms

- **High Availability** — Systems designed to minimize downtime through redundancy and failover mechanisms.
- **Five Nines (99.999%)** — Uptime target allowing only ~5 minutes of downtime per year.
- **Load Balancing** — Distributing workload across multiple servers to optimize performance and prevent overload.
- **Clustering** — Multiple systems acting as a single logical unit for high availability and failover.
- **Hot Site** — Fully operational backup facility with real-time data replication; immediate failover capability.
- **Warm Site** — Partially equipped backup facility; operational within hours to days.
- **Cold Site** — Basic facility with utilities only; operational within weeks to months.
- **Geographic Dispersion** — Distributing resources across different geographic locations to avoid correlated failures.
- **Platform Diversity** — Using different operating systems, hypervisors, and cloud providers to reduce single points of failure.
- **Multi-Cloud** — Distributing workloads across multiple cloud providers for resilience and cost optimization.
- **COOP (Continuity of Operations Plan)** — Ensures organization can recover from disruptive events.
- **Business Continuity Plan (BC)** — Comprehensive plan covering all organizational functions during disruptions.
- **Disaster Recovery Plan (DRP)** — Subset of BC focused on IT systems and data recovery.
- **RPO (Recovery Point Objective)** — Maximum acceptable data loss measured in time (drives backup frequency).
- **RTO (Recovery Time Objective)** — Maximum acceptable downtime (drives recovery speed and site selection).
- **MTTR (Mean Time To Repair)** — Average time to fix a failed component.
- **MTBF (Mean Time Between Failures)** — Average operational time between system failures.
- **Capacity Planning** — Ensuring resources (people, technology, infrastructure) can handle current and future demand.
- **Tabletop Exercise** — Discussion-based scenario walkthrough with no actual resource deployment.
- **Failover Test** — Controlled transition from primary to backup systems to validate DR procedures.
- **Simulation** — Virtual environment mimicking disaster scenarios for hands-on practice.
- **Parallel Processing** — Running primary and secondary systems simultaneously for testing.
- **Onsite Backup** — Data copies stored at same physical location as original data.
- **Offsite Backup** — Data copies stored at geographically separate location.
- **Snapshot** — Point-in-time copy capturing consistent state; records only changes since last snapshot.
- **Replication** — Real-time or near-real-time data copying to maintain data continuity.
- **Journaling** — Detailed record of data changes over time for granular recovery.
- **UPS (Uninterruptible Power Supply)** — Battery backup providing 10-60 minutes of power during outages.
- **Generator** — Converts mechanical energy to electrical energy for extended power during grid outages.
- **PDC (Power Distribution Center)** — Central hub for power distribution, monitoring, and load balancing.

-----

## Examples / scenarios

**Scenario 1:** A financial trading firm requires 99.999% uptime (five nines) and cannot tolerate more than 30 seconds of data loss. What site and backup strategy should they implement?

- **Answer:** Deploy a **hot site** with **synchronous replication**. Hot site provides immediate failover (meets five nines uptime). Synchronous replication ensures zero data loss (exceeds 30-second RPO requirement). Cost is justified by business-critical nature of trading operations.

**Scenario 2:** An e-commerce company has an RTO of 4 hours and RPO of 1 hour. During a disaster recovery test, they discover their warm site takes 8 hours to become operational.

- **Answer:** The warm site does not meet the 4-hour RTO requirement. Options: (1) Upgrade to hot site for faster recovery, (2) Pre-stage more equipment at warm site to reduce activation time to under 4 hours, (3) Revise RTO based on business impact analysis if 8 hours is acceptable after all.

**Scenario 3:** During a power outage, the UPS provides 15 minutes of backup power, but the generator fails to start. What should have been tested?

- **Answer:** Regular **failover testing** of the UPS-to-generator transition. Testing should include: (1) Simulated power loss to verify UPS activates, (2) Generator startup sequence, (3) Load transfer from UPS to generator, (4) Generator run under load. This outage indicates inadequate generator testing and maintenance.

**Scenario 4:** A healthcare provider performs daily full backups. After a ransomware attack at 2 PM, they discover the last backup completed at 11 PM the previous night. They lose 15 hours of patient records.

- **Answer:** The RPO was not properly defined or implemented. If patient records are updated continuously, RPO should be much shorter (e.g., 1-4 hours) requiring more frequent backups (incremental/differential) throughout the day. The 15-hour data loss violates HIPAA requirements for data availability.

**Scenario 5:** An organization tests disaster recovery by running production workload on the backup site while the primary site remains operational.

- **Answer:** This is **parallel processing** testing. Both systems run concurrently to validate the backup site can handle production load without disrupting operations. This is the safest DR testing method — if backup site fails, primary is unaffected.

-----

## Mini quiz

<details>
<summary><strong>Question 1:</strong> What is the difference between RPO and RTO, and how do they drive different decisions?</summary>

**Answer:** **RPO (Recovery Point Objective)** is the maximum acceptable data loss, measured in time. It drives how frequently you must back up. If RPO = 1 hour, you need backups every hour. **RTO (Recovery Time Objective)** is the maximum acceptable downtime. It drives your site selection and recovery speed. If RTO = 30 minutes, you need a hot site; if RTO = 1 week, a cold site suffices.

</details>

<details>
<summary><strong>Question 2:</strong> A company has a hot site with real-time replication. Do they still need backups? Why?</summary>

**Answer:** Yes. The hot site protects against site-wide failures (fire, flood, regional disaster), but backups protect against **logical corruption** — ransomware, accidental deletion, database corruption, application bugs. If ransomware encrypts data on the primary site, real-time replication will replicate the encrypted data to the hot site. Only backups (taken before the attack) can restore clean data.

</details>

<details>
<summary><strong>Question 3:</strong> What is the purpose of a tabletop exercise, and how does it differ from a failover test?</summary>

**Answer:** A **tabletop exercise** is a discussion-based walkthrough of a disaster scenario among stakeholders. No systems are actually switched or disrupted — it’s purely theoretical planning. A **failover test** is an actual controlled switch from primary to backup systems to validate the technical recovery procedures work. Tabletop = planning discussion; Failover = real technical test.

</details>

<details>
<summary><strong>Question 4:</strong> Why does synchronous replication provide zero data loss while asynchronous replication does not?</summary>

**Answer:** **Synchronous replication** requires writes to be committed to both primary and secondary systems before acknowledging success to the application. If primary fails, secondary has identical data (zero loss). **Asynchronous replication** commits to primary first, then replicates to secondary later. The lag between primary write and secondary replication means data loss equals the replication lag if primary fails.

</details>

<details>
<summary><strong>Question 5:</strong> What is the 3-2-1 backup rule, and why is each element important?</summary>

**Answer:** **3 copies** of data (production + 2 backups) protects against single backup failure. **2 different media types** (e.g., disk + tape) protects against media-specific failures or vulnerabilities. **1 offsite** copy protects against site-wide disasters (fire, flood, theft). Together, they provide comprehensive data protection.

</details>

### CompTIA-style practice questions

<details>
<summary><strong>Question 6:</strong> A company's business impact analysis determines their application has an RTO of 2 hours and RPO of 15 minutes. Which combination BEST meets these requirements?<br>A. Cold site with daily backups<br>B. Warm site with hourly backups<br>C. Hot site with continuous replication<br>D. Mobile site with weekly backups</summary>

**Correct Answer: C. Hot site with continuous replication**

RTO of 2 hours requires near-immediate recovery — only a hot site (C) can achieve this. RPO of 15 minutes means no more than 15 minutes of data loss acceptable — continuous replication ensures this (backups every 15 minutes would also work). Cold site (A) takes weeks. Warm site (B) with hourly backups meets RPO but likely cannot achieve 2-hour RTO. Mobile site (D) with weekly backups meets neither requirement.

</details>

<details>
<summary><strong>Question 7:</strong> During a disaster recovery test, the primary data center experiences a simulated power outage. The UPS provides power for 20 minutes, but the generator fails to start automatically. Operations are disrupted for 3 hours while technicians manually start the generator. What should have prevented this?<br>A. More frequent tabletop exercises<br>B. Regular failover testing of UPS-to-generator transition<br>C. Implementing a cold site<br>D. Increasing UPS battery capacity to 4 hours</summary>

**Correct Answer: B. Regular failover testing of UPS-to-generator transition**

The issue was the generator’s failure to automatically start — this would have been discovered through regular failover testing (B). Tabletop exercises (A) are discussion-only and wouldn’t test actual equipment. A cold site (C) doesn’t address power resilience at primary site. Increasing UPS capacity (D) delays but doesn’t solve the generator startup issue.

</details>

<details>
<summary><strong>Question 8 (Multi-select):</strong> An organization is implementing a disaster recovery plan. Which TWO metrics are MOST important for determining backup frequency and site selection? (Choose TWO)<br>A. MTBF (Mean Time Between Failures)<br>B. RPO (Recovery Point Objective)<br>C. MTTR (Mean Time To Repair)<br>D. RTO (Recovery Time Objective)<br>E. SLA (Service Level Agreement)</summary>

**Correct Answers: B. RPO (Recovery Point Objective) and D. RTO (Recovery Time Objective)**

RPO (B) determines how frequently backups must occur (e.g., RPO = 1 hour means hourly backups). RTO (D) determines site selection (e.g., RTO = 30 minutes requires hot site; RTO = 1 week allows cold site). MTBF (A) and MTTR (C) are reliability metrics but don’t directly drive backup/site decisions. SLA (E) may include RTO/RPO but is not itself the determining metric.

</details>

-----

## Related objectives

- [**1.2**]({{ ‘/secplus/objectives/1-2/’ | relative_url }}) — Availability in the CIA triad is achieved through resilience and recovery mechanisms.
- [**3.1**]({{ ‘/secplus/objectives/3-1/’ | relative_url }}) — Cloud and hybrid architectures require geographic dispersion and multi-cloud strategies.
- [**3.2**]({{ ‘/secplus/objectives/3-2/’ | relative_url }}) — Infrastructure redundancy (load balancing, clustering) implements high availability.
- [**5.1**]({{ ‘/secplus/objectives/5-1/’ | relative_url }}) — Security governance defines BC/DR policies and testing requirements.

-----

## Navigation

**Domain 3.0: Security Architecture**

|Objective                              |Title                                                                      |Status                                                                          |
|---------------------------------------|---------------------------------------------------------------------------|--------------------------------------------------------------------------------|
|[**3.1**]({{ ‘/secplus/objectives/3-1/’|relative_url }})                                                           |Compare and contrast security implications of different architecture models.    |
|[**3.2**]({{ ‘/secplus/objectives/3-2/’|relative_url }})                                                           |Given a scenario, apply security principles to secure enterprise infrastructure.|
|[**3.3**]({{ ‘/secplus/objectives/3-3/’|relative_url }})                                                           |Compare and contrast concepts and strategies to protect data.                   |
|3.4 (current)                          |Explain the importance of resilience and recovery in security architecture.|✅ done                                                                          |

[← Back to Dashboard]({{ ‘/secplus/’ | relative_url }}) | [Next: Objective 4.1 →]({{ ‘/secplus/objectives/4-1/’ | relative_url }})