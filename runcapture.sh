#!/bin/bash

# Check if the Canon camera is connected
if lsusb | grep -q "Canon, Inc. Canon Digital Camera"; then
    # Kill any running gphoto2 process
    pkill -f gphoto2

    # Start pigpiod daemon
    sudo pigpiod

    # Run CaptureWithFlash.py script
    python ~/CameraPi/CaptureWithFlash.py
fi
