import subprocess
import time
import pigpio
from gpiozero import LED, MotionSensor

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

while True:
    # Wait for motion
    pir.wait_for_motion()

    # Turn on the LED
    led.on()

    # Trigger the flash
    pi.write(flash_pin, 1)
    time.sleep(0.01)
    pi.write(flash_pin, 0)

    # Take a picture
    try:
        subprocess.check_call(["gphoto2", "--capture-image"])
        print("Photo taken")
    except subprocess.CalledProcessError as e:
        print("Could not take picture:", e)

    # Wait for motion to stop
    pir.wait_for_no_motion()

    # Turn off the LED
    led.off()

# Clean up the resources
pir.close()
led.close()
pi.stop()
