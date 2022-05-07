from PIL import Image as img
import os 
# os is a module, not a package Properly speaking
# every thing could use .fuction is an "object"


for f in os.listdir("orig"): # . means current path 
    if f.endswith(".jpg"):
        # f is name
        # listdir list the name in the dir "orig"
        #image_f = img.open("orig/" + f)  #image_f is an object
        image_f = img.open(os.path.join("orig", f))  #image_f is an object        
        image_f = image_f.convert('L')  #convert to black and white
        image_f.save(os.path.join("result", f[:-4]) + "_grey.png") 
        # endswith is str's function
        # -4 means to the -4 position ()