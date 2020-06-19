# Geometrical transformation - shift
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy import ndimage

# open the input image as numpy array, set datatype
img = np.array(Image.open("car-rgb.png"), dtype = np.uint8)

# apply shift function by (Y/row, X/column, channel)
img_sh =  ndimage.shift(img, shift=[-100,-50, 0])

# save image
imgs = Image.fromarray(img_sh)
imgs.save('car-op-rgb-shifted.png')

# set plot size in inch
plt.figure(figsize=(10, 5), dpi=140)

# plot gray image
plt.subplot(121)
plt.axis('on')
#plt.title('Original', fontsize=10)
plt.imshow(img)

# plot gray edge image
plt.subplot(122)
plt.axis('on')
#plt.title('Shifted', fontsize=10)
plt.imshow(img_sh)

# show the plot
plt.show()
