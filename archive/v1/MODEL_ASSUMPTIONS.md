# Model Assumptions

This document explains the main assumptions used in AeroFlex Computational Lab.

The goal of this project is not to build a full aerodynamic simulation. Instead, the goal is to create a simplified computational model that can compare general flight performance trends between wingtip-inspired configurations.

## Simplified 2D Model

The simulation uses a two-dimensional motion model.

The model tracks:

- horizontal position
- vertical position
- horizontal velocity
- vertical velocity

It does not include full three-dimensional airflow or real wing geometry.

## Drag Coefficient Assumption

The drag coefficient, Cd, is used as a simplified representation of aerodynamic resistance.

In the fixed wingtip comparison, the configurations were assigned different Cd values:

- Baseline Wing: higher drag
- Simple Wingtip: medium drag
- Curved Wingtip: lower drag

These values are conceptual. They were not measured from a wind tunnel or CFD simulation.

The purpose of using them is to compare how lower drag affects flight performance under the same initial conditions.

## Lift Coefficient Assumption

The lift coefficient, Cl, is used as a simplified representation of upward aerodynamic force.

In the lift-and-drag model, the configurations were assigned different Cl values:

- Baseline Wing: lower lift
- Simple Wingtip: moderate lift
- Curved Wingtip: higher lift

These values are also conceptual.

The goal is not to claim that these exact values represent real aircraft wings. The goal is to study how changes in lift and drag affect range, height, and flight time in a simplified model.

## Lift Direction Simplification

In this model, lift is treated as an upward force.

This is a simplification. In real aerodynamics, lift depends on airflow direction, angle of attack, wing shape, and other factors.

This simplified lift model was used to keep the simulation understandable and manageable at this stage.

## Sensitivity Analysis Assumption

The sensitivity analysis tested 10,000 combinations of Cd and Cl.

The tested range was:

- Cd from 0.18 to 0.45
- Cl from 0.06 to 0.18

The purpose was to explore performance trends across a wider design space, not to claim that every tested combination represents a real physical wing.

## What the Model Can Show

The model can show general trends such as:

- lower drag tends to increase range
- higher lift can increase flight time and height
- better Cl/Cd values can improve simplified flight performance
- different assumptions can be compared under the same launch conditions

## What the Model Cannot Show

The model cannot fully represent:

- real wing geometry
- angle of attack
- wingtip vortices
- turbulence
- pressure distribution
- three-dimensional airflow
- structural flexibility
- CFD-level aerodynamic behavior
- wind tunnel results

## Why This Model Is Still Useful

Even though the model is simplified, it is useful because it creates a clear computational framework.

It allows the project to move through several stages:

1. Build a basic flight model.
2. Add drag.
3. Add simplified lift.
4. Compare wingtip-inspired configurations.
5. Run sensitivity analysis.
6. Prepare for physical validation.

The model is not the final answer. It is the first computational step before experimental testing.