-----

## layout: objective
title: “1.2 - Summarize fundamental security concepts”
domain: “1.0 General Security Concepts”
weight: 12
status: pending

# Objective 1.2: Summarize fundamental security concepts

## Official Scope

Confidentiality, Integrity, Availability (CIA), Non-repudiation, Authentication, Authorization, Accounting (AAA), Gap analysis, Zero Trust, Physical security, Deception and disruption technology.

-----

## Key Concepts

### The CIA Triad (Foundation of Security)

#### **Confidentiality** 🔒

**Definition**: Protection of information from unauthorized access and disclosure

**Goal**: Only authorized people can VIEW the data

**Why It Matters**:

1. Protect personal privacy (PII, PHI)
1. Maintain business advantage (trade secrets)
1. Achieve regulatory compliance (GDPR, HIPAA, PCI-DSS)

**Methods to Ensure Confidentiality**:

- **Encryption**: Convert data to unreadable format
  - At rest (stored data)
  - In transit (network traffic)
  - In use (data being processed)
- **Access Controls**: User permissions, least privilege
- **Data Masking**: Obscure specific data (e.g., show only last 4 digits of SSN)
- **Physical Security**: Locked server rooms, badge access
- **Training & Awareness**: Educate users on data protection

**Exam Example**: Encrypting laptop hard drives = Confidentiality

-----

#### **Integrity** ✅

**Definition**: Data remains accurate and unchanged unless modified by authorized personnel

**Goal**: Data is TRUSTWORTHY and UNALTERED

**Why It Matters**:

1. Ensure data accuracy (financial records, medical data)
1. Maintain trust (customers, partners)
1. Ensure system operability (corrupted configs break systems)

**Methods to Ensure Integrity**:

- **Hashing**: Create fixed-size value (MD5, SHA-256)
  - Any change = different hash
  - Used for file verification
- **Digital Signatures**: Hash + encryption = authenticity + integrity
- **Checksums**: Verify data during transmission (CRC)
- **Access Controls**: Prevent unauthorized modifications
- **Regular Audits**: Review logs for unauthorized changes
- **Version Control**: Track changes over time

**Exam Example**: Using SHA-256 hash to verify downloaded file wasn’t tampered with = Integrity

-----

#### **Availability** 🟢

**Definition**: Information and resources are accessible when needed by authorized users

**Goal**: System UPTIME and ACCESS

**Why It Matters**:

1. Ensure business continuity (24/7 operations)
1. Maintain customer trust (e-commerce availability)
1. Uphold organization’s reputation (downtime = lost revenue)

**Key Concept: REDUNDANCY**

- Duplication of critical components to enhance reliability

**Types of Redundancy**:

- **Server Redundancy**: Load balancing, failover clustering
- **Data Redundancy**: RAID, backups (3-2-1 rule)
- **Network Redundancy**: Multiple ISPs, redundant switches/routers
- **Power Redundancy**: UPS (Uninterruptible Power Supply), generators

**Availability Metrics**:

- **Uptime percentage**: 99.999% (“five nines”) = 5.26 minutes downtime/year
- **RTO (Recovery Time Objective)**: Maximum acceptable downtime
- **RPO (Recovery Point Objective)**: Maximum acceptable data loss

**Exam Example**: Implementing RAID 5 for server storage = Availability

-----

### Beyond CIA: The Extended Model

#### **Non-repudiation** 📝

**Definition**: Proof that someone performed an action - they cannot deny it

**Goal**: ACCOUNTABILITY and PROOF

**How It Works**:

1. User creates/sends message
1. Hash the message
1. Encrypt hash with user’s PRIVATE key → Digital signature
1. Recipient decrypts with user’s PUBLIC key
1. Proves sender identity (only they have that private key)

**Why It Matters**:

- Confirm authenticity of digital transactions (contracts, purchases)
- Ensure integrity of critical communications (executive orders)
- Provide accountability (audit trails, legal disputes)

**Technologies**:

- **Digital Signatures**: Primary mechanism
- **Logging & Timestamps**: Audit trails with time/date
- **Delivery Receipts**: Email read receipts, blockchain transactions

**Exam Keyword**: “Cannot deny” = Non-repudiation

-----

### The Triple A’s of Security (AAA)

#### **Authentication** 🆔

**Definition**: Verifying identity - proving you are who you claim to be

**The Five Factors**:

