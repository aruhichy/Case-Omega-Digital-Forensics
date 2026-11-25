
# Case Omega – Tools and Technologies Used

## 1. Investigation Environment

| Component | Details |
|---|---|
| Operating System | Windows (Investigation workstation) |
| Programming Language | Python |
| Code Editor | Visual Studio Code |
| Investigation Type | Academic Digital Forensics Simulation |

## 2. Tools Used

### Visual Studio Code
Used to create, edit, organise, and maintain investigation documentation and Python scripts.

### Python
Used for evidence hashing, hash verification, safe ransomware-behaviour simulation, and timeline generation.

### Python hashlib
Used to calculate SHA-256 hashes of the synthetic evidence files.

### Python csv
Used to read and process synthetic event records and generate a correlated timeline.

### Python pathlib
Used for file and directory handling within the project.

### Matplotlib
Used to generate the visual incident timeline chart.

### PowerShell
Used to execute Python scripts, inspect files, and manage the project directory.

### Git and GitHub
[Update this section after completing the GitHub phase. Do not claim that the repository has already been published.]

## 3. Investigation Scripts

| Script | Purpose |
|---|---|
| generate_hash.py | Calculate SHA-256 hashes |
| verify_hash.py | Verify evidence integrity |
| safe_ransomware_simulator.py | Demonstrate safe file discovery behaviour |
| create_timeline.py | Generate chronological event records |
| generate_timeline_chart.py | Generate the visual timeline |

## 4. Safety Considerations

- Only fictional demonstration data was used.
- No real hospital records were accessed.
- No actual ransomware was downloaded or executed.
- The simulator did not encrypt or delete files.
- The original synthetic evidence was preserved.
- All event records were labelled as synthetic.

## 5. Conclusion

The tools used in this assignment demonstrate basic digital forensic
documentation, hashing, integrity verification, safe behavioural
simulation, and timeline analysis.
