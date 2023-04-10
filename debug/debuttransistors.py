import RPi.GPIO as GPIO
import time

# Set up GPIO pin
transistor_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(transistor_pin, GPIO.OUT)

try:
    # Trigger transistor for 1 second
    print("Triggering transistor for 1 second...")
    GPIO.output(transistor_pin, True)
    time.sleep(1)
    GPIO.output(transistor_pin, False)
    print("Transistor test complete!")
except KeyboardInterrupt:
    GPIO.cleanup()
