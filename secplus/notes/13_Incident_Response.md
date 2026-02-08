# Incident Response

-----

Incident Response
Objective 4.8: Explain appropriate incident response activities

## Incident Response

- Incident Response
  - Systematic approach to managing and mitigating security incidents
  - Goals

## Minimize impact

## Reduce detection and containment time

## Facilitate recovery

- Key Steps

## Detection

## Classification

## Containment

## Eradication

## Evidence preservation

## Communication

## Lessons learned

- Study Topics
  - Incident Response Process

## Steps

- Preparation
- Detection
- Analysis
- Containment
- Eradication
- Recovery
- Lessons Learned
  - Threat Hunting

## Proactive cybersecurity approach for continuous threat identification

## Purpose

- Identify hidden or emerging threats
  - Root Cause Analysis

## Systematic process to investigate incidents and identify underlying factors

## Purpose

- Understand the cause of security breaches or operational issues
  - Incident Response Training and Testing

## Methods

- Tabletop Exercises
- Simulations
- Drills
- Live Exercises

## Purpose

- Prepare personnel and systems for effective incident response
  - Digital Forensic Procedures

## Systematic techniques to gather, analyze, and preserve digital evidence

## Purpose

- Investigate cybercrimes or security incidents
  - Data Collection Procedures

## Established methods for gathering relevant information during incident

response

## Concept

- Order of volatility (prioritizing data collection based on volatility)
  - Disk Imaging and Analysis

## Creating a bit-by-bit copy (image) of a storage device, examining content

## Purpose

- Recover data
- Investigate incidents
- Identify security issues

## Incident Response Process

- Incident
  - An act violating a security policy
- Phases of Incident Response
  - NIST (National Institute for Standards and Technology) defines a four-phase
    incident response process

## Preparation

## Detection and Analysis

## Containment, Eradication and Recovery

## Post-Incident Activity

- In the CompTIA model, “Detection and Analysis” is divided into two phases, and
  “Containment, Eradication, and Recovery” is divided into three, creating a
  seven-phase model
- Seven Phases of Incident Response
  - Preparation

## Gets an organization ready for future incidents

## Focuses on making systems resilient to attacks by hardening systems and

networks

## Involves creating policies, procedures, and a communication plan

- Detection

## Determines if a security incident has occurred

## Identifies a security incident

## Cybersecurity and triage analysts play a vital role in assessing incident

severity

- Analysis

## Thoroughly examines and evaluates the incident

## Provides insights into the incident’s scope and impact

## Notifies stakeholders and initiates containment

- Containment

## Limits the incident’s scope by securing data and minimizing business

impact

## Prevents the spread of malicious activity

- Eradication

## Starts after containment

## Focuses on removing malicious activity from systems or networks

## May involve reimaging affected systems

- Recovery

## Restores affected systems and services to their secure state

## Includes restoring from backups, patching, and updating configurations

## Ensures resilience against future threats

- Post-Incident Activity

## Occurs after containment, eradication, and recovery

## Identifies the initial incident source and improvements to prevent future

incidents

## Involves

- Root cause analysis
  - Identifies the incident’s source and how to prevent it in the
    future
  - Steps

## Define/scope the incident

## Determine the causal relationships that led to the

incident

## Identify an effective solution

## Implement and track the solutions

- Lessons learned
  - Documents experiences during incidents in a forma
- After-action report
  - Collects formalized information about what occurred
- Incident Response Team
  - The core team includes cybersecurity professionals with incident response
    experience

## Temporary members may be added as needed (e.g., database

administrators)

- Large organizations have full-time incident response teams

## Smaller organizations form temporary teams for specific incidents

- Team Roles

## Leader

## Subject Matter Experts

## IT Support

## Legal Counsel

## HR

## Public Relations

- Leadership and management ensure the incident response team has necessary
  funding, resources ,and expertise
- Management makes crucial decisions and communicates them during the
  incident response
- Outsourcing Incident Response
  - Some organizations outsource incident response to specialized teams
  - Effective but expensive; external teams may not be familiar with the
    organization’s network

