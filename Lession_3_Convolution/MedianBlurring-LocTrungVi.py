import cv2 as cv

file_img = '../images/imgnoise.jpg'
img = cv.imread(file_img)
median = cv.medianBlur(img,5)
cv.imshow("mediabBlurring", median)
cv.waitKey(0)