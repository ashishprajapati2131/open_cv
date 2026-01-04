import numpy as np
import cv2
print("\n\n")
img=cv2.imread("download.jpg")
print(img.shape)

# img_crop=img[60:160,70:200,2]

# resize_img=cv2.resize(img,(500,500))

# gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2HLS_FULL)

imgB=img[:,:,0]
imgG=img[:,:,1]
imgR=img[:,:,2]

gray_img=np.vstack((imgB,imgG,imgR))
gray_img=np.hstack((gray_img,gray_img,gray_img))
print(gray_img.shape)

new_img=np.zeros((512,512,3))

cv2.rectangle(new_img,pt1=(100,100),pt2=(400,400),thickness=5,color=(255,255,0))

cv2.circle(new_img,center=(250,250),radius=142,color=(200,255,100),thickness=10)

cv2.line(new_img,pt1=(100,100),pt2=(400,400),color=(255,20,30),thickness=10)

cv2.line(new_img,pt1=(400,100),pt2=(100,400),color=(255,20,30),thickness=10)

cv2.putText(new_img,text="Prajapati ashish",org=(5,60),fontScale=2,fontFace=cv2.FONT_ITALIC,color=(0,0,255),thickness=5)

cv2.imshow("aroplane",new_img)
cv2.waitKey(0)