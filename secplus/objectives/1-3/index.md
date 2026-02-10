---
layout: default
title: "Security+ 1.3 — Explain the importance of change management processes and the impact to security."
objective_id: "1.3"
domain: "1.0 General Security Concepts"
status: "done"
tags:
  - secplus701
permalink: /secplus/objectives/1-3/
---

# Security+ 1.3 — Explain the importance of change management processes and the impact to security.

Status: <span class="status-badge done">done</span>

## Exam objective
Explain the importance of change management processes and the impact to security.

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

### What is Change Management?

**Definition**: Systematic approach to handling organizational changes to implement them smoothly and successfully with minimal disruption.

**Goal**: Control changes to IT systems while maintaining security and minimizing risk.

**Why It Matters for Security**:
- Uncontrolled changes = #1 cause of security incidents
- Configuration errors introduce vulnerabilities
- Unauthorized changes bypass security controls
- Poor planning causes downtime and availability issues

---

### Business Processes Impacting Security Operations

#### 1. Approval Process

**Definition**: Formal authorization required before implementing changes

**Key Principle**: NEVER make changes without approval

**Approval Workflow**:
```
Change Request → Impact Analysis → CAB Review → Approval/Denial → Implementation
```

##### Change Advisory Board (CAB)
- **Who**: Cross-functional team (IT, Security, Business)
- **Role**: Reviews and approves/denies change requests
- **Considerations**:
  - Security implications
  - Business impact
  - Resource requirements
  - Risk assessment
  - Dependencies

##### Levels of Approval
- **Standard Changes**: Pre-approved (low risk, routine)
  - Example: Monthly Windows patches
  - May not need CAB review
- **Normal Changes**: Require CAB approval
  - Example: Firewall rule changes
- **Emergency Changes**: Expedited approval
  - Example: Zero-day patch deployment
  - Still requires approval, just faster

**Exam Tip**: "Approval process" questions — CAB is almost always involved for normal changes

---

#### 2. Ownership

**Definition**: Clear assignment of WHO is responsible for the change

##### Change Owner/Initiator
- Requests the change
- Provides business justification
- Example: Database admin requesting schema update

##### Change Implementer
- Actually performs the change
- May be same as owner or different
- Example: System admin applying the update

##### System/Asset Owner
- Owns the affected system
- Must approve changes to their systems
- Ultimate accountability for the system

**Why Ownership Matters**:
- Ensures accountability
- Clear escalation path
- Someone to contact if issues arise
- Prevents "orphaned" changes

**Exam Scenario**: "Who should approve a firewall change?" — System owner (firewall admin) + Security team

---

#### 3. Stakeholders

**Definition**: Anyone affected by or who can affect the change

**Common Stakeholders**:
- **IT Operations**: System uptime, performance
- **Security Team**: Security posture, compliance
- **Business Units**: Service availability, functionality
- **End Users**: Access to systems, user experience
- **Compliance/Legal**: Regulatory requirements
- **Management**: Budget, strategic alignment

**Stakeholder Involvement**:
- **Identification**: Who needs to be informed/consulted?
- **Communication**: Keep stakeholders updated
- **Approval**: Some stakeholders may have veto power
- **Feedback**: Input on timing, approach, concerns

**Exam Tip**: Questions about "who should be involved" — Think broader than just IT!

---

#### 4. Impact Analysis

**Definition**: Assessing potential effects of a change before implementation

##### Security Impact
- Does this introduce vulnerabilities?
- Does it weaken existing controls?
- Compliance implications?
- Example: Disabling MFA temporarily

##### Business Impact
- Affected systems/services
- Number of users impacted
- Revenue impact if change fails
- Example: Updating payment gateway

##### Technical Impact
- System dependencies
- Integration points
- Performance changes
- Resource requirements

##### Risk Analysis
- Probability of failure
- Severity if it fails
- Mitigation strategies

