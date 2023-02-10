##########################################################################################
#                   Parkwise Senior Design Project, Updated 2/10/23                      #
##########################################################################################


# Imports
import numpy as np
import cv2 as cv
import firebase_admin
from firebase_admin import credentials 
from firebase_admin import db
from datetime import datetime

#Video feed selection

cap = cv.VideoCapture(r'C:\Users\beaum\OneDrive\Desktop\Capstone2_Project_1\Images\PullingOutVideo.MOV')
#cap = cv.VideoCapture(r'C:\Users\beaum\OneDrive\Desktop\Capstone2_Project_1\Images\PullingInVideo.MOV')

#Global Variables
frame_counter = 0
  #fetch the service account key JSON file contents 
cred = credentials.Certificate('ServiceAccountKey.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://fir-knob4ugo-default-rtdb.firebaseio.com/'
    })

def changeImage(frame):
# Attempting to change the original image before being cropped and then croppping that
# Median 61, thresh 21,1
    imgGray2 = cv.cvtColor(frame,cv.COLOR_BGRA2GRAY)
    imgBlur2 = cv.GaussianBlur(imgGray2,(3,5),5)
    imgThreshold2 = cv.adaptiveThreshold(imgBlur2,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,21,1)
    imgMedian2 = cv.medianBlur(imgThreshold2,61)
    

    # Spot 1 filtered and cut out spot
    mask = np.zeros(imgMedian2.shape, dtype=np.uint8)
    roi_corners = np.array([[(279,486), (536,486), (494,564),(131,565)]], dtype=np.int32)
    channel_count = frame.shape[2]  # i.e. 3 or 4 depending on your image
    ignore_mask_color = (255,)*channel_count
    cv.fillPoly(mask, roi_corners, ignore_mask_color)
    newImage = cv.bitwise_and(imgMedian2, mask)

    # Spot 2 filtered and cut out spot
    mask2 = np.zeros(imgMedian2.shape, dtype=np.uint8)
    roi_corners2 = np.array([[(525,486),(720,486),(760,550),(515,535)]], dtype=np.int32)
    cv.circle(frame,(515,550), 5, (0,0,255), -1)
    #cv.circle(frame,(515,535), 5, (0,0,255), -1)
    channel_count = frame.shape[2]  # i.e. 3 or 4 depending on your image
    ignore_mask_color = (255,)*channel_count
    cv.fillPoly(mask2, roi_corners2, ignore_mask_color)
    newImage2 = cv.bitwise_and(imgMedian2, mask2)


    # Spot 3 filtered and cut out spot
    mask3 = np.zeros(imgMedian2.shape, dtype=np.uint8)
    roi_corners3 = np.array([[(755,456),(955,456),(1100,520),(800,520)]], dtype=np.int32)
    #cv.circle(frame,(800,520), 5, (0,0,255), -1)
    channel_count = frame.shape[2]  # i.e. 3 or 4 depending on your image
    ignore_mask_color = (255,)*channel_count
    cv.fillPoly(mask3, roi_corners3, ignore_mask_color)
    newImage3 = cv.bitwise_and(imgMedian2, mask3)

    count1 = cv.countNonZero(newImage)
    count2 = cv.countNonZero(newImage2)
    count3 = cv.countNonZero(newImage3)

    #Image detection threshold control
    if (count1>2001):
        Spot1Status = True
        cv.putText(frame, 'Occupied', (220,317),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),2,cv.LINE_AA)
    if (count1<2000):
        Spot1Status = False
        cv.putText(frame, 'Open', (220,317),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),2,cv.LINE_AA)
    if (count2>2001):
        Spot2Status = True
        cv.putText(frame, 'Occupied', (560,317),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),2,cv.LINE_AA)
    if (count2<2000):
        Spot2Status = False
        cv.putText(frame, 'Open', (580,317),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),2,cv.LINE_AA)
    if (count3>2001):
        Spot3Status = True
        cv.putText(frame, 'Occupied', (800,317),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),2,cv.LINE_AA)
    if (count3<2000):
        Spot3Status = False
        cv.putText(frame, 'Open', (800,317),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),2,cv.LINE_AA)
        
    return frame, Spot1Status , Spot2Status, Spot3Status

def UpdateServer(Spot1Status,Spot2Status,Spot3Status):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    # save data 
    ref = db.reference('Parking Location: Outside of AU Pharmacy/')
    users_ref = ref.child('parking')
    users_ref.set({

            "Is spot 1 occupied?" : Spot1Status,
            "Is spot 2 occupied?" : Spot2Status,
            "Is spot 3 occupied?" : Spot3Status,
            "Last Updated at" : current_time
             })
    

    
    return current_time


while(1):
    ret,frame = cap.read()
    img = cv.resize((frame), (1280, 720))
    videoimage = changeImage(img)
    frame_counter = frame_counter+1
    #If the last frame is reached, reset the capture and the frame_counter
    if frame_counter == cap.get(cv.CAP_PROP_FRAME_COUNT):
        frame_counter = 0 #Or whatever as long as it is the same as next line
        cap.set(cv.CAP_PROP_POS_FRAMES, 0)
    # Our operations on theframe_counter += 1 frame come here
    # Display the resulting frame
    cv.imshow('hello',videoimage[0])
    ServerUpdate = UpdateServer(videoimage[1],videoimage[2],videoimage[3])
    k = cv.waitKey(1) & 0xFF
    # press 'q' to exit
    if k == ord('q'):
        break
cv.destroyAllWindows()
  