## Threat Hunting

- Threat Hunting
  - Proactive cybersecurity technique to detect threats that haven’t been discovered
    by normal security monitoring
  - Involves actively seeking out potential threats within your network, as opposed
    to waiting for them to trigger alerts
- Steps in Threat Hunting
  - Establishing a Hypothesis

## Conduct threat modeling to identify potential threats with high impact

## Use threat intelligence to form hypotheses about threat actors or

campaigns that may target your organization

- Profiling Threat Actors and Activities

## Create scenarios to understand how attackers might attempt an intrusion

## Determine the type of threat actor (insider, hacktivist, criminal, nation

state)

## Identify their objectives and potential targets

- Threat Hunting Process

## Utilizes security monitoring and incident response tools

## Analyzes logs, system data, file systems, and registry information

## Focuses on finding threats not detected by existing rules

## Start by assuming that the current rules haven’t flagged potential threats

## Seeks new tactics, techniques, and procedures used by threat actors

- Key Considerations
  - Threat hunters must stay updated on the latest attacks and threats
  - Use advisories and bulletins published by vendors and researchers to identify
    new TTPs and vulnerabilities
  - Utilize intelligence fusion and threat data, combining SIEM logs with real-world
    threat feeds
- Benefits of Threat Hunting
  - Improves detection capabilities by identifying threats that bypass existing
    defenses
  - Enhances threat intelligence by correlating external threat feeds with internal
    logs
  - Provides actionable intelligence to strengthen security measures

## Root Cause Analysis

- Root Cause Analysis (RCA)
  - Systematic process to identify the initial source of an incident and prevent it from
    recurring
- Steps in Root Cause Analysis
  - Define and Scope the Incident

## Determine the initial cause and scope of the incident

## Understand how many systems/users have been affected and the

operational impact

- Determine Causal Relationships

## Identify the causal relationships that led to the incident

## Understand how the incident occurred, such as through malware

infection via USB drive or other vectors

- Identify Effective Solutions

## Find solutions to prevent the incident from recurring

## Solutions may include adding antivirus, restricting data transfer from USB

devices, or applying software patches

- Implement and Track Solutions

## Execute the solutions and ensure the incident is fully resolved

## Use change management processes to update systems and configurations

## Look across the network and see if there are any other machines that

could have been affected

- Benefits of Root Cause Analysis
  - Identifies vulnerabilities and weaknesses in security practices
  - Creates more robust protections against cyber threats
  - Encourages a no-blame culture, focusing on solutions and improvements rather
    than assigning fault

## No-Blame Approach

- RCA should not assign blame to individuals or teams
- Encourages open and honest reporting to improve cybersecurity
  practices
- Recognizes that human errors often result from systemic issues
  within organizations, such as training procedures or regulatory
  oversight

## Incident Response Training and Testing

- Training
  - Education to ensure employees and staff understand incident response
    processes, procedures, and priorities
  - Training should be tailored to different roles (e.g., first responders, managers,
    executives, end users) with specific needs

## End user training includes teaching them how to report incidents and

remedial training for those who make mistakes

- Capture and incorporate lessons learned from previous incidents into training to
  prevent their recurrence
- Soft skills and relationship building are important in high-functioning incident
  response teams
- Testing
  - Practical exercise of incident response procedures to ensure the practical
    application of knowledge
  - Testing helps assess the effectiveness of your response procedures
  - It can be costly, complex, and resource-intensive, depending on the scenario
- Tabletop Exercise (TTX)
  - A theoretical exercise that presents an incident response scenario
  - Discussion based
  - Participants discuss and role-play their response actions
  - Cost-effective but lacks hands-on experience
  - Useful for exploring decision-making and response planning
- Penetration Test (Pen Test)
  - A red team (attacker) attempts network intrusion based on a specific threat
    modeling scenario
  - Rules of engagement and clear methodology are established beforehand
  - Popular tools and operating systems

## Metasploit

## Cobalt Strike

## Kali Linux

