---
layout: default
title: "Security+ 1.4 — Explain the importance of using appropriate cryptographic solutions."
objective_id: "1.4"
domain: "1.0 General Security Concepts"
status: "done"
tags:
  - secplus701
permalink: /secplus/objectives/1-4/
---

# Security+ 1.4 — Explain the importance of using appropriate cryptographic solutions.

Status: <span class="status-badge done">done</span>

## Exam objective
Explain the importance of using appropriate cryptographic solutions.

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

### What is Cryptography?

**Definition**: Practice and study of writing and solving codes to hide information's true meaning

**Why Critical for Security**:
- Protects confidentiality (CIA Triad)
- Ensures integrity
- Provides authentication
- Enables non-repudiation
- Secures communications

**Two Main Operations**:
- **Encryption**: Converts plaintext → ciphertext
- **Decryption**: Converts ciphertext → plaintext

---

### Encryption Fundamentals

#### Data States (Where to Encrypt)

##### 1. Data at Rest
**Definition**: Inactive data stored on physical or electronic media

**Examples**:
- Files on hard drive
- Database records
- Backup tapes
- USB drives
- Mobile device storage

**Encryption Solutions**:
- Full disk encryption (BitLocker, FileVault)
- Database encryption (TDE — Transparent Data Encryption)
- File-level encryption
- Encrypted archives

**Why Important**: Protects against physical theft, unauthorized access

---

##### 2. Data in Transit
**Definition**: Data actively moving across networks or between systems

**Examples**:
- Email messages
- Web traffic (HTTPS)
- File transfers (SFTP)
- VPN tunnels
- API calls

**Encryption Solutions**:
- TLS/SSL (HTTPS)
- IPSec (VPN)
- SSH
- S/MIME (email)

**Why Important**: Prevents eavesdropping, man-in-the-middle attacks

---

##### 3. Data in Use
**Definition**: Data currently being processed or actively accessed

**Examples**:
- Data in RAM
- Data being processed by CPU
- Active database queries
- Real-time encryption/decryption

**Encryption Solutions**:
- Secure enclaves
- Trusted Execution Environments (TEE)
- Homomorphic encryption (allows computation on encrypted data)

**Why Important**: Protects against memory dumps, process inspection

**Exam Tip**: Know ALL THREE states — exam commonly asks "which state?"

---

#### Algorithm vs Key

##### Algorithm (Cipher)
- **What**: Mathematical process for encryption/decryption
- **Examples**: AES, RSA, SHA-256
- **Public Knowledge**: Algorithms are well-known
- **Security**: Doesn't rely on keeping algorithm secret

**Kerckhoffs's Principle**: Security should rely on the KEY, not the secrecy of the algorithm

##### Key
- **What**: Secret value used by algorithm
- **Determines**: Specific cipher output
- **Must be**: Kept secret
- **Provides**: Actual security

**Analogy**:
- Algorithm = Lock design (everyone knows how it works)
- Key = Unique key that opens the lock (only you have it)

---

#### Key Strength and Security

##### Key Length
- **Relationship**: Longer key = More security
- **Why**: More possible combinations to try (brute force)

**Common Key Sizes**:
- **Symmetric**: 128-bit, 192-bit, 256-bit (AES)
- **Asymmetric**: 2048-bit, 3072-bit, 4096-bit (RSA)
- **ECC**: 256-bit, 384-bit (equivalent to 3072-bit RSA)

**Brute Force Reality**:
- 128-bit key = 2^128 possible combinations (practically unbreakable)
- 256-bit key = 2^256 combinations (absurdly secure)

##### Key Rotation
- **Definition**: Regularly changing encryption keys
- **Why**: Limits exposure if key compromised
- **Best Practice**: Rotate periodically
- **Frequency**: Based on sensitivity and regulations

**Benefits**:
- Limits damage from compromise
- Reduces cryptanalysis risk
- Meets compliance requirements

---

### Symmetric vs Asymmetric Encryption

#### Symmetric Encryption

**Definition**: Uses SAME key for both encryption and decryption

**Also Called**: Private key encryption, secret key encryption

**How It Works**:
```
Alice encrypts with Key-X → Sends ciphertext → Bob decrypts with Key-X
```

**Characteristics**:
- **FAST**: Much faster than asymmetric
- **Efficient**: Good for large data volumes
- **Key Distribution Problem**: How to share key securely?
- **Scalability Issue**: N users = N(N-1)/2 keys needed

**Security Provided**:
- Confidentiality
- **NO** non-repudiation (both parties have same key)

**Common Algorithms**:
- AES (Advanced Encryption Standard)
- DES (Data Encryption Standard) — DEPRECATED
- 3DES (Triple DES)
- Blowfish, Twofish
- RC4 (stream cipher) — DEPRECATED

**Best Use Cases**:
- Encrypting large amounts of data
- Disk encryption
- Database encryption
- When key sharing is already solved

**Exam Keyword**: "Symmetric = Same key = Shared secret = Fast"

---

#### Asymmetric Encryption

**Definition**: Uses TWO mathematically related keys (key pair)

**Also Called**: Public key cryptography

**The Key Pair**:
- **Public Key**: Shared openly, anyone can have it
- **Private Key**: Kept secret, never shared

**How It Works**:
```
Confidentiality:
  Alice encrypts with Bob's PUBLIC key → Bob decrypts with his PRIVATE key

Non-Repudiation/Authentication:
  Alice encrypts with her PRIVATE key → Anyone decrypts with Alice's PUBLIC key
```

