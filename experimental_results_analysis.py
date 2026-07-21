import csv
import matplotlib.pyplot as plt

input_file = "experimental_data_template.csv"


def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


data = []

with open(input_file, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        distance = row["Distance_m"]
        flight_time = row["Flight_Time_s"]
        stability = row["Stability_Rating"]

        if is_number(distance) and is_number(flight_time) and is_number(stability):
            data.append({
                "Configuration": row["Configuration"],
                "Distance_m": float(distance),
                "Flight_Time_s": float(flight_time),
                "Stability_Rating": float(stability)
            })


if len(data) == 0:
    print("\nNo experimental data found yet.")
    print("Fill experimental_data_template.csv with real test results first.")
    print("Then run this script again.")

else:
    configurations = sorted(set(row["Configuration"] for row in data))

    summary = []

    for config in configurations:
        config_data = [row for row in data if row["Configuration"] == config]

        avg_distance = sum(row["Distance_m"] for row in config_data) / len(config_data)
        avg_time = sum(row["Flight_Time_s"] for row in config_data) / len(config_data)
        avg_stability = sum(row["Stability_Rating"] for row in config_data) / len(config_data)

        summary.append({
            "Configuration": config,
            "Average_Distance_m": round(avg_distance, 2),
            "Average_Flight_Time_s": round(avg_time, 2),
            "Average_Stability": round(avg_stability, 2),
            "Trials": len(config_data)
        })

    print("\nEXPERIMENTAL RESULTS SUMMARY")
    print("-----------------------------")

    for row in summary:
        print(row)

    with open("experimental_results_summary.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Configuration",
                "Average_Distance_m",
                "Average_Flight_Time_s",
                "Average_Stability",
                "Trials"
            ]
        )
        writer.writeheader()
        writer.writerows(summary)

    labels = [row["Configuration"] for row in summary]
    distances = [row["Average_Distance_m"] for row in summary]

    plt.figure(figsize=(8, 5))
    plt.bar(labels, distances)

    plt.title("Experimental Prototype Comparison")
    plt.xlabel("Prototype Configuration")
    plt.ylabel("Average Distance (m)")

    plt.tight_layout()
    plt.savefig("experimental_results_comparison.png", dpi=300)
    plt.show()