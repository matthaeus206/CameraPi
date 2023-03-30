from gpiozero import DistanceSensor
import time

sensor = DistanceSensor(echo=4, trigger=5)

while True:
    print("Distance: {:.2f} cm".format(sensor.distance * 100))
    time.sleep(0.5)
