#Các phép biến đổi hình thái
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./images/j.png',0)

#Phép co ảnh
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
#Phép giãn
dilation = cv2.dilate(img,kernel,iterations = 2)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
plt.subplot(181),plt.imshow(img),plt.title('Anh goc')
plt.xticks([]), plt.yticks([])
plt.subplot(182),plt.imshow(erosion),plt.title('co')
plt.xticks([]), plt.yticks([])
plt.subplot(183),plt.imshow(dilation),plt.title('gian')
plt.xticks([]), plt.yticks([])
plt.subplot(184),plt.imshow(opening),plt.title('mo')
plt.xticks([]), plt.yticks([])
plt.subplot(185),plt.imshow(closing),plt.title('dong')
plt.xticks([]), plt.yticks([])
plt.subplot(186),plt.imshow(gradient),plt.title('Gradi')
plt.xticks([]), plt.yticks([])
plt.subplot(187),plt.imshow(tophat),plt.title('top hat')
plt.xticks([]), plt.yticks([])
plt.subplot(188),plt.imshow(blackhat),plt.title('black hat')
plt.xticks([]), plt.yticks([])
plt.show()