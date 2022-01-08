from PIL import ImageGrab
import pyautogui
import sys
import os

fence_color = (83, 83, 83)

if sys.platform in ['win32', 'win64', 'windows']:
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

elif sys.platform in ['linux', 'linux2']:
    try:
        import pgi
        pgi.require_version('Wnck', '3.0')
        from pgi.repository import Wnck
    except:
        print('Please install Wnck')
        Wnck = None
    if Wnck is not None:
        for i in range(10000):
            screen = Wnck.Screen.get_default()
            screen.force_update()
            windows = screen.get_windows()
            for window in windows:
                if window.get_name() == 'chrome://dino/ - Google Chrome':
                    x1,y1,width,height = window.get_geometry()
                    x2 = x1 + width
                    y2 = y1 + height
                    dino_bbox = (x1,y1,x2,y2)
                    dino_screen = ImageGrab.grab(bbox=dino_bbox)
                    fence_pixel = dino_screen.getpixel((350,500))
                    # print(fence_pixel)
                    if fence_pixel == fence_color:
                        print("jumb")
                        pyautogui.press('space')
                    # image = f'screen_{i}.png'
                    # dino_screen.save(image)
                    # if i > 1:
                    #     image = f'screen_{i-2}.png'
                    #     os.remove(image)
                    # os.remove(image)
                    break