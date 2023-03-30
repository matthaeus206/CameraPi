import time
import pigpio

# Initialize the pigpio library and the GPIO pins
pi = pigpio.pi()
trigger_pin = 5
echo_pin = 4

# Set the trigger pin as an output and the echo pin as an input
pi.set_mode(trigger_pin, pigpio.OUTPUT)
pi.set_mode(echo_pin, pigpio.INPUT)

# Set the trigger pin to low (false) initially
pi.write(trigger_pin, 0)

while True:
    # Send a 10us pulse to the trigger pin to start the measurement
    pi.write(trigger_pin, 1)
    time.sleep(0.00001)
    pi.write(trigger_pin, 0)

    # Wait for the echo pin to go high
    start_time = time.time()
    while pi.read(echo_pin) == 0:
        if (time.time() - start_time) > 1:
            print("Echo pin is not detecting any signal")
            break

    # Wait for the echo pin to go low
    end_time = time.time()
    while pi.read(echo_pin) == 1:
        if (time.time() - end_time) > 1:
            print("Echo pin is not going low after being triggered")
            break

    # Calculate the duration of the pulse and convert it to distance in cm
    pulse_duration = end_time - start_time
    distance = pulse_duration * 17150

    # Print the distance
    print("Distance: %.1f cm" % distance)

    # Wait for one second before taking the next measurement
    time.sleep(1)
