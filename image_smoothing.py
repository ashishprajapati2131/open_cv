import cv2
import numpy as np

img=cv2.imread("noisy.jpg")

img=cv2.resize(img,(400,400))

kernal=np.ones((5,5),np.float32)/25

h_filter=cv2.filter2D(img,-1,kernal)

blur=cv2.blur(img,(3,5))

gau=cv2.GaussianBlur(img,(3,5),0)

median_blur=cv2.medianBlur(img,5)

bi_f=cv2.bilateralFilter(img,9,75,75)

cv2.imshow("img",img)
cv2.imshow("h_filter",h_filter)
cv2.imshow("blur",blur)
cv2.imshow("gaussion",gau)
cv2.imshow("median",median_blur)
cv2.imshow("bi_f",bi_f)


cv2.waitKey(0)
cv2.destroyAllWindows()
