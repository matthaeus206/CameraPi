import time
import pigpio

# initialize pigpio
pi = pigpio.pi()

# define GPIO pins
echo_pin = 4
trigger_pin = 5

# set trigger pin as output and echo pin as input
pi.set_mode(trigger_pin, pigpio.OUTPUT)
pi.set_mode(echo_pin, pigpio.INPUT)

# set trigger pin to low
pi.write(trigger_pin, 0)

# wait for the sensor to settle
time.sleep(2)

# send 10us pulse to trigger pin
pi.write(trigger_pin, 1)
time.sleep(0.00001)
pi.write(trigger_pin, 0)

# wait for echo pin to go high
start_time = time.time()
while pi.read(echo_pin) == 0:
    start_time = time.time()

# wait for echo pin to go low
stop_time = time.time()
while pi.read(echo_pin) == 1:
    stop_time = time.time()

# calculate distance
elapsed_time = stop_time - start_time
distance = (elapsed_time * 34300) / 2

print(f"Distance: {distance:.2f} cm")

# cleanup
pi.stop()
