import time
import random
import pyautogui
from pynput import mouse, keyboard
from pynput.mouse import Controller as MouseController
from datetime import datetime


activity_detected = False
last_activity_time = time.time()

# Initialize mouse controller
mouse_controller = MouseController()

def on_move(x, y):
    global activity_detected, last_activity_time
    activity_detected = True
    last_activity_time = time.time()
    # print(f"Mouse moved to ({x}, {y})")

def on_click(x, y, button, pressed):
    global activity_detected, last_activity_time
    activity_detected = True
    last_activity_time = time.time()
    # print(f"Mouse {'pressed' if pressed else 'released'} at ({x}, {y})")

def on_scroll(x, y, dx, dy):
    global activity_detected, last_activity_time
    activity_detected = True
    last_activity_time = time.time()
    # print(f"Mouse scrolled at ({x}, {y}) with delta ({dx}, {dy})")

def on_press(key):
    global activity_detected, last_activity_time
    activity_detected = True
    last_activity_time = time.time()
    # print(f"Key {key} pressed")

def on_release(key):
    global activity_detected, last_activity_time
    activity_detected = True
    last_activity_time = time.time()
    # print(f"Key {key} released")

# Setup the listeners
mouse_listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
keyboard_listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)

mouse_listener.start()
keyboard_listener.start()

try:
    while True:
        current_time = time.time()
        current_timet = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(current_timet)
        if current_time - last_activity_time >= 10:
            # Move mouse randomly
            # screen_width, screen_height = mouse_controller.screen_sizedafasdfçlkjqwerpoiuasdçflkjqwer
            x = random.randint(0, pyautogui.size()[0])
            y = random.randint(0, pyautogui.size()[1])
            pyautogui.moveTo(x, y, duration=0.5)

            current_timet = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Current Time: {current_timet}" + f"Mouse moved to ({x}, {y}) due to inactivity")
            # Reset last activity time to avoid continuous movement
            last_activity_time = current_time
        time.sleep(120)
except KeyboardInterrupt:
    print("Program terminated by user")

mouse_listener.stop()
keyboard_listener.stop()
    