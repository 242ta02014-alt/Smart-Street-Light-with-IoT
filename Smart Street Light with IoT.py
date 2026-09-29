# Smart Street Light with IoT
# Easy Python Code

import random
import time

while True:

    # Simulate LDR sensor
    light = random.randint(0, 100)

    print("\n--- IoT STREET LIGHT ---")
    print("Light Intensity:", light)

    # Automatic control
    if light < 40:
        print("Street Light: ON")
        status = "ON"
    else:
        print("Street Light: OFF")
        status = "OFF"

    # IoT monitoring
    print("IoT Status:", status)

    time.sleep(3)
