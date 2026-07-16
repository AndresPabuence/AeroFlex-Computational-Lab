import numpy as np
import matplotlib.pyplot as plt

# Physical constants
g = 9.81
rho = 1.225  # air density at sea level in kg/m^3

# Object properties
mass = 0.20       # kg
area = 0.01       # frontal area in m^2
v0 = 40           # initial speed in m/s
angle = 45        # launch angle in degrees

# Drag coefficients to compare
drag_coefficients = [0.0, 0.2, 0.5, 0.8]

# Time step
dt = 0.01

plt.figure()

for Cd in drag_coefficients:
    theta = np.radians(angle)

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

        # Drag force magnitude
        drag_force = 0.5 * rho * Cd * area * speed**2

        # Drag acceleration components
        if speed != 0:
            ax_drag = -(drag_force / mass) * (vx / speed)
            ay_drag = -(drag_force / mass) * (vy / speed)
        else:
            ax_drag = 0
            ay_drag = 0

        # Total acceleration
        ax = ax_drag
        ay = -g + ay_drag

        # Update velocity
        vx = vx + ax * dt
        vy = vy + ay * dt

        # Update position
        x = x + vx * dt
        y = y + vy * dt

        if y >= 0:
            x_positions.append(x)
            y_positions.append(y)

            if y > max_height:
                max_height = y

            flight_time += dt

    range_distance = x_positions[-1]

    print(f"Cd = {Cd}")
    print(f"Range: {range_distance:.2f} m")
    print(f"Max height: {max_height:.2f} m")
    print(f"Flight time: {flight_time:.2f} s")
    print("----------------------")

    plt.plot(x_positions, y_positions, label=f"Cd = {Cd}")

plt.title("Projectile Trajectory With Air Resistance")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Height (m)")
plt.legend()
plt.grid(True)
plt.show()