---
layout: objective
title: "Security+ 3.1 — Compare and contrast security implications of different architecture models."
objective_id: "3.1"
domain: "3.0 Security Architecture"
status: "done"
tags:
  - secplus701
permalink: /secplus/objectives/3-1/
---

# Security+ 3.1 — Compare and contrast security implications of different architecture models.

Status: <span class="status-badge done">done</span>

## Exam objective
Compare and contrast security implications of different architecture models.

{% include official_scope_pdf.html objective_id=page.objective_id %}

---

## My notes

### Overview

Architecture decisions determine an organization's security posture, scalability, and operational complexity. This objective covers deployment models (on-premise vs. cloud), virtualization technologies, modern architectures (serverless, microservices, SDN, IaC), specialized systems (IoT, ICS/SCADA, embedded), and centralized vs. decentralized approaches. The exam focuses on understanding the security trade-offs of each model.

---

### On-premise vs. cloud deployment

| Aspect | On-Premise | Cloud |
|---|---|---|
| **Control** | Full control over infrastructure | Shared responsibility with provider |
| **Security** | Organization fully responsible | Provider handles infrastructure security |
| **Cost model** | High upfront CapEx | Pay-as-you-go OpEx |
| **Scalability** | Limited by physical capacity | Elastic scaling on demand |
| **Patching** | Manual; org controls timing | Provider manages infrastructure patches |
| **Availability** | Dependent on org infrastructure | Provider SLAs (typically 99.9%+) |
| **Disaster recovery** | Org implements and tests | Provider offers built-in redundancy |
| **Compliance** | Full data sovereignty | May require specific regions/certifications |

**Hybrid solutions** combine on-premise, private cloud, and public cloud, allowing workload flexibility. Critical for meeting regulatory requirements while maintaining operational agility.

---

### Cloud security considerations

| Risk | Description | Mitigation |
|---|---|---|
| **Shared physical servers** | Multi-tenancy means multiple customers share hardware | Strong hypervisor isolation, regular vulnerability scanning |
| **Inadequate virtual security** | Weak VM configurations expose data | Secure VM templates, network segmentation, monitoring |
| **User access management** | Weak IAM leads to unauthorized access | Strong passwords, MFA, least privilege, activity monitoring |
| **Lack of updates** | Dynamic environments require current security measures | Automated patching, policy reviews, threat intelligence |
| **Single point of failure** | Dependence on specific resources causes outages | Redundancy, failover procedures, multi-region deployment |
| **Weak authentication** | Poor auth/encryption exposes systems | MFA, strong encryption algorithms, key management |
| **Unclear policies** | Inconsistent security implementation | Comprehensive policies covering data handling, access control, incident response |
| **Data remnants** | Residual data after deletion | Secure deletion procedures, cryptographic erasure, backup management |

**Shared responsibility model** — cloud provider secures the infrastructure; customer secures data, applications, and access management.

---

### Virtualization and containerization

**Virtualization** — emulates complete servers with full OS instances running in virtual machines (VMs).

**Containerization** — lightweight alternative encapsulating apps with minimal OS environment.

| Feature | Virtualization | Containerization |
|---|---|---|
| **Isolation** | Full OS isolation per VM | Process-level isolation |
| **Resource overhead** | High (each VM = full OS) | Low (shared kernel) |
| **Startup time** | Minutes | Seconds |
| **Portability** | Less portable (hypervisor-dependent) | Highly portable (Docker, Kubernetes) |
| **Use case** | Strong isolation for different OS needs | Microservices, rapid deployment |

**Hypervisors:**
- **Type 1 (Bare Metal)** — runs directly on hardware (Hyper-V, ESXi, XenServer). More secure, better performance.
- **Type 2 (Hosted)** — runs on a host OS (VirtualBox, VMware Workstation). Easier to deploy, less performant.

