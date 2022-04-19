# The basic Thresholding technique is Binary Thresholding. For every pixel, the same threshold value is applied. If the pixel value is 
# smaller than the threshold, it is set to 0, otherwise, it is set to a maximum value.
# The different Simple Thresholding Techniques are: 
 

# cv2.THRESH_BINARY: If pixel intensity is greater than the set threshold, value set to 255, else set to 0 (black).
# cv2.THRESH_BINARY_INV: Inverted or Opposite case of cv2.THRESH_BINARY.
# cv.THRESH_TRUNC: If pixel intensity value is greater than threshold, it is truncated to the threshold. The pixel values are set to be the same as the threshold. All other values remain the same.
# cv.THRESH_TOZERO: Pixel intensity is set to 0, for all the pixels intensity, less than the threshold value.
# cv.THRESH_TOZERO_INV: Inverted or Opposite case of cv2.THRESH_TOZERO.

# Adaptive thresholding is the method where the threshold value is calculated for smaller regions. This leads to different 
# threshold values for different regions with respect to the change in lighting. We use cv2.adaptiveThreshold for this.
 
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