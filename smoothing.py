# Image Blurring refers to making the image less clear or distinct. It is done with the help of various low pass filter kernels.

# Advantages of blurring:

##It helps in Noise removal. As noise is considered as high pass signal so by the application of low pass filter kernel we restrict noise.
## It helps in smoothing the image.
## Low intensity edges are removed.
## It helps in hiding the details when necessary. For e.g. in many cases police deliberately want to hide the face of the victim, in such cases blurring is required.


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