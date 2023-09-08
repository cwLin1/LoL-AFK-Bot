import cv2
import time
import numpy as np
from PIL import ImageGrab

import pydirectinput as P


def find_target(target):
    template = cv2.imread(target, cv2.IMREAD_GRAYSCALE)
    screen = np.array(ImageGrab.grab(bbox=(0, 0, 1920, 1080)))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc

    x = top_left[0] + w//2
    y = top_left[1] + h//2
    if max_val < 0.75:
        return -1, -1
    else:
        return x, y


# Game start
time.sleep(5)
while find_target('template/ingame.jpg') == (-1, -1):
    time.sleep(5)

print('Game start')
time.sleep(15)

P.mouseDown(960, 540, button = 'left')
P.mouseUp(960, 540, button = 'left')

# Purchase the item
P.keyDown('p')
P.keyUp('p')
time.sleep(0.1)
x, y = find_target('template/ward.jpg')

if (x, y) == (-1, -1):
    P.keyDown('p')
    P.keyUp('p')
    time.sleep(0.1)

P.mouseDown(x, y, button = 'right')
P.mouseUp(x, y, button = 'right')
P.mouseDown(x, y, button = 'right')
P.mouseUp(x, y, button = 'right')
P.keyDown('p')
P.keyUp('p')

time.sleep(0.1)
P.keyDown('ctrl')
P.keyDown('q')
P.keyUp('q')
P.keyUp('ctrl')

# Walk to the jungle
time.sleep(0.1)
# P.keyDown('y')
# P.keyUp('y')

P.mouseDown(1804, 1012, button = 'left')
P.mouseUp(1804, 1012, button = 'left')
P.mouseDown(1198, 479, button = 'right')
P.mouseUp(1198, 479, button = 'right')

time.sleep(60)

# AFK
# Place the ward
P.mouseDown(1804, 1012, button = 'left')
P.mouseUp(1804, 1012, button = 'left')
P.moveTo(878, 793)
P.keyDown('1')
P.keyUp('1')
P.keyDown('2')
P.keyUp('2')
P.keyDown('3')
P.keyUp('3')

while find_target('template/icon.jpg') != (-1, -1):
    P.mouseDown(1804, 1012, button = 'left')
    P.mouseUp(1804, 1012, button = 'left')
    P.mouseDown(707, 570, button = 'right')
    P.mouseUp(707, 570, button = 'right')
    time.sleep(5)
    P.keyDown('q')
    P.keyUp('q')
    P.mouseDown(1198, 479, button = 'right')
    P.mouseUp(1198, 479, button = 'right')
    time.sleep(25)

print('End')
print()
