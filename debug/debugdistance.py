import board
import time
import adafruit_hcsr04
import digitalio

led = digitalio.DigitalInOut(board.GP7)
led.direction = digitalio.Direction.OUTPUT

while True:
    try:
        sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP3, echo_pin=board.GP4)
        distance = sonar.distance
        print("Distance: ", distance, "cm")
        if distance < 10:
            led.value = True
        else:
            led.value = False
    except RuntimeError as e:
        print("Error: ", e)
    finally:
        time.sleep(0.1)  # pause for a bit
        sonar.deinit() # clean up pins
