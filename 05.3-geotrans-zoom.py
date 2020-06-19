# Geometrical transformation - zoom
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy import ndimage

# open the input image as numpy array, set datatype
img = np.array(Image.open("car-rgb.png"), dtype = np.uint8)
# apply zoom function by zoom factor=
# (row/y ratio, column/x Ratio, channel ratio)
# order=0: nearest interpolation
img_zm =  ndimage.zoom(img, zoom=(2,2,1), order=0)

# save image
imgz = Image.fromarray(img_zm)
imgz.save('car-op-rgb-zoom.png')

# set plot size in inch
plt.figure(figsize=(10, 5), dpi=140)

# plot gray image
plt.subplot(121)
plt.axis('on')
plt.title('Original', fontsize=10)
plt.imshow(img)

# plot gray edge image
plt.subplot(122)
plt.axis('on')
plt.title('Zoom', fontsize=10)
plt.imshow(img_zm)

# show the plot
plt.show()
