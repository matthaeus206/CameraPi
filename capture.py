#!/usr/bin/env python3

import subprocess
import time
from gpiozero import MotionSensor, DistanceSensor, LED

# Initialize the motion sensor
pir = MotionSensor(4)

# Initialize the ultrasonic sensor
ultrasonic = DistanceSensor(echo=4, trigger=5)

# Initialize the LED
led = LED(17)

# Define function to take picture
def take_picture():
    led.on()  # Turn on the LED
    subprocess.call(["gphoto2", "--capture-image"])
    led.off()  # Turn off the LED

if __name__ == '__main__':
    # Main program loop
    while True:
        # Get the distance reading from the ultrasonic sensor
        distance = ultrasonic.distance * 100
        # Print distance for debugging
        print('Distance: ', distance)
        # Take the picture if something is close enough
        if distance < 10:
            # Take the picture
            take_picture()
            # Break out of loop
            break
        # Wait for 1 second before checking again
        time.sleep(1)