**Impact Assessment Questions**:
1. What could go wrong?
2. How likely is failure?
3. How bad would failure be?
4. Can we recover quickly?
5. Do benefits outweigh risks?

**Exam Keyword**: "Impact analysis" = Assessing consequences BEFORE implementing

---

#### 5. Test Results

**Definition**: Evidence that change works as expected in test environment

##### Pre-Implementation Testing
- **Unit Testing**: Individual component works
- **Integration Testing**: Works with other systems
- **Security Testing**: No new vulnerabilities introduced
- **Performance Testing**: Acceptable performance
- **User Acceptance Testing (UAT)**: End users approve

##### Test Environment
- Should mirror production
- Isolated from production
- Validates change before going live

**Documentation Required**:
- Test plan
- Test results
- Issues found and resolved
- Sign-off from testers

**Exam Trap**: Changes should NEVER go to production without testing first!

---

#### 6. Backout Plan

**Also called**: Rollback plan, remediation plan

**Definition**: Procedure to reverse a change if it causes problems

**Why Critical**:
- Changes can and do fail
- Need quick recovery
- Minimize downtime
- Restore security posture

##### Rollback Procedure
1. Trigger criteria (when to roll back)
2. Step-by-step reversal process
3. Who performs rollback
4. Time required to roll back

##### Backups
- Configuration backups BEFORE change
- Data backups
- System state snapshots
- Version control

##### Recovery Point
- Known-good configuration
- Last stable state
- Recovery Time Objective (RTO)

**Exam Scenario**: "Change causes system crash. What should be done first?" — Execute backout plan to restore service

**Best Practice**: Test the backout plan too!

---

#### 7. Maintenance Window

**Definition**: Scheduled time period when changes can be made with minimal business impact

**Purpose**:
- Minimize user disruption
- Planned downtime vs unplanned
- Coordinate multiple changes
- Allow time for proper testing

##### Timing
- Off-peak hours (nights, weekends)
- Consider time zones (global operations)
- Avoid critical business periods
- Example: Don't patch e-commerce site on Black Friday!

##### Duration
- Estimated time to complete
- Buffer for issues
- Time to roll back if needed

##### Communication
- Notify users in advance
- During the change
- Confirmation when complete

**Types**:
- **Planned Maintenance**: Scheduled in advance
- **Emergency Maintenance**: Unscheduled (security patches)

**Exam Tip**: "When should changes be made?" — During maintenance windows!

---

#### 8. Standard Operating Procedure (SOP)

**Definition**: Documented step-by-step instructions for implementing changes

**Purpose**:
- Consistency across changes
- Reduces human error
- Training tool for new staff
- Ensures security controls maintained

**SOP Contents**:
- Prerequisite conditions
- Required tools and permissions
- Step-by-step instructions
- Verification steps
- Rollback procedures
- Documentation requirements

**Examples of Change SOPs**:
- Patch management procedures
- Firewall rule change process
- User account provisioning
- System hardening procedures

---

### Technical Implications

#### 1. Allow Lists / Deny Lists

**Impact**: Changes can affect what's permitted/blocked

##### Allow Lists (Whitelists)
- **Definition**: Only explicitly permitted items allowed
- **Security Stance**: Default deny (more secure)
- **Change Impact**:
  - Adding to allow list = new access granted
  - Removing from allow list = access removed
  - Example: Application whitelist update

##### Deny Lists (Blacklists)
- **Definition**: Explicitly blocked items, everything else allowed
- **Security Stance**: Default allow (less secure)
- **Change Impact**:
  - Adding to deny list = blocking something
  - Removing from deny list = unblocking
  - Example: Firewall block list update

**Change Management Considerations**:
- Document ALL allow/deny list changes
- Test before production
- Understand security implications
- Review regularly for accuracy

**Exam Scenario**: "Adding IP to firewall allow list" — Changes who can access (security impact!)

---

#### 2. Restricted Activities

**Definition**: Actions that are limited or prohibited during certain times

