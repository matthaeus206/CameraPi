import subprocess
import time
from gpiozero import MotionSensor

# Initialize the motion sensor
pir = MotionSensor(6)

# Set the gphoto2 configuration to save photos on the camera's memory card
subprocess.call(["gphoto2", "--set-config", "capturetarget=1"])

# Continuously check for motion and take photos when detected
while True:
    if pir.motion_detected:
        # Print a message when motion is detected
        print("Motion detected!")

        # Take a photo and save it on the camera's memory card
        subprocess.call(["gphoto2", "--trigger-capture"])
        
        # Print a message when the photo is captured
        print("Photo captured!")
        
        # Wait for 1 second before checking for motion again
        time.sleep(1)
