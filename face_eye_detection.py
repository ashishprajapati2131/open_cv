import cv2
import numpy as np

img=cv2.imread("images/group.jpg")
face=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye=cv2.CascadeClassifier("haarcascade_eye.xml")
                         # haarcascade_eye

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
# faces=face.detectMultiScale(img_gray,4,4)
faces=face.detectMultiScale(img_gray,2,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(20,255,180),5)
    
    roi=img_gray[y:y+h , x:x+w]
    roi_color=img[y:y+h , x:x+w]
    eyes=eye.detectMultiScale(roi,1.02222,2)
    for (xi,yi,wi,hi) in eyes:
        cv2.rectangle(roi_color,(xi,yi),(xi+wi,yi+hi),(0,0,255),1)
    # img[y:y+h , x:x+w]=roi_color
    # cv2.imshow("roi",roi)
    # print(eyes)
    
cv2.imshow("faces",img)
cv2.waitKey(0)
cv2.destroyAllWindows()