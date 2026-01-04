import cv2
import numpy as np
from matplotlib import pyplot as plt

img1=cv2.imread("hero1.jpg")
img2=cv2.imread("strom_breaker.jpg")

img1=cv2.resize(img1,(1024,650))
img2=cv2.resize(img2,(650,650))

r,c,t=img2.shape
roi=img1[:r,:c]

gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

_,mask=cv2.threshold(gray,50,255,cv2.THRESH_BINARY)

mask_inv=cv2.bitwise_not(mask)

img1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)

img2_fg=cv2.bitwise_and(img2,img2,mask=mask)

result=cv2.add(img1_bg,img2_fg)

# cv2.imshow("original",img1)
# cv2.imshow("img2",img2)
# cv2.imshow("roi",roi)
# cv2.imshow("gray",gray)
# cv2.imshow("mask",mask)
# cv2.imshow("inv_mask",mask_inv)
# cv2.imshow("img1_bg",img1_bg)
# cv2.imshow("img1_fg",img2_fg)
# cv2.imshow("result",result)

images=[img1,img2,roi,gray,mask,mask_inv,img1_bg,img2_fg,result]
print(len(images))

for i in range(len(images)):
    plt.subplot(4,3,i+1)
    plt.imshow(images[i])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()