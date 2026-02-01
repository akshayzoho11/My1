import subprocess
import sys
import time
import os
packages = ['pywinauto', 'pywin32', 'comtypes', 'pyautogui']
print("Checking dependencies...")

try:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + packages)
except subprocess.CalledProcessError as e:
    print(f"Error installing packages: {e}")
    sys.exit(1)

print("All dependencies installed.")

from pywinauto import Application
from pywinauto.keyboard import send_keys

second_path = os.path.join(os.getcwd(), "install-2.exe")

if not os.path.exists(second_path):
    print(f"Error: second_path file not found at {second_path}")
    sys.exit(1)

print("Launching Second...")

# Launch the application
app = Application(backend="uia").start(second_path)

# Wait for the main window to appear
time.sleep(5)
take_screenshot("10_after_launching_second.png")
# Connect to the top window
dlg = app.top_window()
dlg.wait("visible", timeout=15)

# Optional: print controls for debugging
dlg.print_control_identifiers()

# -----------------------------
# 1️⃣ Find the text box and type token
# -----------------------------
token = "zPeYuQdg5Dj0UsxrGv038ARbngn+Tnwo8y6Y7S8iJ3w="

# Most apps expose the input as an Edit control
edit = dlg.child_window(control_type="Edit")
edit.wait("ready", timeout=10)

edit.set_focus()
edit.type_keys(token, with_spaces=True)
take_screenshot("11_after_adding_url.png")
# -----------------------------
# 2️⃣ Press Enter OR click button
# -----------------------------

# Option A: Press Enter
send_keys("{ENTER}")

# Option B (better): Click "Start Earning" button if Enter doesn't work
# btn = dlg.child_window(title="Start Earning", control_type="Button")
# btn.wait("enabled", timeout=10)
# btn.click_input()
take_screenshot("12_after_pressing_enter.png")
print("Token entered and submitted.")
