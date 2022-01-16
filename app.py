from tracemalloc import stop
from perception.screen import getChromeArea,getCanvasArea, getDino
from PIL import ImageGrab
import numpy as np
import cv2
import matplotlib.pyplot as plt
import pyautogui

fence_color = (83, 83, 83)

x,y,w,h=getChromeArea(False)
thresh_img = getCanvasArea(x,y,w,h)
x1,y1,w1,h1 = getDino(thresh_img)

while True:
    image = ImageGrab.grab()
    fence_pixel = image.getpixel((w//4+w1//2,y1+h1//2))
    # print(fence_pixel)
    if fence_pixel == fence_color:
        print("jump")
        pyautogui.press('space')
    #Take the screenshot
    rgb_img = np.array(image).astype(np.uint8)
    rgb_img = cv2.rectangle(rgb_img,(x1,y1),(x1+w1,y1+h1),(255,0,0),2)
    #Imshow the image
    # cv2.imshow('image',rgb_img)
    #Wait for key press
    k = cv2.waitKey(1) & 0xFF
    print(k)
    #If key is pressed
    if k == 27:
        #Break the loop
        break


