import cv2
import numpy as np

img=cv2.imread("download.jpg")

cv2.imshow("window",img)

flip_img=cv2.flip(img,flipCode=5)
cv2.imshow("",flip_img)
cv2.imwrite("flip.jpg",flip_img)
cv2.waitKey(0)

