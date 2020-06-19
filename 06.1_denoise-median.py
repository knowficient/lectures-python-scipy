from scipy import ndimage

# create a 3x3 matrix
im_noise = ([[21,25,26],[30,125,28],[26,23,24]])
print(im_noise)

# apply median filter with size=3
im_med = ndimage.median_filter(im_noise, size=3)
print(im_med)
