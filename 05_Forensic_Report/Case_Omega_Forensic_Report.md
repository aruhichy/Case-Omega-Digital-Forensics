
# DIGITAL FORENSIC INVESTIGATION REPORT

## Case Omega: Investigation of a Ransomware Attack on a Healthcare Network

---

## 1. CASE INFORMATION

| Field | Details |
|---|---|
| Case ID | OCH-2026-001 |
| Organization | OmegaCare Multispeciality Hospital |
| Location | New Delhi, India |
| Incident Date | 20 November 2026 |
| Discovery Time | 09:30 AM IST |
| Primary System | HOSP-SRV-01 |
| Operating System | Windows Server 2022 (Scenario) |
| Investigation Type | Digital Forensics – Academic Simulation |
| Report Status | Draft |

## 2. EXECUTIVE SUMMARY

This report documents an academic digital forensic investigation of a
fictional ransomware incident involving OmegaCare Multispeciality Hospital.

The investigation demonstrates the processes involved in first response,
evidence identification, evidence preservation, integrity verification,
safe malware-behaviour simulation, and timeline analysis.

All evidence files, system events, and hospital-related information used
in this assignment are fictional or synthetically generated.

No real hospital systems or patient information were accessed.

## 3. INCIDENT BACKGROUND

On 20 November 2026, a suspected ransomware incident was reported at
OmegaCare Multispeciality Hospital.

The fictional scenario describes unusual file modifications,
inaccessible hospital files, and a ransom note.

The main system involved in the scenario is identified as HOSP-SRV-01.

The investigation aims to demonstrate how a digital forensic
investigator would identify, preserve, examine, and document
potential digital evidence.

## 4. INVESTIGATION OBJECTIVES

The objectives were:

1. Document the incident and initial observations.
2. Identify potential sources of digital evidence.
3. Demonstrate evidence acquisition documentation.
4. Calculate and verify SHA-256 hashes.
5. Examine simulated ransomware-related behaviour safely.
6. Reconstruct a chronological incident timeline.
7. Document findings, limitations, and conclusions.

## 5. SCOPE AND LIMITATIONS

This assignment is a controlled academic simulation.

The investigation does not involve:
- A real healthcare network.
- Actual patient or employee information.
- Acquisition of a real hospital server image.
- Execution of actual ransomware.
- Examination of a real malware sample.
- Verification of a real cyberattack.

All findings must be interpreted within these limitations.

## 6. FIRST RESPONDER ACTIVITIES

This section documents the initial response procedures.

The activities included:
- Reviewing the fictional incident overview.
- Preparing a first responder standard operating procedure.
- Identifying potential evidence sources.
- Preparing a conceptual network scene sketch.
- Recording the fictional system and network assets.

Supporting documentation is stored in the 01_First_Responder directory.

## 7. EVIDENCE COLLECTION AND PRESERVATION

This section describes the simulated evidence collection process.

The fictional server evidence dataset contains:

1. server_information.txt
2. simulated_ransom_note.txt
3. affected_files.csv
4. server_events.csv

The original evidence files were preserved separately from the malware
analysis working copies.

An acquisition log and chain-of-custody record were prepared to
demonstrate evidence documentation procedures.

**Acquisition limitation:** The files constitute a synthetic academic
evidence dataset, not a bit-for-bit forensic image of a real server.


### 7.1 Evidence Register

| Evidence ID | Evidence Description | Status |
|---|---|---|
| E-01 | HOSP-SRV-01 – Simulated server evidence dataset | Simulated dataset prepared and documented |
| E-02 | HOSP-PC-01 – Employee workstation | Planned; not acquired |
| E-03 | Windows system, security and application logs | Represented using synthetic records |
| E-04 | Firewall logs | Represented using synthetic records |
| E-05 | USB-01 – Removable USB device | Planned; not acquired |
| E-06 | Browser history | Planned; not acquired |
| E-07 | Cloud audit logs | Planned; not acquired |
| E-08 | NET-SW-01 – Network switch logs | Planned; not acquired |

The four files belonging to E-01 are:

- server_information.txt
- simulated_ransom_note.txt
- affected_files.csv
- server_events.csv

These files form one synthetic evidence dataset. The evidence register does not represent actual acquisition of the listed hospital systems.


### 7.2 Chain of Custody

A chain-of-custody record was prepared to demonstrate how evidence
handling activities should be documented.

The record includes fields for:

- Evidence identification.
- Description of the evidence.
- Collection date and time.
- Person responsible for handling.
- Transfer details.
- Storage information.
- Remarks.

The academic dataset was maintained separately from the malware
analysis working copies.

The chain-of-custody documentation is available at:

02_Evidence_Collection/chain_of_custody.csv

**Limitation:** This is an academic documentation exercise and does
not establish a legally admissible chain of custody for real evidence.


## 8. EVIDENCE INTEGRITY VERIFICATION

SHA-256 hashing was demonstrated using Python.

