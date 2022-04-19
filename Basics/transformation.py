import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')
resized = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('CAT', resized)

#translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(resized, 100,100)
cv.imshow('transformation', translated)

# rotation
def rotate(img, angle, rotPoint =None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle,1)
    dimension =(width, height)
    return cv.warpAffine(img, rotMat, dimension)

rotated = rotate(resized, -90) #-45 --> clockwise
cv.imshow('rotated', rotated)

# Flipping

flipped = cv.flip(resized, 1 ) #0 -->vertically 1-->horiz -1-->both
cv.imshow('Flipped', flipped)

# Resize
resized = cv.resize(img,(500,500), interpolation= cv.INTER_CUBIC)
cv.imshow('resized', resized)

#Cropping
cropped = img[50:1000, 200:1500]
cv.imshow('cropped', cropped)


cv.waitKey(0)