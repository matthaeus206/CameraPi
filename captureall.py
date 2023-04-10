import RPi.GPIO as GPIO
from gpiozero import MotionSensor, LED
import subprocess
import time

# Define GPIO pins for HC-SR04
TRIG_PIN = 23
ECHO_PIN = 24

# Define GPIO pins for camera
CAM_HALF_PRESS_PIN = 18
CAM_FULL_PRESS_PIN = 25

# Define GPIO pin for flash
FLASH_PIN = 17

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(CAM_HALF_PRESS_PIN, GPIO.OUT)
GPIO.setup(CAM_FULL_PRESS_PIN, GPIO.OUT)
GPIO.setup(FLASH_PIN, GPIO.OUT)

# Initialize the motion sensor
pir = MotionSensor(6)

# Initialize the LED
led = LED(27)

# Wait for motion
pir.wait_for_motion()
print("Motion detected")
led.on()

try:
    while True:
        # Measure distance with HC-SR04
        GPIO.output(TRIG_PIN, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIG_PIN, GPIO.LOW)
        pulse_start = time.time()
        while GPIO.input(ECHO_PIN) == GPIO.LOW:
            pulse_start = time.time()
        pulse_end = time.time()
        while GPIO.input(ECHO_PIN) == GPIO.HIGH:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        
        # Take a photo if motion is detected and distance is within range
        if pir.motion_detected and 0.3 <= distance <= 7:
            try:
                # Half-press the camera button
                GPIO.output(CAM_HALF_PRESS_PIN, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(CAM_HALF_PRESS_PIN, GPIO.LOW)

                # Wait for autofocus to complete
                time.sleep(1)

                # Full-press the camera button
                GPIO.output(CAM_FULL_PRESS_PIN, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(CAM_FULL_PRESS_PIN, GPIO.LOW)

                # Wait for photo to be taken
                time.sleep(5)

                print("Photo taken")

                # Trigger the flash
                GPIO.output(FLASH_PIN, GPIO.HIGH)
                time.sleep(0.01)
                GPIO.output(FLASH_PIN, GPIO.LOW)
            except Exception as e:
                print("Could not take photo:", e)

        # Wait for motion to stop
        pir.wait_for_no_motion()
        print("Motion stopped")
        led.off()

        # Wait for motion to start again
        pir.wait_for_motion()
        print("Motion detected")
        led.on()

finally:
    # Clean up resources
    GPIO.cleanup([TRIG_PIN, ECHO_PIN, CAM_HALF_PRESS_PIN, CAM_FULL_PRESS_PIN, FLASH_PIN])
    pir.close()
    led.close()
