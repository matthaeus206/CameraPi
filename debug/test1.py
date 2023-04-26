import RPi.GPIO as GPIO
import time
import subprocess

# Set up HC-SR501 motion sensor and output pins
pir_pin = 6
out_pin_4 = 4
out_pin_5 = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_pin, GPIO.IN)
GPIO.setup(out_pin_4, GPIO.OUT)
GPIO.setup(out_pin_5, GPIO.OUT)

# Set up a function to check for undervoltage
def check_undervoltage():
    # Run vcgencmd to check the undervoltage status
    result = subprocess.check_output("vcgencmd get_throttled", shell=True)

    # Check if the "undervoltage" bit is set in the result
    return "0x50000" in result.decode("utf-8")

# Main loop
try:
    while True:
        # Check for motion with HC-SR501
        if GPIO.input(pir_pin):
            print("Motion detected")
            # Alternate between pins 4 and 5 every 5 seconds
            for i in range(2):
                GPIO.output(out_pin_4, GPIO.HIGH)
                GPIO.output(out_pin_5, GPIO.LOW)
                time.sleep(5)
                GPIO.output(out_pin_4, GPIO.LOW)
                GPIO.output(out_pin_5, GPIO.HIGH)
                time.sleep(5)

        # Check for undervoltage
        if check_undervoltage():
            print("Undervoltage detected")

        time.sleep(1)

except KeyboardInterrupt:
    # Clean up GPIO pins and exit gracefully on Ctrl+C
    GPIO.cleanup([pir_pin, out_pin_4, out_pin_5])
