# Backlog — Cybersecurity Portfolio Topics

This backlog is the source of truth for article ideas and progress tracking.

## Status rules
- status: planned | drafted | published

## Evidence expectations (portfolio credibility)
Prefer topics where you can show:
- what you built/changed (or derived for theory posts)
- what you ran (commands/queries/tests — defensive only)
- what you observed (outputs, logs, metrics)
- what you verified (expected vs actual; success criteria)
- small sanitized artifacts (10–30 lines)

---

## A) Foundations & methodology

| ID | Topic | Track | Level | Status | Ownership evidence (examples) | Deliverable |
|---:|------|-------|-------|--------|-------------------------------|------------|
| 1 | Home SOC goal: asynchronous investigations vs real-time alerting | fundamentals | intro | planned | decision rationale + scope statement + example workflow | Post (concept + rubric) |
| 2 | Investigation notebooking: hypotheses → queries → decisions (repeatable format) | fundamentals | intro | planned | your filled template + one real example | Post + reusable template |
| 3 | Playbook template: hypothesis → sources → queries → decision points → outcome | fundamentals | intro | planned | playbook skeleton + one executed run | Post + template |
| 4 | My investigation format: how I structure notes, evidence, and decisions | fundamentals | intro | planned | screenshots/snippets of your workflow | Post + checklist |
| 5 | Noise management: what I ignore (and why) | fundamentals | intermediate | planned | examples of ignored patterns + rationale | Post + “ignore list” rubric |
| 6 | Enrichment discipline: categorizing IPs without over-trusting reputation | fundamentals | intermediate | planned | 2–3 examples of enrichment calls and decisions | Post + decision rubric |
| 7 | Unknown protocol triage: what to do when you can’t classify traffic quickly | fundamentals | advanced | planned | one case + what evidence you sought | Post + runbook |
| 8 | How I validate detections: test → observe telemetry → adjust | fundamentals | intermediate | planned | validation steps + before/after query tuning | Post + validation checklist |
| 9 | Metrics that matter: repeatability, FP rate, coverage | fundamentals | intermediate | planned | simple metric table you maintain | Post + metric sheet |

---

## B) Platform & network observability

| ID | Topic | Track | Level | Status | Ownership evidence (examples) | Deliverable |
|---:|------|-------|-------|--------|-------------------------------|------------|
| 10 | VLAN segmentation for observability: forcing L3 boundaries to increase visibility | operations | intro | planned | diagram + policy intent + one verification test | Post + diagram |
| 11 | SPAN design: trunk mirroring vs targeted port mirrors | operations | intermediate | planned | port map + mirror config excerpt + limitation notes | Post + design notes |
| 12 | Router requirements: VLAN routing, firewall zones, logging strategy | operations | intermediate | planned | ruleset excerpt + test matrix (allowed/denied) | Post + checklist |
| 13 | Sensor placement and failure modes: what SPAN cannot show | operations | intermediate | planned | documented blind spots + mitigation ideas | Post + limitations section |
| 14 | Retention sizing: 7-day storage estimation and tradeoffs | operations | intermediate | planned | measured daily volume + disk calc | Post + sizing worksheet |
| 15 | Hardening the sensor host: services, SSH, patching, backups | operations | intermediate | planned | hardening checklist + before/after state | Post + checklist |
| 16 | Config-as-code: versioning configs and dashboards in Git | operations | intermediate | planned | repo structure + sample PR diffs | Post + conventions |
| 17 | Retention loop reliability: compaction, disk monitoring, backups | operations | advanced | planned | monitoring proof + failure-mode test | Post + runbook |
| 18 | Lessons learned from building observability into a real network | operations | intermediate | planned | concrete “what I changed” timeline | Post |
| 19 | Threat modeling my segmentation: assets, boundaries, abuse cases | governance | intermediate | planned | threat table + control mapping | Post + diagram/table |

---

