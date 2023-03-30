import subprocess
import re
import time

while True:
    # Check for undervoltage
    voltage_output = subprocess.check_output(['vcgencmd', 'measure_volts', 'core'])
    voltage = float(voltage_output.decode().split('=')[1].split('V')[0])
    if voltage < 4.65:
        print("Warning: undervoltage detected!")

    # Check for overtemperature
    temp_output = subprocess.check_output(['vcgencmd', 'measure_temp'])
    temp = float(temp_output.decode().split('=')[1].split("'")[0])
    if temp > 80.0:
        print("Warning: overtemperature detected!")

    # Check for high CPU usage
    cpu_output = subprocess.check_output(['top', '-bn1'])
    cpu_usage_str = re.search(r'%Cpu\(s\):.*?(\d+\.\d+) us', cpu_output.decode(), flags=re.DOTALL).group(1)
    cpu_usage = float(cpu_usage_str)
    if cpu_usage > 90.0:
        print("Warning: high CPU usage detected!")

    # Wait 10 seconds before checking again
    time.sleep(10)
