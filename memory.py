import pyautogui, keyboard, time
from PIL import Image
import win32api, win32con
time.sleep(3)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


click(977,558)

time.sleep(0.8)
while not keyboard.is_pressed('a'):

    L = pyautogui.screenshot(region=(750,250,430,410))
    time.sleep(2)
    Lresize = L.resize((43,41))
    Lresize.save(r"D:\Documents\Python\screen.png")
    px = Lresize.load()

    for x in range(43):
        for y in range(41):
            if px[x,y]==(255,255,255):
                click(10*x+750,10*y+250)

    time.sleep(2)


