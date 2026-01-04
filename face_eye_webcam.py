import cv2
import numpy as np

# cam=cv2.VideoCapture("https://www.vecteezy.com/video/70140687-a-powerful-close-up-of-a-smiling-asian-woman-s-eye")
cam=cv2.VideoCapture(0)
face=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye=cv2.CascadeClassifier("haarcascade_eye.xml")

while True:
    rel,frame=cam.read()
    frame=cv2.flip(frame,2)
    # frame=cv2.imread("a.jpg")
    # frame.resize((700,700))
    img_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # thresh=cv2.threshold(frame,cv2.THRESH_BINARY,200,255,)
    # ret, img_gray = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY_INV)
    faces=face.detectMultiScale(img_gray,1.1,4)
    
    print(faces)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(20,255,20),5)
        cv2.rectangle(img=frame,pt1=(x,y),pt2=(x+w,y+h),color=(20,12,201),thickness=5)
        
    if cv2.waitKey(1) and 0xFF==ord('x'):
        break
    # frame=cv2.resize(frame,(200,200))
    # cv2.imshow("gray",img_gray)
    cv2.imshow("video",frame)
    
cam.release()
cv2.destroyAllWindows()