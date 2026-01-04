import cv2
import numpy as np

# img=cv2.imread("chess.jpg")
img=cv2.imread("shapes.png")
img=cv2.resize(img,(400,400))

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,70,255)

# lines=cv2.HoughLines(edges,1,np.pi/180,200)
# # print(lines)

# for rho,theta in lines[1]:
#     a=np.cos(theta)
#     b=np.sin(theta)
#     x0=a*rho
#     y0=b*rho
#     x1=int(x0-100*b)
#     y1=int(y0+100*a)
#     x2=int(x0+500*b)
#     y2=int(y0-100*a)
    
#     cv2.line(img,pt1=(int(x0),int(y0)),pt2=(x2,y2),color=(0,255,0),thickness=4)
    
#     print("lines",x1,y1,x2,y2)


lines=cv2.HoughLinesP(edges,1,np.pi/180,30,minLineLength=25,maxLineGap=20)
for line in lines:
    x1,y1,x2,y2=line[0]
    cv2.line(img,pt1=(x1,y1),pt2=(x2,y2),color=(20,23,200),thickness=2)
cv2.imshow("img",img)
cv2.imshow("gray",gray)
cv2.imshow("edges",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()