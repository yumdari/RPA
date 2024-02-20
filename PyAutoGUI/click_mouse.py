import pyautogui

# click current mouse cursor
pyautogui.click()

# click at 200, 200
pyautogui.click(200, 200)

# right click 2 times, interval is 0.2 secs
pyautogui.click(clicks=2, interval=0.2, button='right')