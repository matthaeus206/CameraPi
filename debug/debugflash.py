import RPi.GPIO as GPIO
import time

# set up GPIO pins
pir_pin = 6
dslr_pin_1 = 4
dslr_pin_2 = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_pin, GPIO.IN)
GPIO.setup(dslr_pin_1, GPIO.OUT)
GPIO.setup(dslr_pin_2, GPIO.OUT)

# loop to detect motion and take pictures
while True:
    if GPIO.input(pir_pin):
        # motion detected, trigger DSLR
        GPIO.output(dslr_pin_1, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(dslr_pin_2, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(dslr_pin_1, GPIO.LOW)
        GPIO.output(dslr_pin_2, GPIO.LOW)
        print("Picture taken!")
    time.sleep(0.1)
