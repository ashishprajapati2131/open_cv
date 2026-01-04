import cv2

# Load image
img = cv2.imread("images/a.jpg")

# Initialize HOG descriptor
hog = cv2.HOGDescriptor()

# Load pre-trained SVM for people detection
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Detect people
boxes, weights = hog.detectMultiScale(
    img,
    winStride=(8, 8),
    padding=(8, 8),
    scale=1.05
)

# Draw bounding boxes
for (x, y, w, h) in boxes:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("People Detection (HOG)", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
