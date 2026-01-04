import cv2
import numpy as np

img=cv2.imread("roi.jpg")
img_roi=img[55:75,165:180,:]
# 55,165
# 180,75
img[55:75,180:195,:]=img_roi
img[55:75,195:210:]=img_roi

img[55:75,150:165,:]=img_roi

cv2.imshow("window",img_roi)
cv2.imshow("roi",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
