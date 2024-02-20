import pyautogui

# 1초간 400, 400 위치로 이동 후, 절대 좌표 500, 500으로 2초간 드래그
pyautogui.click(400, 400, duration=1)
pyautogui.dragTo(500, 500, 2, button='left')

# 현재 마우스 위치 기준으로 300, 300 범위만큼 왼쪽으로 드래그
pyautogui.dragRel(300, 300, 2, button='left')