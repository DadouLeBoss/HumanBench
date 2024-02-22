import pyautogui, keyboard, time
from PIL import Image
import win32api, win32con
time.sleep(3)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

click(977,558)

time.sleep(1.2)



i = 0

while not keyboard.is_pressed('a'):
    i+=1
    Liste = []

    for _ in range(0,i):
        t1 = time.time()
        L = pyautogui.screenshot(region=(750,250,430,410))
        Lresize = L.resize((43,41))
        Lresize.save(r"D:\Documents\Python\screen.png")
        px = Lresize.load()
        trouve = False
        for x in range(43):
            for y in range(41):
                if px[x,y]==(255,255,255):
                    Liste.append((10*x+750,10*y+250))
                    trouve = True
                    break
            if trouve:
                break
        t2 = time.time()
        time.sleep(0.5-t2+t1)

    time.sleep(1)
    print(i,Liste)
    for el in Liste:
        click(el[0],el[1])
    time.sleep(1.2)

