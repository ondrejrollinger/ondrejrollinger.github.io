# Security Architecture

-----

Security Architecture
Objectives:

## 3.1 - Compare and contrast security implications of different architecture models

## 4.1 - Given a scenario, apply common security techniques to computing resources

## Security Architecture

- Security Architecture
  - Design, structure, and behavior of an organization’s information security
    environment
- On-Premise vs. Cloud Deployment
  - On-Premise

## Traditional local infrastructure setup

- Cloud

## Delivery of computing services over the internet

- Cloud Security Considerations
  - Shared Physical Server Vulnerabilities
  - Inadequate Virtual Environment Security
  - User Access Management
  - Lack of Up-to-date Security Measures
  - Single Point of Failure
  - Weak Authentication and Encryption Practices
  - Unclear Policies and Data Remnants
- Virtualization and Containerization
  - Different virtualization types
  - Containerization benefits and risks
  - Vulnerabilities like vm escape and resource reuse
- Serverless Computing
  - Cloud provider manages server allocation
  - Developers focus solely on writing code
- Microservices Architecture
  - Collection of small, autonomous services
  - Each performs a specific business process
- Software-Defined Network (SDN)
  - Dynamic, programmatically efficient network configuration
  - Improves network performance and monitoring
- Infrastructure as Code (IaC)
  - Automation of managing and provisioning technology stack
  - Software-driven setup instead of manual configuration
- Centralized vs. Decentralized Architectures
  - Benefits and risks of centralized and decentralized setups
- Internet of Things (IoT)
  - Network of physical devices with sensors and connectivity
  - Enables data exchange among connected objects
- ICS and SCADA
  - Industrial Control Systems (ICS)

## For industrial production

- Supervisory Control and Data Acquisition (SCADA)

## Subset of ICS

- Embedded Systems
  - Dedicated computer system designed for specific functions
  - Part of a complete device system with hardware components

## On-premise versus the Cloud

- Cloud Computing
  - Delivery of computing services over the internet, including servers, storage,
    databases, networking, software, analytics, and intelligence
  - Advantages

## Faster innovation

## Flexible resources

## Economies of scale

- Responsibility Matrix
  - Outlines the division of responsibilities between the cloud service provider and
    the customer
- Third-Party Vendors
  - Provides specialized services to enhance functionality, security, and efficiency of
    cloud solutions
- Hybrid Solutions
  - Combined on-premise, private cloud, and public cloud services, allowing
    workload flexibility
  - Considerations

## Sensitive data is protected

## Regulatory requirements are met

## Systems can communicate with each other

## The solution is cost-effectiveness

- On-Premise Solutions
  - Computing infrastructure physically located on-site at a business
- Key Considerations in Cloud Computing
  - Availability

## System’s ability to be accessed when needed

- Resilience

## System’s ability to recover from failures

- Cost

## Consider both upfront and long-term costs

- Responsiveness

## Speed at which the system can adapt to demand

- Scalability

## System’s ability to handle increased workloads

- Ease of Deployment

## Cloud services are easier to set up than on-premise solutions

- Risk Transference

## Some risks are transferred to the provider, but customers are responsible

for security

- Ease of Recovery

## Cloud services offer easy data recovery and backup solutions

- Patch Availability

## Providers release patches for vulnerabilities automatically

- Inability to Patch

## Compatibility issues or lack of control can hinder patching

- Power

## Cloud provider manages infrastructure, including power supply

## Reduces customer costs and eliminates power management concerns

- Compute

## Refers to computational resources, including CPUs, memory, and storage

## Cloud providers offer various compute options to suit different needs

- Remember
  - Cloud computing offers flexibility, scalability, and cost-effectiveness
  - On-premise solutions provide control and security but can be expensive and
    challenging to maintain
  - Hybrid solutions offer flexibility and control but require considerations of
    security, compliance, interoperability, and cost

## Cloud Security

- Shared Physical Server Vulnerabilities
  - In cloud environments, multiple users share the same physical server

## Compromised data from one user can potentially impact others on the

same server

- Mitigation

## Implement strong isolation mechanisms (e.g., hypervisor protection,

secure multi-tenancy)

## Perform regular vulnerability scanning, and patch security gaps

- Inadequate Virtual Environment Security
  - Virtualization is essential in cloud computing

## Inadequate security in the virtual environment can lead to unauthorized

access and data breaches

- Mitigation

## Use secure VM templates

## Regularly update and patch VMs

## Monitor for unusual activities

## Employ network segmentation to isolate VMs

- User Access Management
  - Weak user access management can result in unauthorized access to sensitive
    data and systems
  - Mitigation

## Enforce strong password policies

## Implement multi-factor authentication

## Limit user permissions (Principle of Least Privilege)

## Monitor user activities for suspicious behavior

- Lack of Up-to-date Security Measures
  - Cloud environments are dynamic and require up-to-date security measures

## Failure to update can leave systems vulnerable to new threats

- Mitigation

## Regularly update and patch software and systems

## Review and update security policies

## Stay informed about the latest threats and best practices

