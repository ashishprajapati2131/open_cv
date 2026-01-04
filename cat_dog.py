import cv2
import numpy as np

cat=cv2.CascadeClassifier("haarcascade_frontalcatface (1).xml")

cam=cv2.VideoCapture(0)

while True:
    # img=cv2.imread("dogcat2.jpg")
    _,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    cats=cat.detectMultiScale(gray,1.01,1)

    for (x,y,w,h) in cats:
        cv2.rectangle(img=img,pt1=(x,y),pt2=(x+w,y+h),color=(50,255,50),thickness=4)
    # print(cats)
    cv2.imshow("img",img)
    
    if cv2.waitKey(1) and 0xFF==ord('x'):
        break
cv2.waitKey(0)
cv2.destroyAllWindows()
