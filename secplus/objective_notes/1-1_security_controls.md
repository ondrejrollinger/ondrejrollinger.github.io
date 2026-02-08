## layout: objective
title: “1.1 - Compare and contrast various types of security controls”
domain: “1.0 General Security Concepts”
weight: 12
status: pending

# Objective 1.1: Compare and contrast various types of security controls

## Official Scope

Compare and contrast security control categories (Technical, Managerial, Operational, Physical) and types (Preventive, Deterrent, Detective, Corrective, Compensating, Directive).

-----

## Key Concepts

### Security Control Categories (The Four Pillars)

#### 1. **Technical Controls** 🔧

- **Definition**: Technologies, hardware, and software mechanisms implemented to manage and reduce risks
- **Examples**:
  - Firewalls, IDS/IPS
  - Encryption (at rest, in transit)
  - Antivirus/anti-malware
  - Multi-factor authentication (MFA)
  - Access control lists (ACLs)
  - Biometric scanners
- **Exam Tip**: Think “technology-based” - if it requires IT systems or software, it’s technical

#### 2. **Managerial Controls** 📋

- **Also called**: Administrative controls
- **Definition**: Strategic planning and governance side of security - the policies and procedures
- **Examples**:
  - Security policies and procedures
  - Risk assessments
  - Vulnerability management programs
  - Security awareness training programs
  - Background checks
  - Change management processes
- **Exam Tip**: Think “paperwork and planning” - focuses on the management layer

#### 3. **Operational Controls** 👥

- **Definition**: Procedures and measures designed to protect data on a day-to-day basis
- **Key characteristic**: Mainly governed by internal processes and human actions
- **Examples**:
  - Backup procedures
  - Account reviews
  - Log monitoring
  - Configuration management
  - Incident response activities
  - Security awareness training (execution)
- **Exam Tip**: Think “people doing things” - daily security operations

#### 4. **Physical Controls** 🏢

- **Definition**: Tangible, real-world measures taken to protect assets
- **Examples**:
  - Locks, badge readers
  - Security guards
  - Cameras (CCTV)
  - Fences, bollards
  - Mantraps/access control vestibules
  - Fire suppression systems
  - Environmental controls (HVAC)
- **Exam Tip**: Think “touch it” - if you can physically interact with it, it’s physical

-----

### Security Control Types (The Six Functions)

#### 1. **Preventive Controls** 🛡️

- **Purpose**: Proactive measures to thwart potential security threats BEFORE they occur
- **Goal**: Stop the attack
- **Examples**:
  - Firewalls blocking traffic
  - Security guards preventing unauthorized entry
  - Encryption preventing data reading
  - System hardening
  - Security awareness training
- **Mnemonic**: “PREVENT = Pre-event”

#### 2. **Deterrent Controls** ⚠️

- **Purpose**: Discourage potential attackers by making effort seem less appealing or more challenging
- **Goal**: Make attacker think twice
- **Examples**:
  - Warning signs (“Protected by…”)
  - Security cameras (visible)
  - Login banners
  - Cable locks on equipment
  - Presence of security guards
- **Key Difference from Preventive**: May not actually stop attack, but discourages it
- **Exam Tip**: “Deterrent = Discourages”

#### 3. **Detective Controls** 🔍

- **Purpose**: Monitor and alert organizations to malicious activities as they occur or shortly after
- **Goal**: Identify when something bad happens
- **Examples**:
  - IDS (Intrusion Detection Systems)
  - Log monitoring and SIEM
  - Security cameras (reviewing footage)
  - Motion detectors
  - File integrity monitoring
  - Security audits
- **Mnemonic**: “Detective = Detect it”

#### 4. **Corrective Controls** 🔧

- **Purpose**: Mitigate potential damage and restore systems to normal state AFTER an incident
- **Goal**: Fix the problem
- **Examples**:
  - Backup restoration
  - Patching systems
  - IPS blocking malicious traffic
  - Antivirus quarantining malware
  - Incident response procedures
- **Timeline**: Happens AFTER detection
- **Exam Tip**: “Corrective = Correct the problem”

#### 5. **Compensating Controls** 🔄

