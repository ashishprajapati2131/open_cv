import cv2
import numpy as np

img=cv2.imread("logo.jpg")

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh=cv2.threshold(img_gray,70,255,cv2.THRESH_BINARY)

cnts,hier=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print(hier)

img=cv2.drawContours(img,cnts,-1,(255,240,200),2)
cv2.imshow("img",img)
cv2.imshow("img_gray",img_gray)
cv2.imshow("thresh",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()