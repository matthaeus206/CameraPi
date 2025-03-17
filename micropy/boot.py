import time
import board
import digitalio

# Set up motion sensor (PIR)
pir_sensor = digitalio.DigitalInOut(board.GP6)
pir_sensor.direction = digitalio.Direction.INPUT

# Set up flash trigger transistor
flash_trigger = digitalio.DigitalInOut(board.GP7)
flash_trigger.direction = digitalio.Direction.OUTPUT

# Set up camera trigger transistor
camera_trigger = digitalio.DigitalInOut(board.GP5)
camera_trigger.direction = digitalio.Direction.OUTPUT

# Define a function to trigger the flash and camera
def trigger_flash_and_camera():
    print("Motion detected! Triggering flash and camera...")
    
    # Trigger flash (shorter pulse)
    flash_trigger.value = True
    time.sleep(0.01)  # Shorter duration for responsive flash
    flash_trigger.value = False

    # Trigger camera (slightly longer pulse)
    camera_trigger.value = True
    time.sleep(0.05)  # Ensures the camera registers the trigger
    camera_trigger.value = False

# Main loop
try:
    last_trigger_time = 0  # Timestamp for debouncing

    while True:
        if pir_sensor.value:  # Motion detected
            current_time = time.monotonic()
            if current_time - last_trigger_time > 1:  # 1-second debounce
                trigger_flash_and_camera()
                last_trigger_time = current_time

except KeyboardInterrupt:
    print("Exiting...")

finally:
    print("Cleaning up...")
    # CircuitPython automatically handles GPIO cleanup on exit
