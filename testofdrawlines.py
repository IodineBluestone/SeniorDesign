import numpy as np
import cv2 as cv
from imageResize import resize


#img = cv.imread(r'C:\Users\beaum\OneDrive\Desktop\Capstone2_Project_1\left.jpeg')
#img2 =  resize(img,40)

ix,iy,sx,sy = -1,-1,-1,-1

# mouse callback function
def draw_lines(event, x, y, flags, param):
    global ix,iy,sx,sy
    # if the left mouse button was clicked, record the starting
    if event == cv.EVENT_LBUTTONDOWN:

        # draw circle of 2px
        cv.circle(img, (x, y), 3, (0, 0, 127), -1)

        if ix != -1: # if ix and iy are not first points, then draw a line
            cv.line(img, (ix, iy), (x, y), (0, 0, 127), 2, cv.LINE_AA)
        else: # if ix and iy are first points, store as starting points
            sx, sy = x, y
        ix,iy = x, y
        
    elif event == cv.EVENT_LBUTTONDBLCLK:
        ix, iy = -1, -1 # reset ix and iy
        if flags == 33: # if alt key is pressed, create line between start and end points to create polygon
            cv.line(img, (x, y), (sx, sy), (0, 0, 127), 2, cv.LINE_AA)

# read image from path and add callback
img = cv.resize(cv.imread(r'C:\Users\beaum\OneDrive\Desktop\Capstone2_Project_1\left.jpeg'), (1280, 720))
cv.namedWindow('image') 
cv.setMouseCallback('image',draw_lines)

while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    # press 'q' to exit
    if k == ord('q'):
        break
cv.destroyAllWindows()