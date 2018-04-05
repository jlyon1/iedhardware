void setup() {
  Serial.begin(115200);
  Serial.println("Pressure Sensor Testing:");

}

void loop() {
  int value = analogRead(A0);
  Serial.println(value);

  delay(10);

}