## ParrotOS

## Commando OS

- Awareness of these tools is crucial, as they can be used by both penetration
  testers and attackers
- Simulation
  - Goes beyond tabletop discussions, involving realistic, hands-on scenarios
  - Mimics actual incidents

## Simple

- Phishing attacks,
- Ransomware infections

## Complex

- Multi-stage attacks
- Data breaches in coordination with external parties
  - Tests technical skills, decision-making under pressure, and effective
    communication
  - Align simulations with the organization’s threat landscape and risk profile
  - Identifies gaps in incident response plans, improves team coordination, and
    ensures role clarity during real incidents
  - Regularly incorporating simulations improves an organization’s readiness for
    cybersecurity incidents

## Digital Forensic Procedures

- Digital Forensics
  - Systematic process of investigating and analyzing digital devices and data to
    uncover evidence for legal purposes
- Four Main Phases of Digital Forensic Procedures
  - Identification

## Focus on scene safety, prevention of evidence contamination, and scope

determination

## Secure the scene, preserve evidence, and document the scene

## Identify where relevant data might be stored (e.g., tablets, smartphones,

servers)

- Collection

## Requires proper authorization (e.g., warrant, executive authorization)

## Order of volatility

- Dictates the sequence in which data sources should be collected
  and preserved based on their susceptibility to modification or loss
- Following order of volatility minimizes data loss
- 5 Steps of Order of Volatility
  - Collect data from the system’s memory
  - Capture data from the system state
  - Collect data from storage devices
  - Capture network traffic and logs
  - Collect remotely stored or archived data

## Chain of Custody

- Documented and verifiable record that tracks the handling,
  transfer, and preservation of digital evidence from the moment it
  is collected until it is presented in a court of law

## Evidence Collecting techniques

- Disk imaging
  - Involves creating a bit-by-bit or logical copy of a storage
    device, preserving its entire content, including deleted files
    and unallocated space
- File Carving
  - Focuses on extracting files and data fragments from
    storage media without relying on the file system
  - Analysis

## Examine the forensically sound evidence copy

## Systematically scrutinize data for relevant information, timestamps, user

interactions, and signs of criminal activity

## Follow strict procedures and documented protocols for consistency and

objectivity

- Reporting

## Document methods, tools used, actions performed, findings, and

conclusions in a final report

## The report serves as crucial evidence in legal proceedings, and the

forensic analyst may need to testify

- Additional Concepts
  - Legal Hold

## Issued when litigation is expected and preserves potentially relevant

electronic data

## Ensures evidence is not tampered with, deleted, or lost

## Requires the implementation of preservation practices to protect systems

and evidence

- E-Discovery (Electronic Discovery)

## Process of identifying, collecting, and presenting electronically stored

information for potential legal proceedings

## Involves searching, analyzing, and formatting electronic data for litigation

- Ethical Considerations
  - Adherence to a code of ethics that emphasizes avoiding bias, repeatable actions,
    and evidence preservation

## Avoiding bias

- Analysis should be performed without bias or prejudice and be
  based solely on the evidence
- Use forensic analysts who are removed from the situation to avoid
  potential bias

## Repeatable actions

- All analysis must be based on repeatable processes documented
  in the final report
- Ensuring the original evidence remains unchanged is critical to
  maintaining evidentiary integrity

## Evidence preservation

- Evidence includes both the device (e.g., laptop hard disk) and the
  data recovered from it
- Perform analysis on a disk image, not the original drive, to prevent
  modifications or alterations

## Data Collection Procedures

- Digital Forensic Collection Techniques
  - Involve making forensic images of data for later analysis
  - This approach allows incident response teams to resume operations quickly
    while maintaining evidence
  - Evidence may be required for potential legal action and cooperation with law
    enforcement
- Data collection involves the following
  - Capturing and hashing system images
  - Analyzing data with forensic tools

## FTK (Forensic Toolkit)

## EnCase

- Capturing machine screenshots
- Reviewing network logs
- Collecting CCTV video
- Order of Volatility
  - Guides the sequence of collecting data, from most volatile (CPU registers and
    cache) to least volatile (archival media)
