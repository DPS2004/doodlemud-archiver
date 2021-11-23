import webbrowser
import time
import pyautogui
import sys
import os

screenshot_pos = (350,203,1216,682)
delay = 1.5
world = 1
start_radius = 7
max_radius = 10
screenshots = 0

def xytonwse(x,y):
    ew = ""
    ns = ""
    if x > 0:
        ew = "e"+str(x)
    if x < 0 :
        ew = "w"+str(0-x)
    if y > 0:
        ns = "n"+str(y)
    if y < 0 :
        ns = "s"+str(0-y)
    return(ew+ns)

def screenshot(x,y):
    global screenshots
    p = xytonwse(x,y)
    if p != "":
        p = "_"+p
    webbrowser.open('https://www.doodlemud.com/' + "#w" + str(world)+p)
    pyautogui.moveTo(1560,205+(screenshots%2)*1,1)
    screenshots += 1
    pyautogui.click() 
    time.sleep(delay)
    pyautogui.screenshot("w"+str(world)+"/"+str(x)+"_"+str(y)+".png",region = screenshot_pos)

try:
    os.mkdir("w"+str(world))
except:
    print("dir already exists")



for cur_radius in range(start_radius,max_radius+1):
    print(cur_radius)
    if cur_radius==0:
        screenshot(0,0)
    else:
        for i in range(0-cur_radius, cur_radius):
            screenshot(i, cur_radius) 
            screenshot(cur_radius, 0-i)
            screenshot(0-i,0-cur_radius)
            screenshot(0-cur_radius,i)


