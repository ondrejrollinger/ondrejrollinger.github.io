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

## Backup Strategies

**Backup types:**

**Full backup:**
- **Method:** Copy all data
- **Restoration:** Single backup needed
- **Time:** Longest (hours for TB of data)
- **Storage:** Most space required
- **Frequency:** Weekly or monthly

**Incremental backup:**
- **Method:** Copy only data changed since last backup (any type)
- **Restoration:** Need last full + all incrementals
- **Time:** Fastest backup
- **Storage:** Least space
- **Frequency:** Daily or multiple times per day
- **Risk:** If one incremental lost, can't restore fully

**Differential backup:**
- **Method:** Copy data changed since last FULL backup
- **Restoration:** Need last full + last differential
- **Time:** Slower than incremental (grows until next full)
- **Storage:** More than incremental
- **Frequency:** Daily
- **Benefit:** Faster restoration than incremental

**Backup schedule example:**
```
Sunday: Full backup (all data)
Monday: Differential (changes since Sunday)
Tuesday: Differential (all changes since Sunday)
Wednesday: Differential (all changes since Sunday)
Thursday: Differential (all changes since Sunday)
Friday: Differential (all changes since Sunday)
Saturday: Differential (all changes since Sunday)

Restoration on Friday:
- Restore Sunday's full backup
- Restore Friday's differential
- Done! (2 backups needed)

VS Incremental schedule:
Sunday: Full
Monday-Saturday: Incremental (changes since previous day)

Restoration on Friday:
- Restore Sunday's full
- Restore Monday's incremental
- Restore Tuesday's incremental
- Restore Wednesday's incremental
- Restore Thursday's incremental
- Restore Friday's incremental
- Done (6 backups needed, longer restoration)
```

**Backup locations:**

**On-site:**
- **Storage:** Same building/datacenter
- **Pro:** Fast backup and restoration
- **Con:** Vulnerable to same disasters (fire, flood)
- **Use:** Quick recovery for minor incidents

**Off-site:**
- **Storage:** Different geographic location
- **Pro:** Protected from local disasters
- **Con:** Slower restoration (physical transport or network transfer)
- **Use:** Disaster recovery

**Cloud backup:**
- **Storage:** AWS S3, Azure Blob, Google Cloud
- **Pro:** Scalable, geographically distributed, cost-effective
- **Con:** Requires internet, subscription costs
- **Use:** Long-term retention, disaster recovery

**3-2-1 backup rule:**
- **3 copies** of data (production + 2 backups)
- **2 different media types** (disk + tape, or disk + cloud)
- **1 off-site** backup (protect against local disasters)

**Backup media:**

**Disk (hard drives, NAS, SAN):**
- **Pro:** Fast backup/restoration, random access
- **Con:** More expensive per GB than tape
- **Use:** Recent backups, quick recovery

**Tape (LTO - Linear Tape-Open):**
- **Pro:** Cheap per GB, long-term durability (30+ years)
- **Con:** Sequential access (slow), requires tape drive
- **Use:** Long-term archival

**Cloud storage:**
- **Pro:** No hardware to maintain, unlimited scalability
- **Con:** Ongoing costs, egress fees
- **Use:** Off-site backup, disaster recovery

