import cv2 as cv
import numpy as np

img=cv.imread("black_white.png")
print(img.shape)
# img=cv.transpose(img)
# print(img.shape)
_,new_img=cv.threshold(img,80,255,cv.THRESH_BINARY)
# _,new_img=cv.threshold(img,80,255,cv.THRESH_BINARY_INV)
# _,new_img=cv.threshold(img,50,100,cv.THRESH_TOZERO)
# _,new_img=cv.threshold(img,50,255,cv.THRESH_TRUNC)
# _,new_img=cv.threshold(img,50,255,cv.THRESH_TRIANGLE,)

cv.imshow("new",new_img)
cv.imshow("img",img)
cv.waitKey(0)
cv.destroyAllWindows()