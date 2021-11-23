import webbrowser
import time
import pyautogui
import sys
import os
from PIL import Image

world = 1
radius = 10
image_width = 1368
image_height = 770


print("loading images...")
images = []
for x in range(0,radius*2+1):
    
    images.insert(x,[])
    
    for y in range(0,radius*2+1):
        
        images[x].insert(y,Image.open("w"+str(world)+"/"+str(x-radius)+"_"+str(radius-y)+".png"))
print("done!")

total_width = image_width * (radius * 2) + 1
total_height = image_height * (radius * 2) + 1

print("making vertical stripes...")
verticals = []

for x in range(0,radius*2+1):
    
    verticals.insert(x,Image.new('RGB', (image_width,total_height)))

    for y in range(0,radius*2+1):
        verticals[x].paste(images[x][y],(0,image_height*y))
print("done!")

finalimg = Image.new('RGB', (total_width,total_height))


print("combining vertical stripes...")

for x in range(0,radius*2+1):
    finalimg.paste(verticals[x],(image_width*x,0))
    


finalimg.save("out.png")
print("done! check 'out.png'")