- Licensing and documentation reviews ensure system configurations align with their
  design
- Data Acquisition
  - The method and tools used to create a forensically sound copy of data from a
    source device, such as system memory or a hard disk
  - Policies for bringing one’s own device (BYOD) complicate data acquisition
    because it may not be legally possible to search or seize the devices
  - Some data can only be collected once the system is shutdown or the power is
    disconnected
  - Order of Volatility

## CPU registers and cache memory

## System memory (RAM), routing tables, ARP caches, process table,

temporary swap files

## Data on persistent mass storage

## Remote logging and monitoring data

## Physical configuration and network topology

## Archival data

- WARNING

## Some Windows registry keys, like HKLM/Hardware, are only in memory

and require a memory dump to analyze
Investigating an Incident
Objective 4.9: Given a scenario, you must be able to use data sources to support an investigation

## Investigating an Incident

- Data Sources for Incident Investigation
  - Dashboards and Automated Reports

## Purpose

- Provide high-level insights

## Role

- Initial overview of the security landscape
  - Vulnerability Scans

## Purpose

- Identify system vulnerabilities

## Role

- Foundation for understanding potential entry points
  - Packet Captures

## Purpose

- Capture and analyze network traffic

## Role

- Reveal communication patterns and potential threats
  - Logs (Various Types)

## Firewall Logs

- Monitor network traffic, detect unauthorized access

## Application Logs

- Record application-specific events, identify abnormal behavior

## Endpoint Logs

- Capture activities on individual devices

## OS-Specific Security Logs

- Monitor operating system security events

## IPS and IDS Logs and Alerts

- Track intrusion attempts and system compromises

## Network Logs

- Record network activities and connections

## Metadata

- Provide contextual information about other data sources

## Investigative Data

- SIEM (Security Information and Event Monitoring System)
  - Real-time analysis of security alerts from applications and network hardware
  - Combination of different data sources into one tool
  - Provides a consolidated view of network activity
  - Allows for trend analysis, alert creation, and correlation of data
  - Considerations

## Sensors

## Sensitivity

## Trends

## Alerts

## Correlation

- Log Files
  - Records events and messages in operating systems, software, and network
    devices
  - Includes network, system, application, security, web, DNS, authentication, dump
    files, VoIP, and call managers
- Syslog, Rsyslog, Syslog-ng
  - Tools for centralizing log data from different systems into a repository
  - Commonly used to feed data into SIEM
- JournalCTL
  - Linux command-line utility for querying and displaying logs from the Journal
    Daemon (SystemD’s logging service)
- NXLog
  - Multi-platform, open-source log management tool
  - Identifies security risks and analyzes logs from server, OS, and applications
- NetFlow
  - Network protocol for collecting active IP network traffic data
  - Provides information on source, destination, volume, and paths
- SFlow (Sampled Flow)
  - Open-source alternative to NetFlow
  - Exports truncated packets and interface counter for network monitoring
- IPFIX (Internet Protocol Flow Information Export)
  - Universal standard for exporting IP flow information
  - Used for mediation, accounting, and billing by defining data format for exporters
    and collectors
- Metadata
  - Data that describes other data
  - Useful for understanding details about events, calls, emails, web visits, and files
    during investigations
  - Use Cases for Metadata

## Email

- Analyze metadata for phishing campaigns

## Mobile

- Review data transfer, call duration, and contacts

## Web

- Determine website visits and user behavior

## File

- Examine file details, such as creation time and viewer statistics

## Dashboards

- Dashboards
  - Graphical displays of information across multiple systems
- Single Pane of Glass
  - A single screen for analysts to access everything across the organization
- Splunk
  - A big data platform for ingesting various types of data, including security and
    incident response data
  - Collects data from firewalls, applications, endpoints, operating systems, intrusion
    detection systems, intrusion prevention systems, antivirus software, and
    networks
- Dashboards help analyze trends over time and inform actions
- Use the dashboard as a central starting point for investigations and incident response

