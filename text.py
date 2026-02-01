import subprocess
import sys
import time
packages = ['pywinauto', 'pywin32', 'comtypes', 'pyautogui']
print("Checking dependencies...")

try:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + packages)
except subprocess.CalledProcessError as e:
    print(f"Error installing packages: {e}")
    sys.exit(1)

print("All dependencies installed.")

import pyautogui
import os

# --- CONFIG ---
CLICK_X, CLICK_Y = 1100, 725
WAIT_TIME = 30
SCREENSHOT_DIR = "screenshots"

os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def take_screenshot(name):
    path = os.path.join(SCREENSHOT_DIR, name)
    pyautogui.screenshot(path)
    print(f"Screenshot saved: {path}")

print("Dependencies installed.")
take_screenshot("01_after_install.png")

second_path = os.path.join(os.getcwd(), "install-2.exe")

if not os.path.exists(second_path):
    print(f"Error: second_path file not found at {second_path}")
    sys.exit(1)

print("Launching Second...")
subprocess.Popen(second_path, shell=True)
time.sleep(5)  # short delay to let window appear
take_screenshot("10_after_launching_second.png")
pyautogui.press('tab')
time.sleep(1)
pyautogui.write("7mnLplvIH/Ndjgd0eEvFZDkbJUql0ueyPT11KXiWNCc=")
take_screenshot("11_after_adding_url.png")
