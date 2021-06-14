import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('rdj.jpg')
#img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
face = cv.imread('rdjface.jpg')
#face = cv.cvtColor(face,cv.COLOR_BGR2RGB)
#methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
#'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
# for m in methods:
#     imcopy = img.copy()
#     method =eval(m)
#     #temp matching
#     res = cv.matchTemplate(imcopy,face,method)
#     min_val,max_val,min_loc,max_loc = cv.minMaxLoc(res)
#     if method in [cv.TM_SQDIFF,cv.TM_SQDIFF_NORMED]:
#         top_left = min_loc
#     else:
#         top_left = max_loc
#     height,width,channels = img.shape
#     bright = (top_left[0]+width,top_left[1]+height)
#     cv.rectangle(imcopy,top_left,bright,(255,255,255),thickness=3)
#     cv.imshow('img',res)
#     cv.imshow('img1',imcopy)
#     cv.waitKey(0)
#     cv.destroyAllWindows()
imcopy = img.copy()
font = cv.FONT_HERSHEY_SIMPLEX
method = cv.TM_SQDIFF_NORMED
res = cv.matchTemplate(imcopy,face,method)
if res.all():
    print('FOUND')
min_val,max_val,min_loc,max_loc = cv.minMaxLoc(res)
if method in [cv.TM_SQDIFF,cv.TM_SQDIFF_NORMED]:
    top_left = min_loc
else:
    top_left = max_loc
height,width,channels = face.shape
bright = (top_left[0]+width,top_left[1]+height)
cv.rectangle(imcopy,top_left,bright,(255,255,255),thickness=3)
cv.putText(imcopy,'Face',top_left, font, 1,(255,255,255),2,cv.LINE_AA)
cv.imshow('img',res)
cv.imshow('img1',imcopy)
#im_v = cv.hconcat([res,imcopy]) ###doesnt work because image not in the same size
#cv.imshow('Final',im_v)
plt.subplot(121)
plt.imshow(res)
plt.title('HMP')
print('\n')
plt.subplot(122)
plt.imshow(imcopy)
plt.title('img')
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()

