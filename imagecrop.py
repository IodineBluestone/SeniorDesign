import numpy as np
import cv2 as cv
#from ParkingSpotClass import ParkingSpot
import numpy as np

#spot_1 = ParkingSpot((312,474,537,472,476,538,122,546)
#spot_2 = ParkingSpot((549,501,773,492,848,560,491,569)
#spot_3 = ParkingSpot((788,492,1022,485,1237,555,864,558)


# original image
# -1 loads as-is so if it will be 3 or 4 channel as the original

image = cv.resize(cv.imread(r'C:\Users\beaum\OneDrive\Desktop\Capstone2_Project_1\noimages.jpeg',-1), (1280, 720))
# mask defaulting to black for 3-channel and transparent for 4-channel
# (of course replace corners with yours)
mask = np.zeros(image.shape, dtype=np.uint8)
roi_corners = np.array([[(312,474), (537,472), (476,538),(122,546)]], dtype=np.int32)
roi_corners2 = np.array([[(549,501), (773,492), (848,560),(491,569)]], dtype=np.int32)
roi_corners3 = np.array([[(788,492), (1022,485), (1237,555),(864,558)]], dtype=np.int32)
# fill the ROI so it doesn't get wiped out when the mask is applied
channel_count = image.shape[2]  # i.e. 3 or 4 depending on your image
ignore_mask_color = (255,)*channel_count
cv.fillPoly(mask, roi_corners, ignore_mask_color)
cv.fillPoly(mask, roi_corners2, ignore_mask_color)
cv.fillPoly(mask, roi_corners3, ignore_mask_color)
# from Masterfool: use cv2.fillConvexPoly if you know it's convex

# apply the mask
masked_image = cv.bitwise_and(image, mask)
masked_image2 = cv.bitwise_and(image, mask)
masked_image3 = cv.bitwise_and(image, mask)

while(1):
    
    cv.imshow('image',masked_image)
    cv.imshow('image',masked_image2)
    cv.imshow('image',masked_image3)
    k = cv.waitKey(1) & 0xFF
    # press 'q' to exit
    if k == ord('q'):
        break
cv.destroyAllWindows()
