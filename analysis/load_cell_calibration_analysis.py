"""Analyze AeroFlex V2 load-cell calibration data.

The script expects calibration readings in a CSV with these columns:
sensor, known_mass_g, reading_g, trial, notes

Blank reading_g values are treated as missing data. The script does not invent
readings or calibration results.
"""

from __future__ import annotations

import argparse
import csv
import statistics
from collections import defaultdict
from pathlib import Path


OUTPUT_PATH = Path("data/processed/load_cell_calibration_summary.csv")
REQUIRED_COLUMNS = {"sensor", "known_mass_g", "reading_g", "trial", "notes"}
RESOLUTION_CHECK_MASSES_G = {1.0, 2.0, 5.0}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Analyze load-cell calibration data for AeroFlex V2."
    )
    parser.add_argument(
        "csv_path",
        help="Path to the raw load-cell calibration CSV file.",
    )
    return parser.parse_args()


def parse_float(value: str) -> float | None:
    stripped = value.strip()
    if not stripped:
        return None

    try:
        return float(stripped)
    except ValueError:
        return None


def read_measurements(csv_path: Path) -> dict[tuple[str, float], list[float]]:
    grouped: dict[tuple[str, float], list[float]] = defaultdict(list)

    with csv_path.open("r", newline="", encoding="utf-8-sig") as csv_file:
        reader = csv.DictReader(csv_file)
        if reader.fieldnames is None:
            raise ValueError("Input CSV has no header row.")

        missing_columns = REQUIRED_COLUMNS.difference(reader.fieldnames)
        if missing_columns:
            missing = ", ".join(sorted(missing_columns))
            raise ValueError(f"Input CSV is missing required columns: {missing}")

        for row_number, row in enumerate(reader, start=2):
            sensor = row["sensor"].strip()
            known_mass_g = parse_float(row["known_mass_g"])
            reading_g = parse_float(row["reading_g"])

            if not sensor:
                raise ValueError(f"Row {row_number} has a blank sensor name.")
            if known_mass_g is None:
                raise ValueError(f"Row {row_number} has an invalid known_mass_g value.")
            if reading_g is None:
                continue

            grouped[(sensor, known_mass_g)].append(reading_g)

    return grouped


def sample_stddev(values: list[float]) -> float | None:
    if len(values) < 2:
        return None
    return statistics.stdev(values)


def summarize_measurements(
    grouped: dict[tuple[str, float], list[float]],
) -> list[dict[str, float | int | str | None]]:
    summaries: list[dict[str, float | int | str | None]] = []

    for (sensor, known_mass_g), readings in sorted(grouped.items()):
        mean_reading_g = statistics.mean(readings)
        stddev_reading_g = sample_stddev(readings)
        error_g = mean_reading_g - known_mass_g

        summaries.append(
            {
                "sensor": sensor,
                "known_mass_g": known_mass_g,
                "trial_count": len(readings),
                "mean_reading_g": mean_reading_g,
                "stddev_reading_g": stddev_reading_g,
                "error_g": error_g,
                "resolution_check": "",
            }
        )

    add_resolution_checks(summaries)
    return summaries


def add_resolution_checks(summaries: list[dict[str, float | int | str | None]]) -> None:
    by_sensor_mass = {
        (str(row["sensor"]), float(row["known_mass_g"])): row for row in summaries
    }
    sensors = sorted({str(row["sensor"]) for row in summaries})

    for sensor in sensors:
        zero_row = by_sensor_mass.get((sensor, 0.0))

        for mass_g in sorted(RESOLUTION_CHECK_MASSES_G):
            row = by_sensor_mass.get((sensor, mass_g))
            if row is None:
                continue

            row["resolution_check"] = estimate_resolution(row, zero_row)


def estimate_resolution(
    mass_row: dict[str, float | int | str | None],
    zero_row: dict[str, float | int | str | None] | None,
) -> str:
    if zero_row is None:
        return "insufficient_data_no_zero"

    if int(mass_row["trial_count"]) < 2 or int(zero_row["trial_count"]) < 2:
        return "insufficient_repeated_readings"

    mass_stddev = mass_row["stddev_reading_g"]
    zero_stddev = zero_row["stddev_reading_g"]
    if mass_stddev is None or zero_stddev is None:
        return "insufficient_repeated_readings"

    separation_g = abs(float(mass_row["mean_reading_g"]) - float(zero_row["mean_reading_g"]))
    noise_threshold_g = 3.0 * max(float(mass_stddev), float(zero_stddev))

    if separation_g > noise_threshold_g:
        return "clearly_detectable_vs_zero_noise"
    return "not_clearly_detectable_vs_zero_noise"


def write_summary_csv(summaries: list[dict[str, float | int | str | None]]) -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "sensor",
        "known_mass_g",
        "trial_count",
        "mean_reading_g",
        "stddev_reading_g",
        "error_g",
        "resolution_check",
    ]

    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in summaries:
            writer.writerow(format_row_for_csv(row))


def format_optional_float(value: float | int | str | None) -> str:
    if value is None:
        return ""
    if isinstance(value, (float, int)):
        return f"{value:.6g}"
    return str(value)


def format_row_for_csv(
    row: dict[str, float | int | str | None],
) -> dict[str, str | int]:
    return {
        "sensor": str(row["sensor"]),
        "known_mass_g": format_optional_float(row["known_mass_g"]),
        "trial_count": int(row["trial_count"]),
        "mean_reading_g": format_optional_float(row["mean_reading_g"]),
        "stddev_reading_g": format_optional_float(row["stddev_reading_g"]),
        "error_g": format_optional_float(row["error_g"]),
        "resolution_check": str(row["resolution_check"]),
    }


def print_summary_table(summaries: list[dict[str, float | int | str | None]]) -> None:
    print("AeroFlex V2 load-cell calibration summary")
    print("Calculated only from collected reading_g values.")
    print()
    print(
        f"{'Sensor':<12} {'Mass (g)':>8} {'n':>3} {'Mean (g)':>10} "
        f"{'Std dev (g)':>12} {'Error (g)':>10} {'Resolution check':<38}"
    )
    print("-" * 101)

    for row in summaries:
        print(
            f"{str(row['sensor']):<12} "
            f"{float(row['known_mass_g']):>8.3g} "
            f"{int(row['trial_count']):>3} "
            f"{float(row['mean_reading_g']):>10.4f} "
            f"{format_optional_float(row['stddev_reading_g']):>12} "
            f"{float(row['error_g']):>10.4f} "
            f"{str(row['resolution_check']):<38}"
        )

    print()
    print(f"Saved CSV: {OUTPUT_PATH}")


def main() -> None:
    args = parse_args()
    csv_path = Path(args.csv_path)

    grouped = read_measurements(csv_path)
    if not any(grouped.values()):
        print("Calibration data has not been collected yet: no numeric reading_g values were found.")
        return

    summaries = summarize_measurements(grouped)
    write_summary_csv(summaries)
    print_summary_table(summaries)


if __name__ == "__main__":
    main()
