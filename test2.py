import cv2
import numpy as np

arr=np.ones((29,1,2))
print(arr[0][0].ravel())
for i in arr:
    print(i[0].ravel())