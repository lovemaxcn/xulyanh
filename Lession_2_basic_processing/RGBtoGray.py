import cv2

image = cv2.imread("../images/opencv.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("RGB", image)
cv2.imshow("Gray", gray_image)

cv2.waitKey(0)
