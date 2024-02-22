import pyautogui, keyboard, time
from PIL import Image
import win32api, win32con
time.sleep(3)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)



while not keyboard.is_pressed('a') and pyautogui.pixel(962,574)[2]!=84:
    pic = pyautogui.screenshot(region = (400, 210, 1200, 420))
    touche = False
    for x in range(0,1200,10):
        for y in range(0,420,10):
            if pic.getpixel((x,y)) == (149,195,232):
                click(x+400,y+210)
                print(x,y)
                touche = True
                break
        if touche:
            break