- Single Point of Failure
  - Cloud services relying on specific resources or processes can lead to system-wide
    outages if they fail
  - Mitigation

## Implement redundancy and failover procedures

## Use multiple servers, data centers, or cloud providers

## Regularly test failover procedures

- Weak Authentication and Encryption Practices
  - Weak authentication and encryption can expose cloud systems and data
  - Mitigation

## Use multi-factor authentication

## Strong encryption algorithms

## Secure key management practices

- Unclear Policies
  - Unclear security policies can lead to confusion and inconsistencies in
    implementing security measures
  - Mitigation

## Develop clear, comprehensive security policies covering data handling,

access control, incident response, and more

## Regularly review and update policies and provide effective

communication and training

- Data Remnants
  - Data Remnants

## Residual data left behind after deletion or erasure processes

## In a cloud environment, data may not be completely removed, posing a

security risk

- Mitigation

## Implement secure data deletion procedures

## Use secure deletion methods

## Manage backups securely

## Verify data removal after deletion

- Remember that cloud security is a shared responsibility

## Virtualization and Containerization

- Virtualization
  - Emulates servers, each with its own OS within a virtual machine
- Containerization
  - Lightweight alternative, encapsulating apps with their OS environment
  - Key Benefits

## Efficiency and Speed

## Portability

## Scalability

## Isolation

## Consistency

- Hypervisors
  - Two Types of Hypervisors

## Type 1 (Bare Metal)

- Runs directly on hardware (e.g., Hyper-V, XenServer, ESXi)

## Type 2 (Hosted)

- Operates within a standard OS (e.g., VirtualBox, VMware)
- Virtualization Vulnerabilities
  - Virtual Machine (VM) Escape

## Attackers break out of isolated VMs to access the hypervisor

- Privilege Elevation

## Unauthorized elevation to higher-level users

- Live VM Migration

## Attacker captures unencrypted data between servers

- Resource Reuse

## Improper clearing of resources may expose sensitive data

- Containerization Technologies
  - Docker, Kubernetes, Red Hat OpenShift are popular containerization platforms
  - Revolutionized application deployment in cloud environments
- Securing Virtual Machines
  - Regularly update OS, applications, and apply security patches
  - Install antivirus solutions and software firewalls
  - Use strong passwords and implement security policies
  - Secure the hypervisor with manufacturer-released patches
  - Limit VM connections to physical machines and isolate infected VMs
  - Distribute VMs among multiple servers to prevent resource exhaustion
  - Monitor VMs to prevent “Virtualization Sprawl”
  - Enable encryption of VM files for data safety and confidentiality

## Serverless

- What is Serverless?
  - Serverless computing doesn’t mean no servers; it shifts server management
    away from developers
  - Relies on cloud service providers to handle server management, databases, and
    some application logic
  - Functions as a Service (FaaS) Model

## Developers write and deploy individual functions triggered by events

- Benefits of Serverless
  - Reduced operational costs

## Pay only for compute time used, no charges when code is idle

- Automatic scaling

## Cloud provider scales resources based on workload, ensuring optimal

capacity

- Focus on core product

## Developers can concentrate on application functionality, not server

management

- Faster time to market

## Reduced infrastructure concerns speed up application development

- Challenges and Risks
  - Vendor Lock-in

## Reliance on proprietary interfaces limits flexibility and may increase costs

- Immaturity of best practices

## Serverless is a relatively new field, and best practices are still evolving

- Not a one-size-fits-all solution
  - Consider the specific needs and requirements of your application; serverless
    introduces challenges like Vendor Lock-in and service provider dependencies

## Microservices

- Microservices
  - Architectural style for breaking down large applications into small, independent
    services
  - Each microservice runs a unique process and communicates through a
    well-defined, lightweight mechanism
  - Contrasts with traditional monolithic architecture, where all components are
    interconnected

## Each service in the microservice architecture is self-contained and able to

run independently

- Advantages of Microservices
  - Scalability

## Services can be scaled independently based on demand

- Flexibility

## Microservices can use different technologies and be managed by different

teams

- Resilience

## Isolation reduces the risk of system-wide failures

- Faster Deployments and Updates

## Independent deployment and updates allow for agility and reduced

deployment risk

- Challenges of Microservices
  - Complexity

## Managing multiple services involves inter-service communication, data

consistency, and distributed system testing

- Data Management

## Each microservice can have its own database, leading to data consistency

challenges

- Network Latency

## Increased inter-service communication can result in network latency and

slower response times

- Security

## The distributed nature of microservices increases the attack surface,

requiring robust security measures

## Network Infrastructure

- Network Infrastructure
  - Backbone of modern organizations
  - Comprises hardware, software, services, and facilities for network support and
    management
- Physical Separation
  - Security measures to protect sensitive information
  - Often referred to as “Air Gapping”
  - Isolates a system by physically disconnecting it from all networks
  - Physical separation is one of the most secure methods of security, but it is still
    vulnerable to sophisticated attacks
- Logical Separation
  - Establishes boundaries within a network to restrict access to certain areas
  - Implemented using firewalls, VLANs, and network devices
