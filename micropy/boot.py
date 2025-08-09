import time
import board
import digitalio
import microcontroller
from watchdog import WatchDogMode

# ---- Pin map (RP2040-Zero) ----
PIR_PIN    = board.GP6
FLASH_PIN  = board.GP7
CAM_PIN    = board.GP5

# ---- Tunables ----
COOLDOWN_S           = 1.0   # ignore retriggers for this long after a fire
FLASH_PULSE_S        = 0.010 # 10 ms flash pulse
CAMERA_PULSE_S       = 0.050 # 50 ms camera pulse
FLASH_TO_CAMERA_S    = 0.000 # delay between flash and camera (set >0 if needed)

# ---- Watchdog (optional, safe defaults) ----
microcontroller.watchdog.timeout = 8.0
microcontroller.watchdog.mode = WatchDogMode.RESET

# ---- PIR input ----
pir = digitalio.DigitalInOut(PIR_PIN)
pir.direction = digitalio.Direction.INPUT
# Enable only if your PIR output floats. Most PIR modules drive the line themselves.
# pir.pull = digitalio.Pull.DOWN

# ---- Outputs ----
flash = digitalio.DigitalInOut(FLASH_PIN)
flash.direction = digitalio.Direction.OUTPUT
flash.value = False

camera = digitalio.DigitalInOut(CAM_PIN)
camera.direction = digitalio.Direction.OUTPUT
camera.value = False

def pulse(pin: digitalio.DigitalInOut, duration_s: float) -> None:
    pin.value = True
    time.sleep(duration_s)
    pin.value = False

def trigger_flash_and_camera() -> None:
    # Fire flash (short pulse), optional inter-pulse delay, then camera
    pulse(flash, FLASH_PULSE_S)
    if FLASH_TO_CAMERA_S > 0:
        time.sleep(FLASH_TO_CAMERA_S)
    pulse(camera, CAMERA_PULSE_S)

def main():
    last_state = False
    last_fire_t = 0.0

    while True:
        microcontroller.watchdog.feed()
        state = pir.value

        # Rising edge detection
        if state and not last_state:
            now = time.monotonic()
            if now - last_fire_t >= COOLDOWN_S:
                # print kept minimal to avoid serial latency jitter
                # print("Motion: trigger")
                trigger_flash_and_camera()
                last_fire_t = now
            # else: print("Motion ignored (cooldown)")

        last_state = state
        # Short sleep avoids tight CPU loops while staying responsive
        time.sleep(0.005)

try:
    main()
except Exception as e:
    # Minimal crash handler; expand if you want file logging
    # (import traceback; traceback.print_exception(e))
    while True:
        pass  # watchdog will reset
