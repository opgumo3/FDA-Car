import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('C:/Users/Kim eunhye/Desktop/imageSet/none_00093_090.png', 0)
# none_00000_090
# none_00093_090

ret, thresh1 = cv2.threshold(img,80,255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img,100,255, cv2.THRESH_BINARY)
ret, thresh3 = cv2.threshold(img,127,255, cv2.THRESH_BINARY)
ret, thresh4 = cv2.threshold(img,150,255, cv2.THRESH_BINARY)
ret, thresh5 = cv2.threshold(img,170,255, cv2.THRESH_BINARY)
'''
ret, thresh1 = cv2.threshold(img,110,255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img,115,255, cv2.THRESH_BINARY)
ret, thresh3 = cv2.threshold(img,120,255, cv2.THRESH_BINARY)
ret, thresh4 = cv2.threshold(img,125,255, cv2.THRESH_BINARY)
ret, thresh5 = cv2.threshold(img,127,255, cv2.THRESH_BINARY)
'''
#ret, thresh2 = cv2.threshold(img,127,255, cv2.THRESH_BINARY_INV)
#ret, thresh3 = cv2.threshold(img,127,255, cv2.THRESH_TRUNC)
#ret, thresh4 = cv2.threshold(img,127,255, cv2.THRESH_TOZERO)
#ret, thresh5 = cv2.threshold(img,127,255, cv2.THRESH_TOZERO_INV)

titles =['Original','80','100','127','150','170']
images = [img,thresh1,thresh2,thresh3,thresh4,thresh5]

for i in range(6):
	plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
	plt.title(titles[i])
	plt.xticks([]),plt.yticks([])

plt.show()
