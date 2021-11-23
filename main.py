import webbrowser
import time
import pyautogui
import sys
import os

screenshot_pos = (350,203,1216,682)
delay = 2
world = 1
max_radius = 10


try:
    os.mkdir("w"+str(world))
except:
    print("dir already exists")

cur_radius = 0

webbrowser.open('https://www.doodlemud.com/' + "#w" + str(world))
pyautogui.moveTo(1560,205,1)
pyautogui.click() 
time.sleep(delay)
pyautogui.screenshot("w"+str(world)+"/origin.png",region = screenshot_pos)

