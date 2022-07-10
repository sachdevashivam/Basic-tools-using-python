import sys
import os
from PIL import Image

directory = "C:\Personal\Python\Image_Processing\Jpg_Image_Files"
for image in os.listdir(directory):
    print(image)
    

    img = Image.open("C:/Personal/Python/Image_Processing/Jpg_Image_Files/"+image)
    print(img)
    
    if(image.endswith('.jpg')):
        image = image.replace('.jpg', '.png')
    img.save(f"C:/Personal/Python/Image_Processing/Png_Image_Files/"+image+'_'+"PNG.png", 'png')

