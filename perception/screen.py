from PIL import ImageGrab
import pyautogui
import pygetwindow as gw

#Get the list of windows title
windows = gw.getAllTitles()
#Get dino window info
#Get window name using hard code
dino_win ='Google Chrome chrome://dino/'
x1,y1,width,height = gw.getWindowGeometry(dino_win)
x2 = x1 + width
y2 = y1 + height
#Define the dino bbox
dino_bbox = (x1,y1,x2,y2)
#Get the screen shot of dino window
dino_screen = ImageGrab.grab(bbox=dino_bbox)
#Save the screen shot
dino_screen.save('dino_screen.png')

