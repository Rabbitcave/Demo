import pyautogui
import time

# Get the current mouse position
time.sleep(5)  # Wait for 5 seconds before capturing the position
x, y = pyautogui.position()
print(f"Mouse is at X={x}, Y={y}")