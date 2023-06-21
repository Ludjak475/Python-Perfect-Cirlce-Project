import pyautogui
import cv2
import numpy as np
import time
template = cv2.imread('template.png', cv2.IMREAD_GRAYSCALE)
template2 = cv2.imread('DFC.png', cv2.IMREAD_GRAYSCALE)
template3 = cv2.imread('thirdcap.png', cv2.IMREAD_GRAYSCALE)
threshold = 0.9
pyautogui.PAUSE = 0.01
while True:
    screen = pyautogui.screenshot()
    screen_gray = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2GRAY)
    result = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
    _, max_val1, _, _ = cv2.minMaxLoc(result)
    result2 = cv2.matchTemplate(screen_gray, template2, cv2.TM_CCOEFF_NORMED)
    _, max_val2, _, _ = cv2.minMaxLoc(result2)
    result3 = cv2.matchTemplate(screen_gray, template3, cv2.TM_CCOEFF_NORMED)
    _, max_val3, _, _ = cv2.minMaxLoc(result3)
    if max_val1 >= threshold or max_val2>= threshold or max_val3>= threshold:
        break
    time.sleep(1)
screen_width, screen_height = pyautogui.size()
center_x = (screen_width // 2)
center_y = (screen_height // 2)
radius = 430
points = []
for angle in range(0, 367, 5):
    radian = np.radians(angle)
    x = int(center_x + radius * np.cos(radian))
    y = int(center_y + radius * np.sin(radian))
    points.append((x, y))
pyautogui.moveTo(points[0])
pyautogui.mouseDown()
for point in points:
    pyautogui.moveTo(point, duration=0.01)
pyautogui.mouseUp()
time.sleep(2)
