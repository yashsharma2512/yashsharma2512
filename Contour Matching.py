import cv2 as cv
import numpy as np
img = cv.imread('rdj.jpg')
<<<<<<< Updated upstream
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray,(5,5),1)
can = cv.Canny(blur,100,100)
cv.imshow('can',can)
contours,h = cv.findContours(blur,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)



=======
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
can = cv.Canny(gray,100,100)
blur = cv.GaussianBlur(can,(5,5),5)
contour,h = cv.findContours(blur,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
exc = np.zeros(img.shape,np.uint8)
ixc = np.zeros(img.shape,np.uint8)

for i in range(len(contour)):
    if h[0][i][3] == -1:
        cv.drawContours(exc,contour,i,(255,255,255),-1)
        #cv.drawContours (img,contour,i,(0,0,255),2)
for i in range(len(contour)):
    if h[0][i][3] != -1:
        cv.drawContours(ixc,contour,i,(255,255,255),-1)
        #cv.drawContours (img,contour,i,(0,255,0),2)
print(img.shape)
print(ixc.shape)
mask = cv.cvtColor(exc,cv.COLOR_BGR2GRAY)
print(mask.shape)
res = cv.bitwise_and(img,exc)
# ixc = np.uint8(ixc)\

cv.imshow('Image',exc)
cv.imshow('mage',ixc)
cv.imshow('img',img)
cv.imshow('mask',mask)
cv.imshow('res',res)
>>>>>>> Stashed changes
cv.waitKey(0)
cv.destroyAllWindows()