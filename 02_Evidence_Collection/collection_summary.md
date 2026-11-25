
# Evidence Collection Summary – Case Omega

## 1. Case Information

| Field | Details |
|---|---|
| Case ID | OCH-2026-001 |
| Case Name | Case Omega – Ransomware Investigation |
| Organization | OmegaCare Multispeciality Hospital |
| Incident Date | 20 November 2026 |
| Investigation Type | Digital Forensics |
| Evidence Asset | HOSP-SRV-01 |
| Asset ID | A-01 |
| Evidence ID | E-01 |

## 2. Evidence Collection Overview

The evidence collection phase involved preparing a fictional digital evidence dataset for the academic investigation of a suspected ransomware incident.

The dataset contains four simulated evidence files representing server information, a ransom message, affected-file records, and server event records.

No actual hospital systems, production servers, or patient information were accessed.

## 3. Evidence Collected for the Simulation

| File Name | Description |
|---|---|
| server_information.txt | Fictional server information |
| simulated_ransom_note.txt | Harmless simulated ransom message |
| affected_files.csv | Fictional list of reported inaccessible files |
| server_events.csv | Synthetic server event records |

## 4. Evidence Documentation

The following documentation was prepared:

- acquisition_log.md
- chain_of_custody.csv
- hashes.txt
- integrity_verification_report.txt
- integrity_verification.md

## 5. Integrity Verification

SHA-256 hashes were generated using Python's hashlib library.

A separate verification script recalculated the hashes and compared them with the original baseline values.

Verification outcome: [Enter the actual result from the verification report.]

The detailed verification results are available in integrity_verification_report.txt.

## 6. Evidence Preservation

The original simulated evidence files are retained in:

02_Evidence_Collection/simulated_server/

A separate working copy will be used for the next phase of the academic investigation.

The original files should not be modified during subsequent analysis.

## 7. Tools Used

- Python 3
- Python hashlib library
- Visual Studio Code
- SHA-256 cryptographic hashing

## 8. Limitations

- This project uses fictional academic evidence.
- No actual forensic acquisition of a physical storage device was performed.
- No bit-for-bit disk image was created.
- The ZIP archive format, if used in a later demonstration, must not be described as a raw forensic disk image.
- Hash verification supports integrity checking against the recorded baseline but does not prove evidence authenticity or origin.

## 9. Conclusion

The simulated evidence collection phase has been completed.

Evidence preparation, acquisition documentation, chain-of-custody documentation, SHA-256 hashing, and independent integrity verification have been demonstrated.

The project is now ready to proceed to the malware analysis phase using a separate working copy and safe simulation techniques.

**End of Evidence Collection Summary**
