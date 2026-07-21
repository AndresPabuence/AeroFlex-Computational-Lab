# AeroFlex Computational Lab

AeroFlex Computational Lab is a Python-based computational aerospace project focused on studying how drag and lift affect the flight performance of a simplified wingtip-inspired model.

The project began with a basic projectile motion simulation and gradually developed into a larger study with air resistance, simplified lift modeling, wingtip-inspired comparisons, and a high-resolution sensitivity analysis testing 10,000 combinations of drag coefficient (Cd) and lift coefficient (Cl).

This is not a full CFD simulation or a final aerodynamic model. It is a simplified 2D computational study designed to explore trends, compare assumptions, and create a foundation for future physical validation.

## Research Question

How do changes in drag coefficient and lift coefficient affect the range, height, and flight time of a simplified aerospace-inspired model?

## Project Overview

The project was developed in several stages:

1. Basic projectile motion without air resistance.
2. Projectile motion with quadratic drag.
3. Comparison of simplified wingtip-inspired configurations using drag coefficient only.
4. Extension of the model to include both drag and lift coefficients.
5. High-resolution sensitivity analysis across 10,000 Cd and Cl combinations.
6. Preparation for future experimental validation using physical prototypes.

Each stage adds a new layer to the analysis. The goal is not to create a perfect aerodynamic model, but to build a clear computational workflow that can later be improved with real experimental data.

## Physics Model

The model uses a simplified 2D motion simulation with gravity, drag, and lift.

The drag force is calculated as:

Fd = 0.5 * rho * Cd * A * v^2

Where:

- Fd is drag force
- rho is air density
- Cd is drag coefficient
- A is frontal area
- v is velocity magnitude

In the lift-and-drag version, the model also includes a simplified lift coefficient, Cl. The lift-to-drag ratio, Cl/Cd, is used as a basic indicator of aerodynamic efficiency.

The simulation updates velocity and position step by step using numerical integration.

## Files

### Core simulation files

- trajectory_simulator.py: basic projectile motion without air resistance
- trajectory_with_drag.py: projectile motion with air resistance
- design_comparison.py: comparison of generic low, medium, and high drag designs

### Wingtip analysis files

- wingtip_comparison.py: drag-only comparison of wingtip-inspired configurations
- wingtip_lift_drag_model.py: comparison using both lift and drag coefficients
- wingtip_sensitivity_analysis.py: high-resolution sensitivity analysis testing 10,000 Cd and Cl combinations

### Result files

- aerodynamic_results.csv: numerical results from the generic drag comparison
- aerodynamic_design_comparison.png: graph from the generic drag comparison
- wingtip_results.csv: results from the drag-only wingtip comparison
- wingtip_design_comparison.png: graph from the drag-only wingtip comparison
- wingtip_lift_drag_results.csv: results from the lift-and-drag model
- wingtip_lift_drag_comparison.png: graph from the lift-and-drag model
- wingtip_sensitivity_results.csv: results from the sensitivity analysis
- wingtip_sensitivity_analysis.png: graph from the sensitivity analysis

### Experimental preparation files

- EXPERIMENT_PLAN.md: plan for future physical validation
- PROTOTYPE_DESIGNS.md: proposed prototype designs for physical testing
- experimental_data_template.csv: template for recording physical test data
- experimental_results_analysis.py: script prepared to analyze future experimental results

## Wingtip Configurations

The project compares three simplified wingtip-inspired configurations.

### Baseline Wing

The Baseline Wing is the reference design. It has the highest drag coefficient among the fixed wingtip configurations.

### Simple Wingtip

The Simple Wingtip represents a moderate improvement over the baseline design. It has lower drag and slightly higher lift in the simplified model.

### Curved Wingtip

The Curved Wingtip represents the most efficient of the three fixed configurations. It has the lowest drag coefficient and the highest lift-to-drag ratio in the simplified comparison.

## Results: Drag-Only Wingtip Model

The first wingtip comparison used only drag coefficient, Cd.

| Configuration | Cd | Range (m) | Max Height (m) | Flight Time (s) | Range Improvement |
|---|---:|---:|---:|---:|---:|
| Baseline Wing | 0.40 | 70.35 | 24.10 | 4.39 | 0.00% |
| Simple Wingtip | 0.30 | 80.86 | 26.50 | 4.62 | 14.95% |
| Curved Wingtip | 0.22 | 92.20 | 28.93 | 4.83 | 31.06% |

![Wingtip Design Comparison](wingtip_design_comparison.png)

In this model, reducing drag increased range, maximum height, and flight time.

## Results: Lift and Drag Model

The second model added lift coefficient, Cl, in addition to drag coefficient, Cd.

