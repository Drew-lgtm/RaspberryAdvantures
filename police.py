import machine
import utime

red_led = machine.Pin(17, machine.Pin.OUT)
blue_led = machine.Pin(28, machine.Pin.OUT)

while True:
    blue_led.value(1)# turn on blue led
    red_led.value(0)# turn off red led
    utime.sleep(0.5)# sleep 0.5 sec
    red_led.value(1)# turn on red led
    blue_led.value(0)# turn off blue led
    utime.sleep(0.5)# sleep 0.5 sec