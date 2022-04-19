import cv2 as cv
from cv2 import threshold
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photos/cat.jpg')
resized = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)

#laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap =np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)


#Sobel
sobelx = cv.Sobel(gray, cv.CV_64F,1,0)
sobely = cv.Sobel(gray, cv.CV_64F,0,1)
combined_sobel =cv.bitwise_or(sobelx,sobely)
cv.imshow('sobelx', sobelx)
cv.imshow('sobely', sobely)
cv.imshow('sobelxy', combined_sobel)

#canny
canny = cv.Canny(gray, 150,175)
cv.imshow('Canny',canny)


cv.waitKey(0)