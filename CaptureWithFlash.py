import subprocess
import time
import pigpio
from gpiozero import MotionSensor, LED

# Initialize the pigpio instance
pi = pigpio.pi()

# Initialize the motion sensor
pir = MotionSensor(6)

# Initialize the LED
led = LED(17)

# Initialize the GPIO pin for the flash
flash_pin = 18
pi.set_mode(flash_pin, pigpio.OUTPUT)

# Define function to take picture and trigger flash
def take_picture():
    while True:
        # Wait for motion to be detected
        pir.wait_for_motion()

        # Turn on the LED
        led.on()

        # Try to set autofocus mode to single-shot
        try:
            subprocess.check_call(["gphoto2", "--set-config", "/main/capturesettings/afmode=0"])
        except subprocess.CalledProcessError as e:
            print("Could not set autofocus mode:", e)

        # Try to start autofocus
        try:
            subprocess.check_call(["gphoto2", "--set-config", "/main/actions/autofocus=1"])
        except subprocess.CalledProcessError as e:
            print("Could not start autofocus:", e)

        # Wait for autofocus to lock
        print("Waiting for autofocus to lock...")
        subprocess.call(["gphoto2", "--wait-event", "5s", "--event-to-stdout", "--quiet"])

        # Press the shutter button fully to take the picture
        try:
            subprocess.check_call(["gphoto2", "--set-config", "/main/actions/eosremoterelease=4"])
        except subprocess.CalledProcessError as e:
            print("Could not press shutter button:", e)

        # Wait for the camera to start exposure
        time.sleep(0.01)

        # Try to get the shutter speed
        try:
            shutter_speed_output = subprocess.check_output(["gphoto2", "--get-config", "/main/capturesettings/shutterspeed"]).decode('utf-8').split(" ")[-1]
            shutter_speed = float(shutter_speed_output.strip().split('/')[0]) / float(shutter_speed_output.strip().split('/')[1])
        except (subprocess.CalledProcessError, ValueError) as e:
            print("Could not get shutter speed:", e)
            shutter_speed = 0

        if shutter_speed < 1/300:
            # Trigger the flash at the beginning of the exposure
            pi.write(flash_pin, 1)
            time.sleep(shutter_speed)
            pi.write(flash_pin, 0)
        else:
            # Trigger the flash near the end of the exposure
            time.sleep(shutter_speed * (299/300))
            pi.write(flash_pin, 1)
            time.sleep(shutter_speed * (1/300))
            pi.write(flash_pin, 0)

        # Turn off the LED
        led.off()

        # Wait for 1 second before taking the next picture
        time.sleep(1)

if __name__ == '__main__':
    try:
        # Call the take_picture function
        take_picture()
    except KeyboardInterrupt:
        # Clean up GPIO resources on keyboard interrupt
        print("\nCleaning up GPIO resources...")
        pir.close()
        led.close()
        pi.stop()
