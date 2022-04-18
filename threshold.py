import cv2 as cv
from cv2 import threshold
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photos/cat.jpg')
resized = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)

#simple thresholding
threshold_, thresh = cv.threshold(gray,110,255, cv.THRESH_BINARY)
cv.imshow('Simple threshold', thresh)

#inverse thresholding
threshold_, thresh_inv = cv.threshold(gray,110,255, cv.THRESH_BINARY_INV)
cv.imshow('Simple threshold inv', thresh_inv)

#adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray,255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('adaptive', adaptive_thresh)

cv.waitKey(0)