- Comparison
  - Physical Separation (Air-Gapping)

## High security, complete isolation

- Logical Separation

## More flexible, easier to implement

## Less secure if not configured properly

## Software-defined Network (SDN)

- Software-Defined Network (SDN)
  - Revolutionary approach to network management
  - Enables dynamic, programmatically efficient network configuration
  - Improves network performance and monitoring
  - Reduces complexity in static and inflexible network architectures
  - Provides a centralized view of the entire network
- SDN Architecture
  - Decouples network control and forwarding functions
  - Three Distinct Planes

## Data Plane (Forwarding Plane)

- Responsible for handling data packets
- Makes decisions based on protocols like IP and Ethernet
- Concerned with sending and receiving data

## Control Plane

- Centralized decision-maker in SDN
- Dictates traffic flow across the entire network
- Replaces traditional, distributed router control planes
- Increases network manageability and flexibility

## Application Plane

- Hosts all network applications that interact with the SDN
  controller
- Applications instruct the controller on network management
- Controller manipulates the network based on these instructions

## Infrastructure as Code (IaC)

- Infrastructure as Code (IaC)
  - Modern approach to IT infrastructure management
  - Automates provisioning and management through code
  - Used in DevOps and with cloud computing
- IaC Method
  - Developers and ops teams manage infrastructure through code
  - Code files are versioned, tested, and audited
  - High-level languages like YAML, JSON, or domain-specific languages (e.g., HCL)
    used
  - Idempotence ensures identical environments

## Idempotence

- Operation consistently produces the same results
- Crucial for consistency and reliability in multiple environments
- Benefits of IaC
  - Speed and Efficiency
  - Consistency and Standardization
  - Scalability
  - Cost Savings
  - Auditability and Compliance
- Challenges
  - Learning Curve

## New skills and mindset required

## Teams learn to write, test, and maintain infrastructure code

- Complexity

## Infrastructure code can become complex

## Mitigated with modularization and documentation

- Security Risks

## Sensitive data exposure in code files

## Insecure configurations may be introduced

## Centralized vs Decentralized Architectures

- Centralized Architecture
  - All computing functions managed from a single location or authority
  - Components

## Central Server

## Mainframe

## Data Center

- Data and applications stored in one place, accessed via a network
- Benefits

## Efficiency and Control

- High resource control and efficient resource allocation

## Consistency

- Ensures uniform and accurate data across the organization

## Cost-effective

- Reduced maintenance and infrastructure costs
  - Risks

## Single Point of Failure

- Server failure can disrupt the entire network

## Scalability Issues

- Struggles to handle growth, leading to performance problems

## Security Risks

- Attractive targets for cybercriminals; compromised server risks
  data and app security
- Decentralized Architecture
  - Computing functions distributed across multiple systems or locations
  - No single point of control; each node operates independently
  - Benefits

## Resilience

- Can continue functioning despite individual node failures

## Scalability

- Easily scales with organization growth by adding new nodes

## Flexibility

- Supports remote work and distributed teams
  - Risks

## Security Risks

- Vulnerable to security threats, especially in remote work scenarios

## Management Challenges

- Complex management, coordinating multiple nodes

## Data Inconsistency

- Potential issues with data consistency and synchronization
- Considerations for Choosing Architecture
  - Choice depends on the organization’s specific needs and context
  - Centralized systems for

## Data accuracy and resource management priorities

- Decentralized systems for

## Resilience, flexibility, and rapid scaling needs

## Internet of Things (IoT)

- Internet of Things (IoT)
  - Network of physical devices with sensors, software, and connectivity
  - Enables data exchange among connected objects
- Hub/Control System
  - Central component connecting IoT devices
  - Collects, processes, analyzes data, and sends commands
  - Can be a physical device or software platform
- Smart Devices
  - Everyday objects enhanced with computing and internet capabilities
  - Sense environment, process data, and perform tasks autonomously
- Wearables
  - Subset of smart devices worn on the body
  - Monitor health, provide real-time information, and offer hands-free interface
- Sensors
  - Detect changes in environment, convert into data
  - Measure various parameters (temperature, motion, etc.)
  - Enable interaction and autonomous decisions in smart devices
- IoT Risks
  - Weak Default Settings

## Common security risk

## Default usernames/passwords are easy targets for hackers

## Changing defaults upon installation is essential

- Poorly Configured Network Services

## Devices may have vulnerabilities due to open ports, unencrypted

communications

## Unnecessary services can increase attack surface

## Keeping IoT devices on a separate network is recommended

## ICS and SCADA

- Industrial Control Systems (ICS)
  - Systems used to monitor and control industrial processes, found in various
    industries like electrical, water, oil, gas, and data
  - Distributed Control Systems (DCS)

## Used in control production systems within a single location

- Programmable Logic Controllers (PLCs)

## Used to control specific processes such as assembly lines and factories

- Supervisory Control and Data Acquisition (SCADA) Systems
  - Type of ICS designed for monitoring and controlling geographically dispersed
    industrial processes
  - Common in industries like