- **Purpose**: Alternative measures implemented when primary security controls are not feasible or effective
- **Goal**: Fill the gap when you can’t use the ideal control
- **Examples**:
  - Can’t encrypt? → Use increased monitoring + stricter access controls
  - Can’t patch legacy system? → Network segmentation
  - Can’t afford expensive firewall? → Multiple cheaper solutions
- **Key Phrase**: “Alternative measure”
- **Exam Tip**: Think “Plan B” - when the optimal control isn’t possible

#### 6. **Directive Controls** 📜

- **Purpose**: Guide, inform, or mandate actions
- **Key characteristic**: Often rooted in policy or documentation
- **Examples**:
  - Security policies
  - Procedures and standards
  - Compliance requirements
  - Training materials
  - Acceptable use policies (AUP)
- **Exam Tip**: “Directive = Directs behavior through rules”

-----

## The Matrix: Categories × Types

**Important**: Controls can be BOTH a category AND a type!

|Control Example            |Category              |Type                          |
|---------------------------|----------------------|------------------------------|
|Firewall                   |Technical             |Preventive                    |
|IDS                        |Technical             |Detective                     |
|Security policy            |Managerial            |Directive                     |
|Security awareness training|Managerial/Operational|Preventive                    |
|Security guard             |Physical              |Deterrent/Detective/Preventive|
|CCTV cameras               |Physical              |Detective/Deterrent           |
|Backup procedures          |Operational           |Corrective                    |

-----

## Exam Strategy

### Common Question Patterns

1. **“Which type of control is X?”**
- Focus on the PURPOSE/FUNCTION
- Example: “CCTV cameras” → Detective (they detect/record events)
1. **“Which category does this belong to?”**
- Focus on WHAT it is (tech, people, policy, physical)
- Example: “Account review process” → Operational
1. **Scenario-based**: “Company can’t implement encryption due to legacy systems. They add network monitoring instead.”
- Answer: Compensating control
1. **Multi-select**: “Select TWO control types for a firewall”
- Preventive (blocks traffic)
- Detective (logs activity)

### Key Distinctions to Know

|Comparison                   |Distinction                                  |
|-----------------------------|---------------------------------------------|
|**Preventive vs Deterrent**  |Preventive STOPS it; Deterrent DISCOURAGES it|
|**Detective vs Corrective**  |Detective FINDS it; Corrective FIXES it      |
|**Managerial vs Operational**|Managerial PLANS it; Operational DOES it     |
|**Technical vs Physical**    |Technical is DIGITAL; Physical is TANGIBLE   |

-----

## Memory Aids

### Control Categories: “TMOP”

- **T**echnical (tech solutions)
- **M**anagerial (management/admin)
- **O**perational (operations/procedures)
- **P**hysical (physical security)

### Control Types: “PP-DD-CC”

- **P**reventive
- **P (deterrent)** - think “Please don’t”
- **D**etective
- **D (directive)** - think “Do this”
- **C**orrective
- **C**ompensating

### Quick Decision Tree

```
Is it stopping something BEFORE? → Preventive
Is it discouraging via warning? → Deterrent
Is it finding/alerting? → Detective
Is it fixing after? → Corrective
Is it a backup plan? → Compensating
Is it a rule/guideline? → Directive
```

-----

## Practice Scenarios

### Scenario 1

**Question**: A company implements a login banner that states “Unauthorized access is prohibited and will be prosecuted.” What type of control is this?

<details>
<summary>Answer</summary>

**Deterrent Control** - It discourages unauthorized access by warning of consequences, but doesn’t actually prevent someone from attempting to log in.

Also **Directive** - It directs behavior by stating what is/isn’t allowed.

Category: **Managerial/Operational**

</details>

### Scenario 2

**Question**: After a security incident, the IR team restores systems from backup and applies missing patches. What type of control is this?

<details>
<summary>Answer</summary>

**Corrective Control** - These actions are taken AFTER an incident to fix problems and restore normal operations.

Category: **Operational/Technical**

</details>

### Scenario 3

**Question**: A healthcare organization cannot encrypt a legacy medical device due to compatibility issues. They place it in a separate VLAN with restricted access and enhanced monitoring. What type of control is this?

