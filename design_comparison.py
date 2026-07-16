import numpy as np
import matplotlib.pyplot as plt
import csv

# Physical constants
g = 9.81
rho = 1.225  # air density at sea level in kg/m^3

# Launch conditions
mass = 0.20
area = 0.01
v0 = 40
angle = 45
dt = 0.01

# Conceptual aerodynamic designs
designs = [
    {"name": "Low Drag Design", "Cd": 0.15},
    {"name": "Medium Drag Design", "Cd": 0.40},
    {"name": "High Drag Design", "Cd": 0.80},
]

theta = np.radians(angle)

results = []

plt.figure()

for design in designs:
    name = design["name"]
    Cd = design["Cd"]

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

        vx = vx + ax * dt
        vy = vy + ay * dt

        x = x + vx * dt
        y = y + vy * dt

        if y >= 0:
            x_positions.append(x)
            y_positions.append(y)

            if y > max_height:
                max_height = y

            flight_time += dt

    range_distance = x_positions[-1]

    results.append({
    "Design": name,
    "Cd": float(Cd),
    "Range_m": float(round(range_distance, 2)),
    "Max_Height_m": float(round(max_height, 2)),
    "Flight_Time_s": float(round(flight_time, 2))
})

    plt.plot(x_positions, y_positions, label=f"{name} (Cd={Cd})")

# Save results as CSV
with open("aerodynamic_results.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Design", "Cd", "Range_m", "Max_Height_m", "Flight_Time_s"])
    writer.writeheader()
    writer.writerows(results)

# Print results
print("\nAERODYNAMIC DESIGN COMPARISON")
print("--------------------------------")

for result in results:
    print(result)

# Save graph
plt.title("Aerodynamic Design Comparison")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Height (m)")
plt.legend()
plt.grid(True)
plt.savefig("aerodynamic_design_comparison.png", dpi=300)
plt.show()