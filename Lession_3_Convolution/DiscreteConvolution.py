import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/imgnoise.jpg')

# Averaging Filtering
# blur = cv2.blur(img, (11, 11))

# Gaussian Filtering
# blur = cv2.GaussianBlur(img, (11, 11), 0)

# Median Filtering

blur = cv2.medianBlur(img, 5)
gaussian = cv2.GaussianBlur(img,(5,5),0) #params(img, [x,y], sigmaX) Độ lệch chuẩn theo trục X
averaging = cv2.blur(img,(5,5))
plt.subplot(141), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(142), plt.imshow(blur), plt.title('Trung vi')
plt.xticks([]), plt.yticks([])
plt.subplot(143), plt.imshow(gaussian), plt.title('Loc Gauss')
plt.xticks([]), plt.yticks([])
plt.subplot(144), plt.imshow(averaging), plt.title('Trung binh')
plt.xticks([]), plt.yticks([])
plt.show()