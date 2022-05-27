import os
import cv2 as cv

filepath = 'C:/Users/Kim eunhye/Desktop/imageSet/'
directory_path = 'C:/Users/Kim eunhye/Desktop/anyfile/'

data_list = os.listdir(filepath)
i=0

for name in data_list :
    image = cv.imread(filepath+name, 0)
    ret, image = cv.threshold(image, 118, 255, cv.THRESH_BINARY)
    cv.imwrite(directory_path+name, image)

'''
i=0
image = cv.imread(filepath+data_list[0],0)
cv.imshow('original', image)
ret, image = cv.threshold(image, 118, 255, cv.THRESH_BINARY)
cv.imshow('THRESH_BINARY', image)
print(data_list[0])
#cv.imwrite(directory_path+"image_%05d_000.png" % i, image)
image = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,15,2)
cv.imshow('adaptive', image)
'''
