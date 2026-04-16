---
layout: objective
title: "4.2 Asset Management"
objective_id: "4.2"
domain: "4.0 Security Operations"
status: "done"
tags: ["asset-management", "inventory", "lifecycle", "disposal"]
permalink: /objectives/4-2/
---

## Overview

Asset management involves tracking, maintaining, and securing organizational resources throughout their lifecycle. This includes acquisition, deployment, maintenance, and disposal of hardware, software, and data assets.

---

## Asset Acquisition and Assignment

**Asset types:**
- Hardware: Servers, workstations, network devices, mobile devices
- Software: Applications, licenses, operating systems
- Data: Databases, files, intellectual property
- Virtual assets: Virtual machines, cloud instances

**Acquisition process:**
1. Request/approval (business justification)
2. Procurement (vendor selection, purchase)
3. Receiving (verify against order)
4. Asset tagging (unique identifier)
5. Inventory registration (add to asset database)
6. Configuration (install, harden, baseline)
7. Assignment (user/location assignment)

**Asset tagging:**
- **Barcode:** Machine-readable label
- **RFID:** Radio frequency identification (passive tracking)
- **Asset number:** Unique identifier in inventory system
- **Purpose:** Track location, ownership, maintenance

**Assignment tracking:**
- Who has the asset (user, department)
- Where located (building, room, rack)
- When assigned (date)
- Configuration (specs, software installed)

---

## Classification

**Asset classification criteria:**

**By criticality:**
- **Critical:** Failure causes major business impact (production database)
- **Important:** Significant impact but not catastrophic (file server)
- **Standard:** Minimal impact (individual workstation)

**By sensitivity:**
- **High:** Contains confidential data (customer PII, trade secrets)
- **Medium:** Internal use only (employee directory)
- **Low:** Public information (marketing materials)

**By ownership:**
- **Company-owned:** Organization owns and controls
- **Personal:** Employee-owned (BYOD devices)
- **Leased:** Third-party owned (leased equipment)

**Classification purpose:**
- Determines security controls required
- Influences backup/recovery priority
- Guides disposal procedures
- Affects monitoring intensity

---

## Asset Monitoring and Inventory

**Inventory management:**

**Automated discovery:**
- Network scanning (Nmap, vulnerability scanners)
- Agent-based (installed software reports back)
- SNMP polling (network devices)
- Cloud API queries (AWS, Azure inventory)

**Configuration Management Database (CMDB):**
- Centralized repository of asset information
- Tracks: Hardware specs, software versions, dependencies
- Links assets to services (which systems support which business functions)
- Change tracking (configuration history)

**Inventory attributes tracked:**
- Asset ID and type
- Location and user assignment
- Hardware specifications (CPU, memory, storage)
- Software installed (OS, applications, versions)
- Network configuration (IP, MAC address)
- Purchase date and cost
- Warranty/support expiration
- Last update/patch date

**Enumeration:**
- Active enumeration: Scanning network for devices
- Passive enumeration: Monitoring network traffic
- Purpose: Discover unauthorized assets (shadow IT)

**Tracking methods:**

**Asset management software:**
- Examples: ServiceNow, BMC Asset Manager, Lansweeper
- Capabilities: Automated discovery, license tracking, compliance reporting

**Spreadsheets:**
- Low-tech option for small organizations
- Manual updates required
- Limited scalability

**Mobile Device Management (MDM):**
- Tracks mobile devices (phones, tablets)
- Enrollment status, OS version, installed apps
- Location tracking

---

## Ownership and Lifecycle Management

**Asset lifecycle stages:**

### 1. Procurement
- Vendor selection
- Purchase order
- Budget approval
- Security requirements specified

### 2. Deployment
- Configuration and hardening
- Asset tagging
- User assignment
- Training (if needed)

### 3. Maintenance
- Patching and updates
- Hardware repairs
- License renewals
- Configuration changes

### 4. Retirement
- End of life (EOL) reached
- Replaced by newer technology
- No longer supported by vendor

### 5. Disposal
- Data sanitization
- Physical destruction (if required)
- Recycling or donation
- Certificate of destruction

**Ownership types:**

**Company-owned:**
- Full control over asset
- Company responsible for security
- Can enforce all policies

