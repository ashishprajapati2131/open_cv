import cv2
import numpy as np

cam=cv2.VideoCapture(0)
def temp(x):
    pass
cv2.namedWindow("setting")
cv2.createTrackbar("th1","setting",0,255,temp)
while True:
    _,frame=cam.read()
    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.medianBlur(gray,5)
    th1=cv2.getTrackbarPos("th1","setting")
    edges=cv2.Canny(gray,th1,255)
    
    circles=cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,maxRadius=100,minRadius=15)
    
    if circles is not None:
        for x,y,r in circles[0,:]:
            cv2.circle(frame,(int(x),int(y)),int(r),(240,50,200),-1)
            print(x,y,r)
        
    
    cv2.imshow("img",frame)
    cv2.imshow("edges",edges)

    if cv2.waitKey(1) and 0xFF==ord('x'):
        break
cam.release()
cv2.destroyAllWindows()


# img=cv2.imread("col_balls.jpg")
# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# edges=cv2.Canny(gray,100,255)

# circles=cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,10,param1=50,param2=30,minRadius=0,maxRadius=0)

# for x,y,r in circles[0,:]:
#     cv2.circle(img,(int(x),int(y)),int(r),(50,50,255),3)
#     cv2.circle(img,(int(x),int(y)),5,(255,255,200),-1)

# cv2.imshow("img",img)
# cv2.imshow("edges",edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