## C) Zeek / network security monitoring

| ID | Topic | Track | Level | Status | Ownership evidence (examples) | Deliverable |
|---:|------|-------|-------|--------|-------------------------------|------------|
| 20 | Minimal Zeek logging strategy: conn/dns/tls/notice baseline | nsm | intro | planned | config excerpt + sample log proof | Post + baseline rules |
| 21 | Zeek conn.log essentials: fields that matter | nsm | intro | planned | annotated conn.log excerpt | Post + field guide |
| 22 | DNS investigations: NXDOMAIN spikes, TTL sanity, unusual volume | nsm | intro | planned | dns.log excerpt + Loki queries + conclusion | Post + query set |
| 23 | TLS investigations: SNI, cert metadata, JA3/JA4 limits | nsm | intermediate | planned | tls.log excerpt + cert checks + caveats | Post + rubric |
| 24 | Zeek notice framework: value without alerting | nsm | intermediate | planned | notice sample + “what I do next” steps | Post + runbook |
| 25 | HTTP logging: when to enable and how to control noise | nsm | intermediate | planned | before/after log volume + use cases | Post + decision guide |
| 26 | Inter-VLAN visibility: what “good” looks like | nsm | intermediate | planned | expected flows list + observed proof | Post + baseline checklist |
| 27 | Lightweight Zeek scripting: adding tags/fields | nsm | advanced | planned | script snippet + before/after evidence | Post + code snippet |

---

## D) Loki / Grafana (search, dashboards, ops)

| ID | Topic | Track | Level | Status | Ownership evidence (examples) | Deliverable |
|---:|------|-------|-------|--------|-------------------------------|------------|
| 30 | Why Loki: low-cost search architecture (vs ELK) | operations | intro | planned | reasons + constraints + measured impact | Post |
| 31 | Promtail pipeline: parsing + label design (cardinality traps) | operations | intermediate | planned | config excerpt + label examples + query proof | Post + config notes |
| 32 | Loki query patterns: top talkers, rare domains, outlier ports | operations | intermediate | planned | 5–10 queries + sample results | Post + query cookbook |
| 33 | Dashboard design for investigations (not vanity charts) | operations | intermediate | planned | screenshot + why panels exist | Post + dashboard notes |
| 34 | Scheduled review without alerting: weekly hunting cadence | operations | intermediate | planned | weekly checklist + saved queries | Post + checklist |
| 35 | Loki performance tuning: optimization and anti-patterns | operations | advanced | planned | before/after query latency + fix | Post + tuning list |
| 36 | One-page triage board: core panels + core query set | operations | intermediate | planned | triage board screenshot + queries | Post + board spec |
| 37 | Ops runbook: telemetry stopped ingesting | operations | intermediate | planned | incident timeline + verification query | Post + runbook |
| 38 | Packaging evidence for articles: export while preserving anonymity | governance | intermediate | planned | before/after sanitized exports | Post + publishing process |

---

## E) Hunting & detections

| ID | Topic | Track | Level | Status | Ownership evidence (examples) | Deliverable |
|---:|------|-------|-------|--------|-------------------------------|------------|
| 40 | Baselining: defining “normal” and drift detection | soc | intro | planned | baseline window + delta example | Post + rubric |
| 41 | Top talkers: interpreting high-volume traffic correctly | soc | intro | planned | top talker list + benign explanation | Post + checklist |
| 42 | Rare domain hunting: first-seen per segment + triage rubric | soc | intermediate | planned | first-seen query + triage examples | Post + rubric |
| 43 | Rare port hunting: identify outliers and validate safely | soc | intermediate | planned | outlier table + validation notes | Post + runbook |
| 44 | Asset map from observed services: lightweight inventory | soc | intermediate | planned | inventory file + diff over time | Post + artifact |
| 45 | Beacon-like traffic: periodicity and low-volume patterns | soc | advanced | planned | periodicity query + FP discussion | Post + query + pitfalls |
| 46 | Change detection: baseline drift after new devices/updates | soc | intermediate | planned | before/after comparison evidence | Post + checklist |
| 47 | Server/Lab baseline: expected flows and deny-by-default checks | soc | intermediate | planned | expected flow list + evidence | Post + baseline |
| 48 | IoT baseline: typical destinations and deviation detection | soc | intermediate | planned | IoT destination profile + anomaly example | Post + rubric |

