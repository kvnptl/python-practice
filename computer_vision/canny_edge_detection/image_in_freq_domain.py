
from matplotlib import pyplot as plt
import cv2
import numpy as np

# Read image
img = cv2.imread("lena.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original", img)

def freq_domain(img):
    # Fourier transform
    dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)

    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum = 20 * \
        np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

    # convert to uint8
    magnitude_spectrum = np.uint8(magnitude_spectrum)
    return magnitude_spectrum

magnitude_spectrum1 = freq_domain(img)

# display the Fourier transform
cv2.imshow("Original: Fourier transform", magnitude_spectrum1)


# creating low pass filter
rows, cols = img.shape
crow, ccol = int(rows/2), int(cols/2)
# Create a mask with a square of 1 and the rest 0
mask = np.zeros((rows, cols, 2), np.uint8)
mask[crow-50:crow+50, ccol-50:ccol+50] = 1

# Fourier transform
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)

dft_shift = np.fft.fftshift(dft)

# Use mask
fshift = dft_shift*mask
magnitude_spectrum2 = 20 * \
    np.log(cv2.magnitude(fshift[:, :, 0], fshift[:, :, 1]))

# convert to uint8
magnitude_spectrum2 = np.uint8(magnitude_spectrum2)

# display the Fourier transform
cv2.imshow("Fourier transform with mask", magnitude_spectrum2)


f_ishift = np.fft.ifftshift(fshift)
# inverse Fourier transform
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

# normalize the image to [0, 255]
img_back = cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX)

# convert to uint8
img_back = np.uint8(img_back)

# display the Fourier transform
cv2.imshow("Inverse Fourier transform", img_back)


# gaussian blur
# gaussian_img = cv2.GaussianBlur(img, (5, 5), 0)

# # display the Gaussian blurred image
# cv2.imshow("Gaussian Blurred Image 5x5", gaussian_img)

# freq_domain_gaussian_img = freq_domain(gaussian_img)

# # display the Fourier transform
# cv2.imshow("Gaussian: Fourier transform",
#            freq_domain_gaussian_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