1. **Something You Know** (Knowledge Factor)
- Passwords, PINs, passphrases
- Security questions
- **Weakness**: Can be forgotten, shared, stolen
1. **Something You Have** (Possession Factor)
- Smart cards, key fobs
- Mobile device (for SMS codes)
- Hardware tokens (RSA SecurID)
- **Weakness**: Can be lost, stolen
1. **Something You Are** (Inherence Factor)
- Fingerprints, iris scans
- Facial recognition
- Voice recognition
- **Weakness**: Can’t be changed if compromised
1. **Something You Do** (Action Factor)
- Typing patterns (keystroke dynamics)
- Signature dynamics
- Gait analysis (how you walk)
- **Weakness**: Behavioral patterns can change
1. **Somewhere You Are** (Location Factor)
- GPS coordinates
- IP geolocation
- Network location (inside corporate network)
- **Weakness**: Can be spoofed

**Multi-Factor Authentication (MFA)**:

- Uses TWO or MORE different factors
- **Not MFA**: Password + security question (both “something you know”)
- **Is MFA**: Password + SMS code (knowledge + possession)

**Exam Tip**: Count the TYPES of factors, not the NUMBER of items

-----

#### **Authorization** ✔️

**Definition**: Determining what an authenticated user can ACCESS or DO

**Happens AFTER authentication**

**Key Principles**:

- **Least Privilege**: Minimum access needed to perform job
- **Need-to-Know**: Access only to data required for specific tasks
- **Separation of Duties**: No single person has complete control

**Authorization Models**:

- **DAC (Discretionary Access Control)**: Owner controls access
- **MAC (Mandatory Access Control)**: System enforces based on labels
- **RBAC (Role-Based Access Control)**: Access based on job role
- **ABAC (Attribute-Based Access Control)**: Access based on attributes

**Why It Matters**:

- Protect sensitive data (financial records, customer data)
- Maintain system integrity (prevent unauthorized changes)
- Streamlined user experience (users see only what they need)

**Exam Example**: Setting file permissions so only managers can edit budget spreadsheet = Authorization

-----

#### **Accounting** 📊

**Also called**: Auditing

**Definition**: Tracking and recording user activities

**What It Provides**:

1. **Audit Trail**: Chronological record of activities
- Who did what, when, where
- Trace unauthorized access or changes
1. **Regulatory Compliance**: Maintain activity records (SOX, HIPAA)
1. **Forensic Analysis**: Understand security incidents
1. **Resource Optimization**: Track usage for capacity planning
1. **User Accountability**: Deter misuse through monitoring

**Technologies Used**:

- **Syslog Servers**: Aggregate logs from network devices
- **Network Analysis Tools**: Capture and analyze traffic (Wireshark, tcpdump)
- **SIEM Systems**: Real-time analysis of security alerts (Splunk, QRadar)

**Exam Keywords**:

- “Track user activities” = Accounting
- “Audit logs” = Accounting
- “Who did what when” = Accounting

-----

### Zero Trust Model

**Core Principle**: “Never trust, always verify”

- No implicit trust based on network location
- Verify every user, device, and transaction
- Assume breach has already occurred

**Architecture Components**:

#### **Control Plane** (Policy Layer)

Makes decisions about WHO gets access to WHAT

**Elements**:

1. **Adaptive Identity**
- Real-time validation based on context
- Factors: behavior, device, location, time, risk score
- **Example**: Login from new country → extra verification
1. **Threat Scope Reduction**
- Minimize attack surface
- Limit access to only what’s needed
- Reduces “blast radius” of breach
1. **Policy-Driven Access Control**
- Access based on roles and responsibilities
- Dynamic policies (contextual)
- Continuous evaluation
1. **Secured Zones**
- Isolated network segments for sensitive data
- Micro-segmentation
- Separate high-value assets

**Components**:

- **Policy Engine**: Evaluates access requests against policies
- **Policy Administrator**: Manages and establishes policies

-----

#### **Data Plane** (Enforcement Layer)

WHERE access decisions are enforced

**Components**:

1. **Subject/System**: User or device requesting access
1. **Policy Enforcement Point (PEP)**: Where access grant/deny is executed
- Network gateways
- Application proxies
- Agents on endpoints

**Zero Trust Workflow**:

1. Subject requests access to resource
1. Request goes to Policy Engine
1. Policy Engine evaluates:
- Identity verified?
- Device trusted?
- Location authorized?
- Time appropriate?
- Risk score acceptable?
1. Policy Administrator makes decision
1. Policy Enforcement Point grants/denies access
1. Continuous monitoring and re-evaluation

**Exam Tip**: Know difference between Control Plane (decisions) and Data Plane (enforcement)

-----

### Gap Analysis

**Definition**: Evaluating differences between CURRENT state and DESIRED state

**Purpose**: Identify security gaps and prioritize improvements

**Process Steps**:

