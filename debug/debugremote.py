import RPi.GPIO as GPIO
import time

# set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# set up pins 4 and 5 as output pins
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

# loop forever
while True:
    # toggle transistor connected to pin 4 for 60ms
    GPIO.output(4, GPIO.HIGH)
    time.sleep(0.06)
    GPIO.output(4, GPIO.LOW)

    # wait for 0.5 seconds before toggling transistor connected to pin 5 on
    time.sleep(0.5)

    # toggle transistor connected to pin 5 for 60ms
    GPIO.output(5, GPIO.HIGH)
    time.sleep(0.06)
    GPIO.output(5, GPIO.LOW)

    # wait for 4 seconds before starting the loop again
    time.sleep(4)

# cleanup GPIO pins
GPIO.cleanup()
