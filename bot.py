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
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("jump")
    pyautogui.keyUp('space')
def imageGrab():
    box=(Cordinates.dinosaur[0]+60,Cordinates.dinosaur[1]+35,Cordinates.dinosaur[0]+100,Cordinates.dinosaur[1]+70 )
    image=ImageGrab.grab(box)
    grayImage= ImageOps.grayscale(image)
    a=array(grayImage.getcolors())
    print(a.sum())
    if a.sum()!= 1730:
        pressSpace()
        time.sleep(0.1)
def main():
    restartGame()
    while True:
        imageGrab()
main()