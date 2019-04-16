#include "wifi.h"
#include "ultrasonic.h"
#include "variables.h"

#include <avr/sleep.h>

WiFiConnector connector;
volatile int interrupt_counter;

ISR(RTC_CNT_vect)
{ 
  RTC.INTFLAGS = RTC_OVF_bm;
  interrupt_counter++;
  
  #ifdef SERIAL_DEBUG
  Serial.print(interrupt_counter);
  Serial.println(" Interrupt! ");  
  #endif
}

void sleep()
{
  // Enable sleep and enter sleep until interrupt
  sleep_enable();
  sleep_mode();
  sleep_disable();
}

void setup()
{
  pinMode(TRIGPIN, OUTPUT);
  pinMode(ECHOPIN, INPUT);

  pinMode(LED_BUILTIN, OUTPUT);

  #ifdef SERIAL_DEBUG
  Serial.begin(9600);
  #endif

  // Turn onboard LED on until it has been connected to WiFi
  digitalWrite(LED_BUILTIN, HIGH);
  connector.ConnectToWiFi();
  digitalWrite(LED_BUILTIN, LOW);
  
  // Use 20MHz internal clock
  CLKCTRL.MCLKCTRLA = 0x00;

  // Standby Sleep mode when sleep is enabled
  set_sleep_mode(SLEEP_MODE_STANDBY);
  

  // Enable Real Time Counter (2 seconds)
  // Enable RTC to work in Sleep mode
  RTC.CTRLA  = 0xB1;
  // Use 32.768 kHz clock for RTC
  RTC.CLKSEL = 0x00;
  
  // Real Time Counter period
  RTC.PER = 512*SEC;
  // Enable Overflow Interrupt
  RTC.INTCTRL = 0x01;

  // Initialize interrupt counter
  interrupt_counter = 0; 
}



void loop() 
{ 
  // If the number of interrupts since last POST is equal to COUNTER_LIMIT..
  // Reset counter and send post message
  if(interrupt_counter == COUNTER_LIMIT)
  { 
    // Reset interrupt_counter and send POST 
    interrupt_counter = 0;
    connector.SendPost(ReadUltrasonic());

    // Blink LED to show that a POST request has been sent
    digitalWrite(LED_BUILTIN, HIGH);   
    delay(500);                       
    digitalWrite(LED_BUILTIN, LOW);      
    
    #ifdef SERIAL_DEBUG
    Serial.println("POST Sent!");
    #endif
  }
  
  //  Sleep until next interrupt
  //sleep();
}
