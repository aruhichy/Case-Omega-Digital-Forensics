
import hashlib
from pathlib import Path
from datetime import datetime

# Case information
CASE_ID = "OCH-2026-001"
EVIDENCE_ID = "E-01"

# Find the evidence folder relative to this Python script
BASE_DIR = Path(__file__).resolve().parent
EVIDENCE_DIR = BASE_DIR / "simulated_server"

# Output file for the SHA-256 hash records
OUTPUT_FILE = BASE_DIR / "hashes.txt"

# Files expected in the simulated evidence dataset
EXPECTED_FILES = [
    "server_information.txt",
    "simulated_ransom_note.txt",
    "affected_files.csv",
    "server_events.csv"
]


def calculate_sha256(file_path):
    """Calculate the SHA-256 hash of a file."""

    sha256 = hashlib.sha256()

    # Read the file in chunks to handle larger files efficiently
    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(4096)

            if not chunk:
                break

            sha256.update(chunk)

    return sha256.hexdigest()


def main():
    print("=" * 55)
    print("CASE OMEGA - SHA-256 EVIDENCE HASHING")
    print("=" * 55)

    if not EVIDENCE_DIR.exists():
        print("ERROR: simulated_server folder was not found.")
        return

    records = []

    for filename in EXPECTED_FILES:
        file_path = EVIDENCE_DIR / filename

        if not file_path.is_file():
            print(f"ERROR: Missing evidence file: {filename}")
            return

        file_hash = calculate_sha256(file_path)
        file_size = file_path.stat().st_size

        records.append({
            "filename": filename,
            "hash": file_hash,
            "size": file_size
        })

        print(f"\nFile: {filename}")
        print(f"Size: {file_size} bytes")
        print(f"SHA-256: {file_hash}")

    # Create the hash manifest
    generated_at = datetime.now().astimezone().isoformat(
        timespec="seconds"
    )

    with open(OUTPUT_FILE, "w", encoding="utf-8") as output:
        output.write("CASE OMEGA - EVIDENCE HASH MANIFEST\n")
        output.write("=" * 55 + "\n")
        output.write(f"Case ID: {CASE_ID}\n")
        output.write(f"Evidence ID: {EVIDENCE_ID}\n")
        output.write("Evidence Type: Simulated Server Dataset\n")
        output.write("Hash Algorithm: SHA-256\n")
        output.write(f"Generated At: {generated_at}\n")
        output.write("Evidence Source: simulated_server/\n")
        output.write("\n")

        for record in records:
            output.write(f"Filename: {record['filename']}\n")
            output.write(f"Size: {record['size']} bytes\n")
            output.write(f"SHA-256: {record['hash']}\n")
            output.write("-" * 55 + "\n")

        output.write(
            "\nNote: These hashes establish a baseline for the "
            "prepared academic simulation files. They do not "
            "prove the authenticity of real-world evidence.\n"
        )

    print("\n" + "=" * 55)
    print("HASHING COMPLETED SUCCESSFULLY")
    print(f"Hash records saved to: {OUTPUT_FILE}")
    print("=" * 55)


if __name__ == "__main__":
    main()
