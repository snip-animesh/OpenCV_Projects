#include<cvzone.h>
#include <Servo.h>

SerialData rgb(3, 1);
SerialData servo (1, 3);
SerialData serialData;
Servo myservo;

int red = 2;
int green = 3;
int blue = 4;
int servoPin = 5;

int rgbRec[3];
int servoRec[2];
int sendVals[2];
int i;

void setup() {
  rgb.begin();
  servo.begin();
  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(blue, OUTPUT);
  myservo.attach(servoPin);

}
void runRGB() {

  rgb.Get(rgbRec);
  digitalWrite(red, rgbRec[0]);
  delay(500);
  digitalWrite(green, rgbRec[1]);
  delay(500);
  digitalWrite(blue, rgbRec[2]);
  delay(500);
}
void runServo() {
  servo.Get(servoRec);
  myservo.write(0);
  delay(500);
  myservo.write(servoRec[0]);
  delay(500);
}
void loop() {
  // put your main code here, to run repeatedly:
  i = 1;
  sendVals[0] = i;
  serialData.Send(sendVals);
  runRGB();
  i = 0;
  sendVals[0] = i;
  serialData.Send(sendVals);
  runServo();
}
