import cv2 as cv

#########################reading images
# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat',img)
# cv.waitKey(0)

##########################reading videos
# capture = cv.VideoCapture('Videos/Kitty.mp4')
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()
#########################resize and scaling images
def rescaleFrame(frame, scale=0.25):
    height = int(frame.shape[0]*scale)
    width = int(frame.shape[1]*scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

capture = cv.VideoCapture('Videos/Kitty.mp4')
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

