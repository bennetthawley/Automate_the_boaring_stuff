import pyautogui

# Send keypress to active window
pyautogui.typewrite('Hello World', interval=0.1)
pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'], interval=0.1)
pyautogui.press('f1')
pyautogui.hotkey('ctrl', 'o')
