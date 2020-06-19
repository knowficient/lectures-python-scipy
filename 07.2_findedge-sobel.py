# find edge of object
# using sobel filter, take note of the speed of faster speed of conversion
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy import ndimage

# GrayScale Method 1: Function RGB to Gray Level
# luminance (E'y) in Rec.ITU-R BT.601-7l
# gray = 0.299*r + 0.587*g + 0.114*b
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

img = np.array(Image.open("car-rgb.png"), dtype = np.uint8)
# convert RGB to Grayscale
grayfloat = rgb2gray(img)

# Edge Detection using sobel
sobel_x = ndimage.sobel(grayfloat, axis=0, mode='constant')
sobel_y = ndimage.sobel(grayfloat, axis=1, mode='constant')
sobel_xy = np.hypot(sobel_x,sobel_y)  #compute hypothesis

# save image
sxy = sobel_xy.astype(np.uint8)
ime = Image.fromarray(sxy)
ime.save('car-op-edge-gray.png')

# set plot size in inch
plt.figure(figsize=(10, 5), dpi=140)

# plot gray image
plt.subplot(121)
plt.axis('on')
plt.title('Original', fontsize=10)
plt.imshow(img, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# plot gray edge image
plt.subplot(122)
plt.axis('on')
plt.title('Identified edges', fontsize=10)
plt.imshow(sxy, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# show the plot
plt.show()

