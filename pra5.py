import cv2
import numpy as np

img=cv2.imread("download.jpg")

flag=False
ix,iy=0,0
def draw(event,x,y,flags,param):
    print(event)
    global flag,ix,iy
    if(event==1):
        print("press")
        flags=True
        ix=x
        iy=y
    elif event==4:
        print("release")
        new_img=img[iy:y,ix:x,:]
        cv2.imshow("new",new_img)
        cv2.waitKey(0)
        flag=False
cv2.namedWindow("window")
cv2.setMouseCallback("window",draw)
cv2.imshow("window",img)
cv2.waitKey(0)