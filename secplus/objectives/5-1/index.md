---
layout: objective
title: "5.1 Governance Elements"
objective_id: "5.1"
domain: "5.0 Security Program Management and Oversight"
status: "done"
tags: ["governance", "frameworks", "standards", "regulations"]
permalink: /objectives/5-1/
---

## Overview

Governance elements provide structure and accountability for security programs. This includes policies, standards, procedures, regulations, and frameworks that guide security decision-making.

---

## Governance Structure

**Governance definition:** System of rules, practices, and processes directing and controlling security activities.

**Purpose:**
- Define authority and accountability
- Ensure compliance with laws/regulations
- Align security with business objectives
- Manage risk appropriately

**Governance components:**

**Board of Directors:**
- **Role:** Oversight of organizational risk
- **Responsibilities:** Approve policies, review risk reports, ensure compliance
- **Security involvement:** Receive CISO reports, approve major security investments

**Executive Management (C-suite):**
- **CEO:** Ultimate accountability for organizational security
- **CISO/CSO:** Security program leadership
- **CIO:** IT infrastructure and security
- **CFO:** Security budget approval
- **General Counsel:** Legal/regulatory compliance

**Security Steering Committee:**
- **Composition:** CISO, IT leaders, business unit heads, legal, HR
- **Purpose:** Strategic security decisions
- **Activities:** Review policies, prioritize initiatives, approve budgets
- **Frequency:** Quarterly meetings

**Security Operations:**
- **SOC (Security Operations Center):** 24/7 monitoring and response
- **Risk management team:** Assess and manage risks
- **Compliance team:** Ensure regulatory adherence
- **Security engineering:** Implement controls

---

## Regulations, Standards, and Legislation

**Regulations (legally binding):**

**General Data Protection Regulation (GDPR):**
- **Jurisdiction:** European Union
- **Scope:** Personal data of EU citizens
- **Requirements:**
  - Consent for data collection
  - Right to be forgotten (data deletion)
  - Data breach notification (72 hours)
  - Privacy by design
- **Penalties:** Up to 4% of annual revenue or €20M (whichever higher)

**Health Insurance Portability and Accountability Act (HIPAA):**
- **Jurisdiction:** United States
- **Scope:** Protected Health Information (PHI)
- **Requirements:**
  - Privacy Rule (who can access PHI)
  - Security Rule (safeguards for ePHI)
  - Breach Notification Rule (notify within 60 days)
- **Penalties:** $100-$50,000 per violation

**Payment Card Industry Data Security Standard (PCI DSS):**
- **Jurisdiction:** Global (card brand requirement, not law)
- **Scope:** Organizations handling credit card data
- **12 Requirements:**
  - Firewall configuration
  - No default passwords
  - Protect stored cardholder data
  - Encrypt transmission of cardholder data
  - Antivirus software
  - Secure systems and applications
  - Restrict access (need-to-know)
  - Unique IDs for access
  - Restrict physical access
  - Track and monitor access
  - Test security systems
  - Maintain security policy
- **Penalties:** Fines from card brands, loss of card processing ability

**Sarbanes-Oxley Act (SOX):**
- **Jurisdiction:** United States
- **Scope:** Publicly traded companies
- **Requirements:**
  - Financial reporting controls
  - IT general controls (access, change management)
  - Executive certification of financial statements
- **Penalties:** Criminal penalties for executives

**Gramm-Leach-Bliley Act (GLBA):**
- **Jurisdiction:** United States
- **Scope:** Financial institutions
- **Requirements:**
  - Privacy notice to customers
  - Safeguard customer information
  - Pretexting protection
- **Penalties:** Civil and criminal penalties

**Federal Information Security Management Act (FISMA):**
- **Jurisdiction:** United States federal agencies
- **Scope:** Government information systems
- **Requirements:**
  - Risk-based security programs
  - Annual FISMA audits
  - NIST framework compliance

**Standards (voluntary best practices):**

**ISO/IEC 27001:**
- **Purpose:** Information security management system (ISMS)
- **Scope:** International standard
- **Benefits:** Certification demonstrates security commitment
- **Requirements:** 114 controls across 14 domains

**ISO/IEC 27002:**
- **Purpose:** Code of practice for information security controls
- **Relationship to 27001:** Implementation guidance for 27001

**NIST Cybersecurity Framework (CSF):**
- **Purpose:** Voluntary framework for managing cybersecurity risk
- **Five Functions:**
  1. **Identify:** Asset management, risk assessment
  2. **Protect:** Access control, training, data security
  3. **Detect:** Monitoring, detection processes
  4. **Respond:** Incident response, communications
  5. **Recover:** Recovery planning, improvements
- **Tiers:** Partial (Tier 1) → Risk Informed (Tier 2) → Repeatable (Tier 3) → Adaptive (Tier 4)
- **Profiles:** Current state vs target state

**NIST SP 800-53:**
- **Purpose:** Security and privacy controls for federal systems
- **Scope:** Federal agencies (FISMA compliance)
- **Control families:** 20 families (e.g., Access Control, Incident Response)

**CIS Controls (Center for Internet Security):**
- **Purpose:** Prioritized set of cybersecurity best practices
- **20 Controls:** Organized by implementation groups (IG1, IG2, IG3)
- **Examples:**
  - Control 1: Inventory of assets
  - Control 2: Inventory of software
  - Control 3: Data protection
  - Control 4: Secure configuration
  - Control 5: Account management

