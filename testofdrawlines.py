import numpy as np
import cv2 as cv
#from ParkingSpotClass import ParkingSpot
import numpy as np


# Initialize Variables
ix,iy,sx,sy,lx,ly = -1,-1,-1,-1,-1,-1
counter = 0
#spot_1 = ParkingSpot((312,474,537,472,476,538,122,546)
#spot_2 = ParkingSpot((549,501,773,492,848,560,491,569)
#spot_3 = ParkingSpot((788,492,1022,485,1237,555,864,558)
def draw_lines(event, x, y, flags, param):
    
    #Declare global variables
    global ix,iy,sx,sy,lx,ly, counter

    # if the left mouse button was clicked, record the starting
    if event == cv.EVENT_LBUTTONDOWN:
       
    
        # draw circle of 2px
        cv.circle(img, (x, y), 3, (0, 0, 127), -1)

        if ix != -1: # if ix and iy are not first points, then draw a line
            cv.line(img, (ix, iy), (x, y), (0, 0, 127), 2, cv.LINE_AA)
        else: # if ix and iy are first points, store as starting points
            sx, sy = x, y
        ix,iy = x, y 

        # Counter that counts how many clicks have taken place
        counter = counter + 1
        if(counter % 4 == 0) :
         lx,ly = ix,iy
         ix,iy = -1,-1

        
    elif event == cv.EVENT_RBUTTONDOWN:
       # ix, iy = -1, -1 # reset ix and iy
       # if flags == 33: # if alt key is pressed, create line between start and end points to create polygon
            cv.line(img, (lx, ly), (sx, sy), (0, 0, 127), 2, cv.LINE_AA)

    print(ix,iy,x,y)
    print(counter)
    

    

# read image from path and add callback
img = cv.resize(cv.imread(r'C:\Users\beaum\OneDrive\Desktop\Capstone2_Project_1\noimages.jpeg'), (1280, 720))
cv.namedWindow('image') 
cv.setMouseCallback('image',draw_lines)

while(1):
    
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    # press 'q' to exit
    if k == ord('q'):
        break
cv.destroyAllWindows()