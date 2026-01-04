import cv2
import numpy as np

img=cv2.imread("avengers.jpg")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(img.shape)
template=cv2.imread("head.png",0)
w,h=template.shape[::-1]

res=cv2.matchTemplate(gray_img,template,cv2.TM_CCORR_NORMED)

threshold=0.999
loc=np.where(res>=threshold)

count=0
for i in zip(*loc[::-1]):
    print("i==",i)
    cv2.rectangle(img,pt1=(i[0],i[1]),pt2=(i[0]+w,i[1]+h),color=(0,255,100),thickness=3)
    count+=1
print(count)
print("len",len(loc))

img=cv2.resize(img,(600,650))

cv2.imshow("img",img)
cv2.imshow("head",template)
cv2.waitKey(0)
cv2.destroyAllWindows()