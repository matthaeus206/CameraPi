import RPi.GPIO as GPIO
import time

# Set the pin numbering scheme to use the BCM scheme
GPIO.setmode(GPIO.BCM)

# Set pin 5 as an output
GPIO.setup(5, GPIO.OUT)

# Loop forever
while True:
    # Turn on pin 5
    GPIO.output(5, GPIO.HIGH)

    # Wait for 2 seconds
    time.sleep(2)

    # Turn off pin 5
    GPIO.output(5, GPIO.LOW)

    # Wait for 2 seconds
    time.sleep(2)
