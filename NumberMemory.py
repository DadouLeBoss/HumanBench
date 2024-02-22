import pyautogui, keyboard, time, pytesseract, cv2
from PIL import Image, ImageOps 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

run = True

def binarize(img):

  #initialize threshold
  thresh=240



  #convert image to greyscale
  img=img.convert('L') 

  width,height=img.size

  #traverse through pixels 
  for x in range(width):
    for y in range(height):

      #if intensity less than threshold, assign white
      if img.getpixel((x,y)) < thresh:
        img.putpixel((x,y),0)

      #if intensity greater than threshold, assign black 
      else:
        img.putpixel((x,y),255)

  return img

n = 1
while run:

    if keyboard.is_pressed('8'):
        pyautogui.moveTo(969, 570)
        pyautogui.click()
        pyautogui.moveTo(0, 0)
        run = False
        time.sleep(0.5)
        while not keyboard.is_pressed('7'):
            txt2=''
            if n<17:
                image = pyautogui.screenshot(region=(400, 370, 1200, 85))
                image = binarize(image)
                image = image.resize((400,28))
                image.save(r"D:\Documents\Python\gray.png")
                txt = pytesseract.image_to_string(image, config ="--psm 7 digits")
                
            else:
                image = pyautogui.screenshot(region=(400, 330, 1200, 85))
                image = ImageOps.grayscale(image)
                image = binarize(image)
                image = image.resize((400,28))
                image.save(r"D:\Documents\Python\gray.png")
                txt = pytesseract.image_to_string(image, config ="--psm 7 digits")
                image2 = pyautogui.screenshot(region=(400,235, 1200,85))
                image2 = ImageOps.grayscale(image2)
                image2 = binarize(image2)
                image2 = image2.resize((400,28))
                image2.save(r"D:\Documents\Python\gray2.png")
                txt2 = pytesseract.image_to_string(image2, config ="--psm 7 digits")

            
            rgb = pyautogui.pixel(1022, 503)
            
            print(txt2,txt)
            if rgb[0] > rgb[2]:
                keyboard.write(txt2+txt)
                print("dedans",n, txt)
                n+=1
                keyboard.send("enter")
                keyboard.send("enter")
                time.sleep(0.2)
