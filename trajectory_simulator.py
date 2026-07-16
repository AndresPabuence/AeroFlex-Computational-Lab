import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81
v0 = 40  # initial speed in m/s

# Angles to compare
angles = [20, 30, 40, 45, 50, 60]

# Time setup
dt = 0.01
t_max = 10
time = np.arange(0, t_max, dt)

plt.figure()

for angle in angles:
    theta = np.radians(angle)

    vx = v0 * np.cos(theta)
    vy = v0 * np.sin(theta)

    x_positions = []
    y_positions = []

    for t in time:
        x = vx * t
        y = vy * t - 0.5 * g * t**2

        if y < 0:
            break

        x_positions.append(x)
        y_positions.append(y)

    plt.plot(x_positions, y_positions, label=f"{angle} degrees")

plt.title("Projectile Trajectory Comparison")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Height (m)")
plt.legend()
plt.grid(True)
plt.show()