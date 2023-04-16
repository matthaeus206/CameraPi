import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set the GPIO pins for the half-press and full-press events
half_press_pin = 17
full_press_pin = 4

# Set the GPIO pins as outputs
GPIO.setup(half_press_pin, GPIO.OUT)
GPIO.setup(full_press_pin, GPIO.OUT)

# Define a function to simulate a half-press event
def half_press():
    GPIO.output(half_press_pin, GPIO.HIGH)
    time.sleep(0.5) # adjust the duration as needed
    GPIO.output(half_press_pin, GPIO.LOW)

# Define a function to simulate a full-press event
def full_press():
    GPIO.output(full_press_pin, GPIO.HIGH)
    time.sleep(0.5) # adjust the duration as needed
    GPIO.output(full_press_pin, GPIO.LOW)

# Flash the camera every 5 seconds using a loop
while True:
    half_press() # simulate a half-press event to focus
    time.sleep(1) # wait for the camera to focus
    full_press() # simulate a full-press event to take the photo
    time.sleep(5) # wait for 5 seconds before repeating
