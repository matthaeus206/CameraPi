import os
import glob
import time

# Define the path to the DS18B20 sensor
DS18B20_PATH = '/sys/bus/w1/devices/28-*/w1_slave'

# Initialize the DS18B20 sensor
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

# Loop forever
while True:
    try:
        # Read the CPU temperature
        cpu_temp = os.popen('vcgencmd measure_temp').readline()
        cpu_temp = cpu_temp.replace('temp=', '').replace('\'C\n', '')
        
        # Read the external temperature
        sensor_path = glob.glob(DS18B20_PATH)[0]
        with open(sensor_path, 'r') as f:
            lines = f.readlines()
        temp = float(lines[1].split('=')[1]) / 1000
        
        # Print the temperatures
        print(f'CPU Temperature: {cpu_temp}\'C')
        print(f'External Temperature: {temp}\'C')
        
        # Wait 1 minute before reading again
        time.sleep(60)
    except KeyboardInterrupt:
        # Stop the loop if Ctrl+C is pressed
        break
