from PIL import Image

image1 = Image.open('Desert.jpg')
image2 = Image.open('Lighthouse.jpg')
image3 = Image.open('Koala.jpg')

print('------------------')

print('Image1 Size ', image1.size)

print('------------------')

print('Image2 Size ', image2.size)
# --------------------Image-1-----------------
# ---------Cropping---------

# i am putting image 2 into image 1
area = (100, 100, 200, 200)
image4 = image2.crop(area)
# image4.show()
print('Image 3 size ', image4.size)

# ---------Merging---------

image1, image4

area = (824, 100, 924, 200)
image1.paste(image4, area)

# image1.show()

# --------------------Image-2-----------------

# -----------Cropping-------------


area = (400, 250, 700, 550)
image5 = image3.crop(area)
print(image5.size)

# ---------Merging---------

image1, image5
area = (100, 100, 400, 400)
image1.paste(image5, area)
image1.show()
