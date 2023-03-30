import time
import pigpio

# Set up the motion sensor on GPIO pin 6
pir_pin = 6
pi = pigpio.pi()
pi.set_mode(pir_pin, pigpio.INPUT)
pi.set_pull_up_down(pir_pin, pigpio.PUD_DOWN)

# Get the sensitivity of the motion sensor
sensitivity = pi.read(pir_pin)

# Set the delay and trigger mode of the motion sensor
pi.set_PWM_dutycycle(pir_pin, 10) # Set delay to 10 seconds
pi.set_PWM_frequency(pir_pin, 5) # Set trigger mode to repeatable

# Print the sensitivity, delay, and trigger mode of the motion sensor
print("Sensitivity: {} meters".format(sensitivity))
print("Delay: {} seconds".format(pi.get_PWM_dutycycle(pir_pin)))
print("Trigger mode: {}".format("repeatable" if pi.get_PWM_frequency(pir_pin) == 5 else "single"))

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
