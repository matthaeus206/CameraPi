import subprocess

# Run gphoto2 with the --list-config option to get a list of all available configuration options
output = subprocess.check_output(["gphoto2", "--list-config"])

# Split the output into individual lines
lines = output.decode('utf-8').split("\n")

# Define the configuration options we are interested in
iso_config = "/main/capturesettings/iso"
shutter_speed_config = "/main/capturesettings/shutterspeed"

# Iterate over each line and print the current value for the ISO and shutter speed options
for line in lines:
    if line.startswith(iso_config):
        try:
            # Use the --get-config-value option to get the current value of the ISO option
            iso_value = subprocess.check_output(["gphoto2", "--get-config-value", iso_config]).decode('utf-8').strip()
        except subprocess.CalledProcessError:
            iso_value = "N/A"
        print("Current ISO: " + iso_value)
    elif line.startswith(shutter_speed_config):
        try:
            # Use the --get-config-value option to get the current value of the shutter speed option
            shutter_speed_value = subprocess.check_output(["gphoto2", "--get-config-value", shutter_speed_config]).decode('utf-8').strip()
        except subprocess.CalledProcessError:
            shutter_speed_value = "N/A"
        print("Current Shutter Speed: " + shutter_speed_value)
