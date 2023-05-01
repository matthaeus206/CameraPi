import machine
from machine import Pin
from time import sleep

flash_pin = Pin(9, Pin.OUT)
shutter_pin = Pin(10, Pin.OUT)

while True:
    flash_pin.value(1)
    sleep(1.2)
    flash_pin.value(0)
    shutter_pin.value(1)
    sleep(0.1)
    shutter_pin.value(0)
    sleep(0.1)
