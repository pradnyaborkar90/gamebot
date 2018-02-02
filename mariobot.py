from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class Cordinates():
    replayBtn=(340,390)
    dinosaur =(171,395)

def restartGame():
    pyautogui.click(Cordinates.replayBtn)

def pressSpace():
    pyautogui.keyDown('up')
    time.sleep(0.05)
    print("jump")
    pyautogui.keyUp('up')

def imageGrab():
    box=(Cordinates.dinosaur[0]+40,Cordinates.dinosaur[1]+15,Cordinates.dinosaur[0]+50,Cordinates.dinosaur[1]+28 )
    image=ImageGrab.grab(box)
    grayImage= ImageOps.grayscale(image)
    a=array(grayImage.getcolors())
    print(a.sum())
    if a.sum()!= 290:
        pressSpace()
        time.sleep(0.1)

def main():
    restartGame()
    while True:
        imageGrab()
main()