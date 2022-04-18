import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Photos/cat.jpg')
resized = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)

#Averaging
average = cv.blur(resized,(11,11))
cv.imshow('average', average)

#Gaussian 
gauss = cv.GaussianBlur(resized,(11,11),0)
cv.imshow('Gaussian', gauss)

#Median -->good for noisy image
median = cv.medianBlur(resized, 11)
cv.imshow('Median', median)

#Bilateral -->most effective and useful for advanced CV
bilateral = cv.bilateralFilter(resized, 5, 15,15)
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)