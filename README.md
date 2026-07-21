# AeroFlex Computational Lab

AeroFlex Computational Lab is a Python-based aerospace simulation project focused on studying how drag and lift affect the flight performance of a simplified wingtip-inspired model.

The project began as a basic projectile motion simulation and gradually expanded into a computational study involving air resistance, simplified lift modeling, wingtip-inspired design comparisons, high-resolution sensitivity analysis, and preparation for future physical validation.

This is not a full CFD simulation or a final aerodynamic model. It is a simplified 2D computational project designed to explore trends, compare assumptions, and prepare for future experimental testing.

## Research Question

How do changes in drag coefficient and lift coefficient affect the range, height, and flight time of a simplified aerospace-inspired model?

## Project Structure

The project was developed in stages:

1. Basic projectile motion without air resistance.
2. Projectile motion with quadratic drag.
3. Drag-only comparison of wingtip-inspired configurations.
4. Lift-and-drag comparison using simplified Cd and Cl values.
5. Sensitivity analysis testing 10,000 Cd and Cl combinations.
6. Experimental validation planning.
7. Prototype design planning.
8. SVG cutting template generation for future physical prototypes.

Each stage adds one level of complexity while keeping the model understandable and reproducible.

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

In the lift-and-drag version, the model also includes a simplified lift coefficient, Cl.

The lift-to-drag ratio, Cl/Cd, is used as a basic indicator of aerodynamic efficiency.

The simulation updates velocity and position step by step using numerical integration.

## Model Assumptions

The Cd and Cl values used in this project are conceptual. They are used to compare trends, not to represent measured aerodynamic coefficients from a real aircraft wing, CFD software, or wind tunnel testing.

The model does not include:

- real wing geometry
- angle of attack
- lift distribution
- wingtip vortices
- turbulence
- pressure distribution
- structural flexibility
- full 3D airflow
- CFD-level aerodynamic behavior

Because of these assumptions, the results should be interpreted as a computational exploration, not as a final engineering conclusion.

More details are documented in [MODEL_ASSUMPTIONS.md](MODEL_ASSUMPTIONS.md).

## Files

### Core Simulation

- `trajectory_simulator.py` — basic projectile motion without air resistance
- `trajectory_with_drag.py` — projectile motion with air resistance
- `design_comparison.py` — generic comparison of low, medium, and high drag designs

### Wingtip Models

- `wingtip_comparison.py` — drag-only comparison of wingtip-inspired configurations
- `wingtip_lift_drag_model.py` — comparison using both lift and drag coefficients
- `wingtip_sensitivity_analysis.py` — high-resolution sensitivity analysis testing 10,000 Cd and Cl combinations

### Results and Figures

- `aerodynamic_results.csv` — numerical results from the generic drag comparison
- `aerodynamic_design_comparison.png` — graph from the generic drag comparison
- `wingtip_results.csv` — results from the drag-only wingtip comparison
- `wingtip_design_comparison.png` — graph from the drag-only wingtip comparison
- `wingtip_lift_drag_results.csv` — results from the lift-and-drag model
- `wingtip_lift_drag_comparison.png` — graph from the lift-and-drag model
- `wingtip_sensitivity_results.csv` — results from the sensitivity analysis
- `wingtip_sensitivity_analysis.png` — graph from the sensitivity analysis

### Experimental Preparation

- `EXPERIMENT_PLAN.md` — plan for future physical validation
- `PROTOTYPE_DESIGNS.md` — proposed prototype designs for physical testing
- `BUILD_PLAN.md` — first physical build plan for the prototypes
- `MODEL_ASSUMPTIONS.md` — explanation of the main modeling assumptions
- `experimental_data_template.csv` — template for recording physical test data
- `experimental_results_analysis.py` — script prepared to analyze future experimental results
- `generate_prototype_templates.py` — generates SVG cutting templates for the physical prototypes
- `prototype_cutting_templates.svg` — cutting template for Baseline Wing, Simple Wingtip, and Curved Wingtip

## Wingtip Configurations

The fixed wingtip comparison uses three simplified conceptual configurations.

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

