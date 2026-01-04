import numpy as np
import cv2

img1=cv2.imread("blend1.jpg")
img2=cv2.imread("blend2.jpg")

img1=cv2.resize(img1,(420,240))
img2=cv2.resize(img2,(420,240))

# img3=cv2.add(img1,img2)
def blend(x):
    alpha=x/100
    img3=cv2.addWeighted(img1,alpha,img2,1-alpha,1)
    cv2.imshow("img3",img3)
    cv2.waitKey(0)
    cv2.destroyWindow()
cv2.namedWindow("track-win")
cv2.createTrackbar('alpha','track-win',0,100,blend)
# cv2.imshow("trackbar",)
cv2.imshow("img1",img1)
cv2.imshow("img2",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()