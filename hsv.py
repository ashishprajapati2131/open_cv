import cv2
import numpy as np

img=cv2.imread("color_ball.jpg")

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
def update(x):
    lh=cv2.getTrackbarPos("Lower H","mask")
    ls=cv2.getTrackbarPos("Lower S","mask")
    lv=cv2.getTrackbarPos("Lower V","mask")
    uh=cv2.getTrackbarPos("Upper H","mask")
    us=cv2.getTrackbarPos("Upper S","mask")
    uv=cv2.getTrackbarPos("Upper V","mask")
    
    lower=np.array([lh,ls,lv])
    upper=np.array([uh,us,uv])
    print(lower)
    print(upper)
    mask=cv2.inRange(hsv,lowerb=lower,upperb=upper)
    result=cv2.bitwise_and(img,img,mask)
    cv2.imshow("",mask)
    cv2.imshow("result",result)
    
cv2.namedWindow("mask")

cv2.createTrackbar("Lower H","mask",0,179,update)
cv2.createTrackbar("Lower S","mask",0,255,update)
cv2.createTrackbar("Lower V","mask",0,255,update)
cv2.createTrackbar("Upper H","mask",0,179,update)
cv2.createTrackbar("Upper S","mask",0,255,update)
cv2.createTrackbar("Upper V","mask",0,255,update)

cv2.imshow("original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()