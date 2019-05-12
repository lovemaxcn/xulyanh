import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/res.png',0)
#fourier thuận
f = np.fft.fft2(img)

fshift = np.fft.fftshift(f)


magnitude_spectrum = 20*np.log(np.abs(fshift)) #phổ cường độ tần số
# sau khi sử dụng hàm fft2, thu đc thành phần tân số ở góc trên cùng bên trái
#fftshift dùng để chuyển  thành phần tần số ra tâm (đưa kết quả đi N/2 đơn vị cả 2 trục)

# rows, cols = img.shape
# crow,ccol = rows/2 , cols/2
# fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
f_shift = np.fft.ifftshift(fshift)
f_back = np.fft.ifft2(f_shift)
f_back = np.abs(f_back)

plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])

plt.subplot(132),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

plt.subplot(133),plt.imshow(f_back, cmap = 'gray')
plt.title('Inverse FFT'), plt.xticks([]), plt.yticks([])

plt.show()