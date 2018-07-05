from PIL import Image

img = Image.open('Chrysanthemum.jpg')
print('Img', img.format)
print('Img', img.size)
# img.show()
print('----------------------------------')
img1 = Image.open('Desert.jpg')
print('Img1', img1.format)
print('Img1', img1.size)
print('----------------------------------')

img2 = Image.open('Lighthouse.jpg')
print('Img2 ', img2.format)
print('Img2 ', img2.size)

'''
# Cropping

area = (100, 100, 300, 300)
img_crop = img.crop(area)

# img_crop.show()
print(img_crop.size)
# Merging
img_crop, img1
area1 = (200, 200, 400, 400)
img1.paste(img_crop, area1)
# img1.show()

# Split Colors

r, b, g = img1.split()
r.show()
b.show()
g.show()
'''
# split merge

r1, g1, b1 = img.split()
r2, g2, b2 = img1.split()

new_img = Image.merge("RGB", (r1, g2, b2))

new_img.show()