**Characteristics**:
- **Solves key distribution**: No shared secret needed
- **Scalability**: N users = 2N keys (each has key pair)
- **Non-repudiation**: Private key proves identity
- **SLOW**: 100-1000x slower than symmetric

**Security Provided**:
- Confidentiality (encrypt with public, decrypt with private)
- Authentication (encrypt with private, decrypt with public)
- Integrity (via digital signatures)
- Non-repudiation (private key proves identity)

**Common Algorithms**:
- RSA (Rivest-Shamir-Adleman)
- Diffie-Hellman (key exchange only)
- ECC (Elliptic Curve Cryptography)
- DSA (Digital Signature Algorithm)

**Best Use Cases**:
- Key exchange
- Digital signatures
- Small data encryption
- Authentication

**Exam Keyword**: "Asymmetric = Two keys = Public + Private = Slow but versatile"

---

#### Hybrid Approach (Best of Both Worlds)

**How It Works**:
1. Use **asymmetric** to exchange a symmetric session key
2. Use **symmetric** for actual data encryption

**Example — HTTPS/TLS**:
```
1. Browser and server perform asymmetric key exchange (RSA/ECDHE)
2. They agree on a symmetric session key (AES)
3. All data transferred using fast symmetric encryption (AES)
```

**Benefits**:
- Security of asymmetric
- Speed of symmetric
- Best of both worlds!

**Real-World Use**: Nearly ALL secure communications (HTTPS, VPN, SSH)

---

### Symmetric Encryption Algorithms

#### Block Ciphers vs Stream Ciphers

##### Block Cipher
- **How**: Encrypts data in fixed-size blocks
- **Block Size**: Typically 64, 128, or 256 bits
- **Padding**: Added if data doesn't fit exact block size
- **Use Case**: Most symmetric algorithms
- **Examples**: DES, AES, Blowfish

##### Stream Cipher
- **How**: Encrypts data bit-by-bit or byte-by-byte
- **Keystream**: Generated and XORed with plaintext
- **Use Case**: Real-time data (audio/video)
- **Examples**: RC4, ChaCha20
- **Advantage**: No padding needed
- **Implementation**: Often hardware-based

---

#### Major Symmetric Algorithms

##### DES (Data Encryption Standard) — DEPRECATED
- **Key Size**: 56 bits (64-bit with parity)
- **Block Size**: 64 bits
- **Rounds**: 16
- **Status**: **OBSOLETE** — Can be brute-forced
- **Era**: 1970s-2000s
- **Replacement**: AES

**Exam Note**: Know it's DEPRECATED due to short key length

---

##### 3DES (Triple DES) — BEING PHASED OUT
- **How**: Applies DES three times
- **Key Size**: 168 bits (three 56-bit keys)
- **Effective Security**: 112 bits
- **Block Size**: 64 bits
- **Speed**: 3x slower than DES
- **Status**: Being deprecated
- **Replacement**: AES

**Why Triple?**: DES → Decrypt → DES (Encrypt-Decrypt-Encrypt)

---

##### AES (Advanced Encryption Standard) — CURRENT STANDARD
- **Key Sizes**: 128-bit, 192-bit, 256-bit
- **Block Size**: 128 bits
- **Status**: **Current US Government Standard**
- **Speed**: Very fast (hardware acceleration)
- **Security**: No known practical attacks
- **Use**: Everywhere (Wi-Fi, disk encryption, TLS)

**Rounds by Key Size**:
- AES-128: 10 rounds
- AES-192: 12 rounds
- AES-256: 14 rounds

**AES-256 = Gold Standard** for sensitive data

**Exam Tip**: AES is the go-to answer for modern symmetric encryption!

---

##### Blowfish
- **Key Size**: 32 to 448 bits (variable)
- **Block Size**: 64 bits
- **Status**: Still secure but less common
- **Created**: As DES replacement
- **Adoption**: Limited

---

##### Twofish
- **Key Size**: 128, 192, or 256 bits
- **Block Size**: 128 bits
- **Status**: Secure, open-source
- **Related**: Based on Blowfish
- **Adoption**: Less common than AES

---

##### RC4 — DEPRECATED
- **Type**: Stream cipher
- **Key Size**: 40 to 2048 bits
- **Used In**: WEP (Wi-Fi), SSL (old)
- **Status**: **INSECURE** — Multiple vulnerabilities
- **Problem**: Biases in keystream

**Exam Note**: RC4 is BROKEN — don't use it!

---

### Asymmetric Encryption Algorithms

#### Diffie-Hellman (DH)
- **Purpose**: **KEY EXCHANGE ONLY** (not for encryption/decryption)
- **How**: Two parties agree on shared secret over insecure channel
- **Strength**: Even if attacker sees exchange, can't determine secret
- **Vulnerability**: Man-in-the-middle (needs authentication)
- **Use**: VPN (IPSec), TLS key exchange

**Variants**:
- **DHE**: Diffie-Hellman Ephemeral (temporary keys)
- **ECDHE**: Elliptic Curve DH Ephemeral (faster, more secure)

**Exam Tip**: Diffie-Hellman = Key Exchange, NOT encryption!

---

#### RSA (Rivest-Shamir-Adleman)
- **Uses**: Encryption, digital signatures, key exchange
- **Key Sizes**: 1024-bit (weak), 2048-bit (standard), 4096-bit (high security)
- **Math Basis**: Factoring large prime numbers (hard problem)
- **Speed**: Slow (100-1000x slower than AES)
- **Status**: Still widely used
- **Threat**: Quantum computers could break it

