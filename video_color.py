import cv2
import numpy as np

cap=cv2.VideoCapture(0)

def color_detect(x):
    pass
cv2.namedWindow("hsv")
cv2.createTrackbar("lh","hsv",0,179,color_detect)
cv2.createTrackbar("ls","hsv",0,255,color_detect)
cv2.createTrackbar("lv","hsv",0,255,color_detect)
cv2.createTrackbar("uh","hsv",179,179,color_detect)
cv2.createTrackbar("us","hsv",255,255,color_detect)
cv2.createTrackbar("uv","hsv",255,255,color_detect)

while True:
    _,img=cap.read()
    cv2.imshow("video",img)
    
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    lh=cv2.getTrackbarPos("lh","hsv")
    ls=cv2.getTrackbarPos("ls","hsv")
    lv=cv2.getTrackbarPos("lv","hsv")
    uh=cv2.getTrackbarPos("uh","hsv")
    us=cv2.getTrackbarPos("us","hsv")
    uv=cv2.getTrackbarPos("uv","hsv")

    lower=np.array([lh,ls,lv])
    upper=np.array([uh,us,uv])
    
    mask=cv2.inRange(hsv,lower,upper)
    result=cv2.bitwise_and(img,img,mask=mask)
    
    cv2.imshow("mask",mask)
    cv2.imshow("result",result)
    
    
    if cv2.waitKey(1) & 0xFF==ord('x'):
        break
cv2.destroyAllWindows()