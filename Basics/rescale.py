# Scaling comes in handy in many image processing as well as machine learning applications. 
# It helps in reducing the number of pixels from an image and that has several advantages e.g. 
# It can reduce the time of training of a neural network as more is the number of pixels in an 
# image more is the number of input nodes that in turn increases the complexity of the model.
# It also helps in zooming in images. Many times we need to resize the image i.e. either shrink
#  it or scale up to meet the size requirements. OpenCV provides us several interpolation methods for resizing an image.
 

# Choice of Interpolation Method for Resizing – 

# cv2.INTER_AREA: This is used when we need to shrink an image.
# cv2.INTER_CUBIC: This is slow but more efficient.
# cv2.INTER_LINEAR: This is primarily used when zooming is required. This is the default interpolation technique in OpenCV.



import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

##########################Function for rescaling
# def rescaleFrame(frame, scale=0.25):
#     #proper for images/videos/live videos***********************************
#     height = int(frame.shape[0]*scale)
#     width = int(frame.shape[1]*scale)
#     dimensions = (width, height)

#     return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)


#########################rescaling images
# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat',img)
# resized_image = rescaleFrame(img)
# cv.imshow('Image', resized_image)
# cv.waitKey(0)

#########################rescaling videos

# capture = cv.VideoCapture(0) #webcam
# # capture = cv.VideoCapture('Videos/Kitty.mp4')
# while True:
#     isTrue, frame = capture.read()
#     frame_resized = rescaleFrame(frame)
#     cv.imshow('Video', frame)
#     cv.imshow('Video_resized', frame_resized)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()
###########################Image Resizing 
img = cv.imread('Photos/cat.jpg')
half = cv.resize(img, (0, 0), fx = 0.1, fy = 0.1)
bigger = cv.resize(img, (1050, 1610))
 
stretch_near = cv.resize(img, (780, 540),
               interpolation = cv.INTER_NEAREST)
 
 
Titles =["Original", "Half", "Bigger", "Interpolation Nearest"]
images =[img, half, bigger, stretch_near]
count = 4
 
for i in range(count):
    plt.subplot(2, 2, i + 1)
    plt.title(Titles[i])
    plt.imshow(images[i])
 
plt.show()




cv.waitKey(0)