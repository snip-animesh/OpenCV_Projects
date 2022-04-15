#include <cvzone.h>

SerialData serialData (2, 1); //numOfvalRec,digitsPerValue
int valsRec[2];
int pinFace = 11;
int pinNotFace = 8;
//println(valsRec);
void setup() {
  serialData.begin();
  pinMode(pinFace, OUTPUT);
  pinMode(pinNotFace, OUTPUT);
}

void loop() {
  serialData.Get(valsRec);

  digitalWrite(pinFace, valsRec[0]);
  digitalWrite(pinNotFace, valsRec[1]);
}
