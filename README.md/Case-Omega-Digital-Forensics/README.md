# Case Omega – Digital Forensics Investigation

## Assignment 3 – Unit 3: Investigation of Cyber Crimes

**Case ID:** OCH-2026-001  
**Case Title:** Investigating a Ransomware Attack on a Healthcare Network  
**Organisation:** OmegaCare Multispeciality Hospital  
**Incident Date:** 20 November 2026  
**Investigation Type:** Academic Digital Forensics Simulation

## 1. Project Overview

This project demonstrates a structured digital forensic investigation of a fictional ransomware incident involving a healthcare network.

The investigation covers first responder procedures, evidence identification, evidence preservation, SHA-256 hash verification, safe malware-behaviour simulation, timeline correlation, and forensic reporting.

**All organisations, events, logs, and evidence records used in this project are fictional or synthetically generated for educational purposes. No real hospital systems or patient information were accessed.**

## 2. Investigation Objectives

- Document the incident scenario and first responder procedures.
- Identify and organise potential digital evidence.
- Demonstrate evidence integrity verification using SHA-256.
- Safely simulate ransomware-like behaviour without encrypting or deleting files.
- Build and analyse a chronological incident timeline.
- Prepare a structured forensic investigation report.

## 3. Project Structure

```text
Case-Omega-Digital-Forensics/
│
├── 01_First_Responder/
│   ├── Incident_Overview.md
│   ├── First_Responder_SOP.md
│   ├── Evidence_Identification.md
│   ├── scene_sketch.png
│   └── scene_sketch.drawio
│
├── 02_Evidence_Collection/
│   ├── simulated_server/
│   ├── working documentation and hash reports
│   ├── generate_hash.py
│   └── verify_hash.py
│
├── 03_Malware_Analysis/
│   ├── working_copy/
│   ├── test_victim_files/
│   ├── safe_ransomware_simulator.py
│   └── malware_analysis.md
│
├── 04_Timeline_Analysis/
│   ├── system_logs.csv
│   ├── create_timeline.py
│   ├── correlated_timeline.csv
│   ├── generate_timeline_chart.py
│   ├── attack_timeline.png
│   └── timeline_findings.md
│
├── 05_Forensic_Report/
│   ├── Case_Omega_Forensic_Report.md
│   └── Case_Omega_Forensic_Report.pdf
│
├── 06_Screenshots/
│
├── 07_Documentation/
│   └── Tools_Used.md
│
└── README.md
```

*Some supporting files are grouped in the structure above for readability.*

## 4. Tools and Technologies

- Python
- Visual Studio Code
- SHA-256 hashing using Python hashlib
- CSV and file-handling modules
- Matplotlib
- PowerShell
- Markdown documentation

## 5. Investigation Phases

1. First responder documentation and evidence identification.
2. Simulated evidence collection and integrity verification.
3. Safe ransomware-behaviour simulation and analysis.
4. Synthetic event timeline creation and analysis.
5. Final forensic report preparation.

## 6. Safety and Ethical Considerations

The ransomware simulator is a harmless educational demonstration. It does not encrypt, delete, or overwrite files and does not perform network communication, persistence, or credential theft.

The investigation uses synthetic data and does not represent a real cybercrime investigation or a legally admissible forensic acquisition.

## 7. Final Deliverable

The primary deliverable is:

`05_Forensic_Report/Case_Omega_Forensic_Report.pdf`

The PDF contains the investigation methodology, evidence documentation, integrity verification, malware analysis, timeline findings, recommendations, and limitations.

## 8. Conclusion

This project demonstrates the fundamental stages of a digital forensic investigation through a controlled ransomware incident scenario. It highlights evidence preservation, integrity checking, safe analysis, chronological reconstruction, and accurate forensic documentation.

**Project Status:** Academic simulation completed.
