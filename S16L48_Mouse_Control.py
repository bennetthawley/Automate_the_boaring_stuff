import pyautogui

# Get current screen size and assign to variables
width, height = pyautogui.size()
print(width)
print(height)
# Get current mouse position coordinates
mouse_x, mouse_y = pyautogui.position()
print(mouse_x)
print(mouse_y)
# Move the mouse to a position
pyautogui.moveTo(10, 10, duration=1.5)
pyautogui.moveRel(200, 0, duration=2)
# Click the mouse at a specific position
pyautogui.click(200, 200)
pyautogui.doubleClick(300, 300)
