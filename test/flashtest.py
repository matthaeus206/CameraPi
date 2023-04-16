import RPi.GPIO as GPIO
import time

# Set up GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

try:
    while True:
        # Turn on the flash
        GPIO.output(17, GPIO.HIGH)
        time.sleep(0.1)

        # Turn off the flash
        GPIO.output(17, GPIO.LOW)
        time.sleep(4.9)

except KeyboardInterrupt:
    # Clean up the GPIO pins
    GPIO.cleanup()
