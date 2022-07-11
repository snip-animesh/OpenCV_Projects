#include<cvzone.h>

SerialData serialData(1,3); //numOfValRec,digitsPerValue

int valRec[1];
int pwmPin=6;

void setup() {
  serialData.begin();
  pinMode(pwmPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  serialData.Get(valRec);
  analogWrite(pwmPin, valRec[0]);
}