**Virtualization vulnerabilities:**
- **VM Escape** — attacker breaks out of a VM to access the hypervisor or host.
- **Privilege Escalation** — unauthorized elevation within the virtualized environment.
- **Live VM Migration** — attacker intercepts unencrypted data during VM transfer between hosts.
- **Resource Reuse** — improper clearing of memory/storage exposes previous tenant data.
- **Virtualization Sprawl** — uncontrolled proliferation of VMs increases attack surface and management complexity.

**Container technologies:** Docker, Kubernetes, Red Hat OpenShift.

---

### Serverless computing

Serverless does not mean "no servers" — it means the cloud provider manages server allocation and scaling automatically.

**Functions as a Service (FaaS)** — developers write individual functions triggered by events (HTTP requests, database changes, timers).

| Benefit | Risk |
|---|---|
| Reduced operational costs (pay only for execution time) | Vendor lock-in (proprietary APIs) |
| Automatic scaling based on demand | Immaturity of best practices |
| Faster time to market | Limited control over execution environment |
| No server management overhead | Cold start latency for infrequently-used functions |

**Security considerations:** Limited visibility into underlying infrastructure, reliance on provider security, potential for function-level attacks, secrets management complexity.

---

### Microservices architecture

Breaks large applications into small, independent services that communicate via APIs. Contrasts with monolithic architecture where all components are interconnected.

| Advantage | Challenge |
|---|---|
| **Scalability** — services scale independently | **Complexity** — managing inter-service communication, distributed systems testing |
| **Flexibility** — different tech stacks per service | **Data management** — each service may have own database; consistency challenges |
| **Resilience** — failure isolation reduces blast radius | **Network latency** — increased communication overhead |
| **Fast deployment** — independent updates | **Security** — larger attack surface due to more endpoints |

**Security implications:** Each service is a potential entry point. Requires API gateway security, service mesh for encrypted inter-service communication, distributed authentication/authorization.

---

### Software-Defined Network (SDN)

Decouples network control from data forwarding, enabling centralized, programmable network management.

**Three planes:**

| Plane | Function |
|---|---|
| **Data Plane** | Handles actual packet forwarding based on rules |
| **Control Plane** | Centralized decision-making; dictates traffic flow across the network |
| **Application Plane** | Network applications that interact with SDN controller |

**Benefits:** Dynamic configuration, centralized visibility, improved monitoring, reduced complexity.

**Security risks:** If the centralized controller is compromised, the entire network is at risk. Requires strong controller hardening, access controls, encrypted control channels.

---

### Infrastructure as Code (IaC)

Automates infrastructure provisioning and management through code files (YAML, JSON, HCL).

**Idempotence** — running the same IaC script multiple times produces the same result. Critical for consistency across dev, staging, and production.

| Benefit | Challenge |
|---|---|
| Speed and efficiency | Learning curve for teams |
| Consistency and standardization | Code complexity |
| Scalability | Security risks (credentials in code, insecure defaults) |
| Auditability and compliance (version control) | Sensitive data exposure |

**Security best practices:** Never hardcode credentials, use secret management tools (HashiCorp Vault, AWS Secrets Manager), code review for security misconfigurations, automated scanning for vulnerabilities in IaC templates.

---

### Centralized vs. decentralized architectures

**Centralized:** All functions managed from a single location (mainframe, central data center).

| Benefit | Risk |
|---|---|
| Efficiency and control | Single point of failure |
| Data consistency | Scalability issues |
| Cost-effective maintenance | Attractive target for attackers |

**Decentralized:** Functions distributed across multiple independent nodes.

| Benefit | Risk |
|---|---|
| Resilience (no single point of failure) | Security risks (distributed endpoints) |
| Scalability (add nodes as needed) | Management complexity |
| Flexibility for remote/distributed teams | Data inconsistency and synchronization challenges |

**Blockchain** is an example of extreme decentralization — distributed ledger with no central authority.

---

### Internet of Things (IoT)

