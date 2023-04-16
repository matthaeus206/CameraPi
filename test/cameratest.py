import RPi.GPIO as GPIO
import time

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Define half-press and full-press durations
HALF_PRESS_DURATION = 0.2
FULL_PRESS_DURATION = 0.5

# Function to simulate half-press event
def half_press():
    # Simulate half-press by turning on the half-press transistor for a short duration
    GPIO.output(17, GPIO.HIGH)
    time.sleep(HALF_PRESS_DURATION)
    GPIO.output(17, GPIO.LOW)

# Function to simulate full-press event
def full_press():
    # Simulate full-press by turning on the full-press transistor for a longer duration
    GPIO.output(18, GPIO.HIGH)
    time.sleep(FULL_PRESS_DURATION)
    GPIO.output(18, GPIO.LOW)

# Main loop
try:
    while True:
        # Wait for button press
        GPIO.wait_for_edge(27, GPIO.FALLING)

        # Determine whether to do a half-press or full-press
        if GPIO.input(27):
            full_press()
        else:
            half_press()

except KeyboardInterrupt:
    # Clean up the GPIO pins
    GPIO.cleanup()
