import os

while True:
    # Display menu prompt
    print("Which debug script do you want to run?")
    print("1. Test current camera configs")
    print("2. Test ultrasonic distance sensor")
    print("3. Test camera")
    print("4. Test HC-SR501 motion sensor")
    print("5. Test undervoltage")
    print("6. Test camera trigger")
    print("7. Test Temps")
    print("0. Exit")

    choice = input("Enter your choice (0-7): ")

    # Run selected debug script
    if choice == "1":
        os.system("python3 cameraconfigs.py")
    elif choice == "2":
        os.system("python3 debugdistance.py")
    elif choice == "3":
        os.system("python3 debuggphoto.py")
    elif choice == "4":
        os.system("python3 debugmotion.py")
    elif choice == "5":
        os.system("python3 debugpower.py")
    elif choice == "6":
        os.system("python3 debugtransistors.py")
    elif choice == "7":
        os.system("python3 debugtemp.py")
    elif choice == "0":
        break
