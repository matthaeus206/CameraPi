import RPi.GPIO as GPIO
import time
import subprocess

# Set up GPIO mode and pin for HC-SR501 motion sensor
GPIO.setmode(GPIO.BCM)
PIR_PIN = 6
GPIO.setup(PIR_PIN, GPIO.IN)

# Set up a function to check for undervoltage using subprocess module
def check_undervoltage():
    # Run vcgencmd to check the undervoltage status
    result = subprocess.check_output("vcgencmd get_throttled", shell=True)

    # Check if the "undervoltage" bit is set in the result
    return "0x50000" in result.decode("utf-8")

# Main loop to check for motion and undervoltage
while True:
    # Check for motion with HC-SR501
    if GPIO.input(PIR_PIN):
        print("Motion detected")

    # Check for undervoltage with the check_undervoltage function
    if check_undervoltage():
        print("Undervoltage detected")

    # Wait for 1.5 seconds before checking the sensor again
    time.sleep(1.5)