**Why Restrict**:
- Critical business operations
- High-risk periods
- Compliance requirements
- Change freeze periods

##### Change Freeze
- No changes during critical periods
- Example: Financial quarter-end, tax season
- Exception: Security emergencies

##### Restricted Times
- Business hours (no production changes)
- Peak usage times
- Blackout dates

##### Approval Escalation
- Some changes require higher authority
- Executive approval for high-risk changes

**Exam Keyword**: "Change freeze" = Absolutely NO changes during this period

---

#### 3. Downtime

**Definition**: Period when system is unavailable due to change

**Types**:

##### Planned Downtime
- Scheduled maintenance
- Communicated in advance
- During maintenance window
- Example: Server upgrade

##### Unplanned Downtime
- Unexpected outages
- Failed changes
- Emergency repairs
- Example: Change causes system crash

**Minimizing Downtime**:
- Thorough testing
- Good backout plan
- Blue-green deployments
- Rolling updates
- Redundant systems

**SLA Considerations**:
- Service Level Agreement limits
- Downtime allowances
- Compensation for excess downtime

**Exam Tip**: Changes SHOULD be planned for maintenance windows to minimize downtime

---

#### 4. Service/Application Restart

**What It Is**: Stopping and starting services as part of change

**Why Required**:
- Apply configuration changes
- Load new code
- Clear memory/caches
- Reload security policies

##### Restart Sequence
- Dependencies matter!
- Database → App Server → Web Server
- Wrong order = outages

##### Service State
- Validate service starts correctly
- Check logs for errors
- Verify connectivity

##### User Impact
- Disconnects active sessions
- Data loss if not saved
- Notify users before restart

**Best Practices**:
- Document restart procedures
- Automate where possible
- Monitor during restart
- Verify all services online

**Exam Scenario**: "After firewall config change..." — Typically requires restart to apply!

---

#### 5. Legacy Applications

**Definition**: Older applications still in use but outdated

##### Can't Be Changed
- Vendor no longer supports
- No source code available
- Critical but fragile
- Example: 20-year-old billing system

##### Can't Be Patched
- Updates break functionality
- Not compatible with modern OS
- Security vulnerabilities remain

##### Security Implications
- Known vulnerabilities
- Can't apply security updates
- Potential compliance issues

**Change Management for Legacy Apps**:

**Workarounds**:
- Network segmentation (isolate)
- Compensating controls
- Enhanced monitoring
- Stricter access controls

**Testing**:
- Extra testing required
- Might break unexpectedly
- Maintain test environment

**Exam Scenario**: "Can't patch legacy system..." — Use compensating controls (network segmentation, monitoring)

---

#### 6. Dependencies

**Definition**: Systems, applications, or services that rely on each other

**Why Critical for Change Management**:
- Change one thing — breaks another
- Cascading failures
- Unexpected impacts

##### Technical Dependencies
- Database ← Application ← Web Server
- Authentication ← All services
- Network ← Everything

##### Operational Dependencies
- Backup system ← Production data
- Monitoring ← Agents on servers
- Patch management ← System access

**Dependency Mapping**:
- Document all dependencies
- Understand upstream/downstream impacts
- Test dependent systems after changes

**Change Impact on Dependencies**:
```
Change database schema
  ↓
Application queries fail
  ↓
Web portal down
  ↓
Users can't log in
```

**Exam Tip**: Always consider dependencies in impact analysis!

---

### Documentation

#### 1. Updating Diagrams

**Why Important**: Visual representations must match reality

**Types of Diagrams to Update**:

##### Network Diagrams
- Topology changes
- New devices added
- IP address changes
- VLAN modifications

##### Data Flow Diagrams
- How data moves through systems
- Integration points
- Security boundaries

##### Architecture Diagrams
- System components
- Relationships
- Security zones

**When to Update**:
- IMMEDIATELY after change
- Before change (planned state)
- Never let diagrams become outdated

**Consequences of Outdated Diagrams**:
- Incorrect troubleshooting
- Security gaps unnoticed
- Failed audits
- Longer incident response

