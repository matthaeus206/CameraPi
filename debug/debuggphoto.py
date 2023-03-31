import subprocess
import time
import pigpio
from gpiozero import MotionSensor

# Initialize the motion sensor
pir = MotionSensor(6)

# Define function to take picture when motion is detected
def take_picture():
    while True:
        # Wait for motion to be detected
        pir.wait_for_motion()

        # Set capturetarget to 1 to save images to camera's memory card
        subprocess.call(["gphoto2", "--set-config", "capturetarget=1"])

        # Capture the image and save it to camera's memory card
        subprocess.call(["gphoto2", "--capture-image-and-download"])

        # Print message indicating that image was captured and saved to camera's memory card
        print("Image captured and saved to camera's memory card.")

if __name__ == '__main__':
    try:
        # Call the take_picture function
        take_picture()
    except KeyboardInterrupt:
        # Clean up GPIO resources on keyboard interrupt
        print("\nCleaning up GPIO resources...")
        pir.close()
