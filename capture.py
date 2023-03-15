import subprocess
import time
from gpiozero import MotionSensor, DistanceSensor, LED, OutputDevice

# Initialize the motion sensor
pir = MotionSensor(4)

# Initialize the ultrasonic sensor
ultrasonic = DistanceSensor(echo=4, trigger=5)

# Initialize the LED
led = LED(17)

# Initialize the flash trigger
flash = OutputDevice(27, active_high=False)

# Define function to take picture and trigger flash
def take_picture_and_flash():
    # Trigger the flash
    flash.on()
    time.sleep(0.05)  # Flash duration
    flash.off()
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
            # Take the picture and trigger the flash if something is close enough
            if distance < 10:
                # Take the picture and trigger the flash
                take_picture_and_flash()
                # Break out of loop
                break
            # Wait for 1 second before checking again
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program terminated by user")
    finally:
        # Clean up GPIO resources
        pir.close()
        ultrasonic.close()
        led.close()
        flash.close()
