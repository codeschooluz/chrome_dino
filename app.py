from perception.screen import getChromeArea,getCanvasArea
from PIL import ImageGrab
import numpy as np
import cv2
x,y,w,h=getChromeArea(False)
#Define the loop for the game
#Get canvas
x1,y1,x2,y2=getCanvasArea(x,y,w,h)
while True:
    
    #Take the screenshot
    img = ImageGrab.grab(bbox=(x1,y1,x2,y2))
    #Convert img to numpy array
    rgb_img = np.array(img).astype(np.uint8)
    #Imshow the image
    cv2.imshow('image',rgb_img)
    #Wait for key press
    k = cv2.waitKey(1) & 0xFF
    print(k)
    #If key is pressed
    if k == 27:
        #Break the loop
        break


