#include <cvzone.h>

SerialData serialData;

int sendVals[2]; // min val of 2 even when sending 1

void setup() {
serialData.begin();
}

void loop() {
  int potVal = analogRead(A1);
  sendVals[0] = potVal;
  serialData.Send(sendVals);
}