Network of physical devices with sensors, software, and connectivity enabling data exchange.

**Components:**
- **Hub/Control System** — centralizes data collection and device management.
- **Smart Devices** — everyday objects with computing capabilities (smart thermostats, appliances).
- **Wearables** — body-worn devices (fitness trackers, smartwatches).
- **Sensors** — detect environmental changes and convert to data.

**IoT security risks:**
- **Weak default settings** — unchanged default credentials are common attack vector.
- **Poorly configured network services** — open ports, unencrypted communications, unnecessary services.
- **Outdated firmware** — IoT devices rarely receive timely security patches.
- **Physical access** — many IoT devices are physically accessible to attackers.
- **Limited computing resources** — constraints prevent robust encryption or authentication.

**Mitigations:** Change defaults immediately, segment IoT devices on separate VLANs, disable unused services, implement network-level monitoring, use IoT-specific security frameworks.

---

### Industrial Control Systems (ICS) and SCADA

**ICS** — systems monitoring and controlling industrial processes (manufacturing, power plants, water treatment).

**SCADA** — subset of ICS designed for geographically dispersed processes (electric grid, pipelines, water distribution).

**ICS components:**
- **Distributed Control Systems (DCS)** — control production at a single location.
- **Programmable Logic Controllers (PLCs)** — control specific processes like assembly lines.

**Risks:**
- **Unauthorized access** — attackers manipulating critical infrastructure.
- **Malware** — Stuxnet demonstrated real-world ICS sabotage.
- **Lack of updates** — many ICS systems run outdated, unpatched software.
- **Physical threats** — damage to hardware or facilities.

**Security measures:**
- Strong access controls (MFA, role-based access)
- Air-gapping critical systems from corporate networks
- Regular patching (during maintenance windows)
- Intrusion detection specifically tuned for ICS protocols
- Employee training on ICS-specific threats

---

### Embedded systems

Specialized computing components designed for dedicated functions within larger devices (medical equipment, automotive systems, avionics).

**Real-Time Operating System (RTOS)** — designed for time-critical applications with minimal processing delays (flight navigation, pacemakers).

**Risks:**
- **Hardware failure** — harsh environmental conditions.
- **Software bugs** — can cause malfunctions and safety risks.
- **Security vulnerabilities** — limited patching capabilities.
- **Outdated systems** — long lifecycles mean old, vulnerable software.

**Security strategies:**
- Network segmentation (isolate embedded systems)
- Wrappers like IPSec to protect data in transit
- Firmware code control and integrity verification
- Over-the-Air (OTA) updates with strong authentication

**Patching challenges:** Embedded systems often cannot be easily updated due to operational constraints, certification requirements, or lack of vendor support.

---

### Key distinctions to know for the exam

| Comparison | Distinction |
|---|---|---|
| **On-premise vs. Cloud** | On-premise = full control, high upfront cost; Cloud = shared responsibility, pay-as-you-go |
| **VM vs. Container** | VM = full OS per instance, strong isolation; Container = shared kernel, lightweight, faster startup |
| **Type 1 vs. Type 2 Hypervisor** | Type 1 runs on bare metal (more secure); Type 2 runs on host OS (easier deployment) |
| **Serverless vs. Traditional** | Serverless = no server management, event-driven; Traditional = org manages servers |
| **Monolithic vs. Microservices** | Monolithic = single codebase; Microservices = independent services with API communication |
| **SDN vs. Traditional Networking** | SDN = centralized control plane, programmable; Traditional = distributed control in each device |
| **Centralized vs. Decentralized** | Centralized = single authority, efficiency; Decentralized = distributed control, resilience |
| **IoT vs. Embedded Systems** | IoT = network-connected consumer devices; Embedded = dedicated function in larger systems |
| **ICS vs. SCADA** | ICS = general industrial control; SCADA = geographically dispersed ICS subset |

---

### Common exam traps

