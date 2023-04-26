import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)  # set up GPIO pin 4 as an output
GPIO.setup(5, GPIO.OUT)  # set up GPIO pin 5 as an output

try:
    while True:
        # turn on pin 4 and turn off pin 5
        GPIO.output(4, GPIO.HIGH)
        GPIO.output(5, GPIO.LOW)
        time.sleep(5)

        # turn off pin 4 and turn on pin 5
        GPIO.output(4, GPIO.LOW)
        GPIO.output(5, GPIO.HIGH)
        time.sleep(5)

except KeyboardInterrupt:
    # Clean up GPIO pins and exit gracefully on Ctrl+C
    GPIO.cleanup([4, 5])
