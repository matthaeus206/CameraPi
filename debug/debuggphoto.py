import os
import time
from gpiozero import MotionSensor

while True:
    pir = MotionSensor(6)
    if pir.motion_detected:
        os.system("gphoto2 --capture-image-and-download --filename /store_00010001/DCIM/100CANON/%Y%m%d-%H%M%S.%C")
    time.sleep(1)
