# Application Security

-----

## Uses a Protected Access Credential and TLS tunnel

## Application Security

- Application Security
  - Focuses on building secure applications
  - Aims to prevent, detect, and remediate security vulnerabilities
- Six Key Areas in Application Security
  - Input Validation

## Ensures that applications process well-defined, secure data

## Guards against attacks exploiting data input vulnerabilities (e.g., SQL

injection, XSS, buffer overflows)

## Serves as a kind of quality control for data to ensure that every piece of

information is valid, secure, and correctly formatted

## Validation Rules

- Delineate acceptable and unacceptable inputs

## Validates data early in the process (front-end validation)

## Used with additional tools for defense in-depth

- Secure communication protocols
- Regular security auditing
- Implementing proper error handling
  - Cookies

## Small data pieces stored by web browsers

## Maintain stateful information between the server and client

## Secure Cookies

- Secure cookies are transmitted over HTTPS for enhanced security

## Best practices

- Refraining from persistent cookies for session verification
- Enabling the Secure attribute
- Enabling HttpOnly attribute
- Configuring the SameSite attribute
  - Static Code Analysis (SAST)

## A method of debugging an application by reviewing and examining its

source code before running the program

## Identifies issues like buffer overflows, SQL injection, and XSS

## Important for proper input validation in both front-end and back-end

code

- Dynamic Code Analysis (DAST)

## Analyzes applications while they run

## Common methods of DAST

- Fuzzing (Fuzz Testing)
  - Inputs random data to provoke crashes or exceptions
  - Helps uncover security flaws and weaknesses
- Stress Testing
  - Evaluates system stability and reliability under extreme
    conditions
  - Reveals bottlenecks and assesses system recovery
  - Code Signing

## Confirms the software author’s identity and integrity

## Utilizes digital signatures to verify code authenticity

## Protects against code tampering but doesn’t guarantee absence of

vulnerabilities

- Sandboxing

## Isolates running programs, limiting their access to resources

## Prevents harmful actions on the host device or network

## Used to execute untrusted or untested programs securely

## Network Access Control (NAC)

- Network Access Control (NAC)
  - Used to protect networks from both known and unknown devices by scanning
    devices to assess their security status before granting network access
  - Can be applied to devices within the internal network or those connecting
    remotely via VPN
  - NAC can be implemented as a hardware or software solution
- NAC Process
  - When a device attempts to connect, it is placed in a virtual holding area for
    scanning
  - Scanning checks various factors, including antivirus definitions, security patching,
    and potential security threats
  - If a device passes inspection, it is allowed network access
  - If a device fails inspection, it is placed in a digital quarantine area for remediation
- NAC Agent Types
  - Persistent Agents

## Installed on devices in a corporate environment where the organization

owns and controls device software

- Non-Persistent Agents

## Common in environments with personal devices (e.g., college campuses);

users connect, access a web-based captive portal, download an agent for
scanning, and delete itself after inspection

- 802.1x Standard
  - Port-based Network Access Control mechanism based on the IEEE 802.1x
    standard
  - Modern NAC solutions build on 802.1x, enhancing features and capabilities
- Rule-Based Access Control
  - In addition to health policy, NAC can use rule-based methods for access control

## Time-Based Factors

- Define access periods based on time schedules; may block access
  during non-working hours

## Location-Based Factors

- Evaluate the endpoint’s location using geolocation data to detect
  unusual login locations

## Role-Based Factors

- Reevaluate device authorization based on its role (adaptive NAC)

## Rule-Based Factors

- Implement complex admission policies with logical statements to
  determine access based on conditions

## Web and DNS Filtering

- Web Filtering
  - Web filtering or content filtering is used to control or restrict the content users
    can access on the internet
  - Crucial for businesses, educational institutions, and parents to ensure safe and
    productive internet use
- Different types of web filtering techniques
  - Agent-Based Web Filtering

## Involves installing an agent on each device

## Monitors and enforces web usage policies

## Effective for remote and mobile workers

- Centralized Proxy

## Uses a proxy server as an intermediary between an organization’s end

