import cv2
import numpy as np

img=cv2.imread("shapes.png")
# img=cv2.imread("logo.jpg")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(gray_img,200,255,cv2.THRESH_BINARY_INV)

conts,hier=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# img=cv2.drawContours(img,conts,5,(0,0,0),4)
Areas=[]
for c in conts:
    M=cv2.moments(c)
    cX=int(M["m10"]/M["m00"])
    cy=int(M["m01"]/M["m00"])
    
    area=cv2.contourArea(c)
    Areas.append(area)
    
    if area<10000:
        epsilon=0.3*cv2.arcLength(c,True)
        data=cv2.approxPolyDP(c,epsilon,True)
        
        hull=cv2.convexHull(data)
        x,y,w,h=cv2.boundingRect(hull)
        cv2.rectangle(img,(x,y),(x+w,y+h),(20,55,255),2)
    
    cv2.drawContours(img,[c],-1,(0,255,0),2)
    cv2.circle(img,center=(cX,cy),radius=7,color=(255,245,255),thickness=-1)
    
    cv2.putText(img,"center",(cX,cy),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)
#     print(M)
print(cv2.moments(conts[0]))


cv2.imshow("img",img)
cv2.imshow("gray",gray_img)
cv2.imshow("thresh",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()