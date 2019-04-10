#include "wifi.h"
#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>

WiFiConnector connector;

#define COUNTER_LIMIT 5

volatile int interrupt_counter = 0;

ISR(RTC_CNT_vect)
{ 
  RTC.INTFLAGS = RTC_OVF_bm;
  interrupt_counter++;
  Serial.println("Interrupt!");  
}

void sleep()
{
  // Enable sleep and enter sleep mode
  sleep_enable();
  sleep_mode();
  sleep_disable();
}

void setup()
{
  Serial.begin(9600);
  connector.ConnectToWiFi();

  // Use 20MHz internal clock
  CLKCTRL.MCLKCTRLA = 0x00;

  // Standby Sleep mode when sleep is enabled
  set_sleep_mode(SLEEP_MODE_STANDBY);
  
  //SLPCTRL.CTRLA     |= 0x01;

  // Enable Real Time Counter (2 seconds)
  // Enable RTC to work in Sleep mode
  RTC.CTRLA  = 0xB1;
  // Use 32.768 kHz clock for RTC
  RTC.CLKSEL = 0x00;
  
  // Real Time Counter period
  RTC.PER = 1024;
  // Enable Overflow Interrupt
  RTC.INTCTRL = 0x01;

}

void loop() 
{
  if(interrupt_counter == COUNTER_LIMIT)
  {
    interrupt_counter = 0;
    connector.SendPost("1 50");
    Serial.println("POST Sent!");
    sleep();
  }
}
