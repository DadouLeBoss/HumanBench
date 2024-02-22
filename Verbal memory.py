import pyautogui, keyboard, time, pytesseract
from PIL import ImageGrab
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

run = True
ecran = (676, 447, 1253, 556)
List_mot = []

while run:
    if keyboard.is_pressed('8'):
        run = False
        while not keyboard.is_pressed('7'):
            time.sleep(0.0001)
            image = ImageGrab.grab(bbox=ecran)
            txt = pytesseract.image_to_string(image, lang='eng')
            if txt in List_mot:
                x, y = 869, 612
            else:
                x, y = 1036, 609
                List_mot.append(txt)
            pyautogui.moveTo(x, y)
            time.sleep(0.0001)
            pyautogui.click()