1. **Define Scope**: What are we analyzing? (entire infrastructure, specific system, compliance requirement)
1. **Assess Current State**: Document existing security controls, policies, configurations
1. **Identify Desired State**: What SHOULD it be? (based on standards, regulations, best practices)
1. **Identify Gaps**: Where do we fall short?
1. **Prioritize**: Risk-based prioritization
1. **Develop Plan**: Create remediation roadmap

**Types of Gap Analysis**:

#### **Technical Gap Analysis**

- Evaluate technical infrastructure
- Identify capability shortfalls
- **Example**: Legacy systems can’t support modern encryption

#### **Business Gap Analysis**

- Evaluate business processes
- Identify process shortfalls
- **Example**: No formal change management process

**Output: Plan of Action and Milestones (POA&M)**

- Specific measures to address each vulnerability
- Resource allocation
- Timelines for remediation
- Milestones to track progress

**Exam Scenario**: “Organization wants to achieve SOX compliance. What should they do first?”
→ Answer: Conduct gap analysis to identify compliance gaps

-----

## Relationships Between Concepts

### CIA Triad + Non-repudiation + Authentication = **CIANA Pentagon**

```
         Non-repudiation
              /\
             /  \
            /    \
Confidentiality - Integrity
            \    /
             \  /
              \/
        Availability
    (Authentication at center)
```

### AAA Flow

```
1. Authentication → Who are you?
2. Authorization  → What can you do?
3. Accounting     → What did you do?
```

-----

## Memory Aids & Mnemonics

### CIA Triad

- **C**an’t see it → **C**onfidentiality (encryption)
- **I**s it accurate? → **I**ntegrity (hashing)
- **A**lways available → **A**vailability (redundancy)

### AAA

**“Who, What, When”**

- Authentication: WHO are you?
- Authorization: WHAT can you access?
- Accounting: WHEN did you do it? (and what exactly?)

### Five Authentication Factors: “KHAIL”

- **K**nowledge (something you know)
- **H**ave (something you have)
- **A**re (something you are)
- **I** do (something you do) - action
- **L**ocation (somewhere you are)

### Zero Trust

**“Never trust, always verify, enforce everywhere”**

-----

## Common Exam Scenarios

### Scenario 1: CIA Triad

**Question**: A hospital implements disk encryption on all servers storing patient records. Which principle of the CIA triad does this primarily support?

<details>
<summary>Answer</summary>

**Confidentiality**

Encryption protects data from unauthorized viewing, even if physical media is stolen. While encryption can contribute to integrity (some encryption schemes include integrity checking), the PRIMARY purpose in this scenario is confidentiality of patient data.

</details>

### Scenario 2: Authentication Factors

**Question**: A user logs in with username/password, then receives a code on their smartphone that they must enter. How many factors are being used?

<details>
<summary>Answer</summary>

**Two factors (MFA)**

1. Password = Something you know
1. Smartphone code = Something you have

This is proper multi-factor authentication because it uses two DIFFERENT types of factors.

</details>

### Scenario 3: Zero Trust

**Question**: A company allows remote workers to access internal resources without VPN, but requires device health checks, geolocation verification, and behavior analysis before granting access. What security model is this?

<details>
<summary>Answer</summary>

**Zero Trust**

Key indicators:

- No implicit trust (no automatic VPN trust)
- Continuous verification (device health, location, behavior)
- Context-based access decisions
- “Never trust, always verify” principle

</details>

-----

## CompTIA-Style Practice Questions

### Question 1

Which of the following BEST describes the difference between authentication and authorization?

A. Authentication verifies identity; authorization determines access rights  
B. Authorization verifies identity; authentication determines access rights  
C. Authentication is done first; authorization is optional  
D. Authorization requires MFA; authentication does not

<details>
<summary>Answer & Explanation</summary>

**Correct Answer: A**

**Explanation**:

- Authentication = Proving WHO you are (ID verification)
- Authorization = Determining WHAT you can do (permissions)

They happen in sequence: authenticate FIRST, then authorize.

**Why others are wrong**:

- B: Backwards
- C: Authorization is not optional in secure systems
- D: Either can use MFA; not a distinguishing factor

</details>

### Question 2

A financial services company implements a system that creates tamper-evident logs of all transactions with timestamps and digital signatures. Which security concept is primarily being addressed?

A. Confidentiality  
B. Availability  
C. Non-repudiation  
D. Authorization

<details>
<summary>Answer & Explanation</summary>

**Correct Answer: C. Non-repudiation**

**Explanation**: Digital signatures + timestamps = proof of action that cannot be denied. Key words: “tamper-evident” and “digital signatures” point to non-repudiation.

**Why others are wrong**:

- A: Not about keeping data secret
- B: Not about system uptime
- D: Not about determining access rights

</details>

### Question 3

An organization conducts an assessment comparing their current security controls against industry best practices and compliance requirements. What is this called?

