import board
import digitalio
# import adafruit_hcsr04  # Commenting out this line
import time

# Set up GPIO pins for the transistors
flash_pin = digitalio.DigitalInOut(board.D4)
flash_pin.direction = digitalio.Direction.OUTPUT
shutter_pin = digitalio.DigitalInOut(board.D5)
shutter_pin.direction = digitalio.Direction.OUTPUT

# Initialize the motion and distance sensors
pir = digitalio.DigitalInOut(board.D6)
pir.direction = digitalio.Direction.INPUT
pir.pull = digitalio.Pull.UP
# ultrasonic = adafruit_hcsr04.HCSR04(trigger_pin=board.D17, echo_pin=board.D16)  # Commenting out this line

# Define a function to trigger the flash and shutter release
def trigger_camera():
    # Trigger flash
    flash_pin.value = True
    time.sleep(1.2)
    flash_pin.value = False
    # Trigger shutter release
    shutter_pin.value = True
    time.sleep(0.1)
    shutter_pin.value = False

# Continuously monitor the sensors and trigger the transistors when conditions are met
while True:
    if pir.value:  # Commenting out the condition related to the distance sensor
        trigger_camera()
    time.sleep(0.1)  # Sleep for 100ms between sensor readings
