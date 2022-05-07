from PIL import Image as img
# every thing could use .fuction is an "object"
image_f = img.open("oliverdive.jpg")  #image_f is an object
image_f = image_f.convert('L')  #convert to black and white
image_f.save("result.png")