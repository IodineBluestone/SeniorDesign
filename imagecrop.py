import numpy as np
import cv2 as cv
#from ParkingSpotClass import ParkingSpot
import numpy as np
import time


# Coordinates for each spot
#spot_1 = ParkingSpot((312,474,537,472,476,538,122,546)
#spot_2 = ParkingSpot((549,501,773,492,848,560,491,569)
#spot_3 = ParkingSpot((788,492,1022,485,1237,555,864,558)



# Selecting the image to pass through
image = cv.resize(cv.imread(r'two.jpeg',-1), (1280, 720))
#@image = cv.resize(cv.imread(r'C:\Users\beaum\OneDrive\Desktop\Capstone2_Project_1\Images\nocars.jpeg',-1), (1280, 720))
#image = cv.resize(cv.imread(r'C:\Users\beaum\OneDrive\Desktop\Capstone2_Project_1\Images\leftspot.jpeg',-1), (1280, 720))
#image = cv.resize(cv.imread(r'C:\Users\beaum\OneDrive\Desktop\Capstone2_Project_1\Images\rightspot.jpeg',-1), (1280, 720))

# Attempting to change the original image before being cropped and then croppping that
# Median 61, thresh 21,1
imgGray2 = cv.cvtColor(image,cv.COLOR_BGRA2GRAY)
imgBlur2 = cv.GaussianBlur(imgGray2,(3,5),5)
imgThreshold2 = cv.adaptiveThreshold(imgBlur2,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,21,1)
imgMedian2 = cv.medianBlur(imgThreshold2,61)

# Spot 1 filtered and cut out spot
mask = np.zeros(imgMedian2.shape, dtype=np.uint8)
roi_corners = np.array([[(312,474), (537,472), (476,538),(122,546)]], dtype=np.int32)
channel_count = image.shape[2]  # i.e. 3 or 4 depending on your image
ignore_mask_color = (255,)*channel_count
cv.fillPoly(mask, roi_corners, ignore_mask_color)
newImage = cv.bitwise_and(imgMedian2, mask)

# Spot 2 filtered and cut out spot
mask2 = np.zeros(imgMedian2.shape, dtype=np.uint8)
roi_corners2 = np.array([[(549,501),(773,492),(848,560),(491,569)]], dtype=np.int32)
channel_count = image.shape[2]  # i.e. 3 or 4 depending on your image
ignore_mask_color = (255,)*channel_count
cv.fillPoly(mask2, roi_corners2, ignore_mask_color)
newImage2 = cv.bitwise_and(imgMedian2, mask2)


# Spot 3 filtered and cut out spot
mask3 = np.zeros(imgMedian2.shape, dtype=np.uint8)
roi_corners3 = np.array([[(850,492),(1100,485),(1300,555),(864,558)]], dtype=np.int32)
channel_count = image.shape[2]  # i.e. 3 or 4 depending on your image
ignore_mask_color = (255,)*channel_count
cv.fillPoly(mask3, roi_corners3, ignore_mask_color)
newImage3 = cv.bitwise_and(imgMedian2, mask3)




'''
# mask defaulting to black for 3-channel and transparent for 4-channel
# (of course replace corners with yours)
mask = np.zeros(image.shape, dtype=np.uint8)
mask2 = np.zeros(image.shape, dtype=np.uint8)
mask3 = np.zeros(image.shape, dtype=np.uint8)
'''

# ROI positions for all three spots
'''
roi_corners = np.array([[(312,474), (537,472), (476,538),(122,546)]], dtype=np.int32)
roi_corners2 = np.array([[(549,501), (773,492), (848,560),(491,569)]], dtype=np.int32)
roi_corners3 = np.array([[(788,492), (1022,485), (1237,555),(864,558)]], dtype=np.int32)
'''
'''
# fill the ROI so it doesn't get wiped out when the mask is applied
channel_count = image.shape[2]  # i.e. 3 or 4 depending on your image
ignore_mask_color = (255,)*channel_count
cv.fillPoly(mask, roi_corners, ignore_mask_color)
cv.fillPoly(mask2, roi_corners2, ignore_mask_color)
cv.fillPoly(mask3, roi_corners3, ignore_mask_color)
'''


# Applying the mask to crop out the parking spot
#masked_image = cv.bitwise_and(image, mask)
'''
# Applying the cropped image filtering
imgGray1 = cv.cvtColor(masked_image,cv.COLOR_BGRA2GRAY)
imgBlur1 = cv.GaussianBlur(imgGray1,(3,5),5)
imgThreshold1 = cv.adaptiveThreshold(imgBlur1,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,17,1)
imgMedian = cv.medianBlur(imgThreshold1,21)
kernal = np.ones((3,3),np.uint8)
imgDilate = cv.dilate(imgMedian,kernal,iterations=1)
'''

# Image filter using the original image
# Change values of ImgThreshold 2 and imMedian2 to find best working values
# Possible solution to getting rid of the white rectangle in the cropped picture would be to apply the image
# filter before cropping the image? 
imgGray5 = cv.cvtColor(image,cv.COLOR_BGRA2GRAY)
imgBlur5 = cv.GaussianBlur(imgGray5,(3,5),5)
imgThreshold5 = cv.adaptiveThreshold(imgBlur2,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11,1)
imgMedian5 = cv.medianBlur(imgThreshold5,41)


# Counting the number of pixels to determine if there is a car or not
count1 = cv.countNonZero(newImage)
count2 = cv.countNonZero(newImage2)
count3 = cv.countNonZero(newImage3)


if (count1>1000):
    Spot1Status = True
    cv.putText(image, 'Occupied', (290,317),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),2,cv.LINE_AA)
if (count1<1000):
    Spot1Status = False
    cv.putText(image, 'Open', (290,317),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),2,cv.LINE_AA)
if (count2>1000):
    Spot2Status = True
    cv.putText(image, 'Occupied', (550,317),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),2,cv.LINE_AA)
if (count2<1000):
    Spot2Status = False
    cv.putText(image, 'Open', (600,317),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),2,cv.LINE_AA)
if (count3>1000):
    Spot3Status = True
    cv.putText(image, 'Occupied', (900,317),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),2,cv.LINE_AA)
if (count3<1000):
    Spot3Status = False
    cv.putText(image, 'Open', (900,317),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),2,cv.LINE_AA)
    
    
        


#newImage = cv.bitwise_and(imgMedian2, mask)


while(1):
    cv.imshow('original', image)
    #print('The left sides count is ',count1)
    #cv.imshow('left',newImage)
    #cv.imshow('middle',newImage2)
    #cv.imshow('right',newImage3)
    #cv.imshow('image2',imgBlur2)
    #cv.imshow('image3',imgBlur3)
    k = cv.waitKey(1) & 0xFF
    # press 'q' to exit
    if k == ord('q'):
        break
cv.destroyAllWindows()
