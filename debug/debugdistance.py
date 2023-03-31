import RPi.GPIO as GPIO
import time

# Set up HC-SR04 distance sensor
trig_pin = 4
echo_pin = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(trig_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

# Send a pulse to trigger the sensor and measure the time it takes to receive the echo
def get_distance():
    # Send a 10us pulse to trigger the sensor
    GPIO.output(trig_pin, True)
    time.sleep(0.00001)
    GPIO.output(trig_pin, False)

    # Wait for the echo to start and stop, and measure the duration
    pulse_start = time.time()
    while GPIO.input(echo_pin) == 0:
        pulse_start = time.time()

    pulse_end = time.time()
    while GPIO.input(echo_pin) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    # Convert the duration to distance in cm
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    return distance

while True:
    distance = get_distance()
    print("Distance: {} cm".format(distance))
    time.sleep(0.1)
