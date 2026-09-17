#include "HX711.h"

// AeroFlex V2 sensor validation sketch.
// This is for checking one load cell with one HX711 module only.
// It is not the final aerodynamic testing code.

const int DOUT_PIN = 3;
const int SCK_PIN = 2;

HX711 scale;

void setup() {
  Serial.begin(9600);
  while (!Serial) {
    ; // Wait for Serial on boards that need it.
  }

  Serial.println("AeroFlex V2 single load cell HX711 validation test");
  Serial.println("Raw readings only; no final calibration factor is set.");

  scale.begin(DOUT_PIN, SCK_PIN);

  Serial.println("Remove all load from the sensor.");
  Serial.println("Taring sensor...");
  delay(2000);

  // Simple startup tare/zero procedure for validation.
  // Re-run or reset the board if the zero point drifts during setup.
  scale.tare(20);

  Serial.println("Tare complete.");
  Serial.println("Apply known masses and observe raw reading changes.");
}

void loop() {
  if (scale.is_ready()) {
    long raw_reading = scale.get_value(10);
    Serial.print("Tared raw reading: ");
    Serial.println(raw_reading);
  } else {
    Serial.println("HX711 not ready. Check wiring.");
  }

  delay(500);
}
