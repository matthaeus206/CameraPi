import subprocess

# Run gphoto2 with the --list-config option to get a list of all available configuration options
output = subprocess.check_output(["gphoto2", "--list-config"])

# Split the output into individual lines
lines = output.decode('utf-8').split("\n")

# Define a list of configuration groups to include
config_groups = ["iso", "shutterspeed", "aperture", "imagequality", "whitebalance"]

# Iterate over each line and check if it belongs to a relevant configuration group
for line in lines:
    if line.startswith("/"):
        config_option = line.strip()
        config_group = config_option.split("/")[-2]
        if config_group in config_groups:
            try:
                # Use the --get-config-value option to get the current value of the configuration option
                value = subprocess.check_output(["gphoto2", "--get-config-value", config_option]).decode('utf-8').strip()
            except subprocess.CalledProcessError:
                value = "N/A"
            print(config_option + ": " + value)
