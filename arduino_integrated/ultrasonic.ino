#include "variables.h"

String ReadUltrasonic()
{
  long duration, cm;
  
  String stateID = "";    // variable that holds the current state of trash
  String tableInput = ""; // variable that holds the final input string for the table
  
  int state1 = 0;         //state 1 - 5 are the counters for the quantized states
  int state2 = 0;
  int state3 = 0;
  int state4 = 0;
  int state5 = 0;
  
  int sum1 = 0;          //sum 1 - 5 contains the sum of the distances for each region for averaging
  int sum2 = 0;
  int sum3 = 0;
  int sum4 = 0;
  int sum5 = 0;
  
  int cmLevel;           //variable that holds the average of the distances per pulse cycle
  
  for (int i=0; i<5; i++){
    // The sensor is triggered by a HIGH pulse of 10 or more microseconds.
    // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
    digitalWrite(TRIGPIN, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIGPIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIGPIN, LOW);
   
    // Read the signal from the sensor: a HIGH pulse whose
    // duration is the time (in microseconds) from the sending
    // of the ping to the reception of its echo off of an object.
    duration = pulseIn(ECHOPIN, HIGH);
   
    // Convert the time into a distance
    cm = (duration/2) / 29.1;     // Divide by 29.1 or multiply by 0.0343
    
    // Quantize distances to garbage can states and count number of readings for each state
    if (cm >= 64.25){
      //Serial.print("Empty ");
      state1 = state1+1;
      sum1=sum1+cm;
    }
    
    if (cm < 64.25 && cm >= 53.25){
      //Serial.print("Quarter Full ");
      state2 = state2+1;
      sum2=sum2+cm;
    }
    
    if (cm < 53.25 && cm >= 42.25){
      //Serial.print("Half Full ");
      state3 = state3+1;
      sum3=sum3+cm;
    }
  
    if (cm < 42.25 && cm >= 31.25){
      //Serial.print("Three Quarters Full ");
      state4 = state4+1;
      sum4=sum4+cm;
    }
      
    if (cm < 31.25){
      //Serial.print("Full ");
      state5 = state5+1;
      sum5=sum5+cm;
    }
  
    //Serial.print(cm);
    //Serial.print("cm");
    //Serial.println();
    
    delay(200); //delay between successive pulses
  } //end for loop

  // Define stateID based on majority of pulses (3 out of 5 pulses)
  if (state1>=3){
    //Serial.print("Empty");
    cmLevel=sum1/state1;
  }
  
  if (state2>=3){
    //Serial.print("Quarter Full");
    cmLevel=sum2/state2;
  }
  
  if (state3>=3){
    //Serial.print("Half Full");
    cmLevel=sum3/state3;
  }
  
  if (state4>=3){
    //Serial.print("Three Quarters Full");
    cmLevel=sum4/state4;
  }
  
  if (state5>=3){
    //Serial.print("Full");
    cmLevel=sum5/state5;
  }
  
  tableInput=String(MCUID) + " " + String(cmLevel); // construct final string based on mcuID and stateID
  Serial.print(tableInput);
  Serial.println();

  return(tableInput);
}
