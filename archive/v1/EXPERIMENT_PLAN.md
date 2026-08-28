# Experimental Validation Plan

The next step of AeroFlex Computational Lab is to compare the computational results with a simple physical experiment.

The simulation suggests that configurations with lower drag and better lift-to-drag behavior should travel farther. To test this idea, I will build and compare three simplified physical prototypes:

- Baseline Wing
- Simple Wingtip
- Curved Wingtip

## Goal

The goal is to check whether the same pattern from the simulation appears in a real test.

The main question is:

Does the curved wingtip-inspired prototype travel farther or behave more efficiently than the baseline wing?

## Prototype Designs

### 1. Baseline Wing

A simple wing shape without any wingtip modification.

### 2. Simple Wingtip

A similar wing shape with a small upward wingtip.

### 3. Curved Wingtip

A similar wing shape with a more curved wingtip-inspired ending.

The prototypes should be as similar as possible in size, mass, and material. The main difference should be the wingtip shape.

## Variables

### Independent Variable

Wingtip configuration:

- Baseline Wing
- Simple Wingtip
- Curved Wingtip

### Dependent Variables

Measured results:

- flight distance
- flight time
- stability
- qualitative flight behavior

### Controlled Variables

To make the test fair, these should stay the same:

- material
- wing size
- launch height
- launch angle
- launch location
- launch method
- number of trials
- testing surface
- wind conditions

## Testing Method

Each prototype will be tested several times under the same conditions.

Suggested structure:

- 10 trials for Baseline Wing
- 10 trials for Simple Wingtip
- 10 trials for Curved Wingtip

For each trial, I will record:

- distance traveled
- approximate flight time
- whether the flight was stable
- any visible behavior such as diving, rolling, or turning

## Data Table

| Trial | Configuration | Distance (m) | Flight Time (s) | Stability Rating (1-5) | Notes |
|---:|---|---:|---:|---:|---|
| 1 | Baseline Wing |  |  |  |  |
| 1 | Simple Wingtip |  |  |  |  |
| 1 | Curved Wingtip |  |  |  |  |

## Expected Result

Based on the simulation, I expect the curved wingtip-inspired design to produce the best performance.

The expected pattern is:

- Baseline Wing: shortest range
- Simple Wingtip: moderate improvement
- Curved Wingtip: strongest performance

## How I Will Compare Simulation and Experiment

After collecting the data, I will compare the average distance of each prototype with the trend predicted by the simulation.

The goal is not to prove that the simulation is perfectly accurate. The goal is to see whether the same general trend appears in both the computational model and the physical test.

## Limitations

This experiment will still be simplified.

Possible limitations include:

- small construction differences between prototypes
- inconsistent launch force
- indoor or outdoor air movement
- measurement error
- simplified wing shapes
- lack of professional wind tunnel equipment

Because of these limitations, the experiment will be used as a first validation step, not as a final aerodynamic conclusion.

## Next Step

After testing, I will create a new CSV file with the experimental results and compare the average performance of each prototype using Python.