**Trap: Thinking serverless is more secure because there are no servers to manage.**
Reality: Serverless shifts responsibility to the provider for infrastructure but introduces new risks — limited visibility, vendor lock-in, and function-level vulnerabilities still exist.

**Trap: Assuming containers provide the same isolation as VMs.**
Reality: Containers share the host kernel — a kernel exploit can affect all containers. VMs have full OS isolation via the hypervisor.

**Trap: Believing cloud is always less secure than on-premise.**
Reality: Major cloud providers have enterprise-grade security that most organizations cannot match on-premise. Security is about how you configure and manage the environment, not the deployment model itself.

**Trap: Treating IaC as inherently secure because it's automated.**
Reality: IaC can codify insecure configurations and expose secrets if not properly managed. Automation amplifies both good and bad security practices.

**Trap: Thinking centralized is always worse than decentralized for security.**
Reality: Centralized offers better control and consistency; decentralized offers resilience. Each has trade-offs — the "right" choice depends on threat model and requirements.

---

### Exam tips

1. Questions comparing on-premise vs. cloud will test whether you understand the **shared responsibility model** — provider secures infrastructure, customer secures data and applications.
2. Virtualization questions focus on **VM escape** and **resource reuse** as the top risks. Hypervisor security is critical.
3. For microservices, the exam emphasizes the **increased attack surface** — more services = more potential entry points.
4. SDN questions often ask about the risk of **centralized controller compromise** — a single point of control means a single point of failure if not secured.
5. IoT security always involves **default credentials** and **network segmentation** as primary mitigations.
6. ICS/SCADA questions emphasize **air-gapping** and the difficulty of patching operational technology.

---

## Key terms

- **On-Premise** — Infrastructure physically located and managed at the organization's facilities.
- **Cloud Computing** — Delivery of computing services (servers, storage, databases) over the internet.
- **Hybrid Solution** — Combination of on-premise, private cloud, and public cloud infrastructure.
- **Shared Responsibility Model** — Security division between cloud provider (infrastructure) and customer (data, applications, access).
- **Virtualization** — Running multiple virtual machines on a single physical host, each with its own OS.
- **Containerization** — Lightweight application packaging with minimal OS dependencies; shared kernel.
- **Hypervisor** — Software managing virtual machines. Type 1 = bare metal; Type 2 = hosted on OS.
- **VM Escape** — Attack breaking out of a VM to access the hypervisor or host system.
- **Virtualization Sprawl** — Uncontrolled proliferation of VMs increasing management complexity and risk.
- **Serverless** — Cloud model where provider manages server allocation; developers write event-driven functions.
- **Functions as a Service (FaaS)** — Serverless execution model for individual, event-triggered functions.
- **Microservices** — Architecture breaking applications into small, independent services communicating via APIs.
- **Software-Defined Network (SDN)** — Network architecture decoupling control plane from data plane for centralized management.
- **Infrastructure as Code (IaC)** — Automating infrastructure provisioning through code files; enables version control and consistency.
- **Idempotence** — Property where running the same operation multiple times produces identical results.
- **Centralized Architecture** — All functions managed from a single location or authority.
- **Decentralized Architecture** — Functions distributed across multiple independent nodes.
- **Internet of Things (IoT)** — Network of physical devices with embedded sensors and internet connectivity.
- **Industrial Control Systems (ICS)** — Systems monitoring and controlling industrial processes.
- **SCADA** — Supervisory Control and Data Acquisition; ICS subset for geographically dispersed systems.
- **Embedded Systems** — Specialized computers designed for dedicated functions within larger devices.
- **Real-Time Operating System (RTOS)** — OS designed for time-critical applications with minimal delays.

---

## Examples / scenarios

**Scenario 1:** A company is migrating from on-premise servers to AWS. The security team is concerned about who is responsible for patching the operating systems on EC2 instances.
- **Answer:** Under the shared responsibility model, AWS secures the underlying infrastructure (hypervisor, physical hardware). The customer is responsible for patching the guest OS on EC2 instances, configuring security groups, and managing access.

