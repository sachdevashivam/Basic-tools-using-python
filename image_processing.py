from PIL import Image, ImageFilter
img = Image.open("C:/Personal/Python/Image_Processing/big-one.jpg")
print(img)
print(img.format)
print(img.size)
print(img.mode)

# print(dir(img))

filtered_image = img.filter(ImageFilter.BLUR)
filtered_image.save('C:/Personal/Python/Image_Processing/blur-big-one.png', 'png')

smooth_image = img.filter(ImageFilter.SMOOTH)
smooth_image.save('C:/Personal/Python/Image_Processing/smooth-big-one.png', 'png')

sharpen_image = img.filter(ImageFilter.SHARPEN)
sharpen_image.save('C:/Personal/Python/Image_Processing/sharpen-big-one.png', 'png')

# The PNG format support all these filters so we are saving images into this format.

converted_image = img.convert('L')
converted_image.save('C:/Personal/Python/Image_Processing/converted-big-one.png', 'png')
# converted_image.show()
# Show will open up the file

rotated_img = filtered_image.rotate(90)
# rotated_img.show()

resized_img = filtered_image.resize((300, 300))
# resize accepts tuple of dimentions, else it will throw an error
# resized_img.show()

# If the image is not of same height and width and we try to make it a small thumbnail using resize method, the image clearity got affected and we are not able to get proper output.
# To avaoid this we can use a method thumbnail() 

thumbnail_img = filtered_image.thumbnail((300, 300))
# It will give n error while saving/showing the thumbnail_img cz it actually make changes to the original image
filtered_image.show()
# Thumbnail cannot go above dimentions(400, 400)



# For doing crop we'll put the pixel locations for the 4 corners and apply crop to that
crop_pixels = (100, 100, 400, 400)
crop_img = filtered_image.crop(crop_pixels)
# crop_img.show()



