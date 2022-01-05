from PIL import ImageGrab
import pyautogui

#Get the list of windows title
windows = pyautogui.getWindows()
print(windows)
img = ImageGrab.grab()
#save the image
img.save('screen.png')