The investigation included:
- Generating SHA-256 hashes for the synthetic evidence files.
- Saving the baseline hash values.
- Recalculating hashes independently.
- Comparing calculated hashes against the baseline.
- Documenting the verification results.

**Actual verification result:** [Enter the result recorded in integrity_verification_report.txt.]

Supporting files:
- hashes.txt
- verify_hash.py
- integrity_verification_report.txt
- integrity_verification.md

## 9. MALWARE ANALYSIS

A safe Python ransomware-behaviour simulator was created for
demonstration purposes.

The simulator:
- Identified files in a dedicated test directory.
- Recorded filenames and file sizes.
- Generated a harmless simulated ransom note.
- Generated an activity log.

It did not encrypt, delete, rename, or overwrite files.

It did not establish persistence, access credentials, or communicate
with external systems.

The simulator is not actual ransomware and was not used to analyse
a real malware sample.

Detailed observations are documented in malware_analysis.md.

## 10. INDICATORS OF COMPROMISE

Potential indicators were documented separately in IOCs.md.

Any indicators derived from the fictional scenario must be clearly
distinguished from actual indicators extracted from malware or
authentic system logs.

No real-world compromise indicators were independently established
through this academic simulation.

## 11. TIMELINE ANALYSIS

Six synthetic event records were processed using Python.

The events were arranged chronologically:

| Time (IST) | Event |
|---|---|
| 08:45 AM | LOGIN |
| 08:55 AM | FILE_CREATED |
| 09:05 AM | USB_INSERTION |
| 09:12 AM | OUTBOUND_CONNECTION |
| 09:20 AM | FILE_MODIFICATION |
| 09:30 AM | INCIDENT_REPORTED |

The resulting timeline was saved as correlated_timeline.csv.

A visual representation was generated as attack_timeline.png.

The chronological order does not establish causation or confirm
the exact attack path.

Detailed analysis is available in timeline_findings.md.

## 12. KEY FINDINGS

The academic investigation demonstrated:

1. Documentation of an incident response process.
2. Identification of potential evidence sources.
3. Creation of a synthetic evidence dataset.
4. SHA-256 hashing and integrity verification.
5. Safe demonstration of file discovery behaviour.
6. Chronological organisation of synthetic event records.
7. Preparation of a visual incident timeline.

These findings demonstrate investigative procedures rather than
proof of an actual ransomware incident.

## 13. RECOMMENDATIONS

For a real healthcare organisation, recommended security measures
include:

- Maintain regular offline and tested backups.
- Use multi-factor authentication.
- Apply security patches promptly.
- Monitor unusual outbound network connections.
- Restrict removable media access.
- Implement endpoint detection and response.
- Maintain centralised security logging.
- Conduct regular incident response exercises.
- Train employees to identify phishing and suspicious attachments.
- Maintain a documented incident response and recovery plan.

## 14. CONCLUSION

The Case Omega assignment demonstrates a structured approach to
digital forensic investigation.

The work covers incident documentation, evidence identification,
hash-based integrity verification, safe malware-behaviour simulation,
and timeline reconstruction.

All results are based on fictional and synthetic academic materials.

The investigation does not establish that a real ransomware attack
occurred or identify a real attacker.

## 15. APPENDICES

The following supporting materials are maintained in the project:

- First responder documentation.
- Evidence identification register.
- Scene sketch.
- Evidence acquisition log.
- Chain-of-custody record.
- SHA-256 hash records.
- Integrity verification report.
- Malware analysis documentation.
- Safe simulator source code.
- Indicators of Compromise documentation.
- Synthetic event records.
- Correlated timeline.
- Timeline chart.

---

**Case ID:** OCH-2026-001

**Document:** Case Omega Digital Forensic Investigation Report

**Classification:** Academic Simulation – Fictional Data Only


## 16. INVESTIGATION METHODOLOGY

The investigation followed a structured academic workflow:

1. Incident documentation and first responder preparation.
2. Identification of potential digital evidence.
3. Preparation of a synthetic evidence dataset.
4. Documentation of evidence handling and chain of custody.
5. Calculation and verification of SHA-256 hashes.
6. Creation of a separate malware analysis working copy.
7. Execution of a safe Python behavioural simulator.
8. Preparation of synthetic system event records.
9. Chronological timeline generation and visualisation.
10. Documentation of findings, limitations, and recommendations.

## 17. TOOLS AND TECHNOLOGIES

The investigation used Python, Visual Studio Code, PowerShell,
Python hashlib, Python csv, Python pathlib, and Matplotlib.

Detailed tool descriptions and their purposes are documented in:

07_Documentation/Tools_Used.md

## 18. INVESTIGATION LIMITATIONS

This investigation is an academic simulation, not a real-world
forensic examination.

The synthetic evidence does not establish:
- The identity of an attacker.
- The actual source of a cyberattack.
- The execution of real ransomware.
- The compromise of a real healthcare network.
- The authenticity of real-world system logs.

The results demonstrate investigative methods and should not be
interpreted as findings from an actual hospital incident.