---

#### 2. Updating Policies/Procedures

##### Security Policies
- If change affects security posture
- New controls implemented
- Removed controls

##### Procedures
- SOPs for new configurations
- Updated troubleshooting steps
- Modified workflows

##### Configuration Standards
- Hardening guides
- Baseline configurations
- Security settings

**Documentation Requirements**:
- What changed
- Why it changed
- When it changed
- Who approved it

**Exam Scenario**: "After implementing new firewall..." — Update firewall management procedures and network diagram!

---

#### 3. Version Control

**Definition**: Tracking changes to configurations and code over time

##### Configuration Files
- Network device configs (routers, switches, firewalls)
- Server configurations
- Application settings
- Security policies

##### Code and Scripts
- Automation scripts
- Custom applications
- Infrastructure as Code (IaC)

**Version Control Benefits**:
- Track who changed what and when
- Rollback to previous versions
- Audit trail for compliance
- Compare versions (diff)
- Prevent configuration drift

**Version Control Systems**:
- Git (code and configurations)
- Network Configuration Management tools
- Change tracking databases

**Best Practices**:
- Meaningful commit messages
- Regular commits
- Tag important versions (production releases)
- Never delete version history

**Exam Tip**: Version control provides audit trail and enables quick rollback

---

### Change Management Workflow

**Complete Process**:

```
1. IDENTIFY NEED FOR CHANGE
   ↓
2. CREATE CHANGE REQUEST
   - Document what, why, who, when
   - Include stakeholders
   ↓
3. CONDUCT IMPACT ANALYSIS
   - Security, business, technical impacts
   - Risk assessment
   ↓
4. DEVELOP IMPLEMENTATION PLAN
   - Step-by-step procedure
   - Resource requirements
   - Timeline
   ↓
5. CREATE BACKOUT PLAN
   - Rollback procedures
   - Recovery steps
   ↓
6. CAB REVIEW & APPROVAL
   - Present to Change Advisory Board
   - Answer questions
   - Get approval
   ↓
7. SCHEDULE MAINTENANCE WINDOW
   - Coordinate timing
   - Notify stakeholders
   ↓
8. TEST IN NON-PRODUCTION
   - Validate change works
   - Document test results
   ↓
9. IMPLEMENT CHANGE
   - Follow SOP
   - Monitor during implementation
   ↓
10. VERIFY & TEST
    - Confirm change successful
    - Test dependent systems
    ↓
11. UPDATE DOCUMENTATION
    - Diagrams, policies, procedures
    - Version control
    - Close change request
    ↓
12. POST-IMPLEMENTATION REVIEW
    - Lessons learned
    - Document any issues
    - Update procedures if needed
```

---

### Common Change Management Failures

**Failure: Skipping Approval**
- "Emergency, no time for CAB"
- Reality: Emergency changes still need approval (just expedited)
- Result: Unauthorized change, security incident, compliance violation

**Failure: No Testing**
- "It's a small change, won't cause issues"
- Reality: Small changes can have big impacts
- Result: Production outage, data loss

**Failure: No Backout Plan**
- "This will definitely work"
- Reality: Changes fail, need recovery plan
- Result: Extended downtime, panic

**Failure: Poor Communication**
- Not notifying stakeholders
- Reality: People need to know
- Result: Angry users, business disruption

**Failure: Ignoring Dependencies**
- "This only affects one system"
- Reality: Everything is connected
- Result: Cascading failures

**Failure: Outdated Documentation**
- "I'll update it later"
- Reality: Later never comes
- Result: Knowledge loss, troubleshooting delays

---

### Memory Aids

#### Change Management Steps: "I-CREATE-VERIFY"
- **I**dentify need
- **C**reate request
- **R**eview (CAB approval)
- **E**valuate impact
- **A**rrange maintenance window
- **T**est first
- **E**xecute change
- **V**erify success
- **E**nsure documentation updated
- **R**eview lessons learned
- **I**mprove process
- **F**inalize closure
- **Y**ield results to stakeholders