## Automated Reports

- Automated Reports
  - Generated by computer systems to provide information about various aspects of
    a network’s security
  - Common sources are antivirus software, endpoint detection response
    capabilities, and other security tools
- Automated Security Incident Report Key Elements
  - Report ID

## A unique identifier for the report

- Generation date

## The date the report was generated

- Report period

## The time frame covered by the report

- “Prepared by”

## The entity responsible for creating the report

- Executive Summary

## Provides a brief overview of the report’s content, helping readers

determine its relevance

- Incident Alerts

## Can be categorized into different levels

- Critical
- High
- Moderate
- Informational
  - Incident Details

## Timestamps

## User accounts

## Affected systems

## Incident descriptions

## Actions taken

- Automated responses can include suspending user accounts,
  blocking IP addresses, and resetting passwords
- Outbound traffic and software installations may trigger alerts,
  which require investigation to determine their nature and
  potential security implications
  - Incident Analysis

## May include threat trends, user behavior, and data flow anomalies

- Security Recommendations

## Suggest actions to address identified security issues

- Conclusion

## Summary of the report’s findings and contains outlines of any further

actions to be taken

- Appendices

## May include log snippets, IP addresses, domains, or other relevant data

- Automation and orchestration enable real-time responses to security incidents, helping
  to prevent major security breaches and network outages

## Vulnerability Scans

- Vulnerability Scan Report
  - Generated automatically after completing a vulnerability scan
  - Analysis of the report is essential to confirm the validity of identified
    vulnerabilities
- False Positives
  - Vulnerability scanners may produce false positives, meaning they report
    vulnerabilities that don’t actually exist on your system
  - It is crucial to differentiate real vulnerabilities from false positives
- Analysis of Vulnerabilities
  - For each identified vulnerability, assess whether it was detected by the scanner
    and if it exists on your system
  - Determine the severity and criticality of each vulnerability
  - Create a plan of action and milestones for remediation
- Components of a Vulnerability Scan Report
  - Report ID
  - Scan Date and Time
  - System or Software Version
  - Scan Initiator

## The person who ran the scan

- Executive Summary

## Highlights themes and trends for large networks

- Vulnerabilities – listed by severity (critical, high, medium, low, informational) or
  by hosts

## CVE (Common Vulnerability and Exposure) ID – Vulnerability ID

- CVE website (cve.org) contains detailed information about
  vulnerabilities

## Description

## Affected system

## Impact

## Common Vulnerability Scoring System (CVSS) Score

- Measures severity

## Remediation Recommendations

- Additional Findings
- Recommendations
- Conclusion

## Packet Captures

- Packet Capture
  - Captures data going to or from a network device
  - Can be set up on a span port to capture all data going to and from devices on the
    network
  - Packet captures in exam are typically short snippets, not massive data dumps
- Packet Capture Columns
  - Number

## Packet sequence number in the capture

- Time

## Elapsed time since the capture started

- Source/Destination IP Addresses

## Show where the data is coming from and going to

- Protocol

## Typically TCP or UDP

- Length

## The size of the packet

- Info

## Provides information from the packet header, including flags, sequence,

window, length, MSS, source port, and destination port

- Look for patterns that indicate attack types, such as SYN floods or DDoS attacks
- Consider the relationship between source and destination IP addresses to identify the
  type of attack

## Metadata

- Metadata
  - Information about a file, application, or other data
- MD5/SHA256 Checksum
  - Serves as unique digital fingerprint for file identification, including potential
    malware
    Automation and Orchestration
    Objective 4.7: Explain the importance of automation and orchestration related to secure operations

## Automation and Orchestration

- Automation
  - Execution of tasks without manual intervention
  - Purpose

## Consistency, efficiency, reduction of human error

- Example

## Scripting repetitive tasks

- Orchestration
  - Coordinated execution of multiple automated tasks for a specific outcome or
    workflow
  - Purpose

## Ensures tasks work together harmoniously

- Example

## Sequencing tasks in incident response

