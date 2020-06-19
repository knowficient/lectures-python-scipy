import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

#create a 10x10 matrix
im = np.zeros((10, 10))
im[2:-2, 2:-2] = 1
# apply sobel in x-axis
sx = ndimage.sobel(im, axis=0, mode='constant')
# apply sobel in y-axis
sy = ndimage.sobel(im, axis=1, mode='constant')
# apply hypotenuse of sx and sy
sob = np.hypot(sx, sy)

plt.figure(figsize=(10, 5))

plt.subplot(141)
plt.imshow(im, cmap=plt.get_cmap('gray'))
plt.axis('off')
plt.title('square', fontsize=10)

plt.subplot(142)
plt.imshow(sx)
plt.axis('off')
plt.title('Sobel (x direction)', fontsize=10)

plt.subplot(143)
plt.imshow(sy)
plt.axis('off')
plt.title('Sobel (y direction)', fontsize=10)

plt.subplot(144)
plt.imshow(sob)
plt.axis('off')
plt.title('Sobel applied', fontsize=10)

plt.show()