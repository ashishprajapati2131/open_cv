import cv2
import numpy as np

cap=cv2.VideoCapture("video1.mp4")

feature_param=dict(maxCorners=100,
                   qualityLevel=0.04,
                   minDistance=10,
                   blockSize=7)

lk_params=dict(winSize=(15,15),
               maxLevel=2,
               criteria=(cv2.TermCriteria_EPS|cv2.TermCriteria_COUNT,10,0.03))

color=np.random.randint(0,255,(100,3))

ret,old_frame=cap.read()
old_gray=cv2.cvtColor(old_frame,cv2.COLOR_BGR2GRAY)
p0=cv2.goodFeaturesToTrack(old_gray,mask=None,**feature_param)

mask=np.zeros_like(old_gray)

while True:
    ret,frame=cap.read()
    
    if not ret:
        break
    
    frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    p1,st,err=cv2.calcOpticalFlowPyrLK(old_gray,frame_gray,p0,None,**lk_params)
    
    good_new=p1[st==1]
    good_old=p0[st==1]
    
    for i,(new,old) in enumerate(zip(good_new,good_old)):
        a,b=new.ravel()
        c,d=old.ravel()
        mask=cv2.line(mask,(int(a),int(b)),(int(c),int(d)),color[i].tolist(),2)
        frame=cv2.circle(frame,(int(a),int(b)),5,color[i].tolist(),-1)
    
    mask_color=cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
    
    img=cv2.add(frame,mask_color)
    print("frame",frame.shape,"   mask",mask.shape)
    
    cv2.imshow("video",img)
    if cv2.waitKey(1) and 0xFF==ord('x'):
        break

cap.release()
cv2.destroyAllWindows()