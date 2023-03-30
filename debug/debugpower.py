import time

while True:
    # Check for lightning bolt symbol
    if open('/sys/devices/platform/soc/soc:firmware/get_throttled').read().split()[0] != '0':
        print("Lightning bolt symbol detected")

    # Check for blinking red LED
    with open('/sys/class/leds/led1/trigger', 'r+') as trigger_file:
        if trigger_file.read().startswith('heartbeat'):
            print("Blinking red LED detected")

    # Check for instability or crashes
    print("If the Raspberry Pi is freezing or crashing frequently, it may be a sign of undervoltage.")

    # Wait 10 seconds before checking again
    time.sleep(10)
