##########################################################################################
#                   Parkwise Senior Design Project, Updated 2/28/23                      #
##########################################################################################

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
import numpy as np
from mss import mss

bounding_box = {'top': 400, 'left': 185, 'width': 1750, 'height': 1000}
sct = mss()
i = 0
#Video feed selection

cap = cv.VideoCapture(r'C:\Users\beaum\OneDrive\Desktop\Capstone2_Project_1\Images\PullingOutVideo.MOV')
#cap = cv.VideoCapture(r'C:\Users\beaum\OneDrive\Desktop\Capstone2_Project_1\Images\PullingInVideo.MOV')
img = cv.imread(r'C:\Users\beaum\OneDrive\Desktop\Capstone2_Project_1\newest model 1.jpg')
#Global Variables
frame_counter = 0
  #fetch the service account key JSON file contents 
cred = credentials.Certificate('ServiceAccountKey.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://fir-knob4ugo-default-rtdb.firebaseio.com/'
    })

def changeImage(frame):

    #Attempting to fix Unbound Local Error Fix by declaring spot values before use
    Spot1Status = None
    Spot2Status = None
    Spot3Status = None
    Spot4Status = None
    Spot5Status = None
    Spot6Status = None
    Spot7Status = None
    Spot8Status = None
    Spot9Status = None
    Spot10Status = None
    Spot11Status = None
    Spot12Status = None

