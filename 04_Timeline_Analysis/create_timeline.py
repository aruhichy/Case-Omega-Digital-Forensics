
import csv
from pathlib import Path
from datetime import datetime

# --------------------------------------------------
# CASE OMEGA - TIMELINE GENERATOR
# Academic forensic investigation simulation
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

INPUT_FILE = BASE_DIR / "system_logs.csv"
OUTPUT_FILE = BASE_DIR / "correlated_timeline.csv"

TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"

REQUIRED_COLUMNS = [
    "timestamp",
    "event_id",
    "hostname",
    "event_type",
    "description",
    "source",
    "evidence_status"
]


def load_events():
    """Read and validate the synthetic event records."""

    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Input file not found: {INPUT_FILE}"
        )

    events = []

    with INPUT_FILE.open(
        "r", encoding="utf-8-sig", newline=""
    ) as file:

        reader = csv.DictReader(file)

        if not reader.fieldnames:
            raise ValueError("CSV file is empty.")

        missing_columns = [
            column for column in REQUIRED_COLUMNS
            if column not in reader.fieldnames
        ]

        if missing_columns:
            raise ValueError(
                f"Missing CSV columns: {missing_columns}"
            )

        for row_number, row in enumerate(reader, start=2):

            try:
                timestamp = datetime.strptime(
                    row["timestamp"].strip(),
                    TIMESTAMP_FORMAT
                )

                event = {
                    "timestamp": timestamp,
                    "event_id": row["event_id"].strip(),
                    "hostname": row["hostname"].strip(),
                    "event_type": row["event_type"].strip(),
                    "description": row["description"].strip(),
                    "source": row["source"].strip(),
                    "evidence_status": row["evidence_status"].strip()
                }

                events.append(event)

            except (ValueError, AttributeError) as error:
                raise ValueError(
                    f"Invalid record at CSV row {row_number}: {error}"
                )

    if not events:
        raise ValueError("No event records were found.")

    return events


def generate_timeline(events):
    """Sort events and write the correlated timeline."""

    events.sort(key=lambda event: event["timestamp"])

    output_columns = [
        "sequence",
        "timestamp",
        "event_id",
        "hostname",
        "event_type",
        "description",
        "source",
        "evidence_status"
    ]

    with OUTPUT_FILE.open(
        "w", encoding="utf-8", newline=""
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=output_columns
        )

        writer.writeheader()

        for sequence, event in enumerate(events, start=1):

            writer.writerow({
                "sequence": sequence,
                "timestamp": event["timestamp"].strftime(
                    TIMESTAMP_FORMAT
                ),
                "event_id": event["event_id"],
                "hostname": event["hostname"],
                "event_type": event["event_type"],
                "description": event["description"],
                "source": event["source"],
                "evidence_status": event["evidence_status"]
            })


def main():
    print("=" * 55)
    print("CASE OMEGA - TIMELINE ANALYSIS")
    print("Synthetic academic investigation")
    print("=" * 55)

    try:
        events = load_events()

        print(f"\nRecords loaded: {len(events)}")

        generate_timeline(events)

        print("\nTimeline generated successfully.")
        print(f"Output file: {OUTPUT_FILE.name}")

        print("\nChronological Event Summary:")

        for event in events:
            print(
                event["timestamp"].strftime(TIMESTAMP_FORMAT),
                "|",
                event["event_type"]
            )

        print("\nAll records are marked as synthetic.")
        print("No real hospital logs were processed.")

    except (FileNotFoundError, ValueError, OSError) as error:
        print(f"\nERROR: {error}")


if __name__ == "__main__":
    main()
