from scipy import ndimage

# create a 3x3 matrix
im_noise = ([[21,69,45],[19,48,25],[39,27,63]])
print(im_noise)

# apply gaussian filter with size=3
im_gau = ndimage.gaussian_filter(im_noise, sigma=2)
print(im_gau)