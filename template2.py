import cv2
import numpy as np

img=cv2.imread("group.jpg")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

roi=cv2.imread("gargi.jpg")
roi_gray=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)

w,h,_=roi.shape[::]
print(roi.shape[::-1])
print(w,h)
w=100
h=10
# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 
            'cv2.TM_SQDIFF_NORMED']

res=cv2.matchTemplate(img_gray,roi_gray,cv2.TM_CCOEFF_NORMED)
print(res.shape)

threshold=0.999
log=np.where(res>=threshold)

while len(res[log])<1:
    threshold-=0.001
    log=np.where(res>=threshold)


for i in zip(*log[::-1]):
    pass
    cv2.rectangle(img,pt1=(i[0],i[1]),pt2=(i[0]+w,i[0]+h),color=(0,20,200),thickness=5)
print(len(res[log]))    

img=cv2.resize(img,(600,650))
cv2.imshow("img",img)
cv2.imshow("roi",roi)
cv2.imshow("res",res)
cv2.waitKey(0)
cv2.destroyAllWindows()