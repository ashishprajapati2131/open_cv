import cv2
import numpy as np
import time


cap=cv2.VideoCapture('output.avi')
while True:
    ret,frame=cap.read()
    
    cv2.imshow("webcame",frame)
    time.sleep(1/50)
    
    
    if cv2.waitKey(1) & 0xFF==ord('x'):
        break








# cap=cv2.VideoCapture(0)
# fourcc=cv2.VideoWriter_fourcc(*'XVID')
# width=int(cap.get(3))
# height=int(cap.get(4))
# out=cv2.VideoWriter('output.avi',fourcc,20.0,(width,height))
# while True:
#     a,frame=cap.read()
#     print(a)
#     # frame=frame[:,:,0]
    
#     out.write(frame)
#     img_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2BGRA)
#     cv2.imshow("webcame",img_gray)
#     if cv2.waitKey(1) & 0xFF==ord('x'):
#         break
# out.release() 
# cv2.destroyAllWindows()