import RPi.GPIO as GPIO
import time

# Set up HC-SR04 distance sensor
trig_pin = 18
echo_pin = 17
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
        if pulse_start - time.time() > 0.1:  # If the sensor is not detected for 0.1 seconds, print a message
            print("Sensor not detected!")
            return None

    pulse_end = time.time()
    while GPIO.input(echo_pin) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    # Convert the duration to distance in cm
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    return distance

last_measurement_time = time.time()
try:
    while True:
        distance = get_distance()
        if distance is not None and time.time() - last_measurement_time >= 2:
            print("Distance: {} cm".format(distance))
            last_measurement_time = time.time()
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
