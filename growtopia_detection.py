# imports
import os
import cv2
import win32gui
import numpy as np
from PIL import ImageGrab

#import win32process
#import pyautogui as pag


#door = pag.locateOnScreen(os.path.join(os.getcwd(),'blocks/door.png'))

#print(door)

win32gui.SetForegroundWindow(win32gui.FindWindow(None, 'Growtopia'))

item = cv2.imread(os.path.join(os.getcwd(), 'blocks/rock.png'), 0)

while True:
    dimensions = win32gui.GetWindowRect(win32gui.FindWindow(None, 'Growtopia'))
    screen = np.array(ImageGrab.grab(dimensions, all_screens=True))
    gray_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(gray_screen, item, cv2.TM_CCOEFF_NORMED)
    
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    print(max_loc)
    print(max_val)
    
    threshold = 0.80
    
    locations = np.where(result > threshold)
    locations = list(zip(*locations[::-1]))
    
    if locations:
        
        w = item.shape[0]
        h = item.shape[1]
        
        for loc in locations:
            # Determine the box positions
            top_left = loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            # Draw the box
            cv2.rectangle(screen, top_left, bottom_right, color=(0, 255, 0), thickness=1, lineType=cv2.LINE_4)
        cv2.imshow('Result', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    else:
        cv2.imshow('Result', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    #cv2.imshow('Result', result)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
