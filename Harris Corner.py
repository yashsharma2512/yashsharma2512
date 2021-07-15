from typing import no_type_check
import cv2 as cv
import numpy as np
#from numpy.lib.type_check import _imag_dispatcher

image = cv.imread('alan.jpg')
gray= cv.cvtColor(image,cv.COLOR_BGR2GRAY)
#gray = cv.GaussianBlur(gray,(5,5),1)
gray = np.float32(gray)
dst = cv.cornerHarris(src=gray,blockSize=2,ksize=3,k=0.04)
dst=cv.dilate(dst,None)
#gray = np.float32(gray)
# mask = dst
# mask=np.float32(mask)
# x = cv.bitwise_and(gray,gray,mask=dst)
image[dst>0.01*dst.max()]=[255,0,0]
cv.imshow('frame',image)
cv.imshow('dst',dst)
# 
print(gray.shape)
print(dst.shape)
cv.waitKey(0)
cv.destroyAllWindows()