- SOAR (Security Orchestration, Automation, and Response)
  - Class of security tools for incident response, threat hunting, and security
    configurations
  - Purpose

## Orchestrate and automate runbooks, deliver data enrichment

- Example

## Integrating SIEM and SOAR for advanced security capabilities

- Playbook
  - Checklist of actions for detecting and responding to a specific incident
  - Role

## Guides incident response processes

- Example

## Steps for responding to a phishing campaign

- Runbook
  - Automated version of a playbook with defined interaction points for human
    analysis
  - Role

## Executes automated tasks with human decision points

- Example

## Automated incident response with analyst decision points

- Benefits of Automation and Orchestration
  - Efficiency

## Time-saving and consistent execution

- Standardization

## Enforces baselines and standardized configurations

- Scalability

## Scales securely and efficiently

- Employee Retention

## Reduces repetitive tasks

- Reaction Time

## Faster responses to incidents

- Workforce Multiplier

## Maximizes human resources

## When to Automate and Orchestrate

- Automation and Orchestration
  - Effective automation and orchestration are for repeatable and stable tasks and
    workflows
  - Identify consistent processes in your organization for automation and
    orchestration
- Decision factors for implementing automation and orchestration
  - Complexity

## Automation and orchestration are suitable for complex, repetitive tasks

## Determine process complexity to decide whether to automate or

orchestrate

## Routine backups are suitable for automation, while complex incident

response requires orchestration

- Cost

## Initial investment is a key factor

## Conduct a cost-benefit analysis considering development,

implementation, and maintenance costs

## Include hardware, software, personnel, and support costs in the analysis

## Cost savings often outweigh the initial investment in the long run

- Single Points of Failure

## Implement backup systems or manual processes to mitigate single points

of failure

## Redundancy and failover mechanisms, both technical and manual, can

ensure uninterrupted operations

- Technical Debt

## Technical debt is the cost and complexity of suboptimal software

solutions

## Regular reviews and updates are necessary to avoid technical debt

## Technical debt can impede efficiency and security

- Ongoing supportability

## Automation and orchestration systems need ongoing maintenance and

adaptation

## Teams must possess the necessary skills to maintain and adapt these

systems

## Training and skill development are essential

## Most automation depends on the connection of systems via APIs and

webhooks

## Benefits of Automation and Orchestration

- Increased Efficiency and Time Savings
  - Automation reduces manual tasks
  - Repetitive processes, like patching and backups, can run seamlessly without
    human intervention
  - Frees up human resources and reduces the risk of errors
  - Increases reliability and consistency in processes
- Enforcement of Baselines
  - Consistently enforces security and compliance baselines
  - Defines standardized configurations and policies
  - Ensures systems align with industry best practices and regulatory requirements
  - Minimizes vulnerabilities and security breach risks
- Implementation of Standard Infrastructure Configurations
  - Facilitates the creation and enforcement of standard configurations
  - Ensures consistent setup of all systems
  - Detects deviations from established standards and triggers automated corrective
    action
- Secure Scaling
  - Enables secure scaling of IT infrastructure as organizations grow
  - Dynamically scales resources while adhering to security protocols
  - Provisioning virtual machines, adding network resources, and access control
    adjustments are done securely
- Increased Employee Retention
  - Empowers employees to focus on strategic and creative aspects of their roles
  - Reduces repetitive and mundane tasks
  - Increases job fulfillment and engagement
  - Reduces the risk of burnout, contributing to higher retention rates
- Faster Reaction Times
  - Facilitates rapid response to security incidents and threats
  - Automation and orchestration systems are always available
  - Automates intrusion detection, threat analysis, and incident response
  - Real-time alerts and predefined response actions enhance security
- Workforce Multiplier
  - Augments existing staff’s capabilities
  - Smaller teams can manage larger, more complex infrastructures
  - Reduces staffing needs and optimizes resource allocation for cost savings

## Automating Support Tickets

