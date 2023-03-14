#!/usr/bin/env python3
import subprocess
import time
from gpiozero import MotionSensor, DistanceSensor

# initialize the motion sensor
pir = MotionSensor(4)
# initialize the ultrasonic sensor
ultrasonic = DistanceSensor(echo=4, trigger=5)
def take_picture(filename):
    test = subprocess.Popen([
        "gphoto2",
        "--capture-image-and-download",
        "--filename", "/home/pi/Photos/"+filename],
        stdout=subprocess.PIPE)
    # run the subprocess and capture standard output
    output = test.communicate()[0]
    # print any messages for debugging
    print(output)
if __name__ == '__main__':
    # determine if the sensor was activated
    # pir.wait_for_motion()
    while True:
        # get the distance reading from the sensor distance
        distance = ultrasonic.distance * 100
        print('Distance: ', distance)
        # take the picture if something is close enough
        if distance < 10:
            # set the filename to the current time
            filename = time.strftime("%Y%M%D-%H%M%S.JPG")
            # TAKE THE PICTURE
            take_picture(filename)
            break
        time.sleep(1)