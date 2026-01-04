import cv2
import numpy as np
from matplotlib import pyplot as plt

img=np.zeros((200,200),np.uint8)
cv2.rectangle(img,(0,100),(200,200),(255),-1)
cv2.rectangle(img,(0,50),(50,100),(127),-1)

img=cv2.imread("logo.jpg")


# hist=cv2.calcHist([img],[0],None,[256],[0,256])
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hist=cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist)
plt.show()

# cv2.imshow("img",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# equ=cv2.equalizeHist(img)

clahe=cv2.createCLAHE(clipLimit=2,tileGridSize=(8,8))
equ=clahe.apply(img)
cv2.imshow("equ",equ)
cv2.waitKey(0)

hist1=cv2.calcHist(equ,[0],None,[256],[0,256])
plt.plot(hist1)
plt.show()