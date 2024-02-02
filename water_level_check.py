from machine import Pin, ADC
import time
import network
import urequests
import statistics
import secrets
sensor = ADC(Pin(26))
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.SSID, secrets.PASSWORD)
time.sleep(5)
print(wlan.isconnected())
readings = []
try:
   while True:
       for i in range(5):
           reading = sensor.read_u16()
           readings.append(reading)
           print(readings) 
           time.sleep(1)
       median_value = statistics.median(readings)
       if median_value < 400:
           urequests.get("https://api.telegram.org/bot"+secrets.API+"/sendMessage?text=Gary is thirsty&chat_id="+secrets.ID)
           print("Message Sent")
       else:
           print("Gary has enough water")
       time.sleep(3600)
except OSError:
   print("@"*68)
   print("@ Cannot connect to the Wi-Fi, please check your SSID and PASSWORD @")
print("@"*68)