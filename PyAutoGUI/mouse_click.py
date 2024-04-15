import pyautogui

# 단순 클릭
pyautogui.click()

# 해당 위치에서 클릭
pyautogui.click(200, 200)

# 해당 위치에서 2번 클릭, 클릭 간격은 0.2초, 마우스는 오른쪽 버튼
# middle, right, left 선택 가능
# button 옵션 default는 왼쪽.
pyautogui.click(clicks=2, interval=0.2, button='right')

#
pyautogui.click(x=None, y=None, clicks=1, interval=0, button='left',
               duration=0, tween=linear, logScreenshot=None, _pause=True)