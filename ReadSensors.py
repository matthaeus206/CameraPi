import glob
import time
import pigpio

# Set up pigpio
pi = pigpio.pi()

# Set up HC-SR501
PIR_PIN = 7
pi.set_mode(PIR_PIN, pigpio.INPUT)

# Set up HC-SR04
TRIG_PIN = 11
ECHO_PIN = 12
pi.set_mode(TRIG_PIN, pigpio.OUTPUT)
pi.set_mode(ECHO_PIN, pigpio.INPUT)

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
            pi.stop()
            exit()
        except:
            continue

# Function to read HC-SR501 sensor
def read_hcsr501():
    while True:
        try:
            return pi.read(PIR_PIN)
        except KeyboardInterrupt:
            pi.stop()
            exit()
        except:
            continue

# Function to read HC-SR04 sensor
def read_hcsr04():
    while True:
        try:
            pi.write(TRIG_PIN, 0)
            time.sleep(0.1)
            pi.write(TRIG_PIN, 1)
            time.sleep(0.00001)
            pi.write(TRIG_PIN, 0)

            while pi.read(ECHO_PIN)==0:
                pulse_start = time.time()
            while pi.read(ECHO_PIN)==1:
                pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start
            distance = pulse_duration * 17150
            return distance
        except KeyboardInterrupt:
            pi.stop()
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
        pi.stop()
        exit()
    except:
        continue