<details>
<summary>Answer</summary>

**Compensating Control** - Since the primary control (encryption) can’t be used, alternative measures are implemented to reduce risk.

The network segmentation and monitoring serve as the “workaround” security measures.

</details>

-----

## Common Exam Traps

❌ **TRAP**: Thinking a security guard is ONLY physical
✅ **REALITY**: Security guard can be Physical (category) AND Preventive + Deterrent + Detective (types)

❌ **TRAP**: Assuming all managerial controls are directive
✅ **REALITY**: Security policies are Managerial + Directive, but risk assessments are Managerial + Detective

❌ **TRAP**: Confusing “compensating” with “corrective”
✅ **REALITY**:

- Compensating = Used INSTEAD of primary control (proactive alternative)
- Corrective = Used AFTER an incident (reactive fix)

❌ **TRAP**: Thinking training is only managerial
✅ **REALITY**:

- Training PROGRAM = Managerial
- Training DELIVERY = Operational
- Training CONTENT = Directive

-----

## Related Objectives

- **1.2** - CIA Triad ties to control goals
- **2.5** - Mitigation techniques implement these controls
- **3.2** - Security principles use these controls
- **5.1** - Governance includes control frameworks

-----

## CompTIA-Style Practice Questions

### Question 1

A security administrator implements a system that automatically blocks IP addresses after three failed login attempts. Which type of security control is being described?

A. Detective  
B. Deterrent  
C. Corrective  
D. Preventive

<details>
<summary>Answer & Explanation</summary>

**Correct Answer: D. Preventive**

**Explanation**: The system PREVENTS further unauthorized access attempts by blocking the IP address. While it detects the failed attempts (detective aspect), its PRIMARY function is prevention of future attacks from that IP.

**Why others are wrong**:

- A: Detective would only alert, not block
- B: Deterrent would warn but not enforce
- C: Corrective would fix after an incident occurred

</details>

### Question 2

Which of the following is the BEST example of a compensating control?

A. Installing antivirus on all workstations  
B. Using network segmentation when encryption isn’t possible  
C. Creating a disaster recovery plan  
D. Implementing multi-factor authentication

<details>
<summary>Answer & Explanation</summary>

**Correct Answer: B. Using network segmentation when encryption isn’t possible**

**Explanation**: This is compensating because it’s an ALTERNATIVE measure used when the primary control (encryption) cannot be implemented. Keywords: “when X isn’t possible” → compensating

**Why others are wrong**:

- A: Standard preventive control, not compensating
- C: Standard operational control for business continuity
- D: Standard preventive control, not an alternative to something else

</details>

### Question 3 (Multi-select)

A company installs visible security cameras at all entrances. Select TWO types of controls this represents. (Choose TWO)

A. Preventive  
B. Detective  
C. Deterrent  
D. Corrective  
E. Compensating

<details>
<summary>Answer & Explanation</summary>

**Correct Answers: B. Detective and C. Deterrent**

**Explanation**:

- **Detective**: Cameras record and allow security to detect incidents
- **Deterrent**: VISIBLE cameras discourage would-be attackers

Note: Could argue preventive if they stop crime, but CompTIA typically views cameras as primarily detective/deterrent since they don’t physically prevent entry.

</details>

-----

## Key Takeaways for Exam Day

1. **Controls serve multiple purposes** - A single control can be multiple types
1. **Context matters** - Same technology can be different types based on how it’s used
1. **Look for keywords**:
- “Prevents/Blocks” → Preventive
- “Warns/Discourages” → Deterrent
- “Detects/Monitors/Alerts” → Detective
- “Restores/Fixes” → Corrective
- “Alternative/Instead of” → Compensating
- “Policy/Guideline” → Directive
1. **Category vs Type** - Don’t confuse them!
- Category = WHAT it is (Technical, Managerial, Operational, Physical)
- Type = WHAT it DOES (Preventive, Deterrent, Detective, Corrective, Compensating, Directive)

-----

## Additional Study Resources

- Review gap analysis and Plan of Action & Milestones (POA&M) in your notes
- Understand how security controls map to compliance frameworks
- Practice identifying real-world examples of each control type/category

**Status**: Ready for review ✓
