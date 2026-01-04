# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 00:05:46 2020

@author: NISHANT
"""
#BackProjection using histogram technique

# import cv2
# import numpy as np


# original_image = cv2.imread("img_green.jpg")
# original_image = cv2.resize(original_image,(600,650))
# hsv_original = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)

# roi = cv2.imread("green.jpg")
# hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)


# # Histogram ROI
# roi_hist = cv2.calcHist([hsv_roi], [0, 1], None, [180, 256], [0, 180, 0, 256])
# mask = cv2.calcBackProject([hsv_original], [0, 1], roi_hist, [0, 180, 0, 256], 1)

# # Filtering remove noise
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
# mask = cv2.filter2D(mask, -1, kernel)
# _, mask = cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)

# mask = cv2.merge((mask, mask, mask))
# result = cv2.bitwise_or(original_image, mask)

# cv2.imshow("Mask", mask)
# cv2.imshow("Original image", original_image)
# cv2.imshow("Result", result)
# cv2.imshow("Roi", hsv_original)
# cv2.waitKey(0)
# cv2.destroyAllWindows()





import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("img_green.jpg")
img=cv2.resize(img,(600,650))

img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

roi=cv2.imread("green.jpg")
roi_hsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

roi_hist=cv2.calcHist([roi_hsv],[0,2],None,[180,256],[0,180,0,256])
# cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

mask=cv2.calcBackProject([img_hsv],[0,1],roi_hist,[0,180,0,256],1)

print(mask.shape)
kernal=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
mask=cv2.filter2D(mask,-1,kernal)

_,mask=cv2.threshold(mask,200,255,cv2.THRESH_BINARY)
mask=cv2.merge((mask,mask,mask))
print(img.shape)
# print(mask.shape)
result=cv2.bitwise_or(img,mask)
# plt.plot(roi_hist)
# plt.show()

cv2.imshow("img",img)
cv2.imshow("img_hsv",img_hsv)
cv2.imshow("roi",roi)
cv2.imshow("roi_hsv",roi_hsv)
cv2.imshow("resut",result)
cv2.imshow("mask",mask)
cv2.waitKey()
cv2.destroyAllWindows()