# Attempting to change the original image before being cropped and then croppping that
# Median 61, thresh 21,1
    imgGray2 = cv.cvtColor(frame,cv.COLOR_BGRA2GRAY)
    imgBlur2 = cv.GaussianBlur(imgGray2,(3,5),5)
    imgThreshold2 = cv.adaptiveThreshold(imgBlur2,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,5,1)
    imgMedian2 = cv.medianBlur(imgThreshold2,15)

    # Spot 1 filtered and cut out spot
    
    mask = np.zeros(imgMedian2.shape, dtype=np.uint8)
    roi_corners = np.array([[(105,80), (320,80), (230,440),(105,430)]], dtype=np.int32)
    cv.circle(frame,(105,80), 5, (0,0,255), -1)
    cv.circle(frame,(320,80), 5, (0,0,255), -1)
    cv.circle(frame,(320,440), 5, (0,0,255), -1)
    cv.circle(frame,(105,430), 5, (0,0,255), -1)
    channel_count = frame.shape[2]  # i.e. 3 or 4 depending on your image
    ignore_mask_color = (255,)*channel_count
    cv.fillPoly(mask, roi_corners, ignore_mask_color)
    newImage = cv.bitwise_and(imgMedian2, mask)

    # Spot 2 filtered and cut out spot
    
    mask2 = np.zeros(imgMedian2.shape, dtype=np.uint8)
    roi_corners2 = np.array([[(420,80),(586,80),(590,452),(406,452)]], dtype=np.int32)
    
    cv.circle(frame,(420,80), 5, (0,0,255), -1)
    cv.circle(frame,(586,80), 5, (0,0,255), -1)
    cv.circle(frame,(590,452), 5, (0,0,255), -1)
    cv.circle(frame,(406,452), 5, (0,0,255), -1)
    #cv.circle(frame,(515,541), 5, (0,0,255), -1)
    
    channel_count = frame.shape[2]  # i.e. 3 or 4 depending on your image
    ignore_mask_color = (255,)*channel_count
    cv.fillPoly(mask2, roi_corners2, ignore_mask_color)
    newImage2 = cv.bitwise_and(imgMedian2, mask2)


    # Spot 3 filtered and cut out spot
    
    mask3 = np.zeros(imgMedian2.shape, dtype=np.uint8)
    roi_corners3 = np.array([[(686,80),(831,80),(840,466),(658,452)]], dtype=np.int32)
    
    cv.circle(frame,(686,80), 5, (0,0,255), -1)
    cv.circle(frame,(831,80), 5, (0,0,255), -1)
    cv.circle(frame,(840,466), 5, (0,0,255), -1)
    cv.circle(frame,(658,452), 5, (0,0,255), -1)
    
    #cv.circle(frame,(800,520), 5, (0,0,255), -1)
    channel_count = frame.shape[2]  # i.e. 3 or 4 depending on your image
    ignore_mask_color = (255,)*channel_count
    cv.fillPoly(mask3, roi_corners3, ignore_mask_color)
    newImage3 = cv.bitwise_and(imgMedian2, mask3)

    # Spot 4 filtered and cut out spot
    
    mask4 = np.zeros(imgMedian2.shape, dtype=np.uint8)
    roi_corners4 = np.array([[(938,90),(1106,90),(1086,465),(938,465)]], dtype=np.int32)
    
    cv.circle(frame,(938,90), 5, (0,0,255), -1)
    cv.circle(frame,(1106,90), 5, (0,0,255), -1)
    cv.circle(frame,(1086,465), 5, (0,0,255), -1)
    cv.circle(frame,(938,465), 5, (0,0,255), -1)
      
    channel_count = frame.shape[2]  # i.e. 3 or 4 depending on your image
    ignore_mask_color = (255,)*channel_count
    cv.fillPoly(mask4, roi_corners4, ignore_mask_color)
    newImage4 = cv.bitwise_and(imgMedian2, mask4)

    # Spot 5 filtered and cut out spo
    
    mask5 = np.zeros(imgMedian2.shape, dtype=np.uint8)
    roi_corners5 = np.array([[(1210,90),(1340,90),(1330,465),(1190,465)]], dtype=np.int32)

    cv.circle(frame,(1200,90), 5, (0,0,255), -1)
    cv.circle(frame,(1350,90), 5, (0,0,255), -1)
    cv.circle(frame,(1330,465), 5, (0,0,255), -1)
    cv.circle(frame,(1190,465), 5, (0,0,255), -1)
    
    channel_count = frame.shape[2]  # i.e. 3 or 4 depending on your image
    ignore_mask_color = (255,)*channel_count
    cv.fillPoly(mask5, roi_corners5, ignore_mask_color)
    newImage5 = cv.bitwise_and(imgMedian2, mask5)

    # Spot 6 filtered and cut out spot
    
    mask6 = np.zeros(imgMedian2.shape, dtype=np.uint8)
    roi_corners6 = np.array([[(1440,100),(1610,100),(1610,479),(1428,479)]], dtype=np.int32)
    
    cv.circle(frame,(1440,100), 5, (0,0,255), -1)
    cv.circle(frame,(1610,100), 5, (0,0,255), -1)
    cv.circle(frame,(1610,479), 5, (0,0,255), -1)
    cv.circle(frame,(1428,479), 5, (0,0,255), -1)
    
    channel_count = frame.shape[2]  # i.e. 3 or 4 depending on your image
    ignore_mask_color = (255,)*channel_count
    cv.fillPoly(mask6, roi_corners6, ignore_mask_color)
    newImage6 = cv.bitwise_and(imgMedian2, mask6)
    

    # Spot 7 filtered and cut out spot
    
    mask7 = np.zeros(imgMedian2.shape, dtype=np.uint8)
    roi_corners7 = np.array([[(91,519),(322,519),(301,865),(77,865)]], dtype=np.int32)
    
    cv.circle(frame,(91,519), 5, (0,0,255), -1)
    cv.circle(frame,(322,519), 5, (0,0,255), -1)
    cv.circle(frame,(301,865), 5, (0,0,255), -1)
    cv.circle(frame,(77,865), 5, (0,0,255), -1)
    
    channel_count = frame.shape[2]  # i.e. 3 or 4 depending on your image
    ignore_mask_color = (255,)*channel_count
    cv.fillPoly(mask7, roi_corners7, ignore_mask_color)
    newImage7 = cv.bitwise_and(imgMedian2, mask7)

    # Spot 8 filtered and cut out spot
    
    mask8 = np.zeros(imgMedian2.shape, dtype=np.uint8)
    roi_corners8 = np.array([[(399,519),(588,519),(560,865),(371,865)]], dtype=np.int32)
    
    cv.circle(frame,(399,519), 5, (0,0,255), -1)
    cv.circle(frame,(588,519), 5, (0,0,255), -1)
    cv.circle(frame,(560,865), 5, (0,0,255), -1)
    cv.circle(frame,(371,865), 5, (0,0,255), -1)
    
    channel_count = frame.shape[2]  # i.e. 3 or 4 depending on your image
    ignore_mask_color = (255,)*channel_count
    cv.fillPoly(mask8, roi_corners8, ignore_mask_color)
    newImage8 = cv.bitwise_and(imgMedian2, mask8)

    # Spot 9 filtered and cut out spot
    
    mask9 = np.zeros(imgMedian2.shape, dtype=np.uint8)
    roi_corners9 = np.array([[(665,532),(846,532),(837,865),(658,865)]], dtype=np.int32)
    
    cv.circle(frame,(665,532), 5, (0,0,255), -1)
    cv.circle(frame,(846,532), 5, (0,0,255), -1)
    cv.circle(frame,(837,865), 5, (0,0,255), -1)
    cv.circle(frame,(658,865), 5, (0,0,255), -1)
    
    channel_count = frame.shape[2]  # i.e. 3 or 4 depending on your image
    ignore_mask_color = (255,)*channel_count
    cv.fillPoly(mask9, roi_corners9, ignore_mask_color)
    newImage9 = cv.bitwise_and(imgMedian2, mask9)

    # Spot 10 filtered and cut out spot
    
    mask10 = np.zeros(imgMedian2.shape, dtype=np.uint8)
    roi_corners10 = np.array([[(924,545),(1092,545),(1071,891),(910,891)]], dtype=np.int32)
    
    cv.circle(frame,(924,545), 5, (0,0,255), -1)
    cv.circle(frame,(1092,545), 5, (0,0,255), -1)
    cv.circle(frame,(1071,891), 5, (0,0,255), -1)
    cv.circle(frame,(910,891), 5, (0,0,255), -1)
    
    channel_count = frame.shape[2]  # i.e. 3 or 4 depending on your image
    ignore_mask_color = (255,)*channel_count
    cv.fillPoly(mask10, roi_corners10, ignore_mask_color)
    newImage10 = cv.bitwise_and(imgMedian2, mask10)

    # Spot 11 filtered and cut out spot
    
    mask11 = np.zeros(imgMedian2.shape, dtype=np.uint8)
    roi_corners11 = np.array([[(1176,545),(1404,545),(1323,904),(1162,904)]], dtype=np.int32)
    
    cv.circle(frame,(1176,545), 5, (0,0,255), -1)
    cv.circle(frame,(1404,545), 5, (0,0,255), -1)
    cv.circle(frame,(1323,904), 5, (0,0,255), -1)
    cv.circle(frame,(1162,904), 5, (0,0,255), -1)
    
    channel_count = frame.shape[2]  # i.e. 3 or 4 depending on your image
    ignore_mask_color = (255,)*channel_count
    cv.fillPoly(mask11, roi_corners11, ignore_mask_color)
    newImage11 = cv.bitwise_and(imgMedian2, mask11)

    # Spot 12 filtered and cut out spot
    
    mask12 = np.zeros(imgMedian2.shape, dtype=np.uint8)
    roi_corners12 = np.array([[(1414,565),(1610,565),(1610,917),(1414,917)]], dtype=np.int32)
    
    cv.circle(frame,(1414,565), 5, (0,0,255), -1)
    cv.circle(frame,(1610,565), 5, (0,0,255), -1)
    cv.circle(frame,(1610,917), 5, (0,0,255), -1)
    cv.circle(frame,(1414,917), 5, (0,0,255), -1)
    
    channel_count = frame.shape[2]  # i.e. 3 or 4 depending on your image
    ignore_mask_color = (255,)*channel_count
    cv.fillPoly(mask12, roi_corners12, ignore_mask_color)
    newImage12 = cv.bitwise_and(imgMedian2, mask12)

    count1 = cv.countNonZero(newImage)
    count2 = cv.countNonZero(newImage2)
    count3 = cv.countNonZero(newImage3)
    count4 = cv.countNonZero(newImage4)
    count5 = cv.countNonZero(newImage5)
    count6 = cv.countNonZero(newImage6)
    count7 = cv.countNonZero(newImage7)
    count8 = cv.countNonZero(newImage8)
    count9 = cv.countNonZero(newImage9)
    count10 = cv.countNonZero(newImage10)
    count11 = cv.countNonZero(newImage11)
    count12 = cv.countNonZero(newImage12)

    print('Count 1 is',count1)
    print('Count 2 is',count2)
    print('Count 3 is',count3)
    print('Count 4 is',count4)
    print('Count 5 is',count5)
    print('Count 6 is',count6)
    print('Count 7 is',count7)
    print('Count 8 is',count8)
    print('Count 9 is',count9)
    print('Count 10 is',count10)
    print('Count 11 is',count11)
    print('Count 12 is',count12)
    

    #Image detection threshold control

    #Spot 1
    if (count1>=24):
        Spot1Status = True
        cv.putText(frame, 'Occupied', (105,50),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),2,cv.LINE_AA)
    if (count1<=23):
        Spot1Status = False
        cv.putText(frame, 'Open', (105,50),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),2,cv.LINE_AA)

    #Spot 2
    if (count2>=41):
        Spot2Status = True
        cv.putText(frame, 'Occupied', (420,50),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),2,cv.LINE_AA)
    if (count2<=40):
        Spot2Status = False
        cv.putText(frame, 'Open', (420,50),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),2,cv.LINE_AA)

    #Spot 3
    if (count3>=41):
        Spot3Status = True
        cv.putText(frame, 'Occupied', (686,50),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),2,cv.LINE_AA)
    if (count3<=40):
        Spot3Status = False
        cv.putText(frame, 'Open', (686,50),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),2,cv.LINE_AA)

    #Spot 4
    if (count4>=41):
        Spot4Status = True
        cv.putText(frame, 'Occupied', (938,50),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),2,cv.LINE_AA)
    if (count4<=40):
        Spot4Status = False
        cv.putText(frame, 'Open', (938,50),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),2,cv.LINE_AA)

    #Spot 5
    if (count5>=320):
        Spot5Status = True
        cv.putText(frame, 'Occupied', (1218,50),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),2,cv.LINE_AA)
    if (count5<=319):
        Spot5Status = False
        cv.putText(frame, 'Open', (1218,50),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),2,cv.LINE_AA)

    #Spot 6
    if (count6>=320):
        Spot6Status = True
        cv.putText(frame, 'Occupied', (1470,50),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),2,cv.LINE_AA)
    if (count6<=319):
        Spot6Status = False
        cv.putText(frame, 'Open', (1470,50),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),2,cv.LINE_AA)

    #Spot 7
    if (count7>=71):
        Spot7Status = True
        cv.putText(frame, 'Occupied', (91,895),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),2,cv.LINE_AA)
    if (count7<=70):
        Spot7Status = False
        cv.putText(frame, 'Open', (91,895),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),2,cv.LINE_AA)

    #Spot 8
    if (count8>=41):
        Spot8Status = True
        cv.putText(frame, 'Occupied', (400,895),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),2,cv.LINE_AA)
    if (count8<=40):
        Spot8Status = False
        cv.putText(frame, 'Open', (400,895),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),2,cv.LINE_AA)

    #Spot 9
    if (count9>41):
        Spot9Status = True
        cv.putText(frame, 'Occupied', (665,895),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),2,cv.LINE_AA)
    if (count9<=40):
        Spot9Status = False
        cv.putText(frame, 'Open', (665,895),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),2,cv.LINE_AA)

    #Spot 10
    if (count10>=41):
        Spot10Status = True
        cv.putText(frame, 'Occupied', (924,895),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),2,cv.LINE_AA)
    if (count10<=40):
        Spot10Status = False
        cv.putText(frame, 'Open', (924,895),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),2,cv.LINE_AA)

    #Spot 11
    if (count11>=41):
        Spot11Status = True
        cv.putText(frame, 'Occupied', (1176,895),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),2,cv.LINE_AA)
    if (count11<=40):
        Spot11Status = False
        cv.putText(frame, 'Open', (1176,895),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),2,cv.LINE_AA)
    
    #Spot 12
    if (count12>=41):
        Spot12Status = True
        cv.putText(frame, 'Occupied', (1414,895),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),2,cv.LINE_AA)
    if (count12<=40):
        Spot12Status = False
        cv.putText(frame, 'Open', (1414,895),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),2,cv.LINE_AA)
    print (Spot5Status) 
    return frame, Spot1Status , Spot2Status, Spot3Status,Spot4Status,Spot5Status,Spot6Status,Spot7Status,Spot8Status,Spot9Status,Spot10Status,Spot11Status,Spot12Status,newImage4

