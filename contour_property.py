import cv2
import numpy as np

img=cv2.imread("hand1.jpg")
img=cv2.resize(img,(400,300))
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur=cv2.blur(img_gray,ksize=(2,2))
_,thresh=cv2.threshold(img_blur,242,255,cv2.THRESH_BINARY)

canny=cv2.Canny(thresh,100,200)
cnts,r=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(img,cnts,-1,(20,250,20),5)

for c in cnts:
    epsilon=0.01*cv2.arcLength(c,True)
    data=cv2.approxPolyDP(c,epsilon,True)
    hull=cv2.convexHull(data)
    
    cv2.drawContours(img,[c],-1,(20,255,60),5)
    cv2.drawContours(img,[hull],-1,(20,80,255),5)
    cv2.drawContours(img,[hull],-1,(255,234,34),6)

hull2=cv2.convexHull(cnts[0],returnPoints=False)
defect=cv2.convexityDefects(cnts[0],hull2)
print(defect)

for i in range(defect.shape[0]):
    s,e,f,d = defect[i,0]
    print(s,e,f,d)
    start = tuple(c[s][0])
    end = tuple(c[e][0])
    far = tuple(c[f][0])
    cv2.line(img,start,end,[255,0,0],2)
    cv2.circle(img,far,5,[0,0,255],-1)
    
c_max=max(cnts,key=cv2.contourArea)

extLeft=tuple(c_max[c_max[:,:,0].argmin()][0])
extRight=tuple(c_max[c_max[:,:,0].argmax()][0])
extTop=tuple(c_max[c_max[:,:,1].argmin()][0])
extButtom=tuple(c_max[c_max[:,:,1].argmax()][0])

cv2.circle(img,extLeft,8,(255,0,32),5)
cv2.circle(img,extRight,8,(255,0,32),4)
cv2.circle(img,extTop,8,(255,0,32),5)
cv2.circle(img,extButtom,20,(255,0,32),5)

# for i in range(defect.shape[0]):
#     s,e,f,d = defect[i,0]
#     print(s,e,f,d)
#     start = tuple(c[s][0])
#     end = tuple(c[e][0])
#     far = tuple(c[f][0])
#     cv2.line(img,start,end,[255,0,0],2)
#     cv2.circle(img,far,5,[0,0,255],-1)
     

cv2.imshow("img",img)
cv2.imshow("img_gray",img_gray)
cv2.imshow("thresh",thresh)
cv2.imshow("canny",canny)

cv2.waitKey(0)
cv2.destroyAllWindows()