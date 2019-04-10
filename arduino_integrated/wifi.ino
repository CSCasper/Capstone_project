#include "wifi.h"

WiFiConnector::WiFiConnector()
{
    _server = IPAddress(192, 168, 1, 100);
    //_server = IPAddress(104, 231, 149, 111);
}

void WiFiConnector::ConnectToWiFi()
{
  int status  = WL_IDLE_STATUS;   // the Wifi radio's status
  
  //Initialize serial and wait for port to open:
  
  //while (!Serial) {
  //  ; // wait for serial port to connect. Needed for native USB port only
  //}
  
  int timeout = 0;
  // attempt to connect to Wifi network:
  while (status != WL_CONNECTED) 
  {
    if(timeout == 4)
    {
      break;
    }
    Serial.print("Attempting to connect to WPA SSID: ");
    Serial.println(SECRET_SSID);
    // Connect to WPA/WPA2 network:
    status = WiFi.begin(SECRET_SSID, SECRET_PASS);
    
    delay(500);
    timeout++;
  }

  if(timeout == 4)
  {
    Serial.print("Failed to connect!");
  }
  else
  {
     // you're connected now, so print out the data:
    Serial.print("You're connected to the network");
    printCurrentNet();
    printWifiData();
  }
}

void WiFiConnector::SendPost(String postData)
{ 
    if(_client.connect(_server, PORT)){
      _client.println("POST /test HTTP/1.1");
      _client.println("Connection: close");
      _client.println("Content-Type: application/x-www-form-urlencoded;");
      _client.print("Content-Length: ");
      _client.println(postData.length());
      _client.println();
      _client.println(postData);
  }
}


void WiFiConnector::printWifiData() {
  // print your board's IP address:
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

  // print your MAC address:
  byte mac[6];
  WiFi.macAddress(mac);
  Serial.print("MAC address: ");
  printMacAddress(mac);
}

void WiFiConnector::printCurrentNet() {
  // print the SSID of the network you're attached to:
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  // print the MAC address of the router you're attached to:
  byte bssid[6];
  WiFi.BSSID(bssid);
  Serial.print("BSSID: ");
  printMacAddress(bssid);

  // print the received signal strength:
  long rssi = WiFi.RSSI();
  Serial.print("signal strength (RSSI):");
  Serial.println(rssi);

  // print the encryption type:
  byte encryption = WiFi.encryptionType();
  Serial.print("Encryption Type:");
  Serial.println(encryption, HEX);
  Serial.println();
}

void WiFiConnector::printMacAddress(byte mac[]) {
  for (int i = 5; i >= 0; i--) {
    if (mac[i] < 16) {
      Serial.print("0");
    }
    Serial.print(mac[i], HEX);
    if (i > 0) {
      Serial.print(":");
    }
  }
  Serial.println();
}
