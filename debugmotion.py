import time
import pigpio

# Set up the motion sensor on GPIO pin 6
pir_pin = 6
pi = pigpio.pi()
pi.set_mode(pir_pin, pigpio.INPUT)
pi.set_pull_up_down(pir_pin, pigpio.PUD_DOWN)

# Loop indefinitely
while True:
    # Read the current state of the motion sensor
    motion_detected = pi.read(pir_pin)

    # Print the state of the motion sensor
    if motion_detected:
        print("Motion detected!")
    else:
        print("No motion detected.")

    # Wait for a moment before checking again
    time.sleep(0.1)