A. Penetration test  
B. Gap analysis  
C. Risk assessment  
D. Vulnerability scan

<details>
<summary>Answer & Explanation</summary>

**Correct Answer: B. Gap analysis**

**Explanation**: Gap analysis specifically compares CURRENT state vs DESIRED state (best practices, compliance). Keywords: “comparing current” + “against requirements”

**Why others are wrong**:

- A: Penetration test = simulated attack
- C: Risk assessment = identifying and analyzing risks
- D: Vulnerability scan = identifying technical vulnerabilities

</details>

### Question 4

Which of the following is NOT a component of the Zero Trust control plane?

A. Policy engine  
B. Adaptive identity  
C. Policy enforcement point  
D. Threat scope reduction

<details>
<summary>Answer & Explanation</summary>

**Correct Answer: C. Policy enforcement point**

**Explanation**: PEP is part of the DATA PLANE (where enforcement happens), not the CONTROL PLANE (where decisions are made).

**Control Plane**: Policy engine, policy administrator, adaptive identity, threat scope reduction, secured zones
**Data Plane**: Subject/system, policy enforcement point

This is a common exam trap!

</details>

### Question 5 (Multi-select)

A company wants to implement MFA for all users. Which TWO of the following combinations would provide true multi-factor authentication? (Choose TWO)

A. Password + PIN  
B. Password + Fingerprint scan  
C. Smart card + PIN for the smart card  
D. Fingerprint + Iris scan  
E. Username + Password

<details>
<summary>Answer & Explanation</summary>

**Correct Answers: B and C**

**Explanation**:

- **B**: Password (knowledge) + Fingerprint (inherence) = 2 different factors ✓
- **C**: Smart card (possession) + PIN (knowledge) = 2 different factors ✓

**Why others are wrong**:

- A: Both are “something you know” (same factor)
- D: Both are “something you are” (same factor)
- E: Both are “something you know” (not even MFA, just authentication)

**Key Point**: Count the TYPES of factors, not the number of credentials!

</details>

-----

## Common Exam Traps

### Trap 1: Confusing Integrity and Confidentiality

❌ “Hashing prevents unauthorized access”  
✅ “Hashing detects unauthorized changes”

**Remember**:

- Confidentiality = Can’t SEE it (encryption)
- Integrity = Can’t CHANGE it (hashing)

### Trap 2: Multi-Factor Misconceptions

❌ “Using password + security question = MFA”  
✅ “Both are ‘something you know’ = single factor”

**Count factor TYPES, not number of items!**

### Trap 3: Authentication vs Authorization Order

❌ “Authorize first, then authenticate”  
✅ “Authenticate first, THEN authorize”

**You must prove WHO you are before determining WHAT you can do**

### Trap 4: Zero Trust = Zero Access

❌ “Zero Trust means no one gets access”  
✅ “Zero Trust means verify everyone, no implicit trust”

**It’s about VERIFICATION, not DENIAL**

-----

## Real-World Applications

### Confidentiality in Action

- Healthcare: Encrypting patient records (HIPAA)
- Finance: Protecting credit card numbers (PCI-DSS)
- Government: Classifying sensitive documents

### Integrity in Action

- Software: Code signing certificates
- Updates: Hash verification of downloaded files
- Blockchain: Immutable transaction records

### Availability in Action

- E-commerce: Load-balanced web servers
- Banking: Redundant data centers
- Emergency Services: Backup communication systems

### Zero Trust in Action

- Google’s BeyondCorp
- Microsoft’s Conditional Access
- Cloud access security brokers (CASB)

-----

## Related Objectives

- **1.1**: Security controls implement these concepts
- **1.4**: Cryptographic solutions enable confidentiality, integrity, non-repudiation
- **2.5**: Mitigation techniques protect CIA
- **3.1**: Architecture models implement Zero Trust
- **4.6**: IAM implements authentication, authorization, accounting
- **5.2**: Risk management addresses CIA threats

-----

## Key Takeaways for Exam Day

1. **CIA Triad is FUNDAMENTAL** - Most security measures map back to protecting C, I, or A
1. **AAA is a SEQUENCE** - Authentication → Authorization → Accounting (in that order)
1. **MFA requires DIFFERENT factors** - Two passwords ≠ MFA
1. **Zero Trust = Verify Everything** - Location doesn’t equal trust
1. **Non-repudiation = Cannot Deny** - Think legal proof and digital signatures
1. **Gap Analysis = Current vs Desired** - Identifies what’s missing

**Pro Tip**: When you see a scenario, ask yourself “Which part of CIA does this protect?” That often leads you to the right answer.

-----

**Status**: Ready for review ✓
