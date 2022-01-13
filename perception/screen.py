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
def getChromeArea(save=True):
    """
    Takes a screenshot from chrome window and saves it to the path
    Parameters:
        None
    Returns:
        x1,y1,width,height: coordinates of the window
    """
    #Take the screenshot
    img = ImageGrab.grab()
    rgb_img = np.array(img).astype(np.uint8)
    #PIL to openCV
    img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2HSV)
    # define range of white color in HSV
    lower_white = np.array([0,0,60])
    upper_white = np.array([0,0,255])
    # Threshold the HSV image to get only white colors
    mask = cv2.inRange(img, lower_white, upper_white)
    #Find the contours
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #Find the biggest contour
    cnt = max(contours, key = lambda x: cv2.contourArea(x))
    #Get the coordinates of the biggest contour
    x,y,w,h = cv2.boundingRect(cnt)
    #Print the width and height of the canvas
   
    if save:
        #Save the screenshot        
        cv2.imwrite('img/screen.png',rgb_img)
        #Draw the rectangle on the image
        cv2.rectangle(rgb_img,(x,y),(x+w,y+h),(0,255,0),4)
        #Save the screenshot
        cv2.imwrite('img/mask.png',mask)
        cv2.imwrite('img/screen_bbox.png',rgb_img)
    return x,y,w,h

#Define the function to get the coordinates of the canvas
def getCanvasArea(x,y,w,h):
    """
    Takes a chrome coordinates and returns the coordinates of the canvas
    Parameters:
        x,y,w,h: chrome coordinates
    Returns:
        x1,y1,width,height: coordinates of the canvas
    """
    #Define the bounding box of the canvas
    x1 = x+5
    y1 = y
    x2 = x + w*0.01
    y2 = y + h
    
    #Take the screenshot: x,y,w,h
    img = ImageGrab.grab(bbox=(x1,y1,x2,y2))
    #Convert img to numpy array
    rgb_img = np.array(img).astype(np.uint8)
    #PIL to openCV in grayscale
    img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2GRAY)
    #Threshold the image
    ret,thresh = cv2.threshold(img,127,255,0)
    zero=np.zeros_like(thresh[0])
    h=np.where((thresh==zero).all(axis=1))[0][0]
    #Define the bounding box of the canvas
    x1,y1,x2,y2 = x1,y1,x+w,y+h
    #Take the screenshot
    img = ImageGrab.grab(bbox=(x1,y1,x2,y2))
    #Save the screenshot
    img.save('img/canvas.png')

   
    #Save the threshold image
    cv2.imwrite('img/thresh.png',thresh)

    #Save the screenshot
    # img.save('img/canvas.png')
    
    



    # img = ImageGrab.grab()
    # rgb_img = np.array(img).astype(np.uint8)
    #Get the coordinates of the canvas
    # x1,y1,width,height = x+w,y+h,w,h
    return None #x1,y1,width,height
    

 
x,y,w,h=getChromeArea(False)
#Get canvas
getCanvasArea(x,y,w,h)