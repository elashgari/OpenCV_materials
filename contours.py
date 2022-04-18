import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')
resized = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray,(9,9), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 125, 175)
cv.imshow('CANNY', canny)

blank = np.zeros(resized.shape, dtype='uint8')

#to decrease the number of contours from 2380 to lower number we used blur+canny but simply we can use threshold
ret, thresh = cv.threshold(gray,125,255, cv.THRESH_BINARY)
cv.imshow('threshold', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)  #canny --> thresh
print(len(contours))

cv.drawContours(blank, contours, -1, (0,0,255),1)
cv.imshow('contours', blank)



cv.waitKey(0)