---

## F) Playbooks (repeatable investigations)

| ID | Topic | Track | Level | Status | Ownership evidence (examples) | Deliverable |
|---:|------|-------|-------|--------|-------------------------------|------------|
| 50 | DNS anomaly playbook | soc | intermediate | planned | playbook + one executed case | Post + playbook |
| 51 | TLS anomaly playbook | soc | intermediate | planned | playbook + one executed case | Post + playbook |
| 52 | East-west traffic playbook | soc | intermediate | planned | playbook + evidence queries | Post + playbook |
| 53 | Exfil suspicion playbook (defensive) | soc | advanced | planned | decision tree + evidence checklist | Post + playbook |
| 54 | IoT containment playbook | soc | intermediate | planned | isolate steps + proof of reduction | Post + playbook |
| 55 | Guest network validation playbook | soc | intermediate | planned | test matrix + proof | Post + playbook |
| 56 | New device joined playbook | soc | intermediate | planned | identification example + inventory update | Post + playbook |
| 57 | Server/Lab exposure review playbook | soc | intermediate | planned | services list + evidence checks | Post + playbook |
| 58 | Weekly hunting playbook: 10 recurring queries | soc | intermediate | planned | query list + why + example output | Post + cookbook |

---

## G) Simulations (defensive validation only)

| ID | Topic | Track | Level | Status | Ownership evidence (examples) | Deliverable |
|---:|------|-------|-------|--------|-------------------------------|------------|
| 60 | Simulation: periodic outbound traffic detection | soc | advanced | planned | expected signal → observed proof | Post + validation steps |
| 61 | Simulation: phishing follow-up in NSM view | soc | intermediate | planned | timeline + evidence queries | Post + case |
| 62 | Simulation: first-seen domain/SNI + low-volume connections | soc | advanced | planned | first-seen proof + triage | Post + rubric |
| 63 | Simulation: scan across segments (visibility + limits) | soc | intermediate | planned | scan-like evidence + limits | Post + case |
| 64 | Simulation: brute force to lab service (telemetry inference) | soc | intermediate | planned | evidence + what you can’t infer | Post + case |
| 65 | Simulation: misconfiguration incident (routing opens access) | soc | intermediate | planned | rule diff + verification tests | Post + case |
| 66 | Simulation: shadow IT discovery workflow | soc | intermediate | planned | SaaS discovery + decision rubric | Post + rubric |
| 67 | Simulation: DNS outage troubleshooting | soc | intermediate | planned | symptom → evidence → resolution | Post + runbook |
| 68 | Simulation: certificate error investigation | soc | intermediate | planned | TLS failure evidence + impact | Post + case |
| 69 | Simulation: DNS tunneling indicators (safe framing) | soc | advanced | planned | indicator evidence + FP pitfalls | Post + rubric |

---

## H) Endpoint telemetry (optional / later)

| ID | Topic | Track | Level | Status | Ownership evidence (examples) | Deliverable |
|---:|------|-------|-------|--------|-------------------------------|------------|
| 70 | Why endpoint telemetry matters | endpoint | intro | planned | example of “network-only blind spot” | Post |
| 71 | Sysmon onboarding: minimal config | endpoint | intermediate | planned | config excerpt + sample events | Post + config notes |
| 72 | Correlating endpoint + network evidence | endpoint | advanced | planned | join keys + example timeline | Post + method |
| 73 | PowerShell investigation (defensive) | endpoint | advanced | planned | example chain + correlated network | Post + case |
| 74 | Windows persistence evidence (defensive) | endpoint | advanced | planned | example indicators + triage steps | Post + rubric |
| 75 | Cross-telemetry narrative (end-to-end) | endpoint | advanced | planned | one full timeline with evidence links | Post + template |

