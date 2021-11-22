import numpy as np
import cv2
import pyautogui
from pynput import keyboard
from playsound import playsound



combinations = [{keyboard.Key.shift, keyboard.KeyCode(char='s')},{keyboard.Key.shift, keyboard.KeyCode(char='S')}]




def TakeScreenShot(i):
    # take screenshot using pyautogui
    playsound(r"C:\Users\erdal\OneDrive\Masaüstü\Elektronik\Elektronik resimler\Deklanşör-sesi.wav")
    image = pyautogui.screenshot()

    image = cv2.cvtColor(np.array(image),
                         cv2.COLOR_RGB2BGR)

    # writing it to the disk using opencv
    imgName="image{}.jpg".format(i)
    cv2.imwrite(imgName, image)

current=set()

i=1

def on_press(key):
    global i
    if any([key in z for z in combinations]):
        current.add(key)
        if any(all(k in current for k in z) for z in combinations):
            i=i+1
            TakeScreenShot(i)


def on_release(key):
    if any([key in z for z in combinations]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
