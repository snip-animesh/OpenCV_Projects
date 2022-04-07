#include <cvzone.h>

SerialData serialData (1,1); //numOfvalRc,digitsPerValue
int valsRec[1];
int pinNumber=13;
void setup() {
  serialData.begin();
  pinMode(pinNumber,OUTPUT);
}

void loop() {
  serialData.Get(valsRec);
  digitalWrite(pinNumber,valsRec[0]);
}
