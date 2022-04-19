import cv2 as cv
import numpy as np

#create a blank image
blank = np.zeros((500,500,3), dtype ='uint8')
# cv.imshow('Blank',blank)

# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat', img)

# blank[:] = 0,255,0
# cv.imshow('Green', blank)

#Draw a rectangle
cv.rectangle(blank,(0,100),(250,500),(0,255,0), thickness=cv.FILLED)
cv.imshow('rec', blank)

#Draw a circle
cv.circle(blank,(blank.shape[0]//2, blank.shape[1]//2), 45,(0,0,255), thickness=-1)
cv.imshow('Circle',blank)

#Draw a line
cv.line(blank,(0,100),(250,500), (255,255,0), thickness=6)
cv.imshow('line',blank)

#Write text on the image
cv.putText(blank,'Elnaz',(255,255), cv.FONT_HERSHEY_TRIPLEX, 1.5,(0,255,255), thickness=2)
cv.imshow('text', blank)

cv.waitKey(0)