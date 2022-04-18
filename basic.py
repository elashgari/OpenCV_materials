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