**Industry-specific standards:**
- **NERC CIP:** North American Electric Reliability Corporation - Critical Infrastructure Protection (power grid)
- **HITRUST:** Health Information Trust Alliance (healthcare)
- **FedRAMP:** Federal Risk and Authorization Management Program (cloud services for government)

---

## National vs International Standards

**Key differences:**

**National (country-specific):**
- **Examples:** FISMA (US), PIPEDA (Canada), Data Protection Act (UK)
- **Enforcement:** National government
- **Scope:** Within country borders
- **Penalties:** National laws apply

**International (cross-border):**
- **Examples:** GDPR (EU but global impact), ISO 27001
- **Enforcement:** Various (GDPR enforced by EU member states)
- **Scope:** Multiple countries
- **Extraterritorial reach:** GDPR applies to any org processing EU citizen data

**Example scenario:**
```
US company with customers in EU:
- Must comply with: GDPR (international), SOX (US national if public), PCI DSS (international standard)
- Data storage: May need EU data centers (GDPR data residency)
- Privacy policy: Must meet GDPR requirements even though company is US-based
```

---

## Industry-Specific Considerations

**Healthcare:**
- **Regulations:** HIPAA (US), HITECH Act
- **Standards:** HITRUST
- **Focus:** Patient privacy, PHI protection
- **Penalties:** HIPAA violations up to $1.5M per year per violation

**Financial:**
- **Regulations:** GLBA (US), SOX (if public), PCI DSS
- **Standards:** ISO 27001, COBIT
- **Focus:** Financial data protection, fraud prevention
- **Penalties:** SOX criminal penalties for executives

**Government:**
- **Regulations:** FISMA (federal), CJIS (criminal justice)
- **Standards:** NIST SP 800-53, FedRAMP
- **Focus:** National security, classified information
- **Clearances:** Security clearances required

**Retail:**
- **Regulations:** PCI DSS (if accepting cards), state data breach laws
- **Standards:** ISO 27001
- **Focus:** Payment card data, customer PII
- **Penalties:** PCI fines, breach notification requirements

**Critical Infrastructure:**
- **Regulations:** NERC CIP (power), TSA (transportation), CFATS (chemical)
- **Standards:** NIST CSF, ICS-specific standards
- **Focus:** Operational technology (OT) security
- **Penalties:** Service disruption = national security risk

---

## Benchmarks and Secure Configuration Guides

**Purpose:** Establish baseline security configurations

**CIS Benchmarks:**
- **Coverage:** 100+ technology platforms
- **Examples:**
  - CIS Microsoft Windows 10 Benchmark
  - CIS Ubuntu Linux Benchmark
  - CIS Cisco IOS Benchmark
  - CIS AWS Foundations Benchmark
- **Levels:**
  - **Level 1:** Basic security (minimal business impact)
  - **Level 2:** Defense in depth (may impact functionality)

**DISA STIGs (Security Technical Implementation Guides):**
- **Purpose:** US Department of Defense security standards
- **Scope:** Military and federal contractors
- **Coverage:** Operating systems, applications, network devices
- **Compliance:** Required for DoD systems

**Vendor hardening guides:**
- Microsoft Security Baselines
- Red Hat Security Guide
- Cisco Security Configuration Guide
- AWS Security Best Practices

**Implementation process:**
1. Select appropriate benchmark (CIS, DISA STIG)
2. Test in non-production environment
3. Document deviations (with business justification)
4. Apply to production with change control
5. Audit compliance regularly
6. Update when new benchmark versions released

---

## Key Distinctions

**Regulation vs Standard:**
- Regulation: Legally binding (GDPR, HIPAA)
- Standard: Voluntary best practice (ISO 27001, NIST CSF)

**GDPR vs HIPAA:**
- GDPR: EU personal data (all types)
- HIPAA: US health information only

**ISO 27001 vs ISO 27002:**
- 27001: Certifiable ISMS framework
- 27002: Implementation guidance (not certifiable)

**NIST CSF vs NIST 800-53:**
- CSF: High-level framework (5 functions)
- 800-53: Detailed controls (federal systems)

**National vs International:**
- National: Single country jurisdiction
- International: Cross-border or global scope

---

## Common Exam Traps

1. **Trap:** Thinking all standards are legally required
   - **Reality:** ISO 27001, NIST CSF are voluntary (regulations are mandatory)

2. **Trap:** Believing GDPR only applies to EU companies
   - **Reality:** Applies to ANY organization processing EU citizen data

3. **Trap:** Assuming PCI DSS is a law
   - **Reality:** Card brand requirement (not government regulation)

4. **Trap:** Thinking benchmarks must be followed exactly
   - **Reality:** Can deviate with business justification (document deviations)

5. **Trap:** Believing one framework fits all industries
   - **Reality:** Industry-specific considerations (healthcare ≠ finance ≠ government)

---

## Exam Tips

1. **GDPR = EU personal data** (72-hour breach notification)
2. **HIPAA = US healthcare** (PHI protection)
3. **PCI DSS = payment cards** (12 requirements, not a law)
4. **SOX = financial reporting** (US public companies)
5. **ISO 27001 = certifiable** ISMS (27002 = guidance)
6. **NIST CSF = 5 functions** (Identify, Protect, Detect, Respond, Recover)
7. **CIS Benchmarks = configuration** standards (Level 1 & 2)
8. **DISA STIGs = DoD** security standards
9. **Regulations are mandatory**, standards are voluntary
10. **GDPR has extraterritorial reach** (applies globally if EU data involved)

---

## Quick Navigation
- [→ Next: 5.2 Risk Management](../5-2/)
- [↑ Back to Domain 5](../)
- [⌂ Home](/)
