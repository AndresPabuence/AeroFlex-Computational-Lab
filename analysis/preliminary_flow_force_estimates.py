"""Preliminary force-scale estimates for AeroFlex V2.

These calculations use centerline fan velocity measurements and provisional wing
dimensions. They are not experimental lift or drag results, and they do not
compare wingtip geometries.
"""

from __future__ import annotations

import csv
from pathlib import Path


VELOCITY_MEASUREMENTS = [
    {"distance_cm": 10, "velocity_m_s": 7.8},
    {"distance_cm": 20, "velocity_m_s": 5.7},
    {"distance_cm": 30, "velocity_m_s": 4.0},
    {"distance_cm": 40, "velocity_m_s": 3.8},
]

SPAN_M = 0.20
CHORD_M = 0.07
AREA_M2 = SPAN_M * CHORD_M

RHO_KG_M3 = 1.15
MU_PA_S = 1.9e-5

CL_RANGE = (0.2, 0.8)
CD_RANGE = (0.05, 0.25)
NEWTONS_PER_GRAM_FORCE = 0.00980665

OUTPUT_PATH = Path("data/processed/preliminary_force_estimates.csv")


def newtons_to_gram_force(force_n: float) -> float:
    return force_n / NEWTONS_PER_GRAM_FORCE


def calculate_rows() -> list[dict[str, float]]:
    rows = []

    for measurement in VELOCITY_MEASUREMENTS:
        distance_cm = measurement["distance_cm"]
        velocity_m_s = measurement["velocity_m_s"]

        reynolds_number = RHO_KG_M3 * velocity_m_s * CHORD_M / MU_PA_S
        dynamic_pressure_pa = 0.5 * RHO_KG_M3 * velocity_m_s**2
        q_s_n = dynamic_pressure_pa * AREA_M2

        lift_min_n = q_s_n * CL_RANGE[0]
        lift_max_n = q_s_n * CL_RANGE[1]
        drag_min_n = q_s_n * CD_RANGE[0]
        drag_max_n = q_s_n * CD_RANGE[1]

        rows.append(
            {
                "distance_cm": distance_cm,
                "velocity_m_s": velocity_m_s,
                "reynolds_number": reynolds_number,
                "dynamic_pressure_pa": dynamic_pressure_pa,
                "qS_N": q_s_n,
                "lift_min_N": lift_min_n,
                "lift_max_N": lift_max_n,
                "lift_min_gf": newtons_to_gram_force(lift_min_n),
                "lift_max_gf": newtons_to_gram_force(lift_max_n),
                "drag_min_N": drag_min_n,
                "drag_max_N": drag_max_n,
                "drag_min_gf": newtons_to_gram_force(drag_min_n),
                "drag_max_gf": newtons_to_gram_force(drag_max_n),
            }
        )

    return rows


def save_csv(rows: list[dict[str, float]]) -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "distance_cm",
        "velocity_m_s",
        "reynolds_number",
        "dynamic_pressure_pa",
        "qS_N",
        "lift_min_N",
        "lift_max_N",
        "lift_min_gf",
        "lift_max_gf",
        "drag_min_N",
        "drag_max_N",
        "drag_min_gf",
        "drag_max_gf",
    ]

    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def print_table(rows: list[dict[str, float]]) -> None:
    print("AeroFlex V2 preliminary force-scale estimates only")
    print("Not experimental lift or drag results; no wingtip geometry comparison.")
    print()
    print(
        f"{'Distance':>8}  {'V':>6}  {'Re':>9}  {'q':>8}  {'qS':>8}  "
        f"{'Lift range':>22}  {'Drag range':>22}"
    )
    print(
        f"{'(cm)':>8}  {'(m/s)':>6}  {'(-)':>9}  {'(Pa)':>8}  {'(N)':>8}  "
        f"{'(N / gf)':>22}  {'(N / gf)':>22}"
    )
    print("-" * 116)

    for row in rows:
        lift_range = (
            f"{row['lift_min_N']:.4f}-{row['lift_max_N']:.4f} N / "
            f"{row['lift_min_gf']:.1f}-{row['lift_max_gf']:.1f} gf"
        )
        drag_range = (
            f"{row['drag_min_N']:.4f}-{row['drag_max_N']:.4f} N / "
            f"{row['drag_min_gf']:.1f}-{row['drag_max_gf']:.1f} gf"
        )

        print(
            f"{row['distance_cm']:8.0f}  "
            f"{row['velocity_m_s']:6.1f}  "
            f"{row['reynolds_number']:9.0f}  "
            f"{row['dynamic_pressure_pa']:8.2f}  "
            f"{row['qS_N']:8.4f}  "
            f"{lift_range:>22}  "
            f"{drag_range:>22}"
        )

    print()
    print(f"Saved CSV: {OUTPUT_PATH}")


def main() -> None:
    rows = calculate_rows()
    save_csv(rows)
    print_table(rows)


if __name__ == "__main__":
    main()
