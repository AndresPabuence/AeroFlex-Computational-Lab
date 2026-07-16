import numpy as np
import matplotlib.pyplot as plt
import csv

# =========================
# Physical constants
# =========================
g = 9.81
rho = 1.225

# =========================
# Launch and object conditions
# =========================
mass = 0.20
area = 0.004
v0 = 40
angle = 20
dt = 0.01

theta = np.radians(angle)

# =========================
# High-resolution parameter search
# 100 x 100 = 10,000 designs
# =========================
cd_values = np.linspace(0.18, 0.45, 100)
cl_values = np.linspace(0.06, 0.18, 100)


def simulate_flight(Cd, Cl):
    vx = v0 * np.cos(theta)
    vy = v0 * np.sin(theta)

    x = 0
    y = 0

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

        ax = ax_drag
        ay = -g + ay_drag + (lift_force / mass)

        vx += ax * dt
        vy += ay * dt

        x += vx * dt
        y += vy * dt

        if y >= 0:
            max_height = max(max_height, y)
            flight_time += dt

    return x, max_height, flight_time


# =========================
# Run sensitivity analysis
# =========================
results = []
range_grid = np.zeros((len(cl_values), len(cd_values)))

for i, Cl in enumerate(cl_values):
    for j, Cd in enumerate(cd_values):
        range_distance, max_height, flight_time = simulate_flight(Cd, Cl)
        efficiency = Cl / Cd

        range_grid[i, j] = range_distance

        results.append({
            "Cd": float(round(Cd, 4)),
            "Cl": float(round(Cl, 4)),
            "Cl_to_Cd": float(round(efficiency, 4)),
            "Range_m": float(round(range_distance, 2)),
            "Max_Height_m": float(round(max_height, 2)),
            "Flight_Time_s": float(round(flight_time, 2))
        })

best_design = max(results, key=lambda row: row["Range_m"])
top_10 = sorted(results, key=lambda row: row["Range_m"], reverse=True)[:10]

print("\nWINGTIP SENSITIVITY ANALYSIS")
print("-----------------------------")
print("Total designs tested:", len(results))

print("\nBest design found:")
print(best_design)

print("\nInterpretation:")
print("The best performance occurs in the region of low drag coefficient (Cd)")
print("and high lift coefficient (Cl). In the graph, that corresponds to the")
print("upper-left region.")

print("\nTop 10 designs by range:")
for design in top_10:
    print(design)

# =========================
# Save CSV
# =========================
with open("wingtip_sensitivity_results.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            "Cd",
            "Cl",
            "Cl_to_Cd",
            "Range_m",
            "Max_Height_m",
            "Flight_Time_s"
        ]
    )
    writer.writeheader()
    writer.writerows(results)

# =========================
# Professional plot
# =========================
Cd_mesh, Cl_mesh = np.meshgrid(cd_values, cl_values)

fig, (ax, info_ax) = plt.subplots(
    1, 2,
    figsize=(11, 6),
    gridspec_kw={"width_ratios": [4.8, 1.7]}
)

# Main contour/heatmap
contour = ax.contourf(Cd_mesh, Cl_mesh, range_grid, levels=40)
contour_lines = ax.contour(Cd_mesh, Cl_mesh, range_grid, levels=8, linewidths=0.7)
ax.clabel(contour_lines, inline=True, fontsize=8, fmt="%.0f")

# Best design marker
ax.scatter(
    best_design["Cd"],
    best_design["Cl"],
    s=320,
    marker="*",
    color="red",
    edgecolors="white",
    linewidths=1.6,
    zorder=10,
    clip_on=False
)

# Main labels and title
ax.set_title("Wingtip Sensitivity Analysis", fontsize=14, pad=12)
ax.set_xlabel("Drag Coefficient (Cd)", fontsize=11)
ax.set_ylabel("Lift Coefficient (Cl)", fontsize=11)

ax.set_xlim(min(cd_values), max(cd_values))
ax.set_ylim(min(cl_values), max(cl_values))

# Light grid only
ax.grid(alpha=0.20)

# Colorbar
cbar = fig.colorbar(contour, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label("Range (m)", fontsize=10)

# =========================
# Side information panel
# =========================
info_ax.axis("off")

info_text = (
    "Best Design\n"
    "-----------------\n"
    f"Cd = {best_design['Cd']}\n"
    f"Cl = {best_design['Cl']}\n"
    f"Cl/Cd = {best_design['Cl_to_Cd']}\n"
    f"Range = {best_design['Range_m']} m\n"
    f"Max Height = {best_design['Max_Height_m']} m\n"
    f"Flight Time = {best_design['Flight_Time_s']} s\n\n"
    "Interpretation\n"
    "-----------------\n"
    "Higher range is achieved\n"
    "when drag is lower and\n"
    "lift is higher.\n\n"
    "This means the most\n"
    "favorable region is the\n"
    "upper-left area of the plot."
)

info_ax.text(
    0.02, 0.98, info_text,
    va="top",
    ha="left",
    fontsize=10,
    bbox=dict(boxstyle="round,pad=0.6", alpha=0.95)
)

plt.tight_layout()
plt.savefig("wingtip_sensitivity_analysis.png", dpi=300, bbox_inches="tight")
plt.show()