**Backup testing:**
- **Frequency:** Quarterly minimum
- **Method:** Restore test data, verify integrity
- **Document:** Recovery time actual vs RTO target
- **Purpose:** Verify backups work (don't discover failures during actual disaster)

**Backup security:**
- **Encryption:** Encrypt backups (at rest and in transit)
- **Access control:** Limit who can delete/modify backups
- **Immutability:** Write-once-read-many (WORM) prevents ransomware from encrypting backups
- **Air gap:** Physically disconnect backup media from network

---

## Disaster Recovery

**Disaster types:**
- **Natural:** Hurricane, earthquake, flood, fire
- **Technical:** Hardware failure, power outage, network failure
- **Human-caused:** Cyberattack, sabotage, terrorism
- **Pandemic:** Workforce unavailable

**Disaster Recovery Plan (DRP):**

**Components:**
1. **Emergency contacts:** Who to call (IT, management, vendors)
2. **Recovery procedures:** Step-by-step recovery instructions
3. **System priorities:** Which systems restore first
4. **Backup locations:** Where backups stored, how to access
5. **Alternate sites:** Where to operate if primary site unavailable

**Recovery objectives:**

**RPO (Recovery Point Objective):**
- **Definition:** Maximum acceptable data loss (measured in time)
- **Example:** RPO = 4 hours means max 4 hours of data loss acceptable
- **Determines:** Backup frequency
- **Calculation:** If RPO = 4 hours, must backup every 4 hours or less

**RTO (Recovery Time Objective):**
- **Definition:** Maximum acceptable downtime
- **Example:** RTO = 8 hours means must restore within 8 hours
- **Determines:** Recovery strategy (hot site vs cold site)
- **Calculation:** Time from disaster to full operation

**MTBF (Mean Time Between Failures):**
- **Definition:** Average time system operates before failing
- **Example:** MTBF = 100,000 hours = ~11 years
- **Use:** Hardware reliability metric

**MTTR (Mean Time To Repair):**
- **Definition:** Average time to repair and restore
- **Example:** MTTR = 4 hours
- **Use:** Measure recovery efficiency

**Example RPO/RTO calculation:**
```
Critical database server:
- Business impact if down: $50k/hour revenue loss
- Data sensitivity: High (customer orders)
- Regulatory requirement: Financial data must be recoverable

Decision:
- RPO = 1 hour (max 1 hour data loss acceptable)
- RTO = 4 hours (max 4 hours downtime acceptable)

Implementation:
- Backup every 30 minutes (meets RPO)
- Hot site with real-time replication (meets RTO)
- Cost: $100k/year
- Justification: 4-hour outage costs $200k, hot site prevents this
```

**Recovery sites:**

**Hot site:**
- **Definition:** Fully equipped, operational duplicate datacenter
- **Readiness:** Immediate (real-time replication)
- **RTO:** Minutes to hours
- **Cost:** Most expensive
- **Use:** Mission-critical systems (can't tolerate downtime)

**Warm site:**
- **Definition:** Partially equipped, hardware ready but data delayed
- **Readiness:** Hours to restore (restore from backups)
- **RTO:** Hours to days
- **Cost:** Medium
- **Use:** Important but not mission-critical

**Cold site:**
- **Definition:** Empty facility with power/network (no equipment)
- **Readiness:** Days to weeks (install hardware, restore data)
- **RTO:** Days to weeks
- **Cost:** Least expensive
- **Use:** Non-critical systems, budget constraints

**Mobile site:**
- **Definition:** Portable datacenter (trailer/container)
- **Readiness:** Hours to days (transport and setup)
- **Use:** Temporary recovery, remote locations

**Recovery strategies:**

**Failover:**
- **Definition:** Switch to backup system when primary fails
- **Automatic:** System detects failure, switches automatically
- **Manual:** IT admin initiates failover
- **Example:** Primary database fails, failover to standby replica

**Failback:**
- **Definition:** Return to primary system after recovery
- **Process:** Restore primary, sync data, switch back
- **Timing:** After primary fully restored and tested

**Replication:**
- **Synchronous:** Real-time copy (zero data loss, slower)
- **Asynchronous:** Delayed copy (minimal data loss, faster)
- **Use:** Hot site, database high availability

---

## High Availability and Redundancy

**High availability (HA):**
- **Goal:** Minimize downtime
- **Measure:** Uptime percentage (99.9% = 8.76 hours/year downtime)
- **Methods:** Redundancy, clustering, load balancing

**Availability tiers:**
```
99% = 3.65 days/year downtime
99.9% (three nines) = 8.76 hours/year downtime
99.99% (four nines) = 52.56 minutes/year downtime
99.999% (five nines) = 5.26 minutes/year downtime
```

**Redundancy types:**

**Hardware redundancy:**
- **Redundant power supplies:** Two power supplies per server
- **RAID:** Multiple drives (data survives drive failure)
- **Redundant network interfaces:** Multiple NICs per server
- **UPS:** Uninterruptible Power Supply (battery backup)

**Geographic redundancy:**
- **Multiple datacenters:** Different cities/regions
- **Purpose:** Survive regional disasters
- **Example:** AWS availability zones

**Network redundancy:**
- **Multiple ISPs:** Diverse internet connections
- **Redundant switches/routers:** Eliminate single points of failure
- **Alternate paths:** Multiple network routes

**Clustering:**
- **Definition:** Multiple servers working together as one
- **Active-Active:** All nodes handle traffic (load balanced)
- **Active-Passive:** One node active, others standby (failover)
- **Use:** Database servers, web servers, applications

**Load balancing:**
- **Definition:** Distribute traffic across multiple servers
- **Methods:**
  - **Round robin:** Rotate through servers sequentially
  - **Least connections:** Send to server with fewest active connections
  - **Geographic:** Route to nearest server
- **Benefits:** Performance, redundancy (server fails, others continue)

**Single Point of Failure (SPOF):**
- **Definition:** Component whose failure stops entire system
- **Examples:** Single power supply, single network link, single server
- **Mitigation:** Redundancy (eliminate all SPOFs)

---

## Business Continuity

**Business Continuity Plan (BCP):**

**Difference from DRP:**
- **DRP:** IT systems recovery (technology focus)
- **BCP:** Entire business operations (people, processes, technology)

**BCP components:**

**Business Impact Analysis (BIA):**
- **Purpose:** Identify critical business functions and impact of disruption
- **Process:**
  1. Identify critical functions (payroll, customer support, manufacturing)
  2. Determine impact of downtime (revenue loss, reputation damage)
  3. Calculate maximum tolerable downtime (MTD)
  4. Prioritize recovery (most critical first)

**Continuity of Operations Plan (COOP):**
- **Purpose:** Continue operations during disruption
- **Strategies:**
  - **Work from home:** Remote work capabilities
  - **Alternate work site:** Backup office location
  - **Cross-training:** Employees can cover multiple roles
  - **Succession planning:** Backup for key personnel

**Crisis communication plan:**
- **Internal:** Notify employees of situation
- **External:** Communicate with customers, partners, media
- **Templates:** Pre-written messages for different scenarios

**Testing BCP:**

**Tabletop exercise:**
- **Method:** Discussion-based walkthrough
- **Participants:** Key personnel discuss scenario
- **Benefit:** Identifies plan gaps without disruption
- **Frequency:** Quarterly

**Simulation:**
- **Method:** Simulated disaster, team responds
- **Scope:** Larger than tabletop, may involve technology
- **Benefit:** More realistic than tabletop
- **Frequency:** Annually

**Full interruption test:**
- **Method:** Actually fail over to backup systems
- **Scope:** Complete DR test
- **Benefit:** Proves plan works
- **Frequency:** Rarely (disruptive and expensive)

---

## Key Distinctions

**RPO vs RTO:**
- RPO: How much data loss acceptable (backup frequency)
- RTO: How long downtime acceptable (recovery speed)

**Hot Site vs Cold Site:**
- Hot site: Fully ready, immediate failover (expensive)
- Cold site: Empty facility, days to setup (cheap)

**Full vs Incremental backup:**
- Full: All data, long backup, fast restore
- Incremental: Changed data, fast backup, slow restore

**DRP vs BCP:**
- DRP: IT disaster recovery (technology)
- BCP: Business continuity (entire organization)

**Failover vs Failback:**
- Failover: Switch to backup system
- Failback: Return to primary system

---

## Common Exam Traps

1. **Trap:** Thinking RPO and RTO are the same
   - **Reality:** RPO = data loss, RTO = downtime

2. **Trap:** Believing backups guarantee recovery
   - **Reality:** Must test backups (verify they work)

3. **Trap:** Assuming on-site backup sufficient
   - **Reality:** Need off-site for disaster recovery (3-2-1 rule)

4. **Trap:** Thinking full backup always best
   - **Reality:** Incremental faster, uses less storage (trade-off with restore time)

5. **Trap:** Believing hot site is always required
   - **Reality:** Choose based on RTO/RPO requirements and budget

---

## Exam Tips

1. **RPO = data loss** (time between backups)
2. **RTO = downtime** (time to restore)
3. **3-2-1 backup rule:** 3 copies, 2 media types, 1 off-site
4. **Hot site = immediate** (real-time replication, expensive)
5. **Cold site = days/weeks** (empty facility, cheap)
6. **Full backup = all data** (slow backup, fast restore)
7. **Incremental backup = changed data** (fast backup, slow restore)
8. **Test backups quarterly** (verify they work before disaster)
9. **BCP = entire business**, DRP = IT systems
10. **High availability measured** in uptime percentage (99.9% = 8.76 hours downtime/year)

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