import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Photos/cat.jpg')
resized = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV(hue saturation)
hsv = cv.cvtColor(resized, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b -->washed down version of original image
lab = cv.cvtColor(resized, cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)


# the format of the images in open-cv is BGR but in plt is RGB, test below:
plt.imshow(resized)
plt.show()

# BGR to RGB
rgb = cv.cvtColor(resized, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

#we cannot convert grayscale to LAB!!!! GS>HSV>LAB


cv.waitKey(0)