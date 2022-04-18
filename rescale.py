import cv2 as cv

##########################Function for rescaling
def rescaleFrame(frame, scale=0.25):
    #proper for images/videos/live videos***********************************
    height = int(frame.shape[0]*scale)
    width = int(frame.shape[1]*scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)


#########################rescaling images
# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat',img)
# resized_image = rescaleFrame(img)
# cv.imshow('Image', resized_image)
# cv.waitKey(0)

#########################rescaling videos

capture = cv.VideoCapture(0) #webcam
# capture = cv.VideoCapture('Videos/Kitty.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video_resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

cv.waitKey(0)