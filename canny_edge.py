import cv2
import numpy as np

img=cv2.imread("building.jpg")

img=cv2.resize(img,(500,400))
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
def change(x):
    th1=cv2.getTrackbarPos("th1","img_gray")
    th2=cv2.getTrackbarPos("th2","img_gray")
    canny=cv2.Canny(img_gray,th1,th2)
    cv2.imshow("canny",canny)


cv2.namedWindow("img_gray")
cv2.createTrackbar("th1","img_gray",0,255,change)
cv2.createTrackbar("th2","img_gray",0,255,change)

th1=cv2.getTrackbarPos("th1","img_gray")
th2=cv2.getTrackbarPos("th2","img_gray")

canny=cv2.Canny(img_gray,th1,th2)

cv2.imshow("img",img)
cv2.imshow("img_gray",img_gray)

cv2.waitKey()
cv2.destroyAllWindows()