#### Critical Change Documents: "BAT PITs"
- **B**ackout plan
- **A**pproval
- **T**est results
- **P**lan (implementation)
- **I**mpact analysis
- **T**imeline (maintenance window)
- **S**OP (procedure)

#### Technical Impacts: "DARLA"
- **D**owntime
- **A**llow/deny lists
- **R**estricted activities
- **L**egacy apps
- **A**pp/service restarts

---

### Common Exam Traps

**Trap 1: "Emergency = No Approval Needed"**
- WRONG: "It's an emergency, just make the change!"
- RIGHT: Emergency changes still need approval, just expedited

**Trap 2: "Small Change = No Testing"**
- WRONG: "It's just one line of config, doesn't need testing"
- RIGHT: ALL changes need testing, size doesn't matter

**Trap 3: "Update Docs Later"**
- WRONG: "I'll update the diagram next week"
- RIGHT: Update documentation IMMEDIATELY after change

**Trap 4: "Backout Plan = Nice to Have"**
- WRONG: "If it fails, we'll figure it out"
- RIGHT: Backout plan is MANDATORY before approval

**Trap 5: Legacy Apps Can't Be Secured**
- WRONG: "Can't patch it, nothing we can do"
- RIGHT: Use compensating controls (segmentation, monitoring)

---

### Exam tips

1. **Change management is about CONTROL** — Preventing unauthorized, untested, or poorly planned changes
2. **CAB approves, change owner implements** — Know the roles
3. **Testing is NOT optional** — All changes must be tested first
4. **Backout plan is mandatory** — Must exist before approval
5. **Documentation must be updated immediately** — Not "later"
6. **Maintenance windows minimize impact** — Schedule changes appropriately
7. **Legacy apps need compensating controls** — Can't patch does not equal can't secure
8. **Dependencies matter** — One change can break multiple systems
9. **Emergency changes still need approval** — Just expedited process
10. **Version control provides audit trail** — Track all configuration changes

**Pro Tip**: When you see "change management" in a question, think about the PROCESS and APPROVAL, not just the technical change itself.

---

## Key terms

- **Change Management** — Systematic approach to handling organizational changes to implement them smoothly with minimal disruption.
- **Change Advisory Board (CAB)** — Cross-functional team that reviews and approves/denies change requests based on risk and impact.
- **Approval Process** — Formal authorization required before implementing changes, involving CAB review for normal changes.
- **Ownership** — Clear assignment of who is responsible for requesting, implementing, and being accountable for a change.
- **Stakeholders** — Anyone affected by or who can affect the change, including IT, security, business units, and end users.
- **Impact Analysis** — Assessment of potential security, business, and technical effects of a change before implementation.
- **Test Results** — Evidence that a change works as expected in a non-production test environment before going live.
- **Backout Plan** — Procedure to reverse a change if it causes problems; also called rollback plan or remediation plan.
- **Maintenance Window** — Scheduled time period when changes can be made with minimal business impact, typically off-peak hours.
- **Standard Operating Procedure (SOP)** — Documented step-by-step instructions for implementing changes consistently.
- **Allow List** — List of explicitly permitted items; uses default deny stance (more secure).
- **Deny List** — List of explicitly blocked items; uses default allow stance (less secure).
- **Restricted Activities** — Actions that are limited or prohibited during certain times, such as change freeze periods.
- **Downtime** — Period when a system is unavailable, either planned (maintenance) or unplanned (failed change).
- **Legacy Application** — Older application still in use but outdated, often requiring compensating controls because it cannot be patched.
- **Dependencies** — Systems, applications, or services that rely on each other, where changing one can break another.
- **Version Control** — Tracking changes to configurations and code over time, providing audit trail and rollback capability.
- **Change Freeze** — Period during which no changes are allowed, typically during critical business operations.

---

## Examples / scenarios

