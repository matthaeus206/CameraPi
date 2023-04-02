import subprocess

# Define the configuration options we want to get the current values for
config_options = [
    "/main/capturesettings/capturemode",
    "/main/imgsettings/iso",
    "/main/capturesettings/shutterspeed",
    "/main/capturesettings/aperture"
]

try:
    # Iterate over each configuration option and print its current value
    for config_option in config_options:
        try:
            # Use the --get-config-value option to get the current value of the configuration option
            value = subprocess.check_output(["gphoto2", "--get-config-value", config_option]).decode('utf-8').strip()
        except subprocess.CalledProcessError:
            value = "N/A"
        print(config_option + ": " + value)

    # Write the output to a text file in the same directory as the script
    with open("camera_settings.txt", "w") as f:
        for config_option in config_options:
            try:
                value = subprocess.check_output(["gphoto2", "--get-config-value", config_option]).decode('utf-8').strip()
            except subprocess.CalledProcessError:
                value = "N/A"
            f.write(config_option + ": " + value + "\n")

    print("Settings written to camera_settings.txt")
except Exception as e:
    print("Error: " + str(e))
