import RPi.GPIO as GPIO
import time

# Set up GPIO pins
flash_pin = 18
half_press_pin = 23
full_press_pin = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(flash_pin, GPIO.OUT)
GPIO.setup(half_press_pin, GPIO.OUT)
GPIO.setup(full_press_pin, GPIO.OUT)

try:
    # Display menu prompt
    print("Which transistor do you want to test?")
    print("1. Flash transistor")
    print("2. Half press transistor")
    print("3. Full press transistor")
    choice = int(input("Enter your choice (1-3): "))

    # Test selected transistor
    if choice == 1:
        print("Testing flash transistor...")
        GPIO.output(flash_pin, True)
        time.sleep(0.5)
        GPIO.output(flash_pin, False)
        print("Flash transistor test complete!")
    elif choice == 2:
        print("Testing half press transistor...")
        GPIO.output(half_press_pin, True)
        time.sleep(0.5)
        GPIO.output(half_press_pin, False)
        print("Half press transistor test complete!")
    elif choice == 3:
        print("Testing full press transistor...")
        GPIO.output(full_press_pin, True)
        time.sleep(0.5)
        GPIO.output(full_press_pin, False)
        print("Full press transistor test complete!")
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")

except KeyboardInterrupt:
    GPIO.cleanup()
