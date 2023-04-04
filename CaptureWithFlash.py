import pigpio
from gpiozero import MotionSensor, LED
import subprocess
import time

# Initialize the pigpio instance
pi = pigpio.pi()

# Initialize the motion sensor
pir = MotionSensor(6)

# Initialize the LED
led = LED(17)

# Initialize the GPIO pin for the flash
flash_pin = 18
pi.set_mode(flash_pin, pigpio.OUTPUT)

try:
    while True:
        pir.wait_for_motion()
        print("Motion detected")
        led.on()
        
        # Take a photo
        try:
            subprocess.check_call(["gphoto2", "--set-config", "eosremoterelease=Immediate"])
            subprocess.check_call(["gphoto2", "--set-config", "eosremoterelease=Release Full"])
            subprocess.check_call(["gphoto2", "--wait-event-and-download=FILEADDED"])
            print("Photo taken")
        except subprocess.CalledProcessError as e:
            print("Could not take photo:", e)
            
        # Trigger the flash
        pi.write(flash_pin, 1)
        time.sleep(0.01)
        pi.write(flash_pin, 0)

        pir.wait_for_no_motion()
        print("Motion stopped")
        led.off()

finally:
    # Clean up resources
    pir.close()
    led.close()
    pi.stop()
