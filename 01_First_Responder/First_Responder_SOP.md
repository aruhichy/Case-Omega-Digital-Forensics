
# FIRST RESPONDER STANDARD OPERATING PROCEDURE (SOP)

## Case Details

- Case ID: OCH-2026-001
- Case Name: Case Omega
- Organization: OmegaCare Multispeciality Hospital
- Incident: Suspected Ransomware Attack
- Location: New Delhi, India
- Investigation Type: Digital Forensics

---

## 1. Purpose

The purpose of this SOP is to establish a systematic
procedure for first responders handling a suspected
ransomware incident at OmegaCare Multispeciality
Hospital.

The procedure focuses on protecting people,
securing the scene, preserving digital evidence and
preventing unnecessary modification of compromised
systems.

## 2. First Responder Responsibilities

The first responder must:

- Ensure the safety of hospital patients and staff.
- Secure the affected area.
- Prevent unauthorized access to devices.
- Document the original condition of the scene.
- Identify potentially affected digital devices.
- Preserve volatile and non-volatile evidence.
- Maintain proper evidence records.
- Follow the chain of custody procedure.

## 3. Step-by-Step First Responder Procedure

### Step 1: Ensure Safety

Check whether the incident is affecting hospital
operations or patient care.

Coordinate with hospital management and the IT
department to ensure that critical medical services
remain operational.

### Step 2: Secure the Scene

Restrict access to the affected server room and
workstations.

Only authorized personnel should enter the area.

Maintain an entry and exit record.

### Step 3: Document the Scene

Take photographs of:

- Affected computer screens.
- Server equipment.
- Network devices.
- Connected USB devices.
- Visible error messages or ransom notes.

Record the date, time and person documenting
each photograph.

Do not unnecessarily interact with the devices.

### Step 4: Identify Digital Evidence

Identify potentially relevant evidence, including:

- Hospital servers.
- Employee workstations.
- External storage devices.
- Network switches.
- Firewall devices.
- System and security logs.
- Browser histories.
- Cloud access records.

Assign a unique evidence identification number
to every collected item.

### Step 5: Preserve Volatile Evidence

Where feasible and authorized, preserve volatile
information before shutdown.

Examples include:

- Running processes.
- Active network connections.
- Logged-in users.
- RAM contents.
- Current system time.

Use trained forensic personnel and approved
tools to collect this information.

### Step 6: Isolate Affected Systems

Coordinate with the incident response team to
isolate compromised devices from the network.

Avoid unnecessary shutdown or restart because
volatile evidence may be lost.

Patient safety and continuity of critical hospital
services must be considered before isolation.

### Step 7: Acquire Digital Evidence

Create forensic copies of authorized storage
devices using appropriate forensic tools.

FTK Imager or validated command-line imaging
tools may be used.

Record:

- Device identification.
- Acquisition date and time.
- Acquisition method.
- Tool and version.
- Investigator details.
- Image file location.

### Step 8: Calculate Evidence Hashes

Generate SHA-256 hashes for acquired forensic
images.

Record the hash values and perform verification
to check evidence integrity.

### Step 9: Maintain Chain of Custody

Document every evidence collection, transfer,
access and storage activity.

Record the names, dates, times and signatures
of the persons handling the evidence.

### Step 10: Secure Evidence

Store collected evidence in a controlled and
access-restricted location.

Preserve the original evidence and perform
examination on verified forensic copies.

### Step 11: Prepare Investigation Notes

Document observations, actions performed,
tools used and preliminary findings.

Clearly distinguish observed evidence from
assumptions and conclusions.

### Step 12: Prepare the Final Report

Prepare a forensic investigation report containing:

- Incident summary.
- First responder activities.
- Evidence collected.
- Acquisition and hash verification details.
- Malware analysis.
- Attack timeline.
- Legal considerations.
- Recommendations.

## 4. Important Precautions

1. Never modify original digital evidence unnecessarily.
2. Do not delete suspicious files.
3. Do not execute unknown programs.
4. Do not connect unknown USB devices.
5. Do not access systems without authorization.
6. Maintain accurate date and time records.
7. Protect confidential hospital information.
8. Document every action performed.
9. Preserve original evidence securely.
10. Follow applicable legal and organizational procedures.

## 5. Expected Outcome

Following this SOP helps ensure that the incident
scene is documented, digital evidence is protected,
and forensic examination can be conducted in a
systematic and reproducible manner.

---

**Document:** First Responder SOP  
**Case ID:** OCH-2026-001  
**Project:** Case Omega  
**Status:** Prepared for Academic Simulation