**Scenario 2:** An e-commerce platform uses microservices architecture with 25 independent services communicating via REST APIs. Each service has its own database and can be deployed independently.
- **Answer:** Security implications — increased attack surface (25 potential entry points), need for API gateway with authentication, service mesh for encrypted inter-service communication, distributed logging and monitoring. Advantage: failure of one service does not take down the entire platform.

**Scenario 3:** An attacker exploits a vulnerability in a container's application and gains access to the host kernel, affecting other containers on the same host.
- **Answer:** This demonstrates the shared kernel risk of containerization. Unlike VMs with full OS isolation, containers sharing a compromised kernel are all at risk. Mitigation: kernel hardening, container security scanning, runtime protection (Falco, Aqua).

**Scenario 4:** A power plant uses SCADA to monitor grid operations across hundreds of miles of transmission lines. The system runs Windows XP with proprietary software that cannot be upgraded.
- **Answer:** Classic ICS/SCADA challenge — air-gap the SCADA network from corporate network, implement strict access controls, use one-way data diodes for data export, deploy ICS-specific IDS, and compensate for inability to patch with network-level protections.

**Scenario 5:** A smart home system uses 30 IoT devices (lights, cameras, locks, thermostat). All devices came with default username "admin" and password "admin123."
- **Answer:** Critical IoT vulnerability. Mitigation steps: (1) Change all default credentials immediately, (2) Segment IoT devices on a dedicated VLAN isolated from trusted network, (3) Disable UPnP and unnecessary services, (4) Implement network monitoring for anomalous IoT traffic.

---

## Mini quiz

<details>
<summary><strong>Question 1:</strong> Explain the shared responsibility model in cloud computing. Who is responsible for what?</summary>

**Answer:** The cloud provider secures the infrastructure (physical data centers, hypervisor, network infrastructure, power/cooling). The customer secures their data, applications, operating systems (in IaaS), access management, and configurations. The exact division depends on the service model — in SaaS, the provider handles more; in IaaS, the customer handles more.
</details>

<details>
<summary><strong>Question 2:</strong> What is VM escape, and why is it the most serious virtualization vulnerability?</summary>

**Answer:** VM escape is when an attacker breaks out of a virtual machine's isolation to access the underlying hypervisor or host system. It is critical because successful VM escape gives the attacker access to all VMs on that host, not just the compromised one. It defeats the fundamental security boundary of virtualization.
</details>

<details>
<summary><strong>Question 3:</strong> What security advantage does centralized architecture have over decentralized, and what is its major risk?</summary>

**Answer:** Advantage: Better control, consistency, and easier security policy enforcement. All data and systems are in one place for monitoring and protection. Risk: Single point of failure — if the central system is compromised, the entire organization is at risk. Also, outages affect everything.
</details>

<details>
<summary><strong>Question 4:</strong> Why is patching particularly challenging for ICS/SCADA systems?</summary>

**Answer:** ICS/SCADA systems often run 24/7 with no downtime windows, use proprietary or outdated software with limited vendor support, require extensive testing before patches (safety certification), and may have hardware constraints that prevent updates. Many systems are decades old and cannot be easily replaced.
</details>

<details>
<summary><strong>Question 5:</strong> What is idempotence in Infrastructure as Code, and why does it matter for security?</summary>

**Answer:** Idempotence means running the same IaC script multiple times produces identical infrastructure. This ensures consistency across dev, staging, and production environments — no configuration drift. For security, it means security configurations are reliably applied and can be version-controlled, audited, and rolled back if needed.
</details>

### CompTIA-style practice questions

<details>
<summary><strong>Question 6:</strong> A financial services company is evaluating cloud deployment models. They need full control over encryption keys and must keep all customer data within national borders due to regulatory requirements. Which deployment model BEST meets these requirements?<br>A. Public cloud (multi-tenant)<br>B. Private cloud (on-premise or dedicated hosting)<br>C. Serverless (FaaS)<br>D. Community cloud</summary>

