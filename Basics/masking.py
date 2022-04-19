import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Photos/cat.jpg')
resized = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)

blank = np.zeros(resized.shape[:2], dtype='uint8')
mask = cv.circle(blank, (resized.shape[1]//2,resized.shape[0]//2), 100, 255, -1)
cv.imshow('mask', mask)

masked =  cv.bitwise_and(resized, resized, mask=mask)
cv.imshow('masked', masked)

cv.waitKey(0)