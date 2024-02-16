import pyautogui

# 절대 좌표로 이동

pyautogui.moveTo(100, 100)
pyautogui.moveTo(200, 200, duration = 0.5)

# 상대 좌표로 이동

pyautogui.move(100, 100, duration = 1)