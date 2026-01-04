import cv2
import numpy as np

img=cv2.imread("col_balls.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,mask=cv2.threshold(gray,230,255,cv2.THRESH_BINARY)

# kernal=np.ones((2,2),np.uint8)
# erosion=cv2.erode(mask,kernel=kernal,iterations=5)

# dialion=cv2.dilate(mask,kernal,iterations=3)
# cv2.imshow("img",img)
# cv2.imshow("gray",gray)
# cv2.imshow("th1",mask)
# cv2.imshow("erosion",erosion)
# cv2.imshow("dilate",dialion)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
kernal=np.ones((5,5),np.uint8)

opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel=kernal)
closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel=kernal)
gradient=cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel=kernal)
tophat=cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernel=kernal)

cv2.imshow("opening ",opening)
cv2.imshow("clossing",closing)
cv2.imshow("gradient",gradient)
cv2.imshow("tohpat",tophat)

cv2.waitKey(0)
cv2.destroyAllWindows()