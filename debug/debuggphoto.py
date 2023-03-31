import subprocess
import time
from gpiozero import MotionSensor

# Initialize the motion sensor
pir = MotionSensor(6)

# Define function to take picture and save it on camera's SD card
def take_picture():
    # Define gphoto2 command to take a picture and save it on camera's SD card
    cmd = "gphoto2 --capture-image-and-download --filename /store_00010001/DCIM/100CANON/%Y%m%d_%H%M%S.jpg"

    while True:
        # Wait for motion to be detected
        pir.wait_for_motion()

        # Print message when motion is detected
        print("Motion detected")

        # Try to get the current camera settings
        try:
            settings = subprocess.check_output(["gphoto2", "--get-config"], stderr=subprocess.STDOUT)
            print("Camera settings:\n", settings.decode())
        except subprocess.CalledProcessError as e:
            print("Could not get camera settings:", e)

        # Try to take a picture and save it on the camera's SD card
        try:
            subprocess.check_call(cmd.split())
            print("Picture taken and saved on camera's SD card")
        except subprocess.CalledProcessError as e:
            print("Could not take picture:", e)

if __name__ == '__main__':
    try:
        # Call the take_picture function
        take_picture()
    except KeyboardInterrupt:
        # Clean up resources on keyboard interrupt
        print("\nCleaning up resources...")
        pir.close()
