import time
import board
import digitalio

# Set up motion sensor
pir_pin = board.GP7
pir = digitalio.DigitalInOut(pir_pin)
pir.direction = digitalio.Direction.INPUT

# Loop forever
while True:
    # If motion is detected, print message
    if pir.value:
        print("motion detected")

    # Wait a short time before checking again
    time.sleep(0.1)
