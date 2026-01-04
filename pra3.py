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
    elif(event==4):
        print("release")
        flag=False
    
    if(flag==True and event==0):
        cv2.circle(img,radius=5,center=(x,y),color=(0,0,255),thickness=-1)
        cv2.imshow("window",img)
        cv2.waitKey(0)
        
cv2.namedWindow(winname="window")
cv2.setMouseCallback("window",draw)
cv2.imshow("window",img)
cv2.waitKey(0)