**Scenario 1:** A database administrator wants to apply a critical security patch to the production database server immediately. The patch was just released. What should be the FIRST step?

<details>
<summary>Answer</summary>

**Correct Answer**: Test the patch in a non-production environment

**Explanation**: Even for critical security patches, the change management process must be followed:
1. Test in development/staging first
2. Verify no adverse effects
3. Create change request with test results
4. Get approval (expedited for emergency)
5. Schedule implementation
6. Apply in production

Skipping testing risks breaking the production database, which could be worse than the vulnerability the patch fixes!

**NOT skipping approval** — Emergency changes still need approval, just expedited through CAB.
</details>

**Scenario 2:** During a change implementation, the new firewall rules cause the company's VPN to stop working. What should the security team do NEXT?

<details>
<summary>Answer</summary>

**Correct Answer**: Execute the backout plan to restore the previous firewall configuration

**Explanation**: When a change causes problems:
1. **FIRST**: Execute backout plan — Restore service
2. **THEN**: Investigate what went wrong
3. **FINALLY**: Fix the issue and try again later

Restoring service is the priority. The backout plan should have been prepared before the change, allowing quick recovery.

**Why not troubleshoot first?** Because users are down NOW. Restore service first, debug later.
</details>

**Scenario 3:** A company wants to update a legacy billing application that hasn't been updated in 10 years. The vendor no longer supports it. What compensating controls should be considered?

<details>
<summary>Answer</summary>

**Correct Answer**: Network segmentation, enhanced monitoring, strict access controls

**Explanation**: For legacy applications that can't be patched:

**Compensating Controls**:
- **Network Segmentation**: Isolate in separate VLAN
- **Enhanced Monitoring**: Watch for suspicious activity
- **Strict Access Controls**: Limit who can access
- **Firewall Rules**: Restrict network traffic
- **Data Encryption**: Protect data at rest
- **Regular Backups**: Ensure recovery capability

These controls reduce risk when primary controls (patching) aren't possible.

This is a classic compensating control scenario!
</details>

---

## Mini quiz

<details>
<summary><strong>Question 1:</strong> Which of the following BEST describes the purpose of a Change Advisory Board (CAB)?</summary>

**Answer: To review and approve/deny change requests based on risk and impact**

The CAB's primary function is governance — they review change requests, assess risks and impacts, and make approval decisions. They don't implement changes (that's the change implementer's job), create backout plans (change owner does this), or update documentation (various roles do this).
</details>

<details>
<summary><strong>Question 2:</strong> What TWO things should be completed BEFORE a firewall rule change is approved? (Impact analysis and backout plan)</summary>

**Answer: Impact analysis and backout plan**

BEFORE approval, you need:
- **Impact analysis**: Understand what could go wrong
- **Backout plan**: How to recover if it fails
- **Test results**: Proof it works (also before approval)

AFTER approval: Stakeholder notification, implementation, documentation updates, post-implementation review.
</details>

<details>
<summary><strong>Question 3:</strong> A company implements a new application firewall rule but forgets to update the network diagram. Three months later, this causes a failed audit. Which change management component was neglected?</summary>

**Answer: Documentation**

The network diagram is documentation that must be updated when changes are made. Failing to update it violates the documentation requirement of change management. Best Practice: Update documentation IMMEDIATELY after change, not "later."
</details>

<details>
<summary><strong>Question 4:</strong> Which of the following is the MAIN reason for testing changes in a non-production environment first?</summary>

**Answer: To identify and fix issues before affecting production**

The PRIMARY purpose of testing is to find problems in a safe environment where they won't impact users or business operations. If the change breaks something, it's better to discover it in test/dev than in production!
</details>

<details>
<summary><strong>Question 5:</strong> A legacy medical records system cannot be patched because updates break critical functionality. What should the security team do?</summary>

**Answer: Implement compensating controls such as network segmentation**

