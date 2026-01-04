import cv2
import numpy as np

cam=cv2.VideoCapture("video2.mp4")

algo1=cv2.createBackgroundSubtractorMOG2()
algo2=cv2.createBackgroundSubtractorKNN()

while True:
    ret,frame=cam.read()
    if not ret:
        break
    
    algo1_mask=algo1.apply(frame)
    algo2_mask=algo2.apply(frame)
    
    cv2.imshow("video",frame)
    cv2.imshow("createBackgroundSubtractorMOG2",algo1_mask)
    cv2.imshow("createBackgroundSubtractorKNN",algo2_mask)
    
    cv2.waitKey(5)
    
    keybord=cv2.waitKey(10)
    if keybord=='q' or keybord==27:
        break
cv2.destroyAllWindows()