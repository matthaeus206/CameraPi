import RPi.GPIO as GPIO
from gpiozero import MotionSensor, LED
import subprocess
import time

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
PIR_PIN = 6
FLASH_PIN = 18
HALF_PRESS_PIN = 23
FULL_PRESS_PIN = 24
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(FLASH_PIN, GPIO.OUT)
GPIO.setup(HALF_PRESS_PIN, GPIO.OUT)
GPIO.setup(FULL_PRESS_PIN, GPIO.OUT)

# Initialize the motion sensor and LED
pir = MotionSensor(PIR_PIN)
led = LED(17)

# Wait for motion
pir.wait_for_motion()
print("Motion detected")
led.on()

try:
    while True:
        # Take a photo if motion is detected
        if pir.motion_detected:
            try:
                # Half-press the camera button
                GPIO.output(HALF_PRESS_PIN, GPIO.HIGH)
                time.sleep(1)

                # Full-press the camera button to take the photo
                GPIO.output(FULL_PRESS_PIN, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(FULL_PRESS_PIN, GPIO.LOW)

                # Release the camera button
                GPIO.output(HALF_PRESS_PIN, GPIO.LOW)
                time.sleep(0.5)
            except Exception as e:
                print("Could not take photo:", e)

            # Trigger the flash
            GPIO.output(FLASH_PIN, GPIO.HIGH)
            time.sleep(0.01)
            GPIO.output(FLASH_PIN, GPIO.LOW)

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
    pir.close()
    led.close()
    GPIO.cleanup()
