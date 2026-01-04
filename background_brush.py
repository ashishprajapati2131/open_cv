import cv2
import numpy as np

# Global variables
drawing = False
value = {"FG":1, "BG":0}   # mask values for foreground/background
current_value = value["FG"]
ix, iy = -1, -1

# Colors for drawing
colors = {'FG':(0,255,0), 'BG':(0,0,255)}

img = cv2.imread("car.jpg")
img = cv2.resize(img, (800,800))
clone = img.copy()

mask = np.zeros(img.shape[:2], dtype=np.uint8)

bgModel = np.zeros((1,65), np.float64)
fgModel = np.zeros((1,65), np.float64)

def draw(event, x, y, flags, param):
    global ix, iy, drawing, current_value
    
    if event == cv2.EVENT_LBUTTONDOWN:   # Foreground draw
        drawing = True
        current_value = value["FG"]
        cv2.circle(img, (x,y), 5, colors["FG"], -1)
        cv2.circle(mask, (x,y), 5, value["FG"], -1)
        
    elif event == cv2.EVENT_RBUTTONDOWN: # Background draw
        drawing = True
        current_value = value["BG"]
        cv2.circle(img, (x,y), 5, colors["BG"], -1)
        cv2.circle(mask, (x,y), 5, value["BG"], -1)
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if current_value == value["FG"]:
                cv2.circle(img, (x,y), 5, colors["FG"], -1)
                cv2.circle(mask, (x,y), 5, value["FG"], -1)
            else:
                cv2.circle(img, (x,y), 5, colors["BG"], -1)
                cv2.circle(mask, (x,y), 5, value["BG"], -1)

    elif event == cv2.EVENT_LBUTTONUP or event == cv2.EVENT_RBUTTONUP:
        drawing = False

cv2.namedWindow("Input")
cv2.setMouseCallback("Input", draw)

while True:
    cv2.imshow("Input", img)
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('n'):    # Run GrabCut again
        cv2.grabCut(clone, mask, None, bgModel, fgModel, 5, cv2.GC_INIT_WITH_MASK)
        
        mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')
        output = clone * mask2[:, :, np.newaxis]
        
        cv2.imshow("Cutout", output)
    
    if key == 27:  # ESC to exitH
        break

cv2.destroyAllWindows()
