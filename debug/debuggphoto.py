import os
from gpiozero import MotionSensor
import time

pir = MotionSensor(6)

while True:
    if pir.motion_detected:
        print("Motion detected")
        os.system("gphoto2 --capture-image-and-download --filename '/store_00010001/DCIM/100CANON/%Y%m%d-%H%M%S.%C'")
    time.sleep(5)
