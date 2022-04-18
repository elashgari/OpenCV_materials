# https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

import cv2 as cv
from cv2 import threshold
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photos/group.jpg') #lady.jpg, family.jpg, group.jpg
resized = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow('lady', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(resized, scaleFactor = 1.1, minNeighbors = 8) 
print(f'Number of faces found={len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(resized,(x,y),(x+w,y+h),(0,255,0), thickness=3)
cv.imshow('Detected faces', resized)

cv.waitKey(0)