import time
import pigpio

# Set up the motion sensor on GPIO pin 6
pir_pin = 6
pi = pigpio.pi()
pi.set_mode(pir_pin, pigpio.INPUT)
pi.set_pull_up_down(pir_pin, pigpio.PUD_DOWN)

# Get the current sensitivity, delay, and trigger mode of the motion sensor
sensitivity = pi.get_PWM_dutycycle(pir_pin)
delay = pi.get_PWM_frequency(pir_pin)
trigger_mode = pi.get_PWM_range(pir_pin)

# Print the sensitivity, delay, and trigger mode
print("Sensitivity: ", sensitivity)
print("Delay: ", delay)
print("Trigger Mode: ", trigger_mode)

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
