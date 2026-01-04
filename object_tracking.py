import cv2
import numpy as np

cam=cv2.VideoCapture("video1.mp4")

ret,frame=cam.read()

r=cv2.selectROI("object",frame,False)
x,y,w,h=r
trace_window=(x,y,w,h)
cv2.imshow("roi",r)
cv2.destroyWindow("object")

roi=frame[y:y+h,x:x+w]
hsv_roi=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

mask=cv2.inRange(hsv_roi,np.array((0.,60.,32.)),np.array((180.,255.,255.)))


roi_hist=cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

term_crit=(cv2.TERM_CRITERIA_EPS|cv2.TERM_CRITERIA_COUNT,10,1)
while True:
    ret,frame=cam.read()
    
    if not ret:
        break
    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    dst=cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
    
    # ret,trace_window=cv2.meanShift(dst,trace_window,term_crit)
    ret,trace_window=cv2.CamShift(dst,trace_window,term_crit)
    
    
    x,y,w,h=trace_window
    
    cv2.rectangle(frame,(int(x),int(y)),(int(x+w),int(y+h)),(0,255,0),4)
    
    cv2.imshow("video",frame)
    
    if cv2.waitKey(1) and 0xFF==ord('x'):
        break
cam.release()
cv2.destroyAllWindows()