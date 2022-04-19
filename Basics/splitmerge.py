import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Photos/cat.jpg')
resized = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)

blank = np.zeros(resized.shape[:2], dtype='uint8')

b,g,r = cv.split(resized)
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

# cv.imshow('BLUE',b)
# cv.imshow('GREEN',g)
# cv.imshow('RED',r)

cv.imshow('BLUE',blue)
cv.imshow('GREEN',green)
cv.imshow('RED',red)

merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)

cv.waitKey(0)