**Correct Answer: B. Private cloud (on-premise or dedicated hosting)**

Private cloud provides full control over infrastructure, encryption keys, and data location while still offering cloud-like automation and scalability. Public cloud multi-tenant (A) does not guarantee data sovereignty or key control. Serverless (C) is a compute model, not a deployment model. Community cloud (D) is shared among organizations with similar requirements but does not provide the exclusive control needed here.
</details>

<details>
<summary><strong>Question 7:</strong> An organization uses Infrastructure as Code (IaC) to provision cloud resources. During a security audit, auditors find database credentials hardcoded in Terraform configuration files stored in a Git repository. What is the MOST significant risk?<br>A. Infrastructure drift between environments<br>B. Exposure of sensitive credentials to anyone with repository access<br>C. Inability to roll back infrastructure changes<br>D. Lack of idempotence in deployments</summary>

**Correct Answer: B. Exposure of sensitive credentials to anyone with repository access**

Hardcoded credentials in version-controlled IaC files expose them to developers, auditors, and potentially attackers if the repo is compromised or accidentally made public. This is a critical security violation. Infrastructure drift (A) is about consistency, not credential exposure. Rollback (C) is still possible. Lack of idempotence (D) is not the primary concern here.
</details>

<details>
<summary><strong>Question 8 (Multi-select):</strong> An organization is securing its IoT deployment of smart building sensors and controllers. Which TWO actions provide the MOST effective security improvement? (Choose TWO)<br>A. Air-gap all IoT devices from any network connection<br>B. Change default credentials on all IoT devices<br>C. Segment IoT devices on a separate VLAN isolated from corporate network<br>D. Install antivirus software on each IoT device<br>E. Require all IoT devices to use WPA3 encryption</summary>

**Correct Answers: B. Change default credentials on all IoT devices and C. Segment IoT devices on a separate VLAN isolated from corporate network**

Changing default credentials (B) addresses the most common IoT attack vector. Network segmentation (C) limits the blast radius if an IoT device is compromised. Air-gapping (A) defeats the purpose of IoT connectivity. Most IoT devices lack the resources for antivirus (D). WPA3 (E) helps but is not as fundamental as B and C.
</details>

---

## Related objectives

- [**1.2**]({{ '/secplus/objectives/1-2/' | relative_url }}) — Zero Trust architecture principles apply across all deployment models.
- [**2.5**]({{ '/secplus/objectives/2-5/' | relative_url }}) — Mitigation techniques (segmentation, patching, access controls) apply to each architecture type differently.
- [**3.2**]({{ '/secplus/objectives/3-2/' | relative_url }}) — Security principles for infrastructure build on the architecture models covered here.
- [**4.1**]({{ '/secplus/objectives/4-1/' | relative_url }}) — Applying security techniques to computing resources depends on the underlying architecture.

---

## Navigation

**Domain 3.0: Security Architecture**

| Objective | Title | Status |
|---|---|---|
| **3.1** | Compare and contrast security implications of different architecture models. (current) | done |
| [3.2]({{ '/secplus/objectives/3-2/' | relative_url }}) | Given a scenario, apply security principles to secure enterprise infrastructure. | done |
| [3.3]({{ '/secplus/objectives/3-3/' | relative_url }}) | Compare and contrast concepts and strategies to protect data. | done |
| [3.4]({{ '/secplus/objectives/3-4/' | relative_url }}) | Explain the importance of resilience and recovery in security architecture. | done |

[← Previous: Domain 2]({{ '/secplus/objectives/2-5/' | relative_url }}) | [Back to Dashboard]({{ '/secplus/' | relative_url }}) | [Next: Objective 3.2 →]({{ '/secplus/objectives/3-2/' | relative_url }})