## Electric power generation, transmission, and distribution systems

## Water treatment and distribution systems

## Oil and gas pipeline monitoring and control systems

- Risks and Vulnerabilities
  - Unauthorized Access

## Unauthorized individuals can manipulate system operations without

proper protection

- Malware Attacks

## Vulnerable to disruptive malware attacks

- Lack of Updates

## Running outdated software with unpatched vulnerabilities

- Physical Threats

## Susceptible to damage to hardware or infrastructure

- Securing ICS and SCADA Systems
  - Implement Strong Access Controls

## Strong passwords

## Two-factor authentication

## Limited access to authorized personnel only

- Regularly Update and Patch Systems

## Keep systems updated to protect against known vulnerabilities

- Use Firewall and Intrusion Detection Systems

## Detect and prevent unauthorized access

- Conduct Regular Security Audits

## Identify and address potential vulnerabilities through routine

assessments

- Employee Training

## Train employees on security awareness and response to potential threats

## Embedded Systems

- Embedded Systems
  - Specialized computing components designed for dedicated functions within
    larger devices
  - They integrate hardware and mechanical elements and are essential for various
    daily-use devices
- Real-Time Operating System (RTOS)
  - Designed for real-time applications that process data without significant delays
  - Critical for time-sensitive applications like flight navigation and medical
    equipment
- Risks and Vulnerabilities in Embedded Systems
  - Hardware Failure

## Prone to failure in harsh environments

- Software Bugs

## Can cause system malfunctions and safety risks

- Security Vulnerabilities

## Vulnerable to cyber-attacks and unauthorized access

- Outdated Systems

## Aging software and hardware can be more susceptible to attacks

- Key Security Strategies for Embedded Systems
  - Network Segmentation

## Divide the network into segments to limit potential damage in case of a

breach

- Wrappers (e.g., IPSec)

## Protect data during transfer by hiding data interception points

- Firmware Code Control

## Manage low-level software to maintain system integrity

- Challenges in Patching

## Updates face operational constraints; OTA updates demand meticulous

planning and security measures

- Over-the-Air (OTA) Updates
  - Patches are delivered and installed remotely
    Security Infrastructure
    Objectives:

## 3.2 - Given a scenario, you must be able to apply security principles to secure enterprise

architecture

## 4.5 - Given a scenario, you must be able to modify enterprise capabilities to enhance security

## Security Infrastructure

- Security Infrastructure
  - Encompasses hardware, software, networks, data, and policies working
    cohesively for information asset safeguarding
- Firewalls
  - Types

## Web Application

## Unified Threat Management

## Next-generation

- Intrusion Detection Systems (IDS) and Intrusion Prevention Systems (IPS)
  - Mechanisms

## Identifying trends

## Showcasing signatures

- Network Appliances
  - Specialized hardware or software for specific networking functions
  - Functions

## Load Balancing

## Proxying

## Monitoring

## Security Enforcement

- Port Security
  - Restricting and controlling network access
  - Basis

## Media Access Control (MAC) addresses

- Concepts

## 802.1x and EAP

- Securing Network Communications
  - Technologies

## VPNs

## IPSec

## TLS

- Objective

## Create a secure backbone for communication

- Software-Defined Wide Area Networks (SD-WAN) and Secure Access Service Edge (SASE)
  - SD-WAN

## Optimize WAN connections with software-defined principles

- SASE

## Cloud-based service integrating security and wide area networking

- Infrastructure Considerations
  - Aspects

## Device placement, security zones, screen subnets, attack surfaces

- Connectivity

## Concerns and considerations

- Device Attributes

## Active vs. passive, inline vs. taps or monitors

- Failure Mode Options

## Fail-open or fail-closed for security devices

- Selection of Infrastructure Controls
  - Choosing controls aligned with network needs
  - Tailoring

## Ensuring robust security architecture

## Ports and Protocols

- Ports
  - Logical communication endpoints on a computer or server
  - Classified as either

## Inbound

- Listening for connections

## Outbound

- Used to connect to a server
  - Example

## SSH connection with an inbound port 22 and an outbound port on the

client

- Port Classification
  - Well-Known Ports (0-1023)

## Assigned by IANA, commonly-used protocols

- Registered Ports (1024-49151)

## Vendor-specific, registered with IANA

- Dynamic and Private Ports (49152-65535)

## Temporary outbound connections

- Protocols
  - Rules governing device communication and data exchange
  - Example

## HTTPS (port 443) uses the HTTPS protocol for secure web communication

- Memorization Tips
  - Memorize for each port

## Port number

## Default protocol

## Support for TCP or UDP

## Basic description of the port or protocol

