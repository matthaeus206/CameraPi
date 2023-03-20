import subprocess
import time
from gpiozero import MotionSensor, DistanceSensor, LED

# Initialize the motion sensor
pir = MotionSensor(4)

# Initialize the ultrasonic sensor minimum recharge time is 0.5sec
ultrasonic = DistanceSensor(echo=4, trigger=5)

# Initialize the LED
led = LED(17)

# Define function to take picture
def take_picture():
    # Take the picture
    led.on()  # Turn on the LED
    subprocess.call(["gphoto2", "--trigger-capture"])
    time.sleep(0.01)  # Wait for camera to start exposure
    shutter_speed = float(subprocess.check_output(["gphoto2", "--get-config", "/main/capturesettings/shutterspeed"]).decode('utf-8').split(" ")[-1])
    time.sleep(shutter_speed * (299/300))  # Wait for the last 1/300 of exposure time
    led.off()  # Turn off the LED

if __name__ == '__main__':
    # Main program loop
    try:
        while True:
            # Get the distance reading from the ultrasonic sensor
            distance = ultrasonic.distance * 100
            # Print distance for debugging
            print('Distance: ', distance)
            # Take the picture if something is close enough and there is motion detected
            if distance < 10 and pir.motion_detected:
                # Take the picture
                take_picture()
            # Wait for 1 second before checking again
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program terminated by user")
    finally:
        # Clean up GPIO resources
        pir.close()
        ultrasonic.close()
        led.close()
