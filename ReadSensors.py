import os
import glob
import time
import RPi.GPIO as GPIO

# Set up GPIO pins
GPIO.setmode(GPIO.BOARD)

# Set up HC-SR501
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)

# Set up HC-SR04
TRIG_PIN = 11
ECHO_PIN = 12
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

# Function to read DSD18B20 sensor
def read_ds18b20():
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'
    while True:
        try:
            with open(device_file, 'r') as f:
                lines = f.readlines()
                if lines[0].strip()[-3:] == 'YES':
                    temp_pos = lines[1].find('t=')
                    if temp_pos != -1:
                        temp_string = lines[1][temp_pos+2:]
                        temp_c = float(temp_string) / 1000.0
                        return temp_c
                else:
                    continue
        except KeyboardInterrupt:
            GPIO.cleanup()
            exit()
        except:
            continue

# Function to read HC-SR501 sensor
def read_hcsr501():
    while True:
        try:
            return GPIO.input(PIR_PIN)
        except KeyboardInterrupt:
            GPIO.cleanup()
            exit()
        except:
            continue

# Function to read HC-SR04 sensor
def read_hcsr04():
    while True:
        try:
            GPIO.output(TRIG_PIN, False)
            time.sleep(0.1)
            GPIO.output(TRIG_PIN, True)
            time.sleep(0.00001)
            GPIO.output(TRIG_PIN, False)

            while GPIO.input(ECHO_PIN)==0:
                pulse_start = time.time()
            while GPIO.input(ECHO_PIN)==1:
                pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start
            distance = pulse_duration * 17150
            return distance
        except KeyboardInterrupt:
            GPIO.cleanup()
            exit()
        except:
            continue

# Main loop
while True:
    try:
        # Read sensor data
        temp = read_ds18b20()
        pir = read_hcsr501()
        dist = read_hcsr04()

        # Print data to terminal
        print("Temperature: {:.2f} C".format(temp))
        print("PIR Sensor: {}".format(pir))
        print("Distance: {:.2f} cm".format(dist))

        # Wait for next iteration
        time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()
    except:
        continue
