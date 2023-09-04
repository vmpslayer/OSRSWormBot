from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# To find position and RGB values of a pixel
# pyautogui.displayMousePosition()

# Search for an Item // NOT USED (looking for a way to locate text on screen and not an image)
# item = pyautogui.prompt(text="", title="Enter the Item you are searching for")
# print("Searching for ", item)

# Variables
count = 0
i = 0

# Click function
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)    

def openGame():
    osrs = pyautogui.locateCenterOnScreen("bin\osrs.png", confidence=0.9)
    print("Game is located on task bar at:", osrs)
    # moveTo(osrs[0], osrs[1])
    click(osrs[0], osrs[1])
    time.sleep(0.05)

def collect():    
    worm = pyautogui.locateCenterOnScreen("bin\worm.png", confidence=0.7)
    print("Item is located at:", worm)
    moveTo(worm[0]+5, worm[1]+10)
    time.sleep(0.5)
    for i in range(3):
        worm = pyautogui.locateCenterOnScreen("bin\worm.png", confidence=0.7)
        click(worm[0]+5, worm[1]+10)
    # click(worm[0]+5, worm[1]+10)
    time.sleep(8)
    
osrs = pyautogui.locateCenterOnScreen("bin\osrs.png", confidence=0.9)
print(osrs)

location = pyautogui.locateCenterOnScreen("bin\worm.png", confidence=0.9)
print(location)

# Main Loop // Count until 28 (maximum storage in inventory in OSRS)

print("Start program? Y/N")
choice = input("")

if choice == "Y":
    openGame()
    while count != 28:
        if keyboard.is_pressed("m"):
            break
        else:
            collect()
            count += 1
        