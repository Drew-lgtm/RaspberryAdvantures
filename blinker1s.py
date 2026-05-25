import machine
import utime
led_pin = machine.Pin(25, machine.Pin.OUT)

while True:
    led_pin.value(1)# turn on led
    utime.sleep(1.0)# sleep 1 sec
    led_pin.value(0)# turn led off
    utime.sleep(1.0)# sleep 1 sec