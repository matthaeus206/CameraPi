import time
import board
import digitalio

# Set up motion sensor
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
  # Trigger flash
  flash_trigger.value = True
  time.sleep(0.1)
  flash_trigger.value = False

  # Trigger camera
  camera_trigger.value = True
  time.sleep(0.05)
  camera_trigger.value = False

# Main loop
while True:
  try:
    # Check for motion
    if pir_sensor.value:
      # Trigger flash and camera
      trigger_flash_and_camera()

      # Wait for cooldown
      time.sleep(1)
  except Exception as e:
    print(f"An error occurred: {e}")
    # Log error or take corrective action

# Clean up resources
with contextlib.ExitStack() as stack:
  stack.enter_context(flash_trigger)
  stack.enter_context(camera_trigger)
