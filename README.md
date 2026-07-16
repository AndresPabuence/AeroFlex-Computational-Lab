# AeroFlex Computational Lab

## Overview

AeroFlex Computational Lab is a Python-based simulation project that analyzes how aerodynamic drag affects flight performance.

The project compares three conceptual aerodynamic designs by changing the drag coefficient (Cd):

- Low Drag Design
- Medium Drag Design
- High Drag Design

The simulation measures:

- horizontal range
- maximum height
- flight time
- trajectory shape

## Physics Model

The model uses 2D projectile motion with gravity and quadratic air resistance.

Drag force:

Fd = 0.5 * rho * Cd * A * v^2

Where:

- rho = air density
- Cd = drag coefficient
- A = frontal area
- v = velocity magnitude

## Files

- trajectory_simulator.py: basic projectile motion without air resistance
- trajectory_with_drag.py: projectile motion with air resistance
- design_comparison.py: comparison of three aerodynamic designs
- aerodynamic_results.csv: numerical output from the simulation
- aerodynamic_design_comparison.png: generated comparison graph

## Results

The low-drag design achieved the greatest range and longest flight time.

| Design | Cd | Range (m) | Max Height (m) | Flight Time (s) |
|---|---:|---:|---:|---:|
| Low Drag Design | 0.15 | 105.89 | 31.61 | 5.06 |
| Medium Drag Design | 0.40 | 70.35 | 24.10 | 4.39 |
| High Drag Design | 0.80 | 47.58 | 18.15 | 3.79 |

## Conclusion

The simulation shows that increasing the drag coefficient reduces range, maximum height, and flight time.

This supports the expected aerodynamic principle: lower-drag shapes conserve more velocity and travel farther under the same launch conditions.

## Next Step

The next version will replace generic drag designs with wingtip-inspired configurations:

- Baseline Wing
- Simple Wingtip
- Curved Wingtip

This will make the project more directly connected to aerospace design.