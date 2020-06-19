# Geometrical transformation - rotate
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy import ndimage

# open the input image as numpy array, set datatype
img = np.array(Image.open("car-rgb.png"), dtype = np.uint8)

# apply rotate function by angle, reshape = false
img_rt =  ndimage.rotate(img, angle=90.0, reshape=False)

# save image
imgs = Image.fromarray(img_rt)
imgs.save('car-op-rgb-rotate.png')

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
plt.title('Rotated', fontsize=10)
plt.imshow(img_rt)

# show the plot
#plt.subplots_adjust(wspace=0.02, hspace=0.02, top=1, bottom=0, left=0, right=0.9)
plt.show()
