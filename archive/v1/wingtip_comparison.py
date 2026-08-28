import numpy as np
import matplotlib.pyplot as plt
import csv

# Physical constants
g = 9.81
rho = 1.225  # air density at sea level in kg/m^3

# Launch and object conditions
mass = 0.20
area = 0.01
v0 = 40
angle = 45
dt = 0.01

# Wingtip-inspired conceptual configurations
# Cd is used as a simplified drag-performance proxy.
designs = [
    {"name": "Baseline Wing", "Cd": 0.40},
    {"name": "Simple Wingtip", "Cd": 0.30},
    {"name": "Curved Wingtip", "Cd": 0.22},
]

theta = np.radians(angle)

def simulate_trajectory(Cd):
    vx = v0 * np.cos(theta)
    vy = v0 * np.sin(theta)

    x = 0
    y = 0

    x_positions = []
    y_positions = []

    max_height = 0
    flight_time = 0

    while y >= 0:
        speed = np.sqrt(vx**2 + vy**2)

        drag_force = 0.5 * rho * Cd * area * speed**2

        if speed != 0:
            ax_drag = -(drag_force / mass) * (vx / speed)
            ay_drag = -(drag_force / mass) * (vy / speed)
        else:
            ax_drag = 0
            ay_drag = 0

        ax = ax_drag
        ay = -g + ay_drag

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

    x_positions, y_positions, max_height, flight_time = simulate_trajectory(Cd)
    range_distance = x_positions[-1]

    if name == "Baseline Wing":
        baseline_range = range_distance

    improvement = ((range_distance - baseline_range) / baseline_range) * 100

    results.append({
        "Design": name,
        "Cd": float(Cd),
        "Range_m": float(round(range_distance, 2)),
        "Max_Height_m": float(round(max_height, 2)),
        "Flight_Time_s": float(round(flight_time, 2)),
        "Range_Improvement_%": float(round(improvement, 2))
    })

    plt.plot(x_positions, y_positions, label=f"{name} (Cd={Cd})")


# Save numerical results
with open("wingtip_results.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            "Design",
            "Cd",
            "Range_m",
            "Max_Height_m",
            "Flight_Time_s",
            "Range_Improvement_%"
        ]
    )
    writer.writeheader()
    writer.writerows(results)


# Print results
print("\nWINGTIP-INSPIRED DESIGN COMPARISON")
print("----------------------------------")

for result in results:
    print(result)


# Save graph
plt.title("Wingtip-Inspired Aerodynamic Comparison")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Height (m)")
plt.legend()
plt.grid(True)
plt.savefig("wingtip_design_comparison.png", dpi=300)
plt.show()
