import time
import pigpio
from gpiozero import DistanceSensor

# Initialize the distance sensor
ultrasonic = DistanceSensor(echo=4, trigger=5)

# Initialize pigpio
pi = pigpio.pi()

# Define a callback function to print the distance of the object
def cb_echo(gpio, level, tick):
    distance = ultrasonic.distance * 100 # convert to centimeters
    print(f"Distance: {distance:.2f} cm")

# Add a callback to the echo pin
cb = pi.callback(ultrasonic.echo_pin, pigpio.EITHER_EDGE, cb_echo)

try:
    # Keep the script running indefinitely
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    # Clean up resources on keyboard interrupt
    cb.cancel()
    pi.stop()
    ultrasonic.close()
