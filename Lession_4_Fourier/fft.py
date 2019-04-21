import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/res.png',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
f_back = np.fft.ifft2(fshift)
f_back = np.abs(f_back)
magnitude_spectrum = 20*np.log(np.abs(fshift))

plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])

plt.subplot(132),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

plt.subplot(133),plt.imshow(f_back, cmap = 'gray')
plt.title('Inverse FFT'), plt.xticks([]), plt.yticks([])

plt.show()