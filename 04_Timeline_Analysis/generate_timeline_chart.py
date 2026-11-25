
import csv
from pathlib import Path
from datetime import datetime

import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# --------------------------------------------------
# CASE OMEGA - VISUAL TIMELINE
# Synthetic academic investigation
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

INPUT_FILE = BASE_DIR / "correlated_timeline.csv"
OUTPUT_FILE = BASE_DIR / "attack_timeline.png"

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def load_timeline():
    """Load the correlated synthetic timeline."""

    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"File not found: {INPUT_FILE.name}"
        )

    events = []

    with INPUT_FILE.open(
        "r", encoding="utf-8-sig", newline=""
    ) as file:

        reader = csv.DictReader(file)

        required = [
            "timestamp",
            "event_type",
            "description",
            "evidence_status"
        ]

        if not reader.fieldnames or any(
            column not in reader.fieldnames
            for column in required
        ):
            raise ValueError(
                "The timeline CSV is missing required columns."
            )

        for row in reader:

            timestamp = datetime.strptime(
                row["timestamp"].strip(),
                TIME_FORMAT
            )

            events.append({
                "timestamp": timestamp,
                "event_type": row["event_type"],
                "description": row["description"],
                "evidence_status": row["evidence_status"]
            })

    if not events:
        raise ValueError("No timeline events found.")

    if any(
        event["evidence_status"].lower() != "synthetic"
        for event in events
    ):
        raise ValueError(
            "Expected all records to be marked Synthetic."
        )

    return events


def create_chart(events):
    """Create and save a chronological timeline chart."""

    events.sort(key=lambda event: event["timestamp"])

    dates = [event["timestamp"] for event in events]

    labels = [
        event["event_type"].replace("_", "\n")
        for event in events
    ]

    y_positions = list(range(len(events), 0, -1))

    fig, ax = plt.subplots(figsize=(13, 7))

    # Main horizontal timeline
    ax.hlines(
        y=0,
        xmin=min(dates),
        xmax=max(dates),
        linewidth=2
    )

    # Event markers
    ax.scatter(
        dates,
        [0] * len(dates),
        s=100,
        zorder=3
    )

    # Alternate event labels above and below the timeline
    for index, event in enumerate(events):

        vertical_position = 1 if index % 2 == 0 else -1

        ax.annotate(
            (
                f"{event['event_type']}\n"
                f"{event['timestamp'].strftime('%H:%M')}\n"
                f"{event['description'][:48]}"
            ),
            xy=(event["timestamp"], 0),
            xytext=(event["timestamp"], vertical_position),
            ha="center",
            va="center",
            fontsize=8,
            arrowprops={
                "arrowstyle": "-",
                "linewidth": 1
            }
        )

    ax.set_title(
        "CASE OMEGA - SYNTHETIC INCIDENT TIMELINE",
        fontsize=15,
        fontweight="bold"
    )

    ax.text(
        0.5,
        0.96,
        "Academic simulation | 20 November 2026 | IST",
        transform=ax.transAxes,
        ha="center",
        fontsize=10
    )

    ax.set_xlabel("Time (IST)")
    ax.set_ylim(-1.8, 1.8)
    ax.set_yticks([])
    ax.xaxis.set_major_formatter(
        mdates.DateFormatter("%H:%M")
    )

    ax.grid(
        axis="x",
        linestyle="--",
        alpha=0.4
    )

    ax.text(
        0.5,
        0.02,
        "All events are fictional synthetic records. "
        "Temporal order does not establish causation.",
        transform=ax.transAxes,
        ha="center",
        fontsize=9
    )

    fig.autofmt_xdate()
    fig.tight_layout(rect=[0, 0.08, 1, 0.90])

    fig.savefig(
        OUTPUT_FILE,
        dpi=200,
        bbox_inches="tight"
    )

    plt.close(fig)

    print("Timeline chart generated successfully.")
    print(f"Events displayed: {len(events)}")
    print(f"Saved file: {OUTPUT_FILE.name}")


def main():
    print("CASE OMEGA - TIMELINE CHART GENERATOR")

    try:
        events = load_timeline()
        create_chart(events)

    except (FileNotFoundError, ValueError, OSError) as error:
        print(f"ERROR: {error}")


if __name__ == "__main__":
    main()
