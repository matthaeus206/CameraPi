import subprocess
import time
import RPi.GPIO as GPIO
from gpiozero import MotionSensor, DistanceSensor, LED

# Initialize the motion sensor
pir = MotionSensor(4)

# Initialize the ultrasonic sensor minimum recharge time is 0.5sec
ultrasonic = DistanceSensor(echo=4, trigger=5)

# Initialize the LED
led = LED(17)

# Initialize the GPIO pin for the flash
flash_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(flash_pin, GPIO.OUT)

# Define function to take picture and trigger flash
def take_picture():
    while True:
        # Turn on the LED
        led.on()

        # Trigger the camera shutter
        subprocess.call(["gphoto2", "--trigger-capture"])

        # Wait for the camera to start exposure
        time.sleep(0.01)

        # Check the shutter speed
        shutter_speed = float(subprocess.check_output(["gphoto2", "--get-config", "/main/capturesettings/shutterspeed"]).decode('utf-8').split(" ")[-1])

        if shutter_speed < 1/300:
            # Trigger the flash at the beginning of the exposure
            GPIO.output(flash_pin, GPIO.HIGH)
            time.sleep(shutter_speed)
            GPIO.output(flash_pin, GPIO.LOW)
        else:
            # Trigger the flash near the end of the exposure
            time.sleep(shutter_speed * (299/300))
            GPIO.output(flash_pin, GPIO.HIGH)
            time.sleep(shutter_speed * (1/300))
            GPIO.output(flash_pin, GPIO.LOW)

        # Turn off the LED
        led.off()

        # Wait for one second before taking the next picture
        time.sleep(1)

if __name__ == '__main__':
    # Call the take_picture function
    take_picture()

    # Clean up GPIO resources
    pir.close()
    ultrasonic.close()
    led.close()
    GPIO.cleanup()