The sensitivity analysis showed that the best performance occurred where drag was low and lift was high. In the plot, this corresponds to the upper-left region.

This result matches the expected trend: lower drag and better lift-to-drag efficiency improve range in the simplified model.

## Experimental Validation Plan

The computational results are not treated as final proof. The next step is to compare the simulation trend with a physical test.

The future physical validation will compare three prototypes:

- Baseline Wing
- Simple Wingtip
- Curved Wingtip

The experiment would measure:

- flight distance
- flight time
- stability
- visible flight behavior

The purpose is not to prove that the simplified model is perfectly accurate. The goal is to check whether the same general trend appears in both the simulation and the physical tests.

The experimental validation plan is documented in [EXPERIMENT_PLAN.md](EXPERIMENT_PLAN.md).

The prototype design plan is documented in [PROTOTYPE_DESIGNS.md](PROTOTYPE_DESIGNS.md).

The first physical build plan is documented in [BUILD_PLAN.md](BUILD_PLAN.md).

The experimental data template is included in [experimental_data_template.csv](experimental_data_template.csv).

## Prototype Cutting Templates

The file `generate_prototype_templates.py` generates an SVG cutting template for the three planned physical prototypes.

The generated file is:

- `prototype_cutting_templates.svg`

The template includes:

- Baseline Wing
- Simple Wingtip
- Curved Wingtip

The purpose of the template is to make the future physical build more consistent. Instead of improvising the prototype shapes by hand, the same base dimensions can be used for each design.

The current planned dimensions are:

- wingspan: 30 cm
- wing chord: 8 cm
- wingtip section: 3 cm per side

These dimensions can be adjusted later, but the important point is that all three prototypes should remain as similar as possible except for the wingtip shape.

## Experimental Results Analysis

The file `experimental_results_analysis.py` is prepared for future experimental data.

Once real test data is added to `experimental_data_template.csv`, the script will calculate:

- average distance by prototype
- average flight time by prototype
- average stability rating by prototype
- number of trials
- a comparison graph of the physical results

At the current stage, this script is included as preparation for future testing.

## What I Found

The results showed a consistent trend across the project.

Lower drag improved flight performance. When lift was added, configurations with a better lift-to-drag ratio performed better. In the sensitivity analysis, the best performance appeared where Cd was lowest and Cl was highest within the tested range.

This suggests that aerodynamic efficiency has a strong effect on range, height, and flight time in the simplified model.

## Limitations

This project is simplified and does not represent a complete aerodynamic simulation.

The main limitations are:

- the model is two-dimensional
- Cd and Cl values are conceptual
- lift is simplified as an upward force
- real wing geometry is not modeled
- wingtip vortices are not modeled
- turbulence and pressure distribution are not modeled
- there is no CFD analysis
- there is no wind tunnel validation yet
- there is no physical testing yet

Because of these limitations, the project should be understood as a first computational study, not as a final aerodynamic result.

## How to Run

Install the required libraries:

py -m pip install numpy matplotlib

Run the drag-only wingtip comparison:

py wingtip_comparison.py

Run the lift-and-drag model:

py wingtip_lift_drag_model.py

Run the sensitivity analysis:

py wingtip_sensitivity_analysis.py

Generate the prototype cutting templates:

py generate_prototype_templates.py

Run the experimental results analysis after adding real test data:

py experimental_results_analysis.py

The scripts generate CSV files, PNG graphs, and an SVG prototype template.

## Current Status

Completed:

- projectile simulation
- drag model
- lift-and-drag model
- wingtip-inspired comparison
- 10,000-combination sensitivity analysis
- model assumptions documentation
- experimental validation plan
- prototype design plan
- physical build plan
- experimental data template
- experimental analysis script
- SVG cutting template generator
- prototype cutting template

Not completed yet:

- physical prototype construction
- real flight testing
- experimental data collection
- comparison between simulation and physical results

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

The project began with basic projectile motion and developed into a larger analysis of drag, lift, aerodynamic efficiency, and prototype preparation. The sensitivity analysis tested 10,000 parameter combinations and showed that the best performance occurred with low drag and high lift.

Although the model is simplified, it provides a clear foundation for future experimental validation and more advanced aerospace analysis.