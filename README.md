# AeroFlex Computational Lab

This project is a small computational study about how aerodynamic drag affects flight performance. I built it in Python to better understand how changes in drag and lift can affect the trajectory, range, height, and flight time of a simplified aerospace-inspired model.

The project started with a basic projectile motion simulation. Then I added air resistance. After that, I compared simplified wingtip-inspired configurations. Finally, I added a second version that includes both drag coefficient and lift coefficient.

This is not a full CFD simulation or a complete aerodynamic model. It is a simplified 2D model, but it helped me explore the relationship between drag, lift, and flight performance in a measurable way.

## Research Question

How do changes in aerodynamic drag and lift affect the flight performance of a simplified aerospace-inspired model?

## Model

The simulation uses a 2D motion model with gravity, drag, and a simplified lift force.

The drag force is calculated using:

Fd = 0.5 * rho * Cd * A * v^2

Where:

- Fd is the drag force
- rho is air density
- Cd is the drag coefficient
- A is frontal area
- v is velocity magnitude

In the lift-and-drag version, I also added a simplified lift coefficient, Cl. I used the Cl/Cd ratio as a basic way to compare aerodynamic efficiency.

## Files

- trajectory_simulator.py: basic projectile motion without air resistance
- trajectory_with_drag.py: projectile motion with air resistance
- design_comparison.py: comparison of low, medium, and high drag designs
- wingtip_comparison.py: comparison of wingtip-inspired configurations using drag only
- wingtip_results.csv: results from the wingtip drag-only comparison
- wingtip_design_comparison.png: graph from the wingtip drag-only comparison
- wingtip_lift_drag_model.py: comparison using both lift and drag coefficients
- wingtip_lift_drag_results.csv: results from the lift-and-drag model
- wingtip_lift_drag_comparison.png: graph from the lift-and-drag model

## Wingtip Configurations

I compared three simplified configurations.

### Baseline Wing

This is the reference design. It has the highest drag coefficient in the model.

### Simple Wingtip

This design represents a moderate improvement over the baseline. It has lower drag and slightly higher lift.

### Curved Wingtip

This design represents the most efficient configuration in the simplified model. It has the lowest drag coefficient and the highest lift-to-drag ratio.

## Results: Drag-Only Model

In the first wingtip comparison, I tested the three configurations using only drag coefficient, Cd.

| Configuration | Cd | Range (m) | Max Height (m) | Flight Time (s) | Range Improvement |
|---|---:|---:|---:|---:|---:|
| Baseline Wing | 0.40 | 70.35 | 24.10 | 4.39 | 0.00% |
| Simple Wingtip | 0.30 | 80.86 | 26.50 | 4.62 | 14.95% |
| Curved Wingtip | 0.22 | 92.20 | 28.93 | 4.83 | 31.06% |

![Wingtip Design Comparison](wingtip_design_comparison.png)

## Results: Lift and Drag Model

After the drag-only comparison, I added a second model that includes both drag coefficient, Cd, and lift coefficient, Cl.

This version uses the lift-to-drag ratio, Cl/Cd, as a simple way to compare aerodynamic efficiency.

| Configuration | Cd | Cl | Cl/Cd | Range (m) | Max Height (m) | Flight Time (s) | Range Improvement |
|---|---:|---:|---:|---:|---:|---:|---:|
| Baseline Wing | 0.40 | 0.08 | 0.20 | 85.61 | 9.14 | 2.85 | 0.00% |
| Simple Wingtip | 0.30 | 0.11 | 0.37 | 95.74 | 10.04 | 3.07 | 11.83% |
| Curved Wingtip | 0.22 | 0.14 | 0.64 | 107.16 | 11.08 | 3.32 | 25.17% |

![Wingtip Lift and Drag Comparison](wingtip_lift_drag_comparison.png)

## What I Found

The results showed that reducing drag improved the performance of the model.

In the drag-only version, the curved wingtip had the best performance because it had the lowest drag coefficient. It reached the longest range and stayed in the air longer than the other configurations.

In the lift-and-drag version, the curved wingtip also performed best. This happened because it combined lower drag with a higher lift-to-drag ratio.

Overall, the model suggests that improving aerodynamic efficiency can increase range, height, and flight time under the same initial conditions.

## Limitations

This model is simplified. It does not include real wing geometry, turbulence, wingtip vortices, pressure distribution, or full 3D airflow.

The Cd and Cl values are conceptual. They are not measured from a wind tunnel or CFD software. I used them to compare relative performance between different design ideas.

Because of that, this project should be seen as a first computational exploration, not as a final engineering result.

## How to Run

Install the required libraries:

py -m pip install numpy matplotlib

Run the drag-only wingtip comparison:

py wingtip_comparison.py

Run the lift-and-drag model:

py wingtip_lift_drag_model.py

The programs generate CSV result files and PNG graphs.

## Next Steps

The next version could improve the project by testing many combinations of Cd and Cl instead of only three configurations. That would make it possible to run a sensitivity analysis and find the best parameter combination automatically.

A stronger version could also compare the simulation with real data from physical prototypes.

## Conclusion

This project helped me use Python, physics, and data visualization to study a basic aerospace idea.

Even though the model is simplified, it shows how computational tools can be used to compare design assumptions and understand how drag and lift affect flight performance.