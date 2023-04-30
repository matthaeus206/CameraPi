import RPi.GPIO as GPIO
import time
import subprocess

# Set up HC-SR501 motion sensor
pir_pin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_pin, GPIO.IN)

# Set up a function to check for undervoltage
def check_undervoltage():
    # Run vcgencmd to check the undervoltage status
    result = subprocess.check_output("vcgencmd get_throttled", shell=True)

    # Check if the "undervoltage" bit is set in the result
    return "0x50000" in result.decode("utf-8")

while True:
    # Check for motion with HC-SR501
    if GPIO.input(pir_pin):
        print("Motion detected")

    # Check for undervoltage
    if check_undervoltage():
        print("Undervoltage detected")

    time.sleep(1)
