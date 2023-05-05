import time
import board
import digitalio

# Set up motion sensor
pir = digitalio.DigitalInOut(board.GP6)
pir.direction = digitalio.Direction.INPUT

# Set up transistors to trigger flash
flash1 = digitalio.DigitalInOut(board.GP5)
flash1.direction = digitalio.Direction.OUTPUT
flash1.value = False

flash2 = digitalio.DigitalInOut(board.GP7)
flash2.direction = digitalio.Direction.OUTPUT
flash2.value = False

# Set initial time for triggering flash
flash_time = time.monotonic()

while True:
    if pir.value:
        print("Motion detected!")
        if time.monotonic() - flash_time >= 1:
            flash1.value = True
            flash2.value = True
            time.sleep(0.1)
            flash1.value = False
            flash2.value = False
            # Update flash time
            flash_time = time.monotonic()
    time.sleep(0.1)

    # Clean up pins
    pir.deinit()
    flash1.deinit()
    flash2.deinit()
    time.sleep(0.1)
    pir = digitalio.DigitalInOut(board.GP6)
    pir.direction = digitalio.Direction.INPUT
    flash1 = digitalio.DigitalInOut(board.GP5)
    flash1.direction = digitalio.Direction.OUTPUT
    flash1.value = False
    flash2 = digitalio.DigitalInOut(board.GP7)
    flash2.direction = digitalio.Direction.OUTPUT
    flash2.value = False