---

## I) Honeypots (optional / later)

| ID | Topic | Track | Level | Status | Ownership evidence (examples) | Deliverable |
|---:|------|-------|-------|--------|-------------------------------|------------|
| 80 | Honeypot strategy: goals + safety controls | soc | intro | planned | threat model + success criteria | Post |
| 81 | OpenCanary on VPS: useful event types | soc | intermediate | planned | sample events + triage approach | Post + query ideas |
| 82 | Cowrie SSH honeypot: defensive interpretation | soc | intermediate | planned | session summaries + what you store | Post + rubric |
| 83 | VPS → VPN → home store push model | operations | advanced | planned | shipping design + failure-mode test | Post + design notes |
| 84 | Honeypot noise triage playbook | soc | intermediate | planned | playbook + examples | Post + playbook |
| 85 | Honeypot-driven detections | soc | advanced | planned | pattern → query → validation | Post + detections |
| 86 | Publishing honeypot data responsibly | governance | intro | planned | redaction examples + policy | Post + policy |

---

## J) Malware workflows (optional / later, defensive)

| ID | Topic | Track | Level | Status | Ownership evidence (examples) | Deliverable |
|---:|------|-------|-------|--------|-------------------------------|------------|
| 90 | Malware workflow design: separation + safety | soc | intro | planned | diagram + safety checklist | Post |
| 91 | Static triage basics (defensive) | soc | intermediate | planned | sample triage report (sanitized) | Post + template |
| 92 | Dynamic analysis safety checklist | soc | intermediate | planned | checklist + “what I will not do” | Post |
| 93 | Controlled detonation → capture network indicators | soc | advanced | planned | indicator capture proof | Post + method |
| 94 | Portfolio-safe malware triage report template | soc | intermediate | planned | reusable template file | Post + template |
| 95 | Turning observations into defensive detections | soc | advanced | planned | detection idea + validation plan | Post + rubric |

---

## K) Publishing, privacy, and governance

| ID | Topic | Track | Level | Status | Ownership evidence (examples) | Deliverable |
|---:|------|-------|-------|--------|-------------------------------|------------|
| 100 | Safe publishing: anonymizing telemetry without losing value | governance | intro | planned | before/after excerpts + mapping scheme | Post + checklist |
| 101 | Privacy boundaries: what to log and what not to log | governance | intro | planned | explicit policy + examples | Post + policy |
| 102 | Proof-of-ownership pattern: “built/ran/observed/verified” | governance | intro | planned | a filled example from your work | Post + template |

---

## L) Projects: PKI / password manager / internal services

| ID | Topic | Track | Level | Status | Ownership evidence (examples) | Deliverable |
|---:|------|-------|-------|--------|-------------------------------|------------|
| 110 | Local-first password manager: architecture + threat model | pki | intro | planned | diagram + deployment notes | Post + diagram |
| 111 | Internal PKI: offline root + online intermediate | pki | intermediate | planned | issuance proof + verification output | Post + runbook |
| 112 | TLS for internal services: SANs, trust distribution, verification | pki | intermediate | planned | cert inspection output + trust proof | Post + checklist |
| 113 | Optional mTLS for admin endpoints | pki | advanced | planned | allow/deny proof + config excerpt | Post + test cases |
| 114 | Certificate renewal model: ops checklist + failure modes | pki | advanced | planned | renewal proof + “what breaks” list | Post + runbook |
| 115 | Backups + restore drill for high-value services | operations | intermediate | planned | restore proof + checksum | Post + runbook |
| 116 | Patch cadence and operational controls: my minimum bar | operations | intro | planned | change log + verification checks | Post + checklist |

