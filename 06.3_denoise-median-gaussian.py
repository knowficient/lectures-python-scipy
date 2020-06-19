# remove noise from image
# 2 methods are used, naming
# gaussian filter and medium filter
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy import ndimage

# open the input image as numpy array, datatype as uint8
img = np.array(Image.open("car-gray-noise.png"), dtype = np.uint8)
# focus on section of image, slicing
#img = img[350:550, 250:450]

# de-noise using Guassian filter, sigma (standard deviation)
gauss_denoised = ndimage.gaussian_filter(img, sigma=2)
imdg = Image.fromarray(gauss_denoised)  #PIL to image
imdg.save('car-op-gaufilter-gray.png') #Save image

# de-noise using median filter, size=4
med_denoised = ndimage.median_filter(img, size=4)
imdm = Image.fromarray(med_denoised) #PIL to image
imdm.save('car-op-medfilter-gray.png')

# set plot size in inch
plt.figure(figsize=(10, 5), dpi=140)

# plot gray image before applying filter
plt.subplot(131)
plt.axis('on')
plt.title('Original', fontsize=10)
plt.imshow(img, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# plot gray image de-noising fom guassian filter
plt.subplot(132)
plt.axis('on')
plt.title('Gaussian Filter', fontsize=10)
plt.imshow(gauss_denoised, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# plot gray image de-noising fom medium filter
plt.subplot(133)
plt.axis('on')
plt.title('Median Filter', fontsize=10)
plt.imshow(med_denoised, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# show the plot
plt.show()