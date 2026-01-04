import cv2
import numpy as np

img=cv2.imread("shapes.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corner=cv2.goodFeaturesToTrack(gray,100,0.01,10)

print(corner)
print(len(corner))
print(corner.shape)

for c in corner:
    x,y=c.ravel()
    # cv2.circle(img,(x,y),5,(0,0,0),5)
    cv2.circle(img, (int(x),int(y)), 4, (0, 0, 255),1)
    cv2.circle(img=img,center=(int(x),int(y)),radius=3,color=(0,0,230),thickness=-1)
    # print(x," xy ",y)
cv2.imshow("img",img)
cv2.imshow("gray",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()





# import cv2
# import numpy as np

# img=cv2.imread("shapes.png")

# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# gray=np.float32(gray)

# res=cv2.cornerHarris(gray,2,3,0.1)
# print(res.shape)
# # img=np.where(res>)
# gray[res>0.01*res.max()]=0
# img[res>0.01*res.max()]=[0,0,0]

# cv2.imshow("img",img)
# cv2.imshow("gray",gray)


# cv2.waitKey()
# cv2.destroyAllWindows()