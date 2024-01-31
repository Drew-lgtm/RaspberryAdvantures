import machine
import utime

red_led = machine.Pin(17, machine.Pin.OUT)
blue_led = machine.Pin(28, machine.Pin.OUT)

while True:
    blue_led.value(1)# turn on led
    red_led.value(0)# turn on led
    utime.sleep(0.5)# sleep 1 sec
    red_led.value(1)# turn on led
    blue_led.value(0)# turn led of
    utime.sleep(0.5)
    