- Automating Support Ticket Management
  - Enhances IT and customer support team efficiency
  - Streamlines issue resolution and improves customer satisfaction
  - Support ticket management is critical for addressing issues, incidents, and service
    requests
  - High ticket volume can lead to delays, increased workloads, and decreased
    customer satisfaction
- Automating Support Ticket Creation
  - Six steps in the ticket creation process

## Users submit requests through channels (e.g., email, web form, support

portal)

## Automation tool generates tickets based on predefined criteria

## Capture essential information from user submissions

## Categorize tickets based on content or source

## Assign priority based on predefined rules and criteria

## Automated notification sent to relevant support team or technician

- Benefits of Automating Ticket Creation

## Ensures efficient capture, categorization, and assignment of support

requests

## Reduces the risk of lost or overlooked tickets

## Accelerates response time to user needs

- Ticket Escalation Automation
  - Ticket escalation addresses complex or high-priority issues
  - Follows a five-step process

## Define escalation criteria based on issue nature, urgency, and service

level agreements

## Create automation rules to monitor ticket attributes and trigger

escalation

## Perform predefined escalation actions (e.g., notification, reassignment,

change in priority)

## Monitor and track the escalated ticket’s progress

## Resolve and close the ticket, triggering notification to the user

- Benefits of Automating Ticket Escalation

## Ensures prompt handling of critical issues

## Maintains transparency and accountability in the support process

## Helps meet service level agreements and minimize delays in addressing

urgent matters

## Automating Onboarding

- Automation
  - Involves using technology to execute repetitive tasks without continuous human
    intervention
- Automating the onboarding process impacts organizational productivity, employee
  satisfaction, and retention rates
  - Streamlining onboarding ensures new hires are integrated quickly and efficiently
    into their roles and the organization’s culture
  - Benefits

## Eliminates manual tasks, reduces errors, and provides structured,

consistent onboarding

## Reduces administrative burden on HR and IT departments

## Enhances support ticket management processes

- Areas to Automate in Onboarding
  - Creation of documentation records
  - Scheduling training
  - Provisioning equipment
  - Managing access rights
  - Distributing checklists
  - Collecting feedback
- User Provisioning
  - Involves creating and managing user accounts and access rights
  - Ensures new employees have necessary access to systems, applications, and
    resources
  - Process includes the following

## Collecting information

## Creating accounts

## Assigning roles and access

## Sending notifications

## Conducting synchronization and updates

- Steps in User Provisioning

## Employee provides personal details, role, and department information

## Automation creates user accounts in various systems

## Automation assigns roles and access levels based on department and

position

## Automated notifications sent to the employee, manager, or IT

department

## Automation keeps user information synchronized across platforms

- Resource Provisioning
  - Ensures timely allocation of physical and digital resources needed by new
    employees
  - Resources include

## Workstations

## Software licenses

## Communication tools

- Process involves

## Requirements analysis

## Resource allocation

## Configuration

## Verification and auditing

## Gathering feedback

- Steps in Resource Provisioning

## Analyze role and department information to determine specific resources

## Initiate procurement workflows or allocate available resources based on

rules

## Configure resources to meet the employee’s role

## Verification process to ensure successful allocation

## Auditing to track allocated resources for inventory management and

compliance

## Employee and manager feedback on resource suitability and additional

requirements

## Automating Security

- Automating Security
  - Helps prevent security vulnerabilities, respond to threats swiftly, and maintain
    consistent security policies
  - It involves using technology to perform crucial but repetitive security tasks to
    maintain updated defenses and swift response to security threats
  - Automation includes the use and configuration of guardrails, security groups,
    service access management, and permissions
- Ways to Automate Security
  - Implementing Guardrails

## Guardrails are automated safety controls to protect against insecure

infrastructure configurations

## Configured according to security standards and enforce security policies

automatically

## Continuously monitor infrastructure, detect security violations, and take

predefined corrective actions

- Managing Security Groups

## Security groups act as virtual firewalls for cloud-based server instances

## Specify allowed incoming and outgoing network traffic using predefined

rules

## Automate assignment of instances to appropriate security groups

