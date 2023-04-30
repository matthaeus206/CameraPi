# Import necessary modules
import RPi.GPIO as GPIO
from gpiozero import MotionSensor, DistanceSensor
from time import sleep

# Set up GPIO numbering mode
GPIO.setmode(GPIO.BCM)

# Set up GPIO pins for the transistors
flash_pin = 4
shutter_pin = 5
GPIO.setup(flash_pin, GPIO.OUT)
GPIO.setup(shutter_pin, GPIO.OUT)

# Initialize the motion and distance sensors
pir = MotionSensor(6)
ultrasonic = DistanceSensor(echo=16, trigger=17, max_distance=100, queue_len=2)

# Define a function to trigger the flash and shutter release
def trigger_camera():
    # Trigger flash
    GPIO.output(flash_pin, GPIO.HIGH)
    sleep(1.2)
    GPIO.output(flash_pin, GPIO.LOW)
    # Trigger shutter release
    GPIO.output(shutter_pin, GPIO.HIGH)
    sleep(0.1)
    GPIO.output(shutter_pin, GPIO.LOW)

# Continuously monitor the sensors and trigger the transistors when conditions are met
while True:
    if pir.motion_detected and ultrasonic.distance > 0.254:  # 10 inches in meters
        trigger_camera()
    sleep(0.1)  # Sleep for 100ms between sensor readings
