from gpiozero import Button
import os

# Create a new button object with a hold time of 3 seconds
button = Button(pin="GPIO17", hold_time=3)

# Define a function to turn off the Raspberry Pi when the button is held down
def shutdown():
    try:
        os.system("sudo shutdown now")
    except Exception as e:
        print("Error during shutdown:", e)

# Add an event listener to the button object to call the shutdown function when the button is held down
button.when_held = shutdown

# Keep the script running to continuously listen for button presses
while True:
    pass
