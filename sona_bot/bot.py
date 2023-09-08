import cv2
import time
import numpy as np
from PIL import ImageGrab
from datetime import datetime

import pydirectinput as P

GAMEMODE = 1
# 0: intro, 1: beginner, intermediate

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

n = int(input("Number of games: "))
print()

x, y = find_target('template/queue.jpg')
if (x, y) != (-1, -1):
    P.mouseDown(x, y, button = 'left')
    P.mouseUp(x, y, button = 'left')

    for i in range(n):
        print('*** Game', i+1, '***')
        game_start = False
        while not game_start:
            print('[{}]:'.format(datetime.now().strftime("%H:%M:%S")), 'Queuing...')
            x, y = find_target('template/queue.jpg')
            if (x, y) != (-1, -1):
                P.mouseDown(x, y, button = 'left')
                P.mouseUp(x, y, button = 'left')
            # Queuing
            st = time.time()
            while find_target('template/accept.jpg') == (-1, -1):
                time.sleep(1)
                if time.time() - st > 110:
                    st = time.time()
                    x, y = find_target('template/queue.jpg')
                    if (x, y) != (-1, -1):
                        P.mouseDown(x, y, button = 'left')
                        P.mouseUp(x, y, button = 'left')
                        print('[{}]:'.format(datetime.now().strftime("%H:%M:%S")), 'Queuing...')

            print('[{}]:'.format(datetime.now().strftime("%H:%M:%S")), 'Match Found!')
            x, y = find_target('template/accept.jpg')
            P.mouseDown(x, y, 'left')
            P.mouseUp(x, y, 'left')

            # Champion Select
            st = time.time()
            while find_target('template/sona.jpg') == (-1, -1) and time.time() - st < 15:
                time.sleep(0.5)
            if find_target('template/sona.jpg') != (-1, -1):
                print('[{}]:'.format(datetime.now().strftime("%H:%M:%S")), 'Champion Selection')
                x, y = find_target('template/sona.jpg')
                P.mouseDown(x, y, button = 'left')
                P.mouseUp(x, y, button = 'left')
                x, y = find_target('template/lock.jpg')
                P.mouseDown(x, y, button = 'left')
                P.mouseUp(x, y, button = 'left')
                time.sleep(0.5)

                st = time.time()
                # Loading
                while find_target('template/loading.jpg') == (-1, -1) and time.time() - st < 120:
                    time.sleep(0.5)
                if find_target('template/loading.jpg') != (-1, -1):
                    print('[{}]:'.format(datetime.now().strftime("%H:%M:%S")), 'Loading...')
                    game_start = True

        # Game start
        time.sleep(5)
        while find_target('template/ingame.jpg') == (-1, -1):
            time.sleep(5)

        print('[{}]:'.format(datetime.now().strftime("%H:%M:%S")), 'Game Start')
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
        if GAMEMODE == 0:
            P.keyDown('y')
            P.keyUp('y')

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
            P.mouseDown(1804, 1012, button = 'left')
            P.mouseUp(1804, 1012, button = 'left')
            P.mouseDown(1198, 479, button = 'right')
            P.mouseUp(1198, 479, button = 'right')
            time.sleep(25)

        print('[{}]:'.format(datetime.now().strftime("%H:%M:%S")), 'End')

        # End
        time.sleep(20)
        x, y = find_target('template/skip_res.jpg')
        P.mouseDown(x, y, button = 'left')
        P.mouseUp(x, y, button = 'left')

        time.sleep(5)
        while find_target('template/reward.jpg') != (-1, -1):
            x, y = find_target('template/reward.jpg')
            P.mouseDown(x, y, button = 'left')
            P.mouseUp(x, y, button = 'left')

        time.sleep(5)
        print('[{}]:'.format(datetime.now().strftime("%H:%M:%S")), 'Continue')
        print()

        x, y = find_target('template/continue.jpg')
        if i < n-1:
            P.mouseDown(x, y, button = 'left')
            P.mouseUp(x, y, button = 'left')
            P.mouseDown(x, y, button = 'left')
            P.mouseUp(x, y, button = 'left')
            P.mouseDown(x, y, button = 'left')
            P.mouseUp(x, y, button = 'left')
