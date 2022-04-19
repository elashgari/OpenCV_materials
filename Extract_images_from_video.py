# Importing all necessary libraries
import cv2 as cv
import os
  
# Read the video from specified path
cam = cv.VideoCapture('Videos/Kitty.mp4')
  
try:
      
    # creating a folder named data
    if not os.path.exists('data_Vid2Img'):
        os.makedirs('data')
  
# if not created then raise error
except OSError:
    print ('Error: Creating directory of data')
  
# frame
currentframe = 0
  
while(True):
      
    # reading from frame
    ret,frame = cam.read()
  
    if ret:
        # if video is still left continue creating images
        name = './data/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name)
  
        # writing the extracted images
        cv.imwrite(name, frame)
  
        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        break
  
# Release all space and windows once done
cam.release()
cv.destroyAllWindows()