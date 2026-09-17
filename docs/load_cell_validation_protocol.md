# Load Cell Validation Protocol

## Objective

Determine whether low-range load cells can resolve forces between approximately 0.5 and 10 gram-force before any AeroFlex V2 aerodynamic wingtip testing is performed.

No wingtip comparison should be performed until the load cells pass this validation protocol.

## Required Equipment

- 2 load cells, ideally 100 g, maximum 200 g
- 2 HX711 modules
- Arduino Uno or Nano
- Jumper wires
- Calibration masses: 0 g, 1 g, 2 g, 5 g, 10 g, 20 g, 50 g
- Rigid mounting materials

## Step 1: Test One Load Cell Only

Assemble and test one load cell with one HX711 module before connecting the second sensor. Mount the load cell rigidly so that calibration masses can be applied repeatably in the intended force direction.

## Step 2: Zero the Sensor

With no applied mass, zero the sensor output. Record the zero reading and observe whether it remains stable before calibration begins.

## Step 3: Calibrate With Known Masses

Apply known calibration masses in sequence, including 0 g, 1 g, 2 g, 5 g, 10 g, 20 g, and 50 g. Record the sensor readings for each mass and confirm that the response is monotonic and approximately proportional to applied load.

## Step 4: Check Noise at 0 g

Remove all applied mass and record the unloaded reading over time. Estimate the noise level and zero drift at 0 g.

## Step 5: Check Low-Force Detectability

Apply 1 g, 2 g, and 5 g masses separately. Confirm whether each load is clearly distinguishable from the 0 g noise and drift.

## Step 6: Repeat With the Second Load Cell

Repeat the same zeroing, calibration, noise, drift, and low-force detectability checks with the second load cell and HX711 module.

## Step 7: Fan-On/Fan-Off Force Detection Test

Only after both sensors pass the static load validation, attempt a fan-on/fan-off force detection test using a non-wing test object or mounting setup. This step is for detecting whether the measurement system can resolve small force changes under airflow, not for comparing wingtip geometries.

## Acceptance Criteria

- Sensor detects 1 g clearly.
- Zero drift is small compared with expected drag force.
- Readings return near zero after unloading.
- Repeated readings are reasonably consistent.

## Failure Criteria

- Zero drift is comparable to 1-3 gf.
- 5 g readings fluctuate heavily.
- Sensor cannot distinguish 1 g from noise.

## Testing Restriction

No aerodynamic wingtip comparison should be performed until both load cells pass this validation protocol.
