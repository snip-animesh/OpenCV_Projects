#include<cvzone.h>

SerialData serialData(5,1); //numOfValRec,digitsPerValue
int valsRec[5];
int led1=5;
int led2=6;
int led3=7;
int led4=8;
int led5=9;

void setup(){
  serialData.begin();
  pinMode(led1,OUTPUT);
  pinMode(led2,OUTPUT);
  pinMode(led3,OUTPUT);
  pinMode(led4,OUTPUT);
  pinMode(led5,OUTPUT);
  }

void loop(){
  serialData.Get(valsRec);

  digitalWrite(led1,valsRec[0]);
  digitalWrite(led2,valsRec[1]);
  digitalWrite(led3,valsRec[2]);
  digitalWrite(led4,valsRec[3]);
  digitalWrite(led5,valsRec[4]);
  }
