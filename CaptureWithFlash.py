import subprocess
import time
import pigpio
from gpiozero import MotionSensor, LED

# Set up the camera
subprocess.call(["gphoto2", "--set-config", "eosremoterelease=Immediate"])
subprocess.call(["gphoto2", "--set-config", "eosremoterelease=Release Full"])

# Initialize the pigpio instance
pi = pigpio.pi()

# Initialize the motion sensor
pir = MotionSensor(6)

# Initialize the LED
led = LED(17)

# Initialize the GPIO pin for the flash
flash_pin = 18
pi.set_mode(flash_pin, pigpio.OUTPUT)

# Wait for 10 seconds before starting the loop
print("Waiting for 10 seconds...")
time.sleep(10)

# Start the loop
print("Starting the loop...")
while True:
    if pir.motion_detected:
        # Turn on the LED
        led.on()

        # Trigger the flash
        pi.write(flash_pin, 1)
        time.sleep(0.01)
        pi.write(flash_pin, 0)

        # Take a photo
        print("Taking photo...")
        try:
            subprocess.check_call(["gphoto2", "--capture-image-and-download"])
            print("Photo taken")
        except subprocess.CalledProcessError as e:
            print("Could not take photo:", e)

        # Wait for 5 seconds before checking for motion again
        time.sleep(5)

    else:
        # Turn off the LED
        led.off()

        # Wait for 1 second before checking for motion again
        time.sleep(1)
