# Background Subtraction has several use cases in everyday life, It is being used for object segmentation, 
# security enhancement, pedestrian tracking, counting the number of visitors, number of vehicles in traffic etc.
#  It is able to learn and identify the foreground mask.
# As the name suggests, it is able to subtract or eliminate the background portion in an image. Its output is a 
# binary segmented image which essentially gives information about the non-stationary objects in the image.
#  There lies a problem in this concept of finding non-stationary portion, as the shadow of the moving object
#  can be moving and sometimes being classified in the foreground.
# The popular Background subtraction algorithms are: 
 

# BackgroundSubtractorMOG : It is a gaussian mixture based background segmentation algorithm.
# BackgroundSubtractorMOG2: It uses the same concept but the major advantage that it provides is in terms of 
# stability even when there is change in luminosity and better identification capability of shadows in the frames.
# Geometric multigrid: It makes uses of statistical method and per pixel bayesin segmentation algorithm.

import cv2 as cv
from cv2 import threshold
import matplotlib.pyplot as plt
import numpy as np



capture = cv.VideoCapture(0)
fgbg = cv.createBackgroundSubtractorMOG2()
fgb = cv.createBackgroundSubtractorKNN()

while True:
    isTrue, frame = capture.read()
    fgmask = fgbg.apply(frame)
    fgbmask = fgb.apply(frame)

    cv.imshow('KNNmask', fgbmask)
    cv.imshow('fgmask', fgmask)
    cv.imshow('Video', frame)


    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

cv.waitKey(0)