import machine
from machine import Pin
from gpiozero import MotionSensor, DistanceSensor
from time import sleep

# Set up GPIO pins for the transistors
flash_pin = Pin(4, Pin.OUT)
shutter_pin = Pin(5, Pin.OUT)

# Initialize the motion and distance sensors
pir = MotionSensor(6)
ultrasonic = DistanceSensor(echo=16, trigger=17, max_distance=100, queue_len=2)

# Define a function to trigger the flash and shutter release
def trigger_camera():
    # Trigger flash
    flash_pin.value(1)
    sleep(1.2)
    flash_pin.value(0)
    # Trigger shutter release
    shutter_pin.value(1)
    sleep(0.1)
    shutter_pin.value(0)

# Define a function to continuously monitor the sensors and trigger the transistors when conditions are met
def monitor_sensors():
    while True:
        if pir.motion_detected and ultrasonic.distance > 0.254:  # 10 inches in meters
            trigger_camera()
        sleep(0.1)  # Sleep for 100ms between sensor readings

# Call the function to monitor the sensors and trigger the transistors
monitor_sensors()