**Employee-owned (BYOD):**
- Limited control (MDM/MAM)
- Employee privacy concerns
- Data separation required (containerization)

**Third-party (vendor/partner):**
- Contractor equipment accessing network
- Requires guest network or NAC
- Separate security policies

---

## Asset Disposal and Decommissioning

**Disposal security concerns:**
- Data remanence (residual data on drives)
- Regulatory compliance (HIPAA, PCI-DSS require secure disposal)
- Physical security (prevent dumpster diving)

**Data sanitization methods:**

**Overwriting:**
- Write random data over existing data
- Multiple passes (DoD 5220.22-M: 7 passes)
- Verifiable (can confirm completion)
- Time-consuming for large drives

**Degaussing:**
- Powerful magnetic field destroys data
- Renders drive unusable (magnetic media only)
- Fast for multiple drives
- Not effective on SSDs (no magnetic storage)

**Physical destruction:**
- Shredding (industrial shredder)
- Pulverizing (crushing to small pieces)
- Incineration (complete destruction)
- Most secure (data unrecoverable)
- Expensive, drive not reusable

**Cryptographic erasure:**
- Delete encryption key
- Data remains but unreadable without key
- Fast (instant)
- Relies on strong encryption (if encryption weak, data recoverable)

**Method selection:**

| Drive Type | Reuse? | Method |
|------------|--------|--------|
| HDD | Yes | Overwriting (7 passes) |
| HDD | No | Degaussing or shredding |
| SSD | Yes | Cryptographic erase |
| SSD | No | Physical destruction |
| Tape | No | Degaussing |

**Certificate of destruction:**
- Third-party destruction services provide certificate
- Proves disposal completed
- Required for compliance (audit evidence)
- Includes: Asset IDs, destruction method, date, witness signatures

**Decommissioning process:**
1. Remove from production
2. Backup data (if needed for retention)
3. Remove from inventory
4. Data sanitization
5. Physical disposal
6. Update asset database (status: decommissioned)
7. Obtain certificate of destruction

---

## Key Distinctions

**Enumeration vs Inventory:**
- Enumeration: Discovery process (finding assets)
- Inventory: Tracking process (managing known assets)

**Overwriting vs Degaussing:**
- Overwriting: Writes data over existing (drive reusable)
- Degaussing: Magnetic field destroys data (drive unusable)

**Asset classification vs Data classification:**
- Asset classification: Criticality/ownership of system
- Data classification: Sensitivity of information stored

**CMDB vs Asset inventory:**
- CMDB: Includes relationships and dependencies
- Asset inventory: Simple list of assets

---

## Common Exam Traps

1. **Trap:** Thinking degaussing works on SSDs
   - **Reality:** Degaussing only works on magnetic media (HDDs, tapes)

2. **Trap:** Believing simple deletion secures data
   - **Reality:** Deleted files recoverable, need overwriting or destruction

3. **Trap:** Assuming one overwrite pass is sufficient
   - **Reality:** DoD standard requires 7 passes for sensitive data

4. **Trap:** Thinking all assets need same disposal method
   - **Reality:** Method depends on sensitivity, reuse plans, and media type

5. **Trap:** Believing asset tagging is only for inventory
   - **Reality:** Also enables tracking, theft prevention, and lifecycle management

---

## Exam Tips

1. **Asset lifecycle:** Procurement → Deployment → Maintenance → Retirement → Disposal
2. **Overwriting = multiple passes** of random data (HDD reusable)
3. **Degaussing = magnetic field** (destroys HDD, not SSDs)
4. **Physical destruction most secure** (data unrecoverable)
5. **Cryptographic erase** = Delete encryption key (fast for encrypted drives)
6. **Certificate of destruction** required for compliance audits
7. **CMDB tracks relationships** between assets (dependencies)
8. **Enumeration discovers** unauthorized assets (shadow IT)
9. **Asset classification determines** security controls required
10. **BYOD requires MDM/MAM** for asset management

---

## Quick Navigation
- [← Previous: 4.1 Security Techniques](../4-1/)
- [→ Next: 4.3 Vulnerability Management](../4-3/)
- [↑ Back to Domain 4](../)
