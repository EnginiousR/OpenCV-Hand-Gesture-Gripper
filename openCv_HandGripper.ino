//openCV handGesture robotic arm

#include <Servo.h>

Servo gripper;
bool isClosed = false;

void setup() {
  Serial.begin(9600);
  gripper.attach(9);
  gripper.write(0); // start open
}

void loop() {
  if (Serial.available()) {
    char command = Serial.read();
    if (command == 'G') {
      gripper.write(90); // grab
      isClosed = true;
    } else if (command == 'O') {
      gripper.write(0); // open
      isClosed = false;
    }
  }
}
