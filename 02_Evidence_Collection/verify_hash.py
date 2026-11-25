
import hashlib
import re
from pathlib import Path
from datetime import datetime

# Case information
CASE_ID = "OCH-2026-001"
EVIDENCE_ID = "E-01"

# Project paths
BASE_DIR = Path(__file__).resolve().parent
EVIDENCE_DIR = BASE_DIR / "simulated_server"
HASH_FILE = BASE_DIR / "hashes.txt"
REPORT_FILE = BASE_DIR / "integrity_verification_report.txt"

EXPECTED_FILES = [
    "server_information.txt",
    "simulated_ransom_note.txt",
    "affected_files.csv",
    "server_events.csv"
]


def calculate_sha256(file_path):
    """Calculate a fresh SHA-256 hash."""

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def read_original_hashes():
    """Read the baseline hashes from hashes.txt."""

    if not HASH_FILE.is_file():
        raise FileNotFoundError("hashes.txt was not found.")

    original_hashes = {}

    with open(HASH_FILE, "r", encoding="utf-8") as file:
        for line in file:
            if line.startswith("Filename: "):
                filename = line.strip().split("Filename: ", 1)[1]

            elif line.startswith("SHA-256: "):
                hash_value = line.strip().split("SHA-256: ", 1)[1]

                if not re.fullmatch(r"[0-9a-f]{64}", hash_value):
                    raise ValueError(
                        f"Invalid SHA-256 value for {filename}"
                    )

                original_hashes[filename] = hash_value

    return original_hashes


def main():
    print("=" * 60)
    print("CASE OMEGA - EVIDENCE INTEGRITY VERIFICATION")
    print("=" * 60)

    try:
        original_hashes = read_original_hashes()
    except (FileNotFoundError, ValueError) as error:
        print(f"ERROR: {error}")
        return

    results = []

    for filename in EXPECTED_FILES:
        file_path = EVIDENCE_DIR / filename

        if not file_path.is_file():
            results.append((filename, "MISSING", "Not available"))
            print(f"{filename}: MISSING")
            continue

        if filename not in original_hashes:
            results.append((filename, "NO BASELINE", "Not available"))
            print(f"{filename}: NO BASELINE HASH")
            continue

        original_hash = original_hashes[filename]
        current_hash = calculate_sha256(file_path)

        if original_hash == current_hash:
            status = "MATCH"
        else:
            status = "MISMATCH"

        results.append((filename, status, current_hash))

        print(f"\nFile: {filename}")
        print(f"Original Hash: {original_hash}")
        print(f"Current Hash:  {current_hash}")
        print(f"Result: {status}")

    # Generate a verification report
    verified_at = datetime.now().astimezone().isoformat(
        timespec="seconds"
    )

    with open(REPORT_FILE, "w", encoding="utf-8") as report:
        report.write("CASE OMEGA - INTEGRITY VERIFICATION REPORT\n")
        report.write("=" * 60 + "\n")
        report.write(f"Case ID: {CASE_ID}\n")
        report.write(f"Evidence ID: {EVIDENCE_ID}\n")
        report.write("Algorithm: SHA-256\n")
        report.write(f"Verification Time: {verified_at}\n\n")

        for filename, status, current_hash in results:
            report.write(f"Filename: {filename}\n")
            report.write(f"Verification Result: {status}\n")
            report.write(f"Current SHA-256: {current_hash}\n")
            report.write("-" * 60 + "\n")

        all_match = (
            len(results) == len(EXPECTED_FILES)
            and all(result[1] == "MATCH" for result in results)
        )

        report.write("\nOVERALL RESULT: ")
        report.write(
            "ALL FILES MATCH THE BASELINE\n"
            if all_match
            else "VERIFICATION ISSUES FOUND\n"
        )

        report.write(
            "\nNote: A matching hash supports integrity verification "
            "against the recorded baseline. It does not independently "
            "prove the authenticity or origin of the evidence.\n"
        )

    print("\n" + "=" * 60)

    if all_match:
        print("SUCCESS: ALL FOUR FILES MATCH THE BASELINE.")
    else:
        print("WARNING: ONE OR MORE VERIFICATION ISSUES WERE FOUND.")

    print(f"Report saved to: {REPORT_FILE}")
    print("=" * 60)


if __name__ == "__main__":
    main()