---

## M) Projects: Raspberry Pi / ESP / IoT security

| ID | Topic | Track | Level | Status | Ownership evidence (examples) | Deliverable |
|---:|------|-------|-------|--------|-------------------------------|------------|
| 120 | PKI + mTLS mini-lab on a Pi: rotation + audit trails | pki | intermediate | planned | rotation proof + audit logs | Post + scripts |
| 121 | Secure OTA updates: signed firmware pipeline + tamper tests | iot | advanced | planned | verify fail/success proof | Post + tool notes |
| 122 | Signed telemetry sensor: integrity + replay protection | iot | intermediate | planned | replay rejection proof | Post + schema |
| 123 | DNS privacy/policy box: DoT/DoH + caching + metrics | operations | intermediate | planned | latency/metrics evidence | Post + dashboard |
| 124 | Low-cost telemetry collector: syslog + retention + daily reports | soc | intermediate | planned | ingestion proof + report output | Post + runbook |
| 125 | Bastion host: hardening and audit trails | operations | intermediate | planned | policy + access logs | Post + checklist |
| 126 | Segmentation test harness: “allowed works, denied fails” | operations | advanced | planned | test matrix + results | Post + harness notes |
| 127 | Tamper/physical signals: event schema + buffering ideas | iot | intermediate | planned | ordering + outage buffering proof | Post + schema |
| 128 | Crypto audit playground: AEAD/KDF/signatures misuse demos | fundamentals | advanced | planned | test vectors + benchmarks | Post + lab notes |
| 129 | SSH certificates (SSH CA): short-lived access + auditability | operations | advanced | planned | expiry proof + principals | Post + issuance notes |

---

## N) Implementation / scripting

| ID | Topic | Track | Level | Status | Ownership evidence (examples) | Deliverable |
|---:|------|-------|-------|--------|-------------------------------|------------|
| 200 | Script: baseline report (daily/weekly) from logs (top talkers, rare domains) | automation | intermediate | planned | sample report output + baseline comparison | Script + post |
| 201 | Script: certificate expiry monitor + simple report output | automation | intro | planned | parsed cert list + expected alerts | Script + post |
| 202 | Script: backup verification (restore smoke test + checksum) | automation | advanced | planned | restore proof + checksum verification | Script + post |
| 203 | Script: segmentation test runner (matrix → pass/fail) | automation | advanced | planned | matrix file + run output + failure example | Script + post |

---

## O) Theory companions (cryptography, protocols, foundations)

| ID | Topic | Track | Level | Status | Ownership evidence (examples) | Deliverable |
|---:|------|-------|-------|--------|-------------------------------|------------|
| 300 | Crypto security goals: what “secure” means (IND-CPA, INT-CTXT in plain language) | fundamentals | intermediate | planned | short derivations + sanity checks | Theory post |
| 301 | AEAD: why it matters, nonce discipline, common misuse | fundamentals | intermediate | planned | worked example + test vector verification | Theory post |
| 302 | Hash functions: preimage/collision, domain separation, real pitfalls | fundamentals | intermediate | planned | worked example + misuse cases | Theory post |
| 303 | Key exchange: DH basics, forward secrecy, downgrade risks | fundamentals | intermediate | planned | toy transcript + property explanation | Theory post |
| 304 | Certificates & PKI theory: chains, validation, revocation limits | pki | intermediate | planned | validation walkthrough (defensive) | Theory post |
| 305 | Randomness: entropy sources and practical checks | fundamentals | intermediate | planned | small script check + interpretation | Theory post |
| 306 | Password hashing: salts, work factors, memory hardness | fundamentals | intro | planned | parameter comparison + rationale | Theory post |
| 307 | Auth basics: sessions vs tokens, replay, CSRF, fixation | fundamentals | intermediate | planned | threat scenarios + mitigations | Theory post |
