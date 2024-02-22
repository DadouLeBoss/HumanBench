import pyautogui, keyboard, time # bibliotheque a importer
while not keyboard.is_pressed('a'): # pour arreter le programme sinon chiant
    x,y = pyautogui.position()
    # Regarde si l'endroit de la souris est de la bonne couleur (Vert) :
    if pyautogui.pixel(x , y) == (75,219,106): 
        # Si oui on clic
        pyautogui.click()
        time.sleep(0.5) # pour éviter d'éventuel clic en trop
