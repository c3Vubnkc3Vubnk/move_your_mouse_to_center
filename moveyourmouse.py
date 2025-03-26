import pyautogui
import time
time.sleep(1)
pyautogui.press('shift')
time.sleep(1)
# 获取屏幕分辨率
screen_width, screen_height = pyautogui.size()

# 计算中心位置
center_x, center_y = screen_width // 2, screen_height // 2

# 移动鼠标到屏幕中心
pyautogui.moveTo(center_x, center_y, duration=0.1)