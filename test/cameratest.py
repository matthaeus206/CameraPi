import RPi.GPIO as GPIO
import time

# Pin assignments
shutter_pin = 4

# Set up GPIO pin as output
GPIO.setmode(GPIO.BCM)
GPIO.setup(shutter_pin, GPIO.OUT)

# Define a function to trigger the camera shutter
def trigger_shutter():
    GPIO.output(shutter_pin, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(shutter_pin, GPIO.LOW)

# Continually trigger the camera every 5 seconds
while True:
    trigger_shutter()
    time.sleep(5)
