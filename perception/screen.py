from PIL import ImageGrab
import pyautogui
import sys
import os
import cv2
import numpy as np

#Define the function to take a screenshot
def screenGrab(window_name):
    """
    Takes a screenshot from chrome window and retuns coordinates of window
    Parameters:
        window_name: name of the window to take screenshot
    Returns:
        x, y, width, height: coordinates of the window
    """
    #get OS type 
    os_type = sys.platform
    import pygetwindow as gw
    #Get the window coordinates
    x1,y1,width,height = gw.getWindowGeometry(window_name)
    return x1,y1,width,height 

#Define the function to save the screenshot
def screenSave(x1,y1,width,height,path):
    """
    Takes a screenshot from chrome window and saves it to the path
    Parameters:
        x1,y1,width,height: coordinates of the window
        path: path to save the screenshot
    Returns:
        None
    """
    #get OS type 
    os_type = sys.platform
    #Take the screenshot
    bbox = (x1,y1,x1+width,y1+height)
    img = ImageGrab.grab(bbox=bbox)
    #Save the screenshot
    img.save(path)
    return None

#Define the function to get area of the canvas
def getCanvas():
    """
    Takes a screenshot from chrome window and saves it to the path
    Parameters:
        None
    Returns:
        x1,y1,width,height: coordinates of the window
    """
    #get OS type 
    os_type = sys.platform
    #Take the screenshot
    bbox = (0,0,1920,1080)
    img = ImageGrab.grab(bbox=bbox)
    rgb_img = np.array(img)
    #PIL to openCV
    img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2HSV)
    # define range of white color in HSV
    lower_white = np.array([0,0,0])
    upper_white = np.array([0,0,255])
    # Threshold the HSV image to get only white colors
    mask = cv2.inRange(img, lower_white, upper_white)

    #Save the screenshot
    cv2.imwrite('mask.png',mask)
    cv2.imwrite('screen.png',rgb_img)
    #Save the screenshot
    # img.save('canvas.png')
    return None #x1,y1,width,height

getCanvas()