import RPi.GPIO as GPIO
import time

# Set up HC-SR501 motion sensor
pir_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_pin, GPIO.IN)

# Set up distance sensor
# Replace the following lines with the appropriate code for your specific sensor
distance_pin = 23
GPIO.setup(distance_pin, GPIO.IN)

while True:
    # Check for motion with HC-SR501
    if GPIO.input(pir_pin):
        print("Motion detected")

    # Read distance from distance sensor
    # Replace the following line with the appropriate code for your specific sensor
    distance = GPIO.input(distance_pin)

    # Uncomment the following line if you want to print distance as well
    # print("Distance: {} cm".format(distance))

    time.sleep(0.1)
