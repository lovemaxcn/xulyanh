import cv2
from matplotlib import pyplot as plt

filename = '../images/opencv.png'
W = 1000.
oriimg = cv2.imread(filename)
height, width, depth = oriimg.shape
imgScale = W / width
print("W: {0}".format(W))
print("Width: {0}".format(width))
print("Scale: {0}".format(imgScale))

newX, newY = oriimg.shape[1] * imgScale, oriimg.shape[0] * imgScale

print("newX: {0}".format(newX))
print("newY: {0}".format(newY))
newimg = cv2.resize(oriimg, (int(newX), int(newY)))

cv2.imshow("Origin", oriimg)
cv2.imshow("Resize", newimg)
cv2.waitKey(0)
# cv2.imwrite("resizeimg.jpg", newimg)
