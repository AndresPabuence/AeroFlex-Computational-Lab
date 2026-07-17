# Prototype Designs

This document defines the three physical prototypes planned for the experimental validation phase of AeroFlex Computational Lab.

The goal is to build three simplified glider-style wing prototypes that are as similar as possible, changing mainly the wingtip shape.

## General Design Rules

To make the comparison fair, all prototypes should use:

- same material
- same wingspan
- same wing chord
- same approximate mass
- same launch method
- same testing environment
- same number of trials

The only major difference should be the wingtip configuration.

## Suggested Materials

Possible materials:

- foam board
- light cardboard
- balsa wood
- 3D printed thin parts

The first version should be simple and light. Foam board or light cardboard is recommended for fast testing.

## Shared Dimensions

Suggested starting dimensions:

- wingspan: 30 cm
- wing chord: 8 cm
- fuselage length: 25 cm
- wing thickness: as thin as possible while staying rigid
- target mass: similar across all prototypes

These dimensions can be adjusted later, but all three prototypes should remain consistent.

## Prototype 1: Baseline Wing

The Baseline Wing is the control design.

It uses a straight wing with no wingtip modification.

Purpose:

- provide a reference point
- compare against wingtip-inspired designs
- measure baseline distance, time, and stability

Expected behavior:

- moderate range
- possible lower stability
- no wingtip drag-reduction feature

## Prototype 2: Simple Wingtip

The Simple Wingtip uses the same basic wing shape as the baseline, but adds a small upward wingtip at both ends.

Suggested wingtip angle:

- 30 to 45 degrees upward

Purpose:

- test whether a simple wingtip improves stability or distance
- compare against the baseline wing

Expected behavior:

- slightly improved stability
- slightly longer range than baseline if the design works well

## Prototype 3: Curved Wingtip

The Curved Wingtip uses a smoother upward curve at both wing ends.

Purpose:

- test whether a more refined wingtip-inspired shape improves performance
- compare against both baseline and simple wingtip designs

Expected behavior:

- best stability
- best range
- smoother flight path

## Experimental Notes

The prototypes should be tested gently and safely, preferably indoors or in a calm environment.

Each prototype should be launched from the same height and with the same method.

Suggested test setup:

- launch height: 1.2 m
- launch angle: as consistent as possible
- trials per prototype: 10
- measure distance from launch point to landing point
- record approximate flight time
- rate stability from 1 to 5

## Fair Test Conditions

To keep the experiment consistent:

- do not test during strong wind
- use the same launcher or hand motion
- test on the same surface
- keep the mass similar
- avoid changing more than one design variable at a time

## Next Step

After building the prototypes, the data should be recorded in:

experimental_data_template.csv

Then the results can be analyzed in Python and compared with the simulation trend.