When primary controls (patching) can't be used, implement compensating controls: network segmentation (isolate), enhanced monitoring, strict access controls, dedicated firewall rules. Breaking critical functionality or decommissioning may not be feasible.
</details>

### CompTIA-style practice questions

<details>
<summary><strong>Question 6:</strong> A security engineer is planning to update firewall rules during a maintenance window. Which of the following should be completed BEFORE the change is approved? (Choose TWO)<br>A. Post-implementation review<br>B. Impact analysis<br>C. Backout plan<br>D. Documentation updates<br>E. Stakeholder notification</summary>

**Correct Answers: B. Impact analysis and C. Backout plan**

BEFORE approval, you need:
- **Impact analysis**: Understand what could go wrong
- **Backout plan**: How to recover if it fails

AFTER approval:
- Stakeholder notification (before implementation)
- Implementation
- Documentation updates
- Post-implementation review

**Timeline matters in change management questions!**
</details>

<details>
<summary><strong>Question 7:</strong> Which of the following BEST describes the purpose of a maintenance window?<br>A. To prevent all system changes indefinitely<br>B. To schedule changes during a period of minimal business impact<br>C. To test changes in a production environment<br>D. To eliminate the need for a backout plan</summary>

**Correct Answer: B. To schedule changes during a period of minimal business impact**

Maintenance windows are scheduled time periods for implementing changes with minimal disruption. They don't replace testing or backout plans.
</details>

<details>
<summary><strong>Question 8:</strong> A legacy medical records system cannot be patched because updates break critical functionality. The system is required for regulatory compliance. What should the security team do?<br>A. Patch the system anyway and fix the functionality later<br>B. Decommission the system and migrate to a new platform<br>C. Implement compensating controls such as network segmentation<br>D. Request an exception from the regulatory body</summary>

**Correct Answer: C. Implement compensating controls such as network segmentation**

When primary controls (patching) can't be used, implement compensating controls:
- Network segmentation (isolate)
- Enhanced monitoring
- Strict access controls
- Dedicated firewall rules

**Why not the others?**
- A: Breaking critical functionality is not acceptable
- B: May not be feasible (time, cost, complexity)
- D: Regulatory exceptions are rare and don't fix security issues
</details>

---

## Related objectives

- [**1.1**]({{ '/secplus/objectives/1-1/' | relative_url }}) — Change management implements security controls
- [**1.2**]({{ '/secplus/objectives/1-2/' | relative_url }}) — Changes must maintain CIA triad
- [**2.5**]({{ '/secplus/objectives/2-5/' | relative_url }}) — Changes are mitigation techniques
- [**4.1**]({{ '/secplus/objectives/4-1/' | relative_url }}) — Configuration management relates to change management
- [**4.2**]({{ '/secplus/objectives/4-2/' | relative_url }}) — Asset management tracks what changes affect
- [**4.8**]({{ '/secplus/objectives/4-8/' | relative_url }}) — Incident response may require emergency changes
- [**5.1**]({{ '/secplus/objectives/5-1/' | relative_url }}) — Governance frameworks include change management
- [**5.4**]({{ '/secplus/objectives/5-4/' | relative_url }}) — Compliance requires documented change processes

---

## Navigation

**Domain 1: General Security Concepts**

| Objective | Title | Status |
|---|---|---|
| [1.1]({{ '/secplus/objectives/1-1/' | relative_url }}) | Compare and contrast various types of security controls | done |
| [1.2]({{ '/secplus/objectives/1-2/' | relative_url }}) | Summarize fundamental security concepts | done |
| **1.3** | Explain the importance of change management processes (current) | done |
| [1.4]({{ '/secplus/objectives/1-4/' | relative_url }}) | Explain the importance of using appropriate cryptographic solutions | done |

[← Previous: Objective 1.2]({{ '/secplus/objectives/1-2/' | relative_url }}) | [Back to Dashboard]({{ '/secplus/' | relative_url }}) | [Next: Objective 1.4 →]({{ '/secplus/objectives/1-4/' | relative_url }})
