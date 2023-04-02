import subprocess

# Define the capture settings to be listed
capture_settings = ['aperture', 'shutterspeed', 'iso', 'imageformat', 'imagequality']

# Run gphoto2 with the --list-config option to get a list of all available configuration options
output = subprocess.check_output(["gphoto2", "--list-config"])

# Split the output into individual lines
lines = output.decode('utf-8').split("\n")

# Iterate over each line and print the current configuration value for each capture setting
for line in lines:
    if line.startswith("/main/capturesettings/"):
        config_option = line.strip()
        setting_name = config_option.split("/")[-1]
        if setting_name in capture_settings:
            try:
                # Use the --get-config-value option to get the current value of the capture setting
                value = subprocess.check_output(["gphoto2", "--get-config-value", config_option]).decode('utf-8').strip()
            except subprocess.CalledProcessError:
                value = "N/A"
            print(setting_name + ": " + value)
