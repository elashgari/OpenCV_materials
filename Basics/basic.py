# https://www.youtube.com/watch?v=oXlwWbU8l2o


import cv2 as cv
img = cv.imread('Photos/cat.jpg')
cv.imshow('CAT', img)

# Converting image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (9,9),cv.BORDER_DEFAULT) # the kernel should be odd number
cv.imshow('Blur',blur)

# Edge Cascade
canny = cv.Canny(img,125,175) #img > blur
cv.imshow('Canny', canny)

# Erosion: 
# It is useful for removing small white noises.
# Used to detach two connected objects etc.
# Dilation:
# In cases like noise removal, erosion is followed by dilation. Because, erosion removes white noises, but it also shrinks our object. So we dilate it. Since noise is gone, they won’t come back, but our object area increases.
# It is also useful in joining broken parts of an object.

# Dilating the image
dilate = cv.dilate(canny, (9,9), iterations=1)
cv.imshow('Dilate', dilate)

# Eroading
eroded = cv.erode(dilate,(3,3), iterations=1)
cv.imshow('Erode',eroded)

# Resize
resized = cv.resize(img,(500,500), interpolation= cv.INTER_CUBIC)
cv.imshow('resized', resized)

#Cropping
cropped = img[50:1000, 200:1500]
cv.imshow('cropped', cropped)


cv.waitKey(0)