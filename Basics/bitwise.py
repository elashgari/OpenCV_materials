import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype ='uint8')
rectangle = cv.rectangle(blank.copy(), (30,30),(370,370), 255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

#bitwise AND
bitwise_andd = cv.bitwise_and(rectangle, circle)
cv.imshow('AND', bitwise_andd)

#bitwise OR
bitwise_orr= cv.bitwise_or(rectangle, circle)
cv.imshow('OR', bitwise_orr)

#bitwise XOR
bitwise_xorr= cv.bitwise_xor(rectangle, circle)
cv.imshow('XOR', bitwise_xorr)

#bitwise NOT
bitwise_nott= cv.bitwise_not(rectangle)
cv.imshow('NOT', bitwise_nott)

cv.waitKey(0)