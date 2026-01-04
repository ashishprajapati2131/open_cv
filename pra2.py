import cv2
import numpy as np

img=np.zeros((512,512,3))

flag=False
ix=0
iy=0
def draw(event,x,y,flags,params):
    print(event)
    global flag,ix,iy
    if(event==1):
        flag=True
        ix=x
        iy=y
        print("mouse click")
        cv2.circle(img,radius=25,center=(x,y),thickness=-1,color=(0,0,255))
        cv2.imshow("window",img)
        # cv2.waitKey(0)
    elif(event==4):
        print("release")
        # cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(155,67,34),thickness=10)
        
cv2.namedWindow(winname="window")
cv2.setMouseCallback("window",draw)
cv2.imshow("window",img)
cv2.waitKey(0)