def UpdateServer(Spot1Status,Spot2Status,Spot3Status,Spot4Status,Spot5Status,Spot6Status,Spot7Status,Spot8Status,Spot9Status,Spot10Status,Spot11Status,Spot12Status):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    # save data 

    ref = db.reference('AUParking')
    users_ref = ref.child('parking').set({
    
    "id" : 1, 
    "spot1" : Spot1Status,
    "spot2" : Spot2Status,
    "spot3" : Spot3Status,
    "spot4" : Spot4Status,
    "spot5" : Spot5Status,
    "spot6" : Spot6Status,
    "spot7" : Spot7Status,
    "spot8" : Spot8Status,
    "spot9" : Spot9Status,
    "spot10" : Spot10Status,
    "spot11" : Spot11Status,
    "spot12" : Spot12Status,
    "time" : current_time
             })
    
    

    
    return current_time



while(1):
    i = i+1
    #frame = cv.resize(cv.imread(r'C:\Users\beaum\Desktop\Capstone2_Project_1\Images\model1.jpg',-1), (1280, 895))
    sct_img = sct.grab(bounding_box)
    videoimage = changeImage(np.array(sct_img))
    cv.imshow('hello2',videoimage[13])
    cv.imshow('hello1',videoimage[0])
    #cv.imshow('hello',videoimage[0])

    ServerUpdate = UpdateServer(videoimage[1],videoimage[2],videoimage[3],videoimage[4],videoimage[5],videoimage[6],videoimage[7],videoimage[8],videoimage[9],videoimage[10],videoimage[11],videoimage[12])
    k = cv.waitKey(1) & 0xFF
    # press 'q' to exit
    if k == ord('q'):
        break
cv.destroyAllWindows()
    ## This is the code to use if you want to pass in a video file
'''
    ret,frame = cap.read()
    img = cv.resize((frame), (1280, 895))
    
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
'''
'''
## Newest video code
    ## This is the code to use for using the webcam feed
    sct_img = sct.grab(bounding_box)
    videoimage = changeImage(np.array(sct_img))
    cv.imshow('hello1',videoimage[0])
    ServerUpdate = UpdateServer(videoimage[1],videoimage[2],videoimage[3])
'''
