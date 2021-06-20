import cv2 as cv
import numpy as np
img = cv.imread('rdj.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray,(5,5),1)
can = cv.Canny(blur,100,100)
cv.imshow('can',can)
contours,h = cv.findContours(blur,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)



cv.waitKey(0)
cv.destroyAllWindows()