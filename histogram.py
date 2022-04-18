import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photos/cat.jpg')
resized = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blank = np.zeros(resized.shape[:2], dtype='uint8')
mask = cv.circle(blank, (resized.shape[1]//2,resized.shape[0]//2), 100, 255, -1)

masked =  cv.bitwise_and(resized, resized, mask=mask)
cv.imshow('masked', masked)

#Grayscale histogram
# gray_hist = cv.calcHist([gray],[0], mask, [256],[0,256])
# plt.figure()
# plt.xlabel('Bins')
# plt.ylabel('# of Pixels')
# plt.title('Gray histogram')
# plt.plot(gray_hist)
# plt.show()


#color histogram
plt.figure()
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.title('color histogram')

colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([resized],[i], mask, [256], [0,256])
    plt.plot(hist, color =col)
    plt.xlim([0,256])
plt.show()

