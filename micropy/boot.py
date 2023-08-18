import time
import board
import digitalio

# Set up HC-SR501 PIR Infrared Motion Sensor
pir_sensor = digitalio.DigitalInOut(board.GP6)
pir_sensor.direction = digitalio.Direction.INPUT

# Set up flash trigger transistor
flash_trigger = digitalio.DigitalInOut(board.GP7)
flash_trigger.direction = digitalio.Direction.OUTPUT

# Set up camera trigger transistor
camera_trigger = digitalio.DigitalInOut(board.GP5)
camera_trigger.direction = digitalio.Direction.OUTPUT

# Main loop
while True:
    try:
        # Check for motion
        if pir_sensor.value:
            # Trigger flash
            flash_trigger.value = True
            time.sleep(0.1)
            flash_trigger.value = False

            # Trigger camera 
            camera_trigger.value = True
            time.sleep(0.1)
            camera_trigger.value = False

            # Wait for cooldown
            time.sleep(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        # Log error or take corrective action
