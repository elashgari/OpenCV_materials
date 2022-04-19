import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    haar_cascade = cv.CascadeClassifier('haar_face.xml')
    faces_rect = haar_cascade.detectMultiScale(frame, scaleFactor = 1.1, minNeighbors = 8) 
    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0), thickness=3)

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()







# cv.waitKey(0)