## Dynamically adjust security group configurations to respond to evolving

threats

## Analyze traffic for unauthorized access attempts

- Enabling and Disabling Services and Access

## Automate service access management to prevent unnecessary risks and

maintain operational efficiency

## Regularly review and manage access to services

## Monitor for unusual activity and automatically restrict or disable access if

suspicious

## Enable or disable services based on a predefined schedule when not

continuously needed

- Automating Permissions Management

## Manage permissions using Role-based Access Controls (RBAC)

## Automate provisioning and de-provisioning of access rights based on

assigned roles

## Ensure no unauthorized access to sensitive information

## Perform regular checks on permissions settings to verify compliance with

policies and regulations

## Make necessary adjustments over time to maintain security

## Automating Application Development

- Automating Application Development
  - Enhances efficiency, consistency, and the quality of software products
  - Automation

## In application development, it involves using technology to manage, test,

and deploy applications with minimal human intervention

- Continuous Integration and Continuous Deployment (CI/CD) significantly improve
  software efficiency, consistency, and quality
  - Continuous Integration (CI)

## Developers merge code changes frequently in a central repository

## Automated build process verifies each check-in and detects problems

during integration

## Automation tools manage code integration, provide notifications for

conflicts or errors

## Automated tests ensure software quality after integration

## Developers receive feedback on detected issues to make necessary

corrections

## Release

- Process of finalizing and preparing new software or updates
- Enabling software installation and usage

## Deployment

- Involves automated process of software releases to users
- Actual installation of software in a new environment
  - Continuous Integration and Continuous Delivery (CI/CD)

## CI/CD includes continuous integration

## Continuous Delivery (CD) ensures code is always deployable after every

change

- Automated testing and build processes
- CD stops short of automatic production deployment
- CD is part of the release process
- Full deployment process is automated only to a certain stage
  - Doesn’t deploy into the production environment
    automatically
- Deployment to production environment is a manual business
  decision
- Allows flexibility in timing, market conditions, and stakeholder
  readiness
  - Continuous Deployment

## Takes CI/CD further by automatically deploying code changes to testing

and production environments

## All changes passing through the production pipeline are fully released

with no human intervention

## Automation ensures consistent deployments, faster releases, and offers

rollback capabilities

## Requires a paradigm shift, more developer involvement in the

deployment process

## Promotes increased communication and collaboration within teams for

collective responsibility

- Benefits of CI/CD

## Adapting to changing market demands more quickly

## Efficient workflow from development to deployment

## Improves code quality, streamlines deployment processes, and allows

flexible production release

## Reduces deployment risks and enhances software reliability

## Integrations and APIs

- Integration
  - Combining subsystems or components into a single, functioning system
- API (Application Programming Interface)
  - Set of rules and protocols used for building and integrating application software
  - Enable software developers to access functions or features of another
    application programmatically
- API Communication
  - APIs facilitate communication between different parts of a microservice or
    service-oriented architecture
  - Allows automation of administration, management, and monitoring of services
    and cloud-based infrastructures
  - Common communication methods used by APIs

## REST (Representational State Transfer)

- REST uses standard HTTP methods, status codes, URIs, and MIME
  types for interactions
- Primarily uses JSON for data transfer
- Lightweight protocol suitable for integrating with existing websites

## SOAP (Simple Object Access Protocol)

- SOAP has a structured message format in XML
- Known for robustness, additional security features, and
  transaction compliance requirements
- Suitable for enterprise-level web services with complex
  transactions and regulatory compliance requirements
- Benefits of API Integrations
  - Improved efficiency and consistency
  - Allows direct integration of third-party applications into web applications
  - Reduces the need to build entire services from scratch
- API Testing with CURL
  - CURL

## A tool for transferring data to or from a server using various supported

protocols

- Commonly used protocols for API testing are HTTP and HTTPS
- Use CURL to send data to an API and receive a response for testing
- CURL allows sending data to an API and receiving a JSON response
- Helpful for software developers and cybersecurity professionals, especially in
  penetration testing scenarios
