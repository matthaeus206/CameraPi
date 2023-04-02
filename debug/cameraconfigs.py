import subprocess

# Run gphoto2 with the --list-config option to get a list of all available configuration options
output = subprocess.check_output(["gphoto2", "--list-config"])

# Split the output into individual lines
lines = output.decode('utf-8').split("\n")

# Iterate over each line and print the current configuration value for each option
for line in lines:
    if line.startswith("/"):
        config_option = line.strip()
        try:
            # Use the --get-config-value option to get the current value of the configuration option
            value = subprocess.check_output(["gphoto2", "--get-config-value", config_option]).decode('utf-8').strip()
        except subprocess.CalledProcessError:
            value = "N/A"
        print(config_option + ": " + value)