**Common Uses**:
- TLS/SSL certificates
- Email encryption (PGP/GPG)
- Code signing
- SSH keys

**Best Practice**: Minimum 2048-bit keys (NIST recommendation)

**Exam Scenario**: "Encrypt small data with non-repudiation" → RSA

---

#### ECC (Elliptic Curve Cryptography)
- **Math Basis**: Elliptic curve mathematics
- **Efficiency**: 6x more efficient than RSA for same security
- **Key Size Comparison**:
  - ECC 256-bit ≈ RSA 3072-bit security
  - ECC 384-bit ≈ RSA 7680-bit security
- **Advantages**: Smaller keys, faster, less power
- **Use Case**: Mobile devices, IoT, modern systems

**ECC Variants**:
- **ECDH**: Elliptic Curve Diffie-Hellman (key exchange)
- **ECDHE**: Ephemeral version (perfect forward secrecy)
- **ECDSA**: Digital signatures

**Modern Trend**: ECC replacing RSA for new implementations

**Exam Tip**: ECC = Smaller keys, same security, better for mobile/IoT

---

### Hashing

#### What is Hashing?

**Definition**: One-way cryptographic function producing unique fixed-size digest

**Key Properties**:
1. **One-way**: Can't reverse (hash → original data)
2. **Deterministic**: Same input = same hash
3. **Fixed size**: Any input → fixed output size
4. **Unique**: Different inputs → different hashes (ideally)
5. **Avalanche effect**: Tiny change → completely different hash

**NOT Encryption**: Can't decrypt a hash!

**Purpose**:
- Verify integrity (file unchanged)
- Store passwords (hash instead of plaintext)
- Digital signatures (hash + encrypt)
- Blockchain (linking blocks)

---

#### Hashing Algorithms

##### MD5 (Message Digest 5) — BROKEN
- **Output**: 128-bit hash
- **Status**: **OBSOLETE** — Collision attacks proven
- **Problem**: Easy to create collisions
- **Use**: Legacy systems only (checksums for non-security)

**Exam Note**: MD5 is BROKEN for security purposes!

---

##### SHA Family (Secure Hash Algorithm)

**SHA-1** — DEPRECATED
- **Output**: 160-bit
- **Status**: **DEPRECATED** (2017) — Collision attacks
- **Problem**: Not collision-resistant
- **Replacement**: SHA-2 or SHA-3

**SHA-2** — CURRENT STANDARD
- **Variants**:
  - SHA-224: 224-bit
  - SHA-256: 256-bit (Most common)
  - SHA-384: 384-bit
  - SHA-512: 512-bit
- **Status**: Secure and widely used
- **Use**: Everywhere (TLS, code signing, blockchain)

**SHA-3**
- **Output**: 224, 256, 384, 512-bit
- **Method**: Different internal structure (Keccak)
- **Status**: Secure, modern alternative to SHA-2
- **Rounds**: 120 computations

**Exam Tip**:
- MD5/SHA-1 = BROKEN
- SHA-256 = Current standard
- SHA-3 = Newest, most secure

---

##### HMAC (Hash-based Message Authentication Code)
- **Purpose**: Combines hash with secret key
- **Provides**: Integrity + Authentication
- **How**: Hash(message + secret_key)
- **Variants**: HMAC-MD5, HMAC-SHA1, HMAC-SHA256

**Use Cases**:
- API authentication
- Message integrity verification
- Cookie signing

**Difference from plain hash**: Requires secret key (authenticated)

---

#### Increasing Hash Security

##### Salting
- **What**: Adding random data to input before hashing
- **Why**: Prevents rainbow table attacks
- **How**: Hash(password + random_salt)
- **Result**: Same password → different hashes (different salts)

**Example**:
```
User1: password123 + salt_abc123 → Hash_X
User2: password123 + salt_xyz789 → Hash_Y
```

**Critical**: Store salt WITH hash (not secret, just unique)

---

##### Key Stretching
- **Purpose**: Make weak passwords stronger
- **How**: Apply hash function many times (thousands of rounds)
- **Result**: Slow brute-force attacks significantly
- **Minimum**: 128-bit output

**Algorithms**:
- PBKDF2 (Password-Based Key Derivation Function 2)
- bcrypt
- scrypt

**Example**: Hash password 10,000 times instead of once

---

##### Nonce (Number Used Once)
- **What**: Unique random number for each operation
- **Use**: Prevent replay attacks
- **How**: Include in authentication exchange
- **Result**: Old captured data can't be reused