- List of Ports and Protocols
  - Port 21: FTP (File Transfer Protocol) - TCP
  - Port 22: SSH, SCP, SFTP - TCP
  - Port 23: Telnet - TCP
  - Port 25: SMTP (Simple Mail Transfer Protocol) - TCP
  - Port 53: DNS (Domain Name System) - TCP/UDP
  - Port 69: TFTP (Trivial File Transfer Protocol) - UDP
  - Port 80: HTTP (Hypertext Transfer Protocol) - TCP
  - Port 88: Kerberos - UDP
  - Port 110: POP3 (Post Office Protocol) - TCP
  - Port 119: NNTP (Network News Transfer Protocol) - TCP
  - Port 135: RPC (Remote Procedure Call) - TCP/UDP
  - Ports 137, 138, 139: NetBIOS - TCP/UDP
  - Port 143: IMAP (Internet Message Access Protocol) - TCP
  - Port 161: SNMP (Simple Network Management Protocol) - UDP
  - Port 162: SNMPTrap - UDP
  - Port 389: LDAP (Lightweight Directory Access Protocol) - TCP
  - Port 443: HTTPS (HTTP Secure) - TCP
  - Port 445: SMB (Server Message Block) - TCP
  - Ports 465, 587: SMTPS (SMTP Secure) - TCP
  - Port 514: Syslog - UDP
  - Port 636: LDAPS (LDAP Secure) - TCP
  - Port 993: IMAPS (IMAP over SSL/TLS) - TCP
  - Port 995: POP3S (POP3 over SSL/TLS) - TCP
  - Port 1433: Microsoft SQL - TCP
  - Ports 1645, 1646: RADIUS (Remote Authentication) - TCP
  - Ports 1812, 1813: RADIUS UDP - UDP
  - Port 3389: RDP (Remote Desktop Protocol) - TCP
  - Port 6514: Syslog TLS - TCP
- Study Tips
  - Create flashcards with protocol, port, and connection details
  - Regularly test yourself to memorize ports and protocols
  - Understanding these is crucial for success in exams related to cybersecurity

## Firewalls

- Firewall
  - A network security device or software that monitors and controls network traffic
    based on security rules
  - Protects networks from unauthorized access and potential threats
- Screened Subnet (Dual-homed Host)
  - Acts as a security barrier between external untrusted networks and internal
    trusted networks using a protected host with security measures like a
    packet-filtering firewall
- Types of Firewalls
  - Packet Filtering Firewalls

## Inspect packet headers for IP addresses and port numbers

## Limited in inspection, operates at Layer 4 (Transport Layer)

- Stateful Firewalls

## Track connections and requests, allowing return traffic for outbound

requests

## Operates at Layer 4, with improved awareness of connection state

- Proxy Firewalls

## Make connections on behalf of endpoints, enhancing security

## Two Types of Proxy Firewalls

- Session layer(Layer 5)
- Application layer (Layer 7)
  - Kernel Proxy Firewalls

## Minimal impact on network performance, full inspection of packets at

every layer

## Placed close to the system they protect

- Firewall Evolutions
  - Next Generation Firewall (NGFW)

## Application-aware

- distinguish between different types of traffic

## Conduct deep packet inspection and use signature-based intrusion

protection

## Operate fast within minimal network performance impact

## Offer full-stack traffic visibility

## Can integrate with other security products

- Can be a problem if organizations become reliant on a single
  vendor due to firewall configurations tailored to one product line
  - Unified Threat Management (UTM) Firewall

## Combines multiple security functions in a single device

## Functions include firewall, intrusion prevention, antivirus, and more

## Reduces the number of devices

## Are a single point of failure

## UTMs use separate individual engine

- NGFW uses a single engine
  - Web Application Firewall (WAF)

## Focuses on inspecting HTTP traffic

## Prevents common web application attacks like cross-site scripting and SQL

injections

## Can be placed

- In-line (live attack prevention)
  - Device sits between the network firewall and the web
    servers
- Out of band (detection)
  - Device receives a mirrored copy of web server traffic
- Layer based Firewalls
  - Layer 4 Firewall

## Operates at the transport layer

## Filters traffic based on port numbers and protocol data

- Layer 7 Firewall

## Operates at the application layer

## Inspects, filters, and controls traffic based on content and data

characteristics

## Configuring Firewalls

- Firewalls and Access Control Lists (ACLs)
  - Firewalls

## Dedicated devices for using Access Control Lists (ACLs) to protect

networks

- Access Control Lists (ACLs)

## Essential for securing networks from unwanted traffic

## Consist of permit and deny statements, often based on port numbers

## Rule sets placed on firewalls, routers, and network infrastructure devices

## Control the flow of traffic into and out of networks

## May define quality of service levels inside networks but are primarily

used for network security in firewalls

- Configuring ACLs
  - A web-based interface or a text-based command line interface can be used
  - The order of ACL rules specifies the order of actions taken on traffic (top-down)
  - The first matching rule is executed, and no other ACLs are checked
  - Place the most specific rules at the top and generic rules at the bottom
  - Some devices support implied deny functions, while others require a “deny all”
    rule at the end
  - Actions taken by network devices should be logged, including deny actions
- ACL Rules
  - Made up of some key pieces of information including

## Type of traffic

## Source of traffic

## Destination of traffic

## Action to be taken against the traffic

- Firewall Types
  - Hardware-Based Firewall

## A dedicated network security device that filters and controls network

