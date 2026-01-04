import cv2
import numpy as np

img=np.zeros((512,512,3))
# img2=cv2.copyMakeBorder(img,100,110,10,10,cv2.BORDER_CONSTANT,value=[200,200,230])
img2=cv2.copyMakeBorder(img,100,110,10,10,20,value=[200,200,230])


cv2.imshow("win",img2)
def color(r):
    r=cv2.getTrackbarPos('Red','win')
    g=cv2.getTrackbarPos('Green','win')
    b=cv2.getTrackbarPos('Blue','win')
    img[:,:,0]=b
    img[:,:,1]=g
    img[:,:,2]=r
    print(img[10,10,:])
    cv2.imshow("win",img)
    
cv2.createTrackbar("Red","win",0,255,color)
cv2.createTrackbar("Green",'win',0,255,color)
cv2.createTrackbar("Blue",'win',0,255,color)
cv2.waitKey(0)
cv2.destroyAllWindows()