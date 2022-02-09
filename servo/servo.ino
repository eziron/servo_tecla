#include <Servo.h>

Servo sv;

char C = ' ';
void setup() {
  Serial.begin(9600);
  sv.attach(9);
  pinMode(13, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    C = Serial.read();
    if (C == 'A') {
      sv.write(0);
      digitalWrite(13, 0);
    }
    if (C == 'B') {
      sv.write(90);
      digitalWrite(13, 1);
    }
  }
}
