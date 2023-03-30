import time
import pigpio

# Set up the motion sensor on GPIO pin 6
pir_pin = 6
pi = pigpio.pi()
pi.set_mode(pir_pin, pigpio.INPUT)
pi.set_pull_up_down(pir_pin, pigpio.PUD_DOWN)

# Check whether the pin is a PWM pin and print the sensitivity if available
try:
    if pi.get_PWM_range(pir_pin) != 0:
        sensitivity = pi.get_PWM_dutycycle(pir_pin)
        print(f"Sensitivity: {sensitivity}")
except:
    print("Error reading sensitivity")

# Get the current delay and trigger mode of the motion sensor
try:
    delay = pi.get_mode(pir_pin)
    trigger = pi.get_pull_up_down(pir_pin)
    print(f"Delay: {delay}, Trigger mode: {trigger}")
except:
    print("Error reading delay and trigger mode")

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
