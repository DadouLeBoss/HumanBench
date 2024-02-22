import pyautogui, keyboard, time, pytesseract, cv2
from PIL import ImageGrab

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

while True:
    ecran = (250, 450, 1700, 700)
    image = ImageGrab.grab(bbox=ecran)
    """image = cv2.imread("image.png")"""
    txt = ""
    if keyboard.is_pressed("enter"):
        txt = pytesseract.image_to_string(image, lang='eng')
    if txt != "":
        txt2 = ""
        for i in range(len(txt)):
            if txt[i] == "|":
                txt2 += "I"
            elif txt[i] == '\n':
                txt2 += " "
            else:
                txt2 += txt[i]

        print(txt2)
        pyautogui.write(txt2)
        pyautogui.press('enter')