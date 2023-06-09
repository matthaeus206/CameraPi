import RPi.GPIO as GPIO
import time

# Set the pin numbering scheme to use the BCM scheme
GPIO.setmode(GPIO.BCM)

# Set pin 4 as an output
GPIO.setup(4, GPIO.OUT)

try:
    # Loop forever
    while True:
        # Turn on pin 4
        GPIO.output(4, GPIO.HIGH)

        # Wait for 2 seconds
        time.sleep(2)

        # Turn off pin 4
        GPIO.output(4, GPIO.LOW)

        # Wait for 2 seconds
        time.sleep(2)

except KeyboardInterrupt:
    # Clean up the GPIO pins if the user interrupts the script
    GPIO.cleanup()

except Exception as e:
    # Clean up the GPIO pins if an exception is raised
    GPIO.cleanup()
    print("An error occurred: " + str(e))