| Configuration | Cd | Cl | Cl/Cd | Range (m) | Max Height (m) | Flight Time (s) | Range Improvement |
|---|---:|---:|---:|---:|---:|---:|---:|
| Baseline Wing | 0.40 | 0.08 | 0.20 | 85.61 | 9.14 | 2.85 | 0.00% |
| Simple Wingtip | 0.30 | 0.11 | 0.37 | 95.74 | 10.04 | 3.07 | 11.83% |
| Curved Wingtip | 0.22 | 0.14 | 0.64 | 107.16 | 11.08 | 3.32 | 25.17% |

![Wingtip Lift and Drag Comparison](wingtip_lift_drag_comparison.png)

The Curved Wingtip also performed best in this version because it combined lower drag with a higher lift-to-drag ratio.

## Sensitivity Analysis

After comparing only three fixed configurations, the project was expanded with a high-resolution sensitivity analysis.

This version tested 10,000 combinations of drag coefficient and lift coefficient. The goal was to identify which Cd and Cl combination produced the greatest range under the same initial conditions.

The best result found was:

| Cd | Cl | Cl/Cd | Range (m) | Max Height (m) | Flight Time (s) |
|---:|---:|---:|---:|---:|---:|
| 0.18 | 0.18 | 1.00 | 119.73 | 12.35 | 3.65 |

![Wingtip Sensitivity Analysis](wingtip_sensitivity_analysis.png)

The sensitivity analysis showed that the best performance occurred in the upper-left region of the plot, where drag is low and lift is high. This matches the expected trend: lower drag and higher lift-to-drag efficiency improve range in the simplified model.

## Experimental Validation Plan

The computational results are not being treated as final proof. The next step is to compare the simulation trend with a physical test.

The experimental validation plan is documented in [EXPERIMENT_PLAN.md](EXPERIMENT_PLAN.md).

The prototype design plan is documented in [PROTOTYPE_DESIGNS.md](PROTOTYPE_DESIGNS.md).

The experimental data template is included in [experimental_data_template.csv](experimental_data_template.csv).

The planned physical test will compare:

- Baseline Wing
- Simple Wingtip
- Curved Wingtip

The experiment would measure:

- flight distance
- flight time
- stability
- visible flight behavior

The goal is to check whether the physical prototypes follow the same general trend as the simulation, not to prove that the simplified model is perfectly accurate.

## Experimental Results Analysis

The file experimental_results_analysis.py is prepared for future experimental data.

Once real test data is added to experimental_data_template.csv, the script will calculate:

- average distance by prototype
- average flight time by prototype
- average stability rating by prototype
- number of trials
- a comparison graph of the physical results

At the current stage, the script is included as preparation for future testing.

## What I Found

The results showed a consistent trend across the project.

Lower drag improved flight performance. When lift was added, configurations with a better lift-to-drag ratio performed better. In the sensitivity analysis, the best performance appeared where Cd was lowest and Cl was highest within the tested range.

This suggests that aerodynamic efficiency has a strong effect on range, height, and flight time in the simplified model.

## Limitations

This project is simplified and does not represent a complete aerodynamic simulation.

The model does not include:

- real wing geometry
- lift distribution
- wingtip vortices
- turbulence
- pressure distribution
- full 3D airflow
- CFD analysis
- wind tunnel validation

The Cd and Cl values are conceptual. They are used to compare trends, not to represent measured aerodynamic coefficients from a physical wing or CFD software.

Because of this, the results should be interpreted as a computational exploration, not as a final engineering conclusion.

## How to Run

Install the required libraries:

py -m pip install numpy matplotlib

Run the drag-only wingtip comparison:

py wingtip_comparison.py

Run the lift-and-drag model:

py wingtip_lift_drag_model.py

Run the sensitivity analysis:

py wingtip_sensitivity_analysis.py

Run the experimental results analysis after adding real test data:

py experimental_results_analysis.py

The simulation scripts generate CSV files and PNG graphs with the results.

## Current Status

The computational part of the project is complete for this stage.

Completed:

- projectile simulation
- drag model
- lift-and-drag model
- wingtip-inspired comparison
- 10,000-combination sensitivity analysis
- experimental validation plan
- prototype design plan
- experimental data template
- experimental analysis script

Not completed yet:

- physical prototype construction
- real flight testing
- experimental data collection
- comparison between simulation and real results

## Next Steps

The next major step is physical validation.

A stronger future version of this project could include:

- building three physical prototypes
- testing a baseline wing, simple wingtip, and curved wingtip
- measuring distance, flight time, and stability
- comparing experimental results with the simulation trend
- refining Cd and Cl assumptions using real data

This would turn the project from a computational model into a simulation-and-validation study.

## Conclusion

AeroFlex Computational Lab shows how Python, physics, and data visualization can be used to explore aerospace design ideas.

The project began with basic projectile motion and developed into a larger analysis of drag, lift, and aerodynamic efficiency. The sensitivity analysis tested 10,000 parameter combinations and showed that the best performance occurred with low drag and high lift.

Although the model is simplified, it provides a clear foundation for future experimental validation and more advanced aerospace analysis.