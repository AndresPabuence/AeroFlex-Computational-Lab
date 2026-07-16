import numpy as np
import matplotlib.pyplot as plt
import csv

# Physical constants
g = 9.81
rho = 1.225  # air density at sea level in kg/m^3

# Launch and object conditions
mass = 0.20
area = 0.004
v0 = 40
angle = 20
dt = 0.01

# Simplified wingtip-inspired configurations
# Cd = drag coefficient
# Cl = lift coefficient
designs = [
    {"name": "Baseline Wing", "Cd": 0.40, "Cl": 0.08},
    {"name": "Simple Wingtip", "Cd": 0.30, "Cl": 0.11},
    {"name": "Curved Wingtip", "Cd": 0.22, "Cl": 0.14},
]

theta = np.radians(angle)


def simulate_flight(Cd, Cl):
    vx = v0 * np.cos(theta)
    vy = v0 * np.sin(theta)

    x = 0
    y = 0

    x_positions = []
    y_positions = []

    max_height = 0
    flight_time = 0

    while y >= 0 and flight_time < 30:
        speed = np.sqrt(vx**2 + vy**2)

        drag_force = 0.5 * rho * Cd * area * speed**2
        lift_force = 0.5 * rho * Cl * area * speed**2

        if speed != 0:
            ax_drag = -(drag_force / mass) * (vx / speed)
            ay_drag = -(drag_force / mass) * (vy / speed)
        else:
            ax_drag = 0
            ay_drag = 0

        # Simplified lift model: lift is treated as an upward force.
        ax = ax_drag
        ay = -g + ay_drag + (lift_force / mass)

        vx += ax * dt
        vy += ay * dt

        x += vx * dt
        y += vy * dt

        if y >= 0:
            x_positions.append(x)
            y_positions.append(y)
            max_height = max(max_height, y)
            flight_time += dt

    return x_positions, y_positions, max_height, flight_time


results = []
plt.figure()

baseline_range = None

for design in designs:
    name = design["name"]
    Cd = design["Cd"]
    Cl = design["Cl"]

    x_positions, y_positions, max_height, flight_time = simulate_flight(Cd, Cl)
    range_distance = x_positions[-1]

    if name == "Baseline Wing":
        baseline_range = range_distance

    improvement = ((range_distance - baseline_range) / baseline_range) * 100
    lift_to_drag_ratio = Cl / Cd

    results.append({
        "Design": name,
        "Cd": float(Cd),
        "Cl": float(Cl),
        "Lift_to_Drag_Ratio": float(round(lift_to_drag_ratio, 2)),
        "Range_m": float(round(range_distance, 2)),
        "Max_Height_m": float(round(max_height, 2)),
        "Flight_Time_s": float(round(flight_time, 2)),
        "Range_Improvement_%": float(round(improvement, 2))
    })

    plt.plot(x_positions, y_positions, label=f"{name} (Cl/Cd={lift_to_drag_ratio:.2f})")


with open("wingtip_lift_drag_results.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            "Design",
            "Cd",
            "Cl",
            "Lift_to_Drag_Ratio",
            "Range_m",
            "Max_Height_m",
            "Flight_Time_s",
            "Range_Improvement_%"
        ]
    )
    writer.writeheader()
    writer.writerows(results)


print("\nWINGTIP LIFT-DRAG COMPARISON")
print("----------------------------")

for result in results:
    print(result)


plt.title("Wingtip-Inspired Lift and Drag Comparison")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Height (m)")
plt.legend()
plt.grid(True)
plt.savefig("wingtip_lift_drag_comparison.png", dpi=300)
plt.show()