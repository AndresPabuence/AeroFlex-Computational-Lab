# Sensor Test Quick Guide

## Connect

- Connect one load cell to one HX711 module.
- Connect HX711 `DT` or `DOUT` to Arduino pin 3.
- Connect HX711 `SCK` to Arduino pin 2.
- Connect HX711 `VCC` and `GND` to the Arduino power and ground.
- Keep the load cell mounted rigidly before testing.

## Serial Monitor

- Upload `arduino/single_load_cell_hx711_test.ino`.
- Open Serial Monitor in the Arduino IDE.
- Set the baud rate to 9600.
- Remove all load before the startup tare finishes.

## Stable Zero

- With no mass applied, the raw reading should stay near a steady baseline.
- Small fluctuations are expected.
- Large drift or jumping values mean the wiring, mounting, or sensor noise must be fixed before testing forces.

## Test Small Masses

- Apply 1 g and confirm the reading changes clearly from zero.
- Remove the mass and confirm the reading returns near zero.
- Repeat with 2 g, 5 g, and 10 g.
- Repeat each mass several times and watch whether the readings are consistent.

## Usable Sensor Result

The sensor is usable for AeroFlex V2 validation only if 1 g, 2 g, and 5 g are clearly distinguishable from zero noise, readings return near zero after unloading, and repeated readings are reasonably consistent.