traffic at the hardware level

## Commonly used to protect an entire network or subnet by implementing

ACLs and rules

- Software-Based Firewall

## A firewall that runs as a software application on individual devices, such

as workstations

## Utilizes ACLs and rules to manage incoming and outgoing traffic,

providing security at the software level on a per-device basis

- Key Takeaway
  - Firewalls use ACLs to control network traffic, ensuring security by specifying
    permitted and denied actions
  - Proper ACL configuration and rule order are crucial for effective network
    protection

## IDS and IPS

- Key difference
  - IDS - Logs and alerts
  - IPS - Logs, alerts, and takes action
- Intrusion Detection Systems (IDS)
  - Logs or alerts that it found something suspicious or malicious
  - Three Types of Intrusion Detection Systems (IDS)

## Network-based IDS (NIDS)

- Monitors the traffic coming in and out of a network

## Host-based IDS (HIDS)

- Looks at suspicious network traffic going to or from a single or
  endpoint

## Wireless IDS (WIDS)

- Detects attempts to cause a denial of a service on a wireless
  network
  - Intrusion detection systems operate either using signature-based or
    anomaly-based detection algorithms

## Signature-based IDS

- Analyzes traffic based on defined signatures and can only
  recognize attacks based on previously identified attacks in its
  database
  - Pattern-matching

## Specific pattern of steps

## NIDS, WIDS

- Stateful-matching

## Known system baseline

## HIDS

## Anomaly-based IDS

- Analyzes traffic and compares it to a normal baseline of traffic to
  determine whether a threat is occurring
- Five Types of Anomaly-based Detection Systems
  - Statistical
  - Protocol
  - Traffic
  - Rule or Heuristic
  - Application-based
- Intrusion Prevention Systems (IPS)
  - Logs, alerts, and takes action when it finds something suspicious or malicious
  - Scans traffic to look for malicious activity and takes action to stop it

## Network Appliances

- Network Appliance
  - A dedicated hardware device with pre-installed software for specific networking
    services
- Different Types of Network Appliances
  - Load Balancers

## Distribute network/application traffic across multiple servers

## Enhance server efficiency and prevent overload

## Ensure redundancy and reliability

## Perform continuous health checks

## Application Delivery Controllers (ADCs) offer advanced functionality

## Essential for high-demand environments and high-traffic websites

- Proxy Servers

## Act as intermediaries between clients and servers

## Provide content caching, requests filtering, and login management

## Enhance request speed and reduce bandwidth usage

## Add a security layer and enforce network utilization policies

## Protect against DDoS attacks

## Facilitate load balancing and user authentication

## Handle data encryption and ensure compliance with data sovereignty

laws

- Sensors

## Monitor, detect, and analyze network traffic and data flow

## Identify unusual activities, security breaches, and performance issues

## Provide real-time insights for proactive network management

## Aid in performance monitoring and alerting

## Act as the first line of defense against cyber threats

- Jump Servers/Jump Box

## Secure gateways for system administrators to access devices in different

security zones

## Control access and reduce the attack surface area

## Offer protection against downtime and data breaches

## Simplify logging and auditing

## Speed up incident response during cyber-attacks

## Streamline system management and maintenance

## Host essential tools and scripts

## Monitor system health for performance and security

## Port Security

- Port Security
  - A network switch feature that restricts device access to specific ports based on
    MAC addresses
  - Enhances network security by preventing unauthorized devices from connecting
- Network Switches
  - Networking devices that operate at Layer 2 of the OSI model
  - Use MAC addresses for traffic switching decisions through transparent bridging
  - Efficiently prevent collisions, operate in full duplex mode
  - Remember connected devices based on MAC addresses
  - Broadcast traffic only to intended receivers, increasing security
- CAM Table (Content Addressable Memory)
  - Stores MAC addresses associated with switch ports
  - Vulnerable to MAC flooding attacks, which can cause the switch to fail open
- Port Security Implementation
  - Associate specific MAC addresses with interfaces
  - Prevent unauthorized devices from connecting
  - Can use Sticky MACs for easier setup
  - Susceptible to MAC spoofing attacks
- 802.1x Authentication
  - Provides port-based authentication for wired and wireless networks
  - Requires three roles

## Supplicant

## Authenticator

## Authentication server

- Utilizes RADIUS for actual authentication, typically using EAP
- Prevents rogue device access
- RADIUS vs. TACACS+
  - RADIUS is cross-platform, while TACACS+ is Cisco proprietary
  - TACACS+ is slower but offers additional security and independently handles
    authentication, authorization, and accounting
  - TACACS+ supports all network protocols, whereas RADIUS lacks support for some
- EAP (Extensible Authentication Protocol)
  - A framework for various authentication methods
  - Has different variants which have their own features

## EAP-MD5

- Uses simple passwords and the challenge handshake
  authentication process to provide remote access authentication
- One-way authentication process
- Doesn’t provide mutual authentication

## EAP-TLS

- Uses public key infrastructure with a digital certificate which is
  installed on both the client and the server
- Uses mutual authentication

## EAP-TTLS

- Requires a digital certificate on the server, but not on the client
- The client uses a password for authentication

## EAP-FAST

- Uses protected access credential, instead of a certificate, to
  establish mutual authentication

## PEAP

- Supports mutual authentication using server certificates and
  Active Directory databases to authenticate a password from the
  client

## EAP-LEAP

- Cisco proprietary and limited to Cisco devices
- Integration for Network Security
  - Combining port security, 802.1X, and EAP enhances network security
  - Ensures only authenticated and authorized devices can access sensitive resources

## Securing Network Communications

- Virtual Private Networks (VPNs)
  - Extend private networks across public networks
  - Allow remote users to securely connect to an organization’s network
  - Can be configured as site-to-site, client-to-site, or clientless VPNs

## Site-to-Site VPN

- Connects two sites cost-effectively
- Replaces expensive leased lines
- Utilizes a VPN tunnel over the public internet
- Encrypts and secures data between sites
- Slower, but more secure

## Client-to-Site VPN

- Connects a single host (e.g., laptop) to the central office
- Ideal for remote user access to the central network
- Options for full tunnel and split tunnel configurations

## Clientless VPN

- Uses a web browser to establish secure, remote-access VPN
- No need for dedicated software or hardware client
- Utilizes HTTPS and TLS protocols for secure connections to
  websites
  - In addition to site-to-site and client-to-site VPNs, we have to decide whether we
    are going to use a full tunnel or split tunnel VPN configuration

## Full Tunnel VPN

- Encrypts and routes all network requests through the VPN
- Provides high security, clients fully part of central network
- Limits access to local resources
- Suitable for remote access to central resources

## Split Tunnel VPN

- Divides traffic, routing some through the VPN, some directly to
  the internet
- Enhances performance by bypassing VPN for non-central traffic
- Less secure; potential exposure to attackers
- Recommended for better performance but requires caution on
  untrusted networks
- Transport Layer Security (TLS)
  - Provides encryption and security for data in transit
  - Used for secure connections in web browsers (HTTPS)
  - Uses Transmission Control Protocol (TCP) for secure connections between a client
    and a server

## may slow down the connection

- Datagram Transport Layer Security (DTLS)

## A faster User Datagram Protocol-based (UDP-based) alternative

## Ensures end-user security and protects against eavesdropping in clientless

VPN connections

## Ensures confidentiality, integrity, and authentication of data

- Internet Protocol Security (IPSec)
  - A secure protocol suite for IP communication
  - Provides confidentiality, integrity, authentication, and anti-replay protection
  - Used for both site-to-site and client-to-site VPNs
  - Five key steps in establishing an IPSec VPN

## Request to start the Internet Key Exchange (IKE)

- PC1 initiates traffic to PC2, triggering IPSec tunnel creation by
  RTR1

## Authentication - IKE Phase 1

- RTR1 and RTR2 negotiate security associations for the IPSec IKE
  Phase 1 (ISAKMP) tunnel

## Negotiation - IKE Phase 2

- IKE Phase 2 establishes a tunnel within the tunnel

## Data transfer

- Data transfer between PC1 and PC2 takes place securely

## Tunnel termination

- Tunnel torn down including the deletion of IPSec security
  associations
  - IPSec Tunneling Modes (Data transfer)

## Transport Mode

- Uses original IP header
- Suitable for client-to-site VPNs
- Avoids potential fragmentation issues from MTU constraints
  - MTU (Maximum Transmission Unit)

## set by default at 1500 bytes and may cause

fragmentation and other VPN problems

- Does not increase packet size

## Tunneling Mode

- Adds a new header to encapsulate the entire packet
- Ideal for site-to-site VPNs
- May increase packet size and require jumbo frames
- Provides confidentiality for both payload and header
  - Authentication Header (AH)

## Offers connectionless data integrity and data origin authentication for IP

datagrams using cryptographic hashes as identification information

- Encapsulating Security Payload (ESP)

## Provides confidentiality, integrity, and encryption

## Provides replay protection

## Encrypts the packet’s payload

- Considerations
  - Balance between security and performance when choosing VPN tunnel type
  - Use full tunnel VPNs for higher security but reduced local access
  - Use split tunnel VPNs for better performance but potentially lower security
  - Ensure proper MTU settings when using tunneling mode in site-to-site VPNs
  - AH for integrity and ESP for encryption in IPSec, but both can be used together
    for comprehensive security

## SD-WAN and SASE

- SD-WAN (Software-Defined Wide Area Network)
  - A virtualized approach to managing and optimizing wide area network
    connections
  - Purpose

## Efficiently routes traffic between remote sites, data centers, and cloud

environments

- Benefits

## Increased agility, security, and efficiency for geographically distributed

workforces

- Control

## Software-based architecture with control extracted from underlying

hardware

- Transport Services

## Allows the use of various transport services

- MPLS
- Cellular
- Microwave links
- Broadband internet
  - Centralized Control

## Utilizes centralized control function for intelligent traffic routing

- Traditional WAN vs. SD-WAN

## Traditional WANs

