
# Evidence Integrity Verification – Case Omega

## 1. Case Information

| Field | Details |
|---|---|
| Case ID | OCH-2026-001 |
| Evidence ID | E-01 |
| Evidence Source | Simulated Server Dataset |
| Hash Algorithm | SHA-256 |
| Verification Method | Independent hash recalculation and comparison |

## 2. Objective

The objective of this activity is to verify the integrity of the simulated digital evidence files by comparing their current SHA-256 hashes with the baseline hashes recorded during the initial hashing process.

## 3. Verification Procedure

The following steps were performed:

1. Generated initial SHA-256 hashes using Python hashlib.
2. Stored the original hash values in hashes.txt.
3. Created a separate Python verification script.
4. Recalculated SHA-256 hashes for all four evidence files.
5. Compared the recalculated values with the original baseline values.
6. Generated an integrity verification report.

## 4. Verification Results

Record the actual results from integrity_verification_report.txt.

| Evidence File | Original Hash | Current Hash | Result |
|---|---|---|---|
| server_information.txt | Refer to hashes.txt | Refer to verification report | Record actual result |
| simulated_ransom_note.txt | Refer to hashes.txt | Refer to verification report | Record actual result |
| affected_files.csv | Refer to hashes.txt | Refer to verification report | Record actual result |
| server_events.csv | Refer to hashes.txt | Refer to verification report | Record actual result |

## 5. Technical Findings

SHA-256 generates a 256-bit cryptographic digest for each input file.

If the recalculated hash matches the original baseline hash, the file's contents are consistent with the contents at the time the baseline was generated, subject to the integrity of the baseline record itself.

A mismatch indicates that the file contents differ from the recorded baseline and requires further investigation.

## 6. Conclusion

The SHA-256 verification procedure was implemented using Python's hashlib library.

The results were recorded in integrity_verification_report.txt.

The verification outcome must be reported according to the actual results obtained during execution.

This activity demonstrates an important digital forensic practice: maintaining and checking the integrity of digital evidence.

## 7. Limitations

- All evidence files are fictional academic data.
- Hashing does not establish who created a file or where it originated.
- Matching hashes do not prove that the original evidence was authentic.
- The baseline hash manifest must itself be protected against unauthorized modification.
- This exercise does not constitute a real forensic disk acquisition.

**End of Integrity Verification**
