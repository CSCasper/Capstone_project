#ifndef wifi_h
#define wifi_h
#define PORT 8080

#define SECRET_SSID "WiFi@OSU"
#define SECRET_PASS "Not-Needed"

#include <SPI.h>
#include <WiFiNINA.h>

class WiFiConnector
{
	public:
    WiFiConnector();
		void ConnectToWiFi();
		void ConnectToServer();
    void SendPost(String postData);
	private:
    IPAddress _server;
    WiFiClient _client;
		void printMacAddress(byte mac[]);
    void printCurrentNet();
    void printWifiData();
};

#endif
