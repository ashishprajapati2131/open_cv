import cv2
import numpy as np

cam=cv2.VideoCapture(0)
def nothing(x):
    pass
cv2.namedWindow("track")
cv2.createTrackbar("lh","track",0,255,nothing)
cv2.createTrackbar("ls","track",0,255,nothing)
cv2.createTrackbar("lv","track",0,255,nothing)
cv2.createTrackbar("uh","track",255,255,nothing)
cv2.createTrackbar("us","track",255,255,nothing)
cv2.createTrackbar("uv","track",255,255,nothing)

while True:
    _,frame=cam.read()
    frame=cv2.resize(frame,(400,400))
    
    hsv_img=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lh=cv2.getTrackbarPos("lh","track")
    ls=cv2.getTrackbarPos("ls","track")
    lv=cv2.getTrackbarPos("lv","track")
    uh=cv2.getTrackbarPos("uh","track")
    us=cv2.getTrackbarPos("us","track")
    uv=cv2.getTrackbarPos("uv","track")
    
    th1=np.array([lh,ls,lv])
    th2=np.array([uh,us,uv])
    
    # ret,thresh=cv2.threshold(gray_img,th1,th2,cv2.THRESH_BINARY_INV)
    # thresh=cv2.blur(thresh,(3,3))
    mask=cv2.inRange(hsv_img,th1,th2)
    mask=cv2.bitwise_not(mask)
    filter=cv2.bitwise_and(frame,frame,mask=mask)
    
    cnts,hier=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    cv2.drawContours(frame,cnts,-1,(0,255,50),5)
    
    cv2.imshow("video",frame)
    cv2.imshow("gray",hsv_img)
    cv2.imshow("filter",filter)
    cv2.imshow("thresha",mask)
    
    
    if cv2.waitKey(1) & 0xFF=='x':
        break
    
cv2.waitKey(0)
cv2.destroyAllWindows()