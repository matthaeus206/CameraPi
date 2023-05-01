# Use Circuitpython
import board
import digitalio
import time

flash_pin = digitalio.DigitalInOut(board.D9)
flash_pin.direction = digitalio.Direction.OUTPUT
shutter_pin = digitalio.DigitalInOut(board.D10)
shutter_pin.direction = digitalio.Direction.OUTPUT

while True:
    flash_pin.value = True
    time.sleep(1.2)
    flash_pin.value = False
    shutter_pin.value = True
    time.sleep(0.1)
    shutter_pin.value = False
    time.sleep(0.1)

