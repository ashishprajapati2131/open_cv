import cv2
import numpy as np

img=cv2.imread("page.jpg")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,th1=cv2.threshold(gray,80,150,cv2.THRESH_BINARY)
# adaptive=cv2.threshold(gray,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,255,cv2.THRESH_BINARY)

adaptive=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,5)
adaptive2=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,7,9)
cv2.imshow("original",img)
cv2.imshow("thresh",th1)
cv2.imshow("adaptive",adaptive)
cv2.imshow("adaptive2",adaptive2)
cv2.waitKey(0)
cv2.destroyAllWindows()