users and the Internet

## Evaluates and controls web requests based on policies

## If the request does not conform with the policies, the request is simply

blocked or denied

- URL Scanning

## Analyzes website URLs to check for matches in a database of known

malicious websites

- Content Categorization

## Classifies websites into categories (e.g., social media, adult content) and

blocks or allows categories based on policies

- Block Rules

## Specific guidelines set by organizations to prevent access to certain

websites or categories, often used to address security threats

- Reputation-Based Filtering

## Blocks or allows websites based on a reputation score determined by

third-party services, considering factors like hosting malware or phishing

- DNS Filtering
  - DNS filtering (Domain Name System filtering) blocks access to specific websites
    by preventing the translation of domain names to their IP addresses
  - Users’ devices request domain name translation from DNS servers; if the domain
    is on the block list, the server withholds the IP address to prevent access
  - Commonly used to enforce internet usage policies, block inappropriate content,
    and protect against malicious websites
  - Often employed by schools, universities, and organizations to ensure safe and
    educational internet usage

## Email Security

- Email Security
  - Encompasses techniques and protocols to protect email content, accounts, and
    infrastructure from unauthorized access, loss, or compromise
- Key email security techniques
  - DKIM (DomainKeys Identified Mail)

## Allows the receiver to verify the source and integrity of an email by

adding a digital signature to the email headers

## The recipient server validates the DKIM signature using the sender’s

public cryptographic key in the domain’s DNS records

## Benefits

- Email authentication
- Protection against email spoofing
- Improved email deliverability
- Enhanced reputation score
  - SPF (Sender Policy Framework)

## Prevents sender address forgery by verifying the sender’s IP against

authorized IPs listed in the sender’s domain DNS records

## A receiving server checks if the sender’s IP is authorized in the SPF record

before accepting the email

## Benefits

- Preventing email spoofing
- Improving email deliverability
- Enhancing the domain’s reputation
  - DMARC (Domain-based Message Authentication, Reporting and Conformance)

## DMARC detects and prevents email spoofing by setting policies for email

sending and handling failures

## DMARC can work with DKIM, SPF, or both

## Implementation helps protect against

- Business email compromise attacks
- Phishing
- Scams
- Cyber threats
  - Email Gateway Protocol Configuration

## Email gateways serve as entry and exit points for emails, facilitating

secure and efficient email transmission

## They use SMTP (Simple Mail Transfer Protocol) to send and receive emails

## Email gateways handle email routing, email security, policy enforcement,

and email encryption

## Email Gateway Deployment Options

- On-Premises Email Gateway
  - A physical server located within an organization’s
    premises, offering full control but requiring maintenance
    and updates
- Cloud-Based Email Gateway
  - Hosted by third-party cloud service providers, providing
    scalability but limited control over configurations
- Hybrid Email Gateway
  - Combines on-premises and cloud-based gateways for a
    balance between control and convenience
- Spam Filtering
  - Spam filtering detects and prevents unwanted and unsolicited emails from
    reaching users’ inboxes
  - Techniques

## Content analysis

## Bayesian filtering

## DNS-based sinkhole list

## Email filtering rules

- Emails with spam-like keywords are flagged and often moved to the spam folder

## Endpoint Detection and Response

- Endpoint Detection and Response (EDR)
  - Category of security tools that monitor endpoint and network events and record
    the information in a central database
  - Continuously monitoring and response to advanced threats
  - Monitors endpoint and network events, providing data for the following

## Analysis

## Detection

## Investigation

## Reporting

## Alerting

- Focuses on incident data for enhancing security monitoring, incident response,
  and forensic investigations
- How EDR Works
  - Data Collection

## Collects data from endpoints (devices that are physically on the endpoint

of a network)

- System processes
- Registry changes
- Memory usage
- Network traffic patterns
  - Data Consolidation

## Sends collected data to a centralized security solution or database

- Threat Detection

## Analyzes data using techniques like signature-based and behavioral-based

detection to identify threats

- Alerts and Threat Response

## Takes actions such as creating alerts or performing threat response

actions when threats are detected

- Threat Investigation

## Provides tools for security teams to investigate threats, including detailed

timelines and forensic data

- Remediation

## Removing malicious files

## Reversing changes

## Restoring systems to their normal state

- File Integrity Monitoring (FIM)
  - Validates the integrity of operating system and application software files by
    comparing their current state with a known, good baseline
  - Identifies changes to

## Binary files

## System and Application Files

## Configuration and Parameter Files

- Monitors critical system files for changes using agents and hash digests,
  triggering alerts when unauthorized changes occur
- Extended Detection and Response (XDR)
  - Security strategy that integrates multiple protection technologies into a single
    platform
  - Improves detection accuracy and simplified incident response
  - Correlates data across multiple security layers to detect threats faster, including

## email

## endpoint

## server

## cloud workloads

## network

- Difference between EDR and XDR
  - EDR is focused on the endpoints to detect and respond to potential threats
  - XDR is more comprehensive solution because it focuses on endpoints, but also
    on networks, cloud, and email to detect and respond to potential threats

## It integrates multiple protection technologies

## User Behavior Analytics

- User Behavior Analytics (UBA)
  - Advanced cybersecurity strategy that uses big data and machine learning to
    analyze user behaviors for detecting security threats
  - Focuses on understanding user behavior within systems and networks to identify
    patterns and anomalies
- User and Entity Behavior Analytics (UEBA)
  - Technology similar to UBA but extends the monitoring of entities like routers,
    servers, and endpoints in addition to user accounts
  - Enhances security by analyzing both user and entity behavior to detect
    anomalies
- Key Aspects of UBA and UEBA
  - UBA leverages data analytics to collect and analyze user behavior data to
    establish normal behavior baselines

## Knowing the baseline makes it easier to spot anomalies

- Machine learning algorithms are used to identify deviations from normal
  behavior, which may indicate security threats
- UBA systems process data from various sources

## Network traffic

## User devices

## Application logs

- Alerts are generated when anomalies are detected, which are then investigated
  by the security team
- Benefits of UBA and UEBA
  - Early Detection of Threats

## UBA tools can identify potential threats before significant damage occurs,

allowing for quicker and more effective responses

- Insider Threat Detection

## Effective at identifying insider threats by detecting suspicious activities

that deviate from typical behavior

- Improved Incident Response

## Provides detailed information about user behavior, helping security teams

respond effectively to incidents, such as compromised credentials or
unauthorized actions

## Selecting Secure Protocols

- Secure Protocols
  - Choose secure protocols to protect data in transit from unauthorized access

## Examples include HTTP vs. HTTPS, FTP vs. SFTP, Telnet vs. SSH

- Secure protocols use encryption to safeguard data during transmission
- Telnet

## Application layer protocol that allows a user on one computer to log onto

another computer that is part of the same network

## Transmits in plaintext

## Use SSH instead

- Always use the encrypted version of the protocol

## Examples

- HTTPS
- SFTP
- SSH
- IMAPS
- POP3S
- SMTPS
- SNMPS
- Port Selection
  - Ports are logical constructs used to identify processes or services on a system
  - Categorized into the following

## Well-known ports (0-1023)

## Registered ports (1024-49151)

## Dynamic/private ports (49152-65535)

- Default port numbers often indicate whether a protocol is secure (e.g., HTTP on
  port 80 vs. HTTPS on port 443)
- Additional security considerations

## Follow the principle of least privilege by opening only necessary ports to

minimize the attack surface

## Changing port numbers can add a layer of obscurity but should not

replace robust security measures

- Transport Methods
  - Choose a transport method (TCP or UDP) based on the application’s needs
  - TCP (Transmission Control Protocol)

## Connection-oriented, ensuring data delivery without errors

## Ideal for applications where data accuracy is crucial, like web and email

servers

## Uses acknowledgments, retransmission, and sequencing for data integrity

- UDP (User Datagram Protocol)

## Connectionless and faster, but doesn’t guarantee data delivery

## Suitable for applications prioritizing speed over accuracy, like streaming

video or gaming