**Example — Authentication**:
1. Server sends nonce
2. Client: Hash(password + nonce)
3. Server verifies
4. Nonce expires (can't replay)

---

#### Hash Attacks

##### Collision Attack
- **Goal**: Find two inputs producing same hash
- **Impact**: Breaks integrity verification
- **Defense**: Use longer hashes (SHA-256+)

**Birthday Paradox**: Collisions more likely than expected

---

##### Pass-the-Hash Attack
- **How**: Steal password hash, use without cracking
- **Target**: Windows authentication (NTLM)
- **Tool**: Mimikatz
- **Defense**:
  - Multi-factor authentication
  - Least privilege
  - Credential Guard
  - Regular patching

---

### Public Key Infrastructure (PKI)

#### What is PKI?

**Definition**: Comprehensive framework for managing digital keys and certificates

**Purpose**: Enable secure data transfer, authentication, encrypted communications

**Components**:
- Certificate Authorities (CA)
- Registration Authorities (RA)
- Digital certificates
- Certificate databases
- Key storage/management

**Real-World Use**: HTTPS websites, email encryption, code signing

---

#### PKI Components

##### Certificate Authority (CA)
- **Role**: Trusted third party issuing digital certificates
- **Responsibilities**:
  - Issue certificates
  - Validate identities
  - Sign certificates
  - Revoke compromised certificates
  - Maintain Certificate Revocation List (CRL)

**Types**:
- **Root CA**: Highest trust level, self-signed
- **Intermediate CA**: Issued by root, issues end-entity certs
- **Subordinate CA**: Under intermediate

**Commercial Examples**: DigiCert, Let's Encrypt, GlobalSign

---

##### Registration Authority (RA)
- **Role**: Handles certificate requests
- **Responsibilities**:
  - Verify requestor identity
  - Validate information
  - Forward to CA for issuance
- **NOT**: Actually issues certificates (CA does that)

**Think**: RA = Front desk, CA = Manager who makes final decision

---

##### Certificate Signing Request (CSR)
- **What**: Request sent to CA for certificate
- **Contains**:
  - Organization info
  - Public key
  - Domain name(s)
  - Contact information
- **Does NOT contain**: Private key (stays with requester!)

**Process**:
1. Generate key pair
2. Create CSR with public key
3. Submit CSR to CA
4. CA validates and issues certificate

---

##### Digital Certificate
- **What**: Electronic document binding public key to identity
- **Standard**: X.509
- **Contains**:
  - Subject (owner) info
  - Public key
  - Issuer (CA) info
  - Validity period (start/end dates)
  - Serial number
  - Digital signature (CA's)

**Purpose**: Proves "this public key belongs to this person/server"

---

#### Certificate Types

##### Wildcard Certificate
- **Covers**: Main domain + ALL subdomains
- **Example**: *.example.com covers:
  - www.example.com
  - mail.example.com
  - blog.example.com
- **Pros**: Easy management, cost-effective
- **Cons**: If compromised, ALL subdomains affected

---

##### SAN (Subject Alternative Name)
- **Covers**: Multiple different domains
- **Example**: One cert for:
  - example.com
  - example.net
  - differentdomain.com
- **Use**: When domains don't share root domain

---

##### Single-Sided vs Dual-Sided

**Single-Sided** (Most common):
- Only server validated
- Client trusts server
- Example: HTTPS websites

**Dual-Sided** (Mutual TLS):
- Both server AND client validated
- Both have certificates
- Higher security, more processing
- Example: Enterprise VPN, API authentication

---

##### Self-Signed Certificate
- **Issued by**: The entity itself (not CA)
- **Pros**: Free, quick, easy
- **Cons**: No trust, browser warnings
- **Use**: Testing, internal systems

**Problem**: Browsers don't trust (no CA validation)

---

##### Third-Party Certificate
- **Issued by**: Trusted CA
- **Pros**: Browser trust, validation
- **Cons**: Cost (though Let's Encrypt is free)
- **Use**: Public-facing websites

---

#### Certificate Revocation

##### Certificate Revocation List (CRL)
- **What**: List of revoked certificates (before expiration)
- **Maintained by**: CA
- **How**: Client downloads list, checks serial number
- **Pros**: Complete list
- **Cons**: Can be large, slower

**When Revoked**:
- Private key compromised
- CA compromised
- Certificate info changed
- No longer needed

---

##### OCSP (Online Certificate Status Protocol)
- **What**: Real-time certificate status check
- **How**: Query specific certificate by serial number
- **Response**: Good, Revoked, or Unknown
- **Pros**: Faster, smaller data transfer
- **Cons**: Privacy (CA knows who checks what)

---

##### OCSP Stapling
- **What**: Server gets OCSP response, includes in TLS handshake
- **Pros**:
  - Faster (client doesn't query CA)
  - Privacy (CA doesn't see client queries)
  - Reduces CA load
- **How**: Server refreshes OCSP response periodically

**Modern Standard**: OCSP Stapling preferred

---

#### Advanced PKI Concepts

##### Public Key Pinning
- **Purpose**: Prevent fraudulent certificates
- **How**: Browser stores trusted public keys for domain
- **Result**: Alerts if different cert presented
- **Use**: High-security sites

---

##### Key Escrow
- **What**: Secure third-party storage of private keys
- **Purpose**: Key recovery if lost
- **Pros**: Can recover encrypted data
- **Cons**: Security risk if escrow compromised
- **Controversy**: Government backdoor concerns

---

##### Certificate Transparency (CT)
- **What**: Public log of all issued certificates
- **Purpose**: Detect mis-issued certificates
- **How**: CAs must log certificates publicly
- **Benefit**: Catch fraudulent certificates quickly

---

### Encryption Tools

#### Trusted Platform Module (TPM)

**What**: Dedicated crypto chip on motherboard

**Purpose**: Hardware-level security for cryptographic operations

**Functions**:
- Generate and store keys
- Hardware random number generation
- Secure boot verification
- Remote attestation
- Key sealing (bind to specific hardware)

**Common Uses**:
- BitLocker (Windows drive encryption)
- Secure boot
- Hardware authentication
- Measured boot

**Versions**:
- TPM 1.2 (older)
- TPM 2.0 (current standard)

**Advantage**: Keys never exposed to software (hardware-protected)

**Exam Scenario**: "Hardware-based encryption for laptops" → TPM + BitLocker

---

#### Hardware Security Module (HSM)

**What**: Physical device for safeguarding cryptographic keys

**Purpose**: Enterprise-grade key management and crypto operations

**Functions**:
- Generate keys
- Store keys securely
- Perform crypto operations
- Tamper-resistant/evident
- High-speed encryption

**Use Cases**:
- Financial transactions
- Certificate authorities
- Database encryption
- Code signing
- Regulatory compliance

**Characteristics**:
- FIPS 140-2/140-3 certified
- Physically secure
- Tamper detection (self-destructs if opened)
- Clustered for redundancy

**TPM vs HSM**:
- TPM: Consumer devices, built-in, lower cost
- HSM: Enterprise, dedicated device, high security, expensive

**Exam Tip**: HSM = Enterprise crypto, mission-critical operations

---

#### Key Management System (KMS)

**What**: Centralized system for managing cryptographic keys

**Lifecycle Management**:
1. **Generation**: Create keys
2. **Distribution**: Securely share keys
3. **Storage**: Secure key repository
4. **Rotation**: Regular key changes
5. **Backup**: Key recovery
6. **Destruction**: Secure key disposal

**Functions**:
- Automated key rotation
- Access control
- Audit logging
- Compliance reporting
- Key escrow

**Examples**:
- AWS KMS
- Azure Key Vault
- Google Cloud KMS
- HashiCorp Vault

**Why Important**: Manual key management doesn't scale

**Exam Tip**: KMS manages entire key lifecycle

---

#### Secure Enclave

**What**: Isolated coprocessor within main CPU

**Purpose**: Secure data processing separate from main OS

**How It Works**:
- Dedicated secure area
- Isolated from main processor
- Own encrypted memory
- Boot verified independently

**Uses**:
- Biometric data (fingerprints, Face ID)
- Payment credentials
- Encryption keys
- Secure boot

**Devices**:
- Apple devices (iPhone, Mac)
- Android (Trusted Execution Environment)
- ARM TrustZone

**Protection**: Even compromised OS can't access enclave

**Exam Tip**: Secure enclave = Hardware isolation for sensitive data

---

### Obfuscation Techniques

#### Steganography

**Definition**: Hiding data within other data to conceal its existence

**How It Works**: Modify image, audio, or video to embed hidden message

**Techniques**:
- Least significant bit (LSB) manipulation
- Spread spectrum
- Transform domain methods

**Examples**:
- Hide message in image pixel data
- Embed file in audio waveform
- Conceal data in video frames

**Goal**: No one suspects hidden data exists

**vs Encryption**:
- Encryption: Obvious something is hidden (ciphertext visible)
- Steganography: Looks innocent (message invisible)

**Combined**: Encrypt THEN hide (defense in depth)

**Detection**: Steganalysis (looking for statistical anomalies)

**Exam Scenario**: "Hide the existence of communication" → Steganography

---

#### Tokenization

**Definition**: Replace sensitive data with non-sensitive substitute (token)

**How It Works**:
1. Original data stored securely in vault
2. Token generated (random value)
3. Token used in systems
4. Token has NO mathematical relationship to original

**Example — Credit Cards**:
```
Real Card: 4532-1234-5678-9010
Token:     8721-4893-2847-1234
```

**Purpose**: Reduce exposure of sensitive data

**Use Cases**:
- Payment processing (PCI DSS compliance)
- Personal data protection
- Database security
- Cloud applications

**Benefits**:
- Reduces compliance scope
- Breach of tokens = useless data
- Preserves data format

**vs Encryption**:
- Encryption: Can be decrypted with key
- Tokenization: Lookup required (no mathematical reversal)

**Exam Tip**: Tokenization = Payment data, no decrypt (lookup required)

---

#### Data Masking

**Definition**: Hiding original data by modifying it while maintaining usability

**Techniques**:

##### Static Masking
- Permanent replacement
- Used for non-production environments
- Example: Production DB → Masked test DB

##### Dynamic Masking
- Real-time masking based on user
- Production data, different views
- Example: Support can see last 4 digits only

**Methods**:
- Substitution: Replace with similar data
- Shuffling: Randomize within column
- Nulling: Replace with NULL
- Masking out: XXX-XX-1234 (show only last 4)
- Variance: Add random noise to numbers

**Examples**:
```
Original SSN: 123-45-6789
Masked:       XXX-XX-6789

Original Email: john.doe@company.com
Masked:        j***d**@company.com
```

**Use Cases**:
- Software testing
- Development environments
- Training databases
- Customer service displays
- Analytics (aggregate data)

**Benefits**:
- Usable data for testing
- Preserves format/structure
- Reduces breach risk
- Compliance (GDPR, HIPAA)

**Exam Tip**: Data masking = Non-production environments, preserves format

---

### Cryptographic Attacks

#### Downgrade Attack
**What**: Force system to use older, weaker crypto protocols

**How**:
1. Attacker intercepts negotiation
2. Modifies to request weak protocol
3. Systems agree to weaker crypto
4. Attacker exploits known vulnerabilities

**Example**: POODLE attack (force SSL 3.0 instead of TLS)

**Defense**:
- Disable old protocols (SSL 2.0, SSL 3.0)
- Enforce minimum TLS version (TLS 1.2+)
- Version intolerance checks

**Exam Tip**: Downgrade = Forcing weaker crypto to exploit vulnerabilities

---

#### Collision Attack
**What**: Finding two different inputs producing same hash

**Impact**: Breaks integrity verification

**Why Possible**: Hash output smaller than input space (pigeonhole principle)

**Birthday Paradox**: Collisions occur sooner than expected

**Famous Cases**:
- MD5 collisions (demonstrated 2004)
- SHA-1 collisions (demonstrated 2017)

**Defense**:
- Use longer hashes (SHA-256+)
- Avoid MD5, SHA-1
- Key stretching

**Exam Scenario**: "Hash collision vulnerability" → Use SHA-256 instead of MD5

---

#### Quantum Computing Threat
**The Problem**: Quantum computers can break current crypto

**How Quantum Works**:
- Uses qubits (quantum bits)
- Superposition (many states simultaneously)
- Entanglement
- Parallel processing at massive scale

**What's Vulnerable**:
- RSA (prime factorization)
- Diffie-Hellman
- ECC (somewhat more resistant)

**What's Safe**:
- Symmetric encryption (AES-256)
- Hashing (SHA-256+)

**Why Asymmetric Is Vulnerable**:
- Based on "hard" math problems
- Quantum algorithms (Shor's algorithm) solve these efficiently

---

#### Post-Quantum Cryptography
**Definition**: Algorithms resistant to quantum attacks

**Approaches**:

##### 1. Increase Key Sizes
- Longer keys = more permutations
- But diminishing returns
- AES-128 → AES-256

##### 2. New Algorithm Types
- Lattice-based cryptography
- Hash-based signatures
- Code-based crypto
- Multivariate polynomial crypto

**NIST Standards (2024)**:

**General Encryption**:
- CRYSTALS-Kyber

**Digital Signatures**:
- CRYSTALS-Dilithium
- FALCON
- SPHINCS+

**Exam Tip**: Post-quantum = Algorithms resistant to quantum computer attacks

---

### Memory Aids and Mnemonics

#### Data States: "RAT"
- **R**est (stored)
- **A**ctive (in use)
- **T**ransit (moving)

#### Symmetric vs Asymmetric: "SAFE"
- **S**ymmetric = Same key
- **A**symmetric = Asymmetric (different keys)
- **F**ast = Symmetric
- **E**verywhere = Asymmetric (key distribution)

#### Good Hashes: "SHA-2/3"
- MD5 — broken
- SHA-1 — broken
- SHA-2 — current standard (SHA-256)
- SHA-3 — newest, most secure

#### PKI Components: "CRACK"
- **C**A (Certificate Authority)
- **R**A (Registration Authority)
- **A**uthorization/Authentication
- **C**ertificate
- **K**ey management

#### Obfuscation Types: "STM"
- **S**teganography (hide existence)
- **T**okenization (substitute sensitive data)
- **M**asking (obscure while maintaining format)

#### Encryption Tools: "THE KEYS"
- **T**PM (Trusted Platform Module)
- **H**SM (Hardware Security Module)
- **E**nclave (Secure Enclave)
- **K**MS (Key Management System)

---

### Common Exam Traps

**Trap 1: Confusing Encryption and Hashing**
- WRONG: "Hash the data to keep it confidential"
- RIGHT: "Encrypt for confidentiality, hash for integrity"
- Remember: Hashing is ONE-WAY (can't reverse)

**Trap 2: "Symmetric is Always Better"**
- WRONG: "Use symmetric because it's faster"
- RIGHT: Consider the use case (large data = symmetric, key exchange = asymmetric)

**Trap 3: MD5/SHA-1 Are Still OK**
- WRONG: "MD5 is fine for checksums"
- RIGHT: MD5/SHA-1 are broken for security (use SHA-256+)

**Trap 4: Diffie-Hellman Encrypts Data**
- WRONG: "Use Diffie-Hellman to encrypt the message"
- RIGHT: Diffie-Hellman is for KEY EXCHANGE only

**Trap 5: TPM = HSM**
- WRONG: "TPM and HSM are the same thing"
- RIGHT: TPM = Consumer devices, built-in, lower cost; HSM = Enterprise, dedicated, high security, expensive

---

### Exam tips

1. **Know the three data states**: At rest, in transit, in use
2. **Symmetric = Fast, same key**: AES is the standard
3. **Asymmetric = Slow, key pairs**: RSA/ECC for key exchange and signatures
4. **Hashing = One-way, integrity**: SHA-256 is standard, MD5/SHA-1 broken
5. **Hybrid approach** = Real-world (asymmetric key exchange + symmetric data encryption)
6. **PKI manages certificates**: CA issues, RA verifies, CRL/OCSP for revocation
7. **TPM = Consumer hardware crypto**: BitLocker, secure boot
8. **HSM = Enterprise hardware crypto**: High-security, mission-critical
9. **Salting prevents rainbow tables**: Add random data before hashing
10. **Quantum threat = Post-quantum crypto needed**: NIST standards emerging

**Pro Tip**: When you see "appropriate cryptographic solution," think:
- Large data → Symmetric (AES)
- Key exchange → Asymmetric (DH, RSA, ECC)
- Integrity → Hashing (SHA-256)
- Passwords → Salted hashes + key stretching
- Certificates → PKI

---

## Key terms

- **Cryptography** — Practice and study of writing and solving codes to hide information's true meaning.
- **Encryption** — Process of converting plaintext to ciphertext using an algorithm and key; reversible with correct key.
- **Hashing** — One-way cryptographic function producing a unique fixed-size digest; NOT reversible.
- **Symmetric Encryption** — Uses the same key for encryption and decryption; fast but has key distribution problems.
- **Asymmetric Encryption** — Uses a key pair (public + private); slower but solves key distribution and enables non-repudiation.
- **AES (Advanced Encryption Standard)** — Current standard symmetric algorithm; key sizes 128, 192, 256-bit.
- **DES (Data Encryption Standard)** — Deprecated symmetric algorithm with 56-bit key; easily brute-forced.
- **3DES (Triple DES)** — Applies DES three times; being phased out in favor of AES.
- **RSA** — Asymmetric algorithm for encryption, signatures, and key exchange; minimum 2048-bit recommended.
- **ECC (Elliptic Curve Cryptography)** — Efficient asymmetric algorithm; smaller keys provide equivalent security to RSA.
- **Diffie-Hellman** — Key exchange algorithm only; does NOT encrypt data.
- **SHA-256** — Current standard hashing algorithm from the SHA-2 family; 256-bit output.
- **MD5** — Broken hashing algorithm; 128-bit output with known collision vulnerabilities.
- **HMAC** — Hash-based Message Authentication Code; combines hash with secret key for integrity + authentication.
- **Salt** — Random data added to input before hashing to prevent rainbow table attacks.
- **Key Stretching** — Applying hash function many times to slow brute-force attacks (PBKDF2, bcrypt, scrypt).
- **PKI (Public Key Infrastructure)** — Framework for managing digital keys and certificates.
- **Certificate Authority (CA)** — Trusted third party that issues, validates, and revokes digital certificates.
- **Registration Authority (RA)** — Entity that verifies identity of certificate requestors before forwarding to CA.
- **Digital Certificate** — X.509 electronic document binding a public key to an identity, signed by a CA.
- **CRL (Certificate Revocation List)** — List of revoked certificates maintained by a CA.
- **OCSP (Online Certificate Status Protocol)** — Real-time certificate status checking; responses are Good, Revoked, or Unknown.
- **OCSP Stapling** — Server includes OCSP response in TLS handshake for faster, more private validation.
- **Wildcard Certificate** — Covers a domain and all its subdomains (e.g., *.example.com).
- **SAN (Subject Alternative Name)** — Certificate covering multiple different domain names.
- **TPM (Trusted Platform Module)** — Hardware crypto chip on motherboard for key storage and secure boot.
- **HSM (Hardware Security Module)** — Enterprise hardware device for high-security key management and crypto operations.
- **KMS (Key Management System)** — Centralized system managing the full lifecycle of cryptographic keys.
- **Secure Enclave** — Isolated coprocessor within CPU for secure data processing separate from main OS.
- **Steganography** — Hiding data within other data (images, audio) to conceal its existence.
- **Tokenization** — Replacing sensitive data with non-sensitive tokens; requires lookup to reverse (no mathematical relationship).
- **Data Masking** — Modifying data to hide originals while maintaining usability; used for testing and non-production environments.
- **Downgrade Attack** — Forcing a system to use older, weaker cryptographic protocols.
- **Collision Attack** — Finding two different inputs that produce the same hash output.
- **Post-Quantum Cryptography** — Algorithms designed to resist attacks from quantum computers.
- **Nonce** — Number used once; prevents replay attacks in authentication exchanges.

---

## Examples / scenarios

**Scenario 1:** A company needs to encrypt a 500GB database. Which encryption type should they use and why?

<details>
<summary>Answer</summary>

**Answer**: Symmetric encryption (AES-256)

**Explanation**:
- Large data volume = need speed
- Symmetric is 100-1000x faster than asymmetric
- AES-256 is current standard
- Key distribution not an issue (database server has the key)

**NOT asymmetric**: Too slow for 500GB of data
</details>

**Scenario 2:** A developer wants to verify that a downloaded software file hasn't been tampered with. The vendor provides an MD5 hash. What's the security concern?

<details>
<summary>Answer</summary>

**Answer**: MD5 is broken and vulnerable to collision attacks

**Explanation**:
- MD5 has known collision vulnerabilities
- Attacker could create malicious file with same MD5 hash
- Should use SHA-256 or SHA-512 instead
- MD5 is fine for non-security checksums but NOT for integrity verification

**Better approach**: Vendor should provide SHA-256 hash
</details>

**Scenario 3:** A web application stores credit card numbers. Compliance requires protecting this data. What cryptographic technique should be used?

<details>
<summary>Answer</summary>

**Answer**: Tokenization

**Explanation**:
- Payment card data = perfect tokenization use case
- PCI DSS compliance
- Reduces scope (tokens in system, real data in vault)
- No decryption key to steal (lookup required)

**Could also encrypt**: But tokenization is PCI DSS best practice for payments

**NOT masking**: Masking is for display/testing, not storage
</details>

---

## Mini quiz

<details>
<summary><strong>Question 1:</strong> Which of the following BEST describes the difference between encryption and hashing?</summary>

**Answer: Encryption is reversible; hashing is one-way**

- **Encryption**: Plaintext → Ciphertext → Plaintext (reversible with key)
- **Hashing**: Data → Hash (NOT reversible, one-way function)

Purpose difference:
- Encryption: Confidentiality (hide data)
- Hashing: Integrity (verify unchanged)
</details>

<details>
<summary><strong>Question 2:</strong> A company wants to securely exchange encryption keys over the internet without a pre-shared secret. Which algorithm should they use?</summary>

**Answer: Diffie-Hellman**

Key exchange without pre-shared secret = Diffie-Hellman. DH specifically designed for this purpose. Allows two parties to agree on shared key over insecure channel.

NOT AES/3DES (symmetric — need shared key first), NOT SHA-256 (hashing — not for key exchange).
</details>

<details>
<summary><strong>Question 3:</strong> Which symmetric encryption algorithm provides the STRONGEST security?</summary>

**Answer: AES with 256-bit key**

AES-256 = Current gold standard. No known practical attacks. DES is obsolete, 3DES is being deprecated, RC4 is broken.
</details>

<details>
<summary><strong>Question 4:</strong> What additional security measure makes passwords more resistant to rainbow table attacks?</summary>

**Answer: Add salt to passwords before hashing**

Salting = Adding random data before hashing. Each password gets unique salt. Same password = different hashes (different salts). Rainbow tables useless (pre-computed for unsalted hashes).
</details>

<details>
<summary><strong>Question 5:</strong> Which TWO cryptographic solutions are MOST appropriate for protecting data at rest on a company laptop?</summary>

**Answer: TPM and BitLocker**

Data at rest = Stored data (hard drive). BitLocker = Full disk encryption (Windows). TPM = Hardware chip storing encryption keys. Together: BitLocker encrypts drive, TPM secures keys.

NOT TLS, IPSec, or SSH (all for data in transit).
</details>

### CompTIA-style practice questions

<details>
<summary><strong>Question 6:</strong> Which of the following BEST describes the difference between encryption and hashing?<br>A. Encryption is reversible; hashing is one-way<br>B. Hashing is reversible; encryption is one-way<br>C. Both are reversible with the correct key<br>D. Neither is reversible</summary>

**Correct Answer: A. Encryption is reversible; hashing is one-way**

- **Encryption**: Plaintext → Ciphertext → Plaintext (reversible with key)
- **Hashing**: Data → Hash (NOT reversible, one-way function)

This is a fundamental concept — know this cold for the exam!
</details>

<details>
<summary><strong>Question 7:</strong> A company wants to securely exchange encryption keys over the internet without a pre-shared secret. Which algorithm should they use?<br>A. AES<br>B. 3DES<br>C. Diffie-Hellman<br>D. SHA-256</summary>

**Correct Answer: C. Diffie-Hellman**

Key exchange without pre-shared secret = Diffie-Hellman. DH specifically designed for this purpose.

**Why not others**:
- A/B: Symmetric algorithms (need shared key first)
- D: Hashing algorithm (not for key exchange)
</details>

<details>
<summary><strong>Question 8:</strong> Which of the following provides the STRONGEST security for symmetric encryption?<br>A. DES with 56-bit key<br>B. 3DES with 168-bit key<br>C. AES with 256-bit key<br>D. RC4 with 128-bit key</summary>

**Correct Answer: C. AES with 256-bit key**

AES-256 = Current gold standard. Strongest option listed. No known practical attacks.

**Why others are weaker**:
- A: DES is obsolete (easily broken)
- B: 3DES being deprecated
- D: RC4 is broken (multiple vulnerabilities)
</details>

<details>
<summary><strong>Question 9:</strong> A security administrator wants to verify that a password hasn't been compromised. The password database stores hashed passwords. What additional security measure would make passwords more resistant to rainbow table attacks?<br>A. Increase hash iterations<br>B. Add salt to passwords before hashing<br>C. Use longer passwords<br>D. Implement account lockout</summary>

**Correct Answer: B. Add salt to passwords before hashing**

**Salting** = Adding random data before hashing. Each password gets unique salt. Same password = different hashes. Rainbow tables useless.

**Why others help but don't solve rainbow tables**:
- A: Key stretching (helps, but salt is more direct answer)
- C: Good practice, but doesn't stop rainbow tables
- D: Prevents brute force, not rainbow tables
</details>

<details>
<summary><strong>Question 10 (Multi-select):</strong> Which TWO cryptographic solutions would be MOST appropriate for protecting data at rest on a company laptop? (Choose TWO)<br>A. TLS<br>B. IPSec<br>C. TPM<br>D. BitLocker<br>E. SSH</summary>

**Correct Answers: C. TPM and D. BitLocker**

**Data at rest** = Stored data (hard drive). **BitLocker** = Full disk encryption (Windows). **TPM** = Hardware chip storing encryption keys.

**Why not others** (all for data in transit):
- A: TLS = HTTPS, secure web
- B: IPSec = VPN tunnels
- E: SSH = Secure remote access
</details>

---

## Related objectives

- [**1.2**]({{ '/secplus/objectives/1-2/' | relative_url }}) — Confidentiality (encryption), Integrity (hashing), Non-repudiation (digital signatures)
- [**2.3**]({{ '/secplus/objectives/2-3/' | relative_url }}) — Cryptographic vulnerabilities
- [**2.4**]({{ '/secplus/objectives/2-4/' | relative_url }}) — Cryptographic attack indicators
- [**3.1**]({{ '/secplus/objectives/3-1/' | relative_url }}) — Cloud encryption, VPN
- [**3.3**]({{ '/secplus/objectives/3-3/' | relative_url }}) — Data protection strategies
- [**4.1**]({{ '/secplus/objectives/4-1/' | relative_url }}) — Encryption implementation
- [**5.4**]({{ '/secplus/objectives/5-4/' | relative_url }}) — Compliance requirements for encryption

---

## Navigation

**Domain 1: General Security Concepts**

| Objective | Title | Status |
|---|---|---|
| [1.1]({{ '/secplus/objectives/1-1/' | relative_url }}) | Compare and contrast various types of security controls | done |
| [1.2]({{ '/secplus/objectives/1-2/' | relative_url }}) | Summarize fundamental security concepts | done |
| [1.3]({{ '/secplus/objectives/1-3/' | relative_url }}) | Explain the importance of change management processes | done |
| **1.4** | Explain the importance of using appropriate cryptographic solutions (current) | done |

[← Previous: Objective 1.3]({{ '/secplus/objectives/1-3/' | relative_url }}) | [Back to Dashboard]({{ '/secplus/' | relative_url }}) | [Next: Domain 2 →]({{ '/secplus/objectives/2-1/' | relative_url }})
