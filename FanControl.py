import os
import glob
import time
from gpiozero import PWMOutputDevice
import RPi.GPIO as GPIO

# Set the pin number to which the fan is connected
FAN_PIN = 18

# Set the temperature threshold at which the fan should turn on (in degrees Celsius)
TEMP_THRESHOLD = 40

# Set the maximum safe temperature for the processor (in degrees Celsius)
MAX_TEMP = 85

# Set the delay between temperature readings (in seconds)
DELAY_TIME = 5

# Set the minimum and maximum duty cycles for the fan (0 to 1)
MIN_DUTY_CYCLE = 0.2
MAX_DUTY_CYCLE = 1.0

# Initialize the fan and set its initial speed to 0 (off)
fan = PWMOutputDevice(FAN_PIN)
fan.value = 0

# Find the ds18b20 temperature sensor device ID
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
device_folder = glob.glob('/sys/bus/w1/devices/28*')[0]
device_file = device_folder + '/w1_slave'

# Function to read the temperature from the ds18b20 sensor
def read_temperature():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

# Function to set the fan speed based on the CPU temperature
def set_fan_speed():
    temperature = read_temperature()
    duty_cycle = (MAX_DUTY_CYCLE - MIN_DUTY_CYCLE) * ((temperature - TEMP_THRESHOLD) / (MAX_TEMP - TEMP_THRESHOLD)) + MIN_DUTY_CYCLE
    duty_cycle = min(max(duty_cycle, MIN_DUTY_CYCLE), MAX_DUTY_CYCLE)  # Ensure duty cycle is between MIN and MAX
    fan.value = duty_cycle

# Function to put the Raspberry Pi into standby mode
def standby_mode():
    GPIO.cleanup()
    os.system('sudo systemctl suspend')

# Main loop to read the temperature, control the fan, and check for standby mode
while True:
    temperature = read_temperature()
    if temperature >= TEMP_THRESHOLD:
        set_fan_speed()
    else:
        fan.value = 0
    if temperature >= MAX_TEMP:
        standby_mode()
    time.sleep(DELAY_TIME)