- Cannot efficiently integrate cloud services

## SD-WAN

- Enables dynamic and efficient routing, improving visibility,
  performance, and manageability
  - Use Cases

## Ideal for enterprises with multiple branch offices moving towards

cloud-based services

- IaaS
- PaaS
- SaaS
- SASE (Secure Access Service Edge)
  - A network architecture combining network security and WAN capabilities in a
    single cloud-based service
  - Purpose

## Addresses challenges of securing and connecting users and data across

distributed locations

- Key Technology

## Utilizes software-defined networking (SDN) for security and networking

services from the cloud

- Components

## Firewalls

## VPNs

## Zero-trust network access

## Cloud Access Security Brokers (CASBs)

- Policy and Management

## Delivered through a common set of policy and management platforms

- Cloud Providers

## Major cloud providers offer services aligned with SASE

## Examples:

- AWS VPC
- Azure Virtual WAN
- Azure ExpressRoutes
- Google Cloud Interconnect
- Google Cloud VPN

## Alignment

- These cloud services offer secure, flexible, and global networking
  capabilities, aligning with SASE principles
- Importance
  - As cyber threats evolve and organizations become more geographically
    dispersed, understanding and implementing SD-WAN and SASE are crucial for
    enhanced security and successful migration to cloud-based environments

## Infrastructure Considerations

- Device Placement
  - Proper placement of routers, switches, and access points is crucial
  - Correct placement ensures

## Optimal data flow,

## Minimizes latency

## Enhances security

- Routers at the network’s edge help filter traffic efficiently
- Strategic placement of access points ensures coverage and reduces interference
- Switches should be located for easy connection to network segments
- Security Zones and Screened Subnets
  - Security Zones

## Isolate devices with similar security requirements

- Screened Subnets

## Act as buffer zones between internal and external networks

## Hosts public-facing services, protecting core internal networks

## Use the term “screened subnet” instead of “DMZ” for modern

configurations

- Attack Surface
  - Refers to points where unauthorized access or data extraction can occur
  - A larger attack surface increases the risk of vulnerabilities
  - Identify and mitigate vulnerabilities to reduce the attack surface
  - Regularly assess and minimize the attack surface for network security
- Connectivity Methods
  - Choose connectivity methods that influence network performance, reliability,
    and security
  - Wired (e.g., Ethernet) offers stability and speed but restricts mobility
  - Wireless (e.g., Wi-Fi) provides flexibility but may suffer from interference and
    security issues
  - Consider factors like scalability, speed, security, and budget constraints when
    choosing connectivity methods
- Device Attributes
  - Consider whether devices are active or passive, and if they are inline or tapped
  - Active devices (e.g., intrusion prevention systems)

## monitor and act on network traffic.

- Passive devices (e.g., intrusion detection systems)

## observe and report without altering traffic

- Inline devices are in the path of network traffic
- Taps and monitors capture data without disruption
- Align device choices with network goals and challenges
- Failure Mode
  - Choose between “fail-open” and “fail-closed” modes to handle device failures
  - Fail-open

## Allows traffic to pass during a failure, maintaining connectivity but

reducing security

- Fail-closed

## Blocks all traffic during a failure, prioritizing security over connectivity

- The choice depends on the organization’s security policy and the criticality of the
  network segment

## Selecting Infrastructure Controls

- Control
  - A protective measure put in place to reduce potential risks and safeguard an
    organization’s assets
- Key Principles
  - Least Privilege

## Users and systems should have only necessary access rights to reduce the

attack surface

- Defense in Depth

## Utilize multiple layers of security to ensure robust protection even if one

control fails

- Risk-based Approach

## Prioritize controls based on potential risks and vulnerabilities specific to the

infrastructure

- Lifecycle Management

## Regularly review, update, and retire controls to adapt to the evolving

threat landscape

- Open Design Principle

## Ensure transparency and accountability through rigorous testing and

scrutiny of controls

- Methodology
  - Assess Current State

## Understand existing infrastructure, vulnerabilities, and current controls

- Gap Analysis

## Identify discrepancies between current and desired security postures

- Set Clear Objectives

## Define specific goals for adding new controls (data protection, uptime,

compliance, etc.)

- Benchmarking

## Compare your organization’s processes and security metrics with industry

best practices

- Cost-Benefit Analysis

## Evaluate the balance between desired security level and required

resources

- Stakeholder Involvement

## Engage relevant stakeholders to ensure controls align with business

operations

- Monitoring and Feedback Loops

## Continuously revisit control selection to adapt to evolving threats

- Best Practices
  - Conduct Risk Assessment

## Regularly assess threats and vulnerabilities specific to your organization,

and update it with significant changes

- Align with Frameworks

## Utilize established frameworks (e.g., NIST, ISO) to ensure comprehensive

and tested methodologies

- Customize Frameworks

## Tailor framework controls to your organization’s unique risk profile and

business operations

- Stakeholder Engagement and Training

## Engage all relevant stakeholders in the decision-making process, and

conduct regular training to keep the workforce updated on security
controls and threats
