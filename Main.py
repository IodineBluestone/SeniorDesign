##########################################################################################
#                   Parkwise Senior Design Project, Updated 2/28/23                      #
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
import PySimpleGUI as sg

# Initialize Variables
bounding_box = {'top': 300, 'left': 220, 'width': 1200, 'height': 600}
sct = mss()
i = 0
#Video feed selection
cap = cv.VideoCapture(r'C:\Users\beaum\Desktop\SeniorDesign-main\ParkingLotImages\PullingOutVideo.MOV')
#cap = cv.VideoCapture(r'C:\Users\beaum\OneDrive\Desktop\Capstone2_Project_1\Images\PullingInVideo.MOV')
sct_img = sct.grab(bounding_box)
newimg = (np.array(sct_img))
#Global Variables
frame_counter = 0
#fetch the service account key JSON file contents 
cred = credentials.Certificate('ServiceAccountKey.json')
ix,iy,sx,sy,lx,ly = -1,-1,-1,-1,-1,-1
counter = 0
sg.theme('System Default ')
LIGHT_GRAY_BUTTON_COLOR = f'#212021 on #e0e0e0'
DARK_GRAY_BUTTON_COLOR = '#e0e0e0 on #212021'




def draw_lines(event, x, y, flags, param):
    
     #Declare global variables
    global ix,iy,sx,sy,lx,ly, counter
        
    # if the left mouse button was clicked, record the starting
    if event == cv.EVENT_LBUTTONDOWN:
       
    
        # draw circle of 2px
        cv.circle(newimg, (x, y), 3, (0, 0, 127), -1)

        if ix != -1: # if ix and iy are not first points, then draw a line
            cv.line(newimg, (ix, iy), (x, y), (0, 0, 127), 2, cv.LINE_AA)
        else: # if ix and iy are first points, store as starting points
            sx, sy = x, y
        ix,iy = x, y 

        ## Writing X coordinate for spot click into file
        file = open('ModelParking.txt','a')

        data = str(ix)+'\n'
        file.write(data)
        file.close
        ## Writing Y coordinate for spot click into file
        file = open('ModelParking.txt','a')

        data = str(iy)+'\n'
        file.write(data)
        file.close
        # Counter that counts how many clicks have taken place
        counter = counter + 1
        if(counter % 4 == 0) :
         lx,ly = ix,iy
         ix,iy = -1,-1

        
    elif event == cv.EVENT_RBUTTONDOWN:
       # ix, iy = -1, -1 # reset ix and iy
       # if flags == 33: # if alt key is pressed, create line between start and end points to create polygon
            cv.line(newimg, (lx, ly), (sx, sy), (0, 0, 127), 2, cv.LINE_AA)
             ## Writing X coordinate for spot click into file

def changefitersettings():
    ViewParkinglayout = [
    [sg.Text(text='Change Filter Settings:',
   font=('Arial Bold', 20),
   size=20,
   expand_x=True,
   justification='center')],

   [sg.Image(filename= [],size = (300,300),key = 'image2')],

    [sg.Text(text='This will be the area where you can change the image filters of each spot.',font=('Arial', 10),size=10,expand_x=True,justification='center')],

    [sg.Text(text='Filter Setting 1:',font=('Arial Bold', 15),size=10,expand_x=True,expand_y=True),sg.Slider(range=(10, 30), default_value=12,expand_x=True,expand_y=True, enable_events=True,orientation='horizontal', key='-F1-')],

    [sg.Text(text='Filter Setting 2:',font=('Arial Bold', 15),size=10,expand_x=True,expand_y=True),sg.Slider(range=(10, 30), default_value=12,expand_x=True,expand_y=True, enable_events=True,orientation='horizontal', key='-F2-')],

    [sg.Text(text='Filter Setting 3:',font=('Arial Bold', 15),size=10,expand_x=True,expand_y=True),sg.Slider(range=(10, 30), default_value=12,expand_x=True,expand_y=True, enable_events=True,orientation='horizontal', key='-F3-')],

    [sg.Button('View Current Detection Filter', size=(1000,2), button_color=DARK_GRAY_BUTTON_COLOR)],],

    [sg.Button('Quit', size=(10,2), button_color='red')],
    
    areawindow = sg.Window('Filter Settings',ViewParkinglayout,size = (1000,1000))
    while True: 
        event,values = areawindow.read()
        if event in (None,'Quit'):
            break
        elif event == 'View Current Detection Filter':
            sct_img = sct.grab(bounding_box)
            getcountvalues = changeImage(x,np.array(sct_img))
            resized_frame_settings = cv.resize(getcountvalues[25],(1200,500))
            imgbytes_settings = cv.imencode('.png',resized_frame_settings)[1].tobytes()
            areawindow['image2'].update(data =imgbytes_settings)
    areawindow.close             

def Settings():
    Settingslayout = [
    [sg.Text(text='Edit Lot Settings:',
   font=('Arial Bold', 20),
   size=20,
   expand_x=True,
   justification='center')],

    [sg.Text(text='This will be the area where you can change the detection threshholds of each spot.',
   font=('Arial', 10),
   size=10,
   expand_x=True,
   justification='center'
   )],
    [sg.Image(filename= [],size = (300,300),key = 'image1')],
    ## Pixel Count, to be gathered from count variable and inserted into this table for easier threshold changing.
    [sg.Table([['count1','count2','count3','count4','count5','count6'], ['count7','count8','count9','count10','count11','count12']], ['Col 1','Col 2','Col 3','Col 4','Col 5','Col 6',], num_rows=2,expand_x=True,enable_events=True,key='Table1')],
    [[sg.Button('Refresh Pixel Counts', size=(200,2), button_color=DARK_GRAY_BUTTON_COLOR)]],
    ## Spot 1&2 pixel threshold control
   [sg.Text(text='Spot 1:',font=('Arial Bold', 15),size=10,expand_x=True,expand_y=True),sg.Slider(range=(10, 30), default_value=12,expand_x=True,expand_y=True, enable_events=True,orientation='horizontal', key='-SP1-')
    ,sg.Text(text='Spot 2:',font=('Arial Bold', 15),size=10,expand_x=True,expand_y=True),sg.Slider(range=(10, 30), default_value=12,expand_x=True,expand_y=True, enable_events=True,orientation='horizontal', key='-SP2-')],
    ## Spot 3&4 pixel threshold control
    [sg.Text(text='Spot 3:',font=('Arial Bold', 15),size=10,expand_x=True,expand_y=True),sg.Slider(range=(10, 30), default_value=12,expand_x=True,expand_y=True, enable_events=True,orientation='horizontal', key='-SP3-')
    ,sg.Text(text='Spot 4:',font=('Arial Bold', 15),size=10,expand_x=True,expand_y=True),sg.Slider(range=(10, 30), default_value=12,expand_x=True,expand_y=True, enable_events=True,orientation='horizontal', key='-SP4-')],
    ## Spot 5&6 pixel threshold control
    [sg.Text(text='Spot 5:',font=('Arial Bold', 15),size=10,expand_x=True,expand_y=True),sg.Slider(range=(10, 30), default_value=12,expand_x=True,expand_y=True, enable_events=True,orientation='horizontal', key='-SP5-')
    ,sg.Text(text='Spot 6:',font=('Arial Bold', 15),size=10,expand_x=True,expand_y=True),sg.Slider(range=(10, 30), default_value=12,expand_x=True,expand_y=True, enable_events=True,orientation='horizontal', key='-SP6-')],
    ## Spot 7&8 pixel threshold control
    [sg.Text(text='Spot 7:',font=('Arial Bold', 15),size=10,expand_x=True,expand_y=True),sg.Slider(range=(10, 30), default_value=12,expand_x=True,expand_y=True, enable_events=True,orientation='horizontal', key='-SP7-')
    ,sg.Text(text='Spot 8:',font=('Arial Bold', 15),size=10,expand_x=True,expand_y=True),sg.Slider(range=(10, 30), default_value=12,expand_x=True,expand_y=True, enable_events=True,orientation='horizontal', key='-SP8-')],
    ## Spot 9&10 pixel threshold control
    [sg.Text(text='Spot 9:',font=('Arial Bold', 15),size=10,expand_x=True,expand_y=True),sg.Slider(range=(10, 30), default_value=12,expand_x=True,expand_y=True, enable_events=True,orientation='horizontal', key='-SP9-')
    ,sg.Text(text='Spot 10:',font=('Arial Bold', 15),size=10,expand_x=True,expand_y=True),sg.Slider(range=(10, 30), default_value=12,expand_x=True,expand_y=True, enable_events=True,orientation='horizontal', key='-SP10-')],
    ## Spot 11&12 pixel threshold control
    [sg.Text(text='Spot 11:',font=('Arial Bold', 15),size=10,expand_x=True,expand_y=True),sg.Slider(range=(10, 30), default_value=12,expand_x=True,expand_y=True, enable_events=True,orientation='horizontal', key='-SP11-')
    ,sg.Text(text='Spot 12:',font=('Arial Bold', 15),size=10,expand_x=True,expand_y=True,),sg.Slider(range=(10, 30), default_value=12,expand_x=True,expand_y=True, enable_events=True,orientation='horizontal', key='-SP12-')],
    ##Apply Settings Button, restart program and apply desired detection values
    [[sg.Button('Apply Settings', size=(200,2), button_color=DARK_GRAY_BUTTON_COLOR)]],
    ##Display Current detection positions, Will show the current coordinates of desired spot coordinates
    [[sg.Button('View Current Detection Coordinates', size=(200,2), button_color=DARK_GRAY_BUTTON_COLOR)]],
    ##Remap Spots button, Will change the detection coordinates of each current spot
    [sg.Button('Remap Spot Locations', size=(200,2), button_color='green')]

]
    settingswindow = sg.Window('Change Detection Parameters',Settingslayout,size = (1200,1200))
    while True: 
        event,values = settingswindow.read(1)
        
        if event in (None,'Quit'):
            break
        elif event == 'Refresh Pixel Counts':
            sct_img = sct.grab(bounding_box)
            getcountvalues = changeImage(x,np.array(sct_img))
            table_data_main_menu1 = [getcountvalues[13],getcountvalues[14],getcountvalues[15],getcountvalues[16],getcountvalues[17],getcountvalues[18]], [getcountvalues[19],getcountvalues[20],getcountvalues[21],getcountvalues[22],getcountvalues[23],getcountvalues[24]]
            settingswindow['Table1'].update(values =table_data_main_menu1)
        elif event == 'Remap Spot Locations':
            open('ModelParking.txt','w').close()
            testOfDrawLines()
        elif event == 'View Current Detection Coordinates':
            sct_img = sct.grab(bounding_box)
            getcountvalues = changeImage(x,np.array(sct_img))
            resized_frame_settings = cv.resize(getcountvalues[25],(1200,500))
            imgbytes_settings = cv.imencode('.png',resized_frame_settings)[1].tobytes()
            settingswindow['image1'].update(data =imgbytes_settings)
           
            
    settingswindow.close

def testOfDrawLines():
    #img= cv.resize(cv.imread(r'C:\Users\beaum\Desktop\Capstone2_Project_1\Images\model1.jpg',-1), (1280, 720))
    cv.namedWindow('image') 
    cv.setMouseCallback('image',draw_lines)
    while(1):
        temps = []
        with open("ModelParking.txt", "r") as file:
            for line in file:
                values = line.split()
                for value in values:
                    temps.append(int(value))
        #for line in file.readlines():
         #       temps.append(int(line))
          #      file.close() 
        print(len(temps))
        cv.imshow('image',newimg)
        k = cv.waitKey(1) & 0xFF
        # press 'q' to exit
        if (len(temps) >= 96):
            print('All spots have been successfully mapped')
            break
        if k == ord('q'):
            break
    cv.destroyAllWindows()
    print(type(temps[1]))
    return temps

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://fir-knob4ugo-default-rtdb.firebaseio.com/'
    })

def changeImage(x,frame):

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
    frame_with_mapped_spots = frame
# Attempting to change the original image before being cropped and then croppping that
# Median 61, thresh 21,1
    imgGray2 = cv.cvtColor(frame,cv.COLOR_BGRA2GRAY)
    imgBlur2 = cv.GaussianBlur(imgGray2,(3,5),5)
    imgThreshold2 = cv.adaptiveThreshold(imgBlur2,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,17,1)
    imgMedian2 = cv.medianBlur(imgThreshold2,55)

    # Spot 1 filtered and cut out spot
    
    mask = np.zeros(imgMedian2.shape, dtype=np.uint8)
    roi_corners = np.array([[(x[0],x[1]), (x[2],x[3]), (x[4],x[5]),(x[6],x[7])]], dtype=np.int32)
    channel_count = frame.shape[2]  # i.e. 3 or 4 depending on your image
    ignore_mask_color = (255,)*channel_count
    cv.fillPoly(mask, roi_corners, ignore_mask_color)
    newImage = cv.bitwise_and(imgMedian2, mask)
    cv.circle(frame_with_mapped_spots,(x[0],x[1]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[2],x[3]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[4],x[5]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[6],x[7]), 5, (0,0,255), -1)

    # Spot 2 filtered and cut out spot
    mask2 = np.zeros(imgMedian2.shape, dtype=np.uint8)
    roi_corners2 = np.array([[(x[8],x[9]),(x[10],x[11]),(x[12],x[13]),(x[14],x[15])]], dtype=np.int32)
    channel_count = frame.shape[2]  # i.e. 3 or 4 depending on your image
    ignore_mask_color = (255,)*channel_count
    cv.fillPoly(mask2, roi_corners2, ignore_mask_color)
    newImage2 = cv.bitwise_and(imgMedian2, mask2)
    cv.circle(frame_with_mapped_spots,(x[8],x[9]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[10],x[11]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[12],x[13]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[14],x[15]), 5, (0,0,255), -1)

    # Spot 3 filtered and cut out spot
    
    mask3 = np.zeros(imgMedian2.shape, dtype=np.uint8)
    roi_corners3 = np.array([[(x[16],x[17]),(x[18],x[19]),(x[20],x[21]),(x[22],x[23])]], dtype=np.int32)
    channel_count = frame.shape[2]  # i.e. 3 or 4 depending on your image
    ignore_mask_color = (255,)*channel_count
    cv.fillPoly(mask3, roi_corners3, ignore_mask_color)
    newImage3 = cv.bitwise_and(imgMedian2, mask3)
    cv.circle(frame_with_mapped_spots,(x[16],x[17]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[18],x[19]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[20],x[21]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[22],x[23]), 5, (0,0,255), -1)

    # Spot 4 filtered and cut out spot
    
    mask4 = np.zeros(imgMedian2.shape, dtype=np.uint8)
    roi_corners4 = np.array([[(x[24],x[25]),(x[26],x[27]),(x[28],x[29]),(x[30],x[31])]], dtype=np.int32)
      
    channel_count = frame.shape[2]  # i.e. 3 or 4 depending on your image
    ignore_mask_color = (255,)*channel_count
    cv.fillPoly(mask4, roi_corners4, ignore_mask_color)
    newImage4 = cv.bitwise_and(imgMedian2, mask4)
    cv.circle(frame_with_mapped_spots,(x[24],x[25]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[26],x[27]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[28],x[29]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[30],x[31]), 5, (0,0,255), -1)

    # Spot 5 filtered and cut out spo
    
    mask5 = np.zeros(imgMedian2.shape, dtype=np.uint8)
    roi_corners5 = np.array([[(x[32],x[33]),(x[34],x[35]),(x[36],x[37]),(x[38],x[39])]], dtype=np.int32)
    channel_count = frame.shape[2]  # i.e. 3 or 4 depending on your image
    ignore_mask_color = (255,)*channel_count
    cv.fillPoly(mask5, roi_corners5, ignore_mask_color)
    newImage5 = cv.bitwise_and(imgMedian2, mask5)
    cv.circle(frame_with_mapped_spots,(x[32],x[33]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[34],x[35]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[36],x[37]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[38],x[39]), 5, (0,0,255), -1)

    # Spot 6 filtered and cut out spot
    
    mask6 = np.zeros(imgMedian2.shape, dtype=np.uint8)
    roi_corners6 = np.array([[(x[40],x[41]),(x[42],x[43]),(x[44],x[45]),(x[46],x[47])]], dtype=np.int32)
    channel_count = frame.shape[2]  # i.e. 3 or 4 depending on your image
    ignore_mask_color = (255,)*channel_count
    cv.fillPoly(mask6, roi_corners6, ignore_mask_color)
    newImage6 = cv.bitwise_and(imgMedian2, mask6)
    cv.circle(frame_with_mapped_spots,(x[40],x[41]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[42],x[43]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[44],x[45]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[46],x[47]), 5, (0,0,255), -1)
    

    # Spot 7 filtered and cut out spot
    
    mask7 = np.zeros(imgMedian2.shape, dtype=np.uint8)
    roi_corners7 = np.array([[(x[48],x[49]),(x[50],x[51]),(x[52],x[53]),(x[54],x[55])]], dtype=np.int32)
    channel_count = frame.shape[2]  # i.e. 3 or 4 depending on your image
    ignore_mask_color = (255,)*channel_count
    cv.fillPoly(mask7, roi_corners7, ignore_mask_color)
    newImage7 = cv.bitwise_and(imgMedian2, mask7)
    cv.circle(frame_with_mapped_spots,(x[48],x[49]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[50],x[51]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[52],x[53]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[54],x[55]), 5, (0,0,255), -1)

    # Spot 8 filtered and cut out spot
    
    mask8 = np.zeros(imgMedian2.shape, dtype=np.uint8)
    roi_corners8 = np.array([[(x[56],x[57]),(x[58],x[59]),(x[60],x[61]),(x[62],x[63])]], dtype=np.int32)
    channel_count = frame.shape[2]  # i.e. 3 or 4 depending on your image
    ignore_mask_color = (255,)*channel_count
    cv.fillPoly(mask8, roi_corners8, ignore_mask_color)
    newImage8 = cv.bitwise_and(imgMedian2, mask8)
    cv.circle(frame_with_mapped_spots,(x[56],x[57]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[58],x[59]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[60],x[61]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[62],x[63]), 5, (0,0,255), -1)

    # Spot 9 filtered and cut out spot
    
    mask9 = np.zeros(imgMedian2.shape, dtype=np.uint8)
    roi_corners9 = np.array([[(x[64],x[65]),(x[66],x[67]),(x[68],x[69]),(x[70],x[71])]], dtype=np.int32)
    channel_count = frame.shape[2]  # i.e. 3 or 4 depending on your image
    ignore_mask_color = (255,)*channel_count
    cv.fillPoly(mask9, roi_corners9, ignore_mask_color)
    newImage9 = cv.bitwise_and(imgMedian2, mask9)
    cv.circle(frame_with_mapped_spots,(x[64],x[65]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[66],x[67]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[68],x[69]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[70],x[71]), 5, (0,0,255), -1)

    # Spot 10 filtered and cut out spot
    mask10 = np.zeros(imgMedian2.shape, dtype=np.uint8)
    roi_corners10 = np.array([[(x[72],x[73]),(x[74],x[75]),(x[76],x[77]),(x[78],x[79])]], dtype=np.int32)
    
    channel_count = frame.shape[2]  # i.e. 3 or 4 depending on your image
    ignore_mask_color = (255,)*channel_count
    cv.fillPoly(mask10, roi_corners10, ignore_mask_color)
    newImage10 = cv.bitwise_and(imgMedian2, mask10)
    cv.circle(frame_with_mapped_spots,(x[72],x[73]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[74],x[75]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[76],x[77]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[78],x[79]), 5, (0,0,255), -1)

    # Spot 11 filtered and cut out spot
    
    mask11 = np.zeros(imgMedian2.shape, dtype=np.uint8)
    roi_corners11 = np.array([[(x[80],x[81]),(x[82],x[83]),(x[84],x[85]),(x[86],x[87])]], dtype=np.int32)
    channel_count = frame.shape[2]  # i.e. 3 or 4 depending on your image
    ignore_mask_color = (255,)*channel_count
    cv.fillPoly(mask11, roi_corners11, ignore_mask_color)
    newImage11 = cv.bitwise_and(imgMedian2, mask11)
    cv.circle(frame_with_mapped_spots,(x[80],x[81]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[82],x[83]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[84],x[85]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[86],x[87]), 5, (0,0,255), -1)

    # Spot 12 filtered and cut out spot
    
    mask12 = np.zeros(imgMedian2.shape, dtype=np.uint8)
    roi_corners12 = np.array([[(x[88],x[89]),(x[90],x[91]),(x[92],x[93]),(x[94],x[95])]], dtype=np.int32)

    channel_count = frame.shape[2]  # i.e. 3 or 4 depending on your image
    ignore_mask_color = (255,)*channel_count
    cv.fillPoly(mask12, roi_corners12, ignore_mask_color)
    newImage12 = cv.bitwise_and(imgMedian2, mask12)
    cv.circle(frame_with_mapped_spots,(x[88],x[89]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[90],x[91]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[92],x[93]), 5, (0,0,255), -1)
    cv.circle(frame_with_mapped_spots,(x[94],x[95]), 5, (0,0,255), -1)

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
    #Image detection threshold control

    #Spot 1
    if (count1>=2000):
        Spot1Status = True
    if (count1<2000):
        Spot1Status = False
    #Spot 2
    if (count2>=2000):
        Spot2Status = True
    if (count2<2000):
        Spot2Status = False

    #Spot 3
    if (count3>=2000):
        Spot3Status = True
    if (count3<2000):
        Spot3Status = False
    #Spot 4
    if (count4>=2000):
        Spot4Status = True
    if (count4<2000):
        Spot4Status = False
    #Spot 5
    if (count5>=2800):
        Spot5Status = True
    if (count5<2800):
        Spot5Status = False
    #Spot 6
    if (count6>=2000):
        Spot6Status = True
    if (count6<2000):
        Spot6Status = False
    #Spot 7
    if (count7>=2000):
        Spot7Status = True
    if (count7<2000):
        Spot7Status = False
    #Spot 8
    if (count8>=2000):
        Spot8Status = True
    if (count8<2000):
        Spot8Status = False
    #Spot 9
    if (count9>=2000):
        Spot9Status = True
    if (count9<2000):
        Spot9Status = False
    #Spot 10
    if (count10>=2000):
        Spot10Status = True
    if (count10<2000):
        Spot10Status = False
    #Spot 11
    if (count11>=2000):
        Spot11Status = True
    if (count11<2000):
        Spot11Status = False
    #Spot 12
    if (count12>=2000):
        Spot12Status = True
    if (count12<2000):
        Spot12Status = False
    
    return frame, Spot1Status , Spot2Status, Spot3Status,Spot4Status,Spot5Status,Spot6Status,Spot7Status,Spot8Status,Spot9Status,Spot10Status,Spot11Status,Spot12Status,count1,count2,count3,count4,count5,count6,count7,count8,count9,count10,count11,count12,frame_with_mapped_spots,imgMedian2
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



layout = [
    [sg.Text(text='Parkwise Control Panel',
   font=('Arial Bold', 20),
   size=20,
   expand_x=True,
   )],

   [sg.Text(text='Current Lot View:',
   font=('Arial Bold', 10),
   size=10,
   expand_x=True,
   )],

   [sg.Image(filename= [],size = (300,300),key = 'image')],

   [sg.Table([['Spot 1 Status','Spot 2 Status','Spot 3 Status','Spot 4 Status','Spot 5 Status','Spot 6 Status'], ['Spot 7 Status','Spot 8 Status','Spot 9 Status','Spot 10 Status','Spot 11 Status','Spot 12 Status']], ['Col 1','Col 2','Col 3','Col 4','Col 5','Col 6',], num_rows=2,expand_x=True,enable_events=True,key='Table')],

    [sg.Button('Filter Settings', size=(10,2), button_color=DARK_GRAY_BUTTON_COLOR),sg.Button('Lot Settings', size=(10,2), button_color=DARK_GRAY_BUTTON_COLOR),sg.Button('Quit', size=(10,2), button_color='red'),],

    [[sg.Button('Start Detection', size=(200,2), button_color=DARK_GRAY_BUTTON_COLOR)]],
    [[sg.Button('Stop Detection', size=(200,2), button_color=DARK_GRAY_BUTTON_COLOR)]]

]
x = testOfDrawLines()
y = len(x)
window = sg.Window('Parkwise',layout,size = (1000,1000))

if (y<96):
    testOfDrawLines()
else:
   
    while(1):
        event,values = window.read()
        if event in (None,'Quit'):
            break
        elif event == 'Filter Settings':
            changefitersettings()
        ## Put in an image for the item detection in here
            print('View the Parking Lot')
        elif event == 'Lot Settings':
            Settings()
        elif event =='Start Detection':
            while(1):
                event,values = window.read(1)
                if event == 'Stop Detection':
                    break
                else:
                    print(1)
                    print(2)
                    #frame = cv.resize(cv.imread(r'C:\Users\beaum\Desktop\Capstone2_Project_1\Images\model1.jpg',-1), (1280, 895))
                    sct_img = sct.grab(bounding_box)
                    videoimage = changeImage(x,np.array(sct_img))
                    resized_frame = cv.resize(videoimage[0],(1000,600))
                    imgbytes = cv.imencode('.png',resized_frame)[1].tobytes()
                    window['image'].update(data =imgbytes)
                    table_data_main_menu = [videoimage[1],videoimage[2],videoimage[3],videoimage[4],videoimage[5],videoimage[6]], [videoimage[7],videoimage[8],videoimage[9],videoimage[10],videoimage[11],videoimage[12]]
                    window['Table'].update(values =table_data_main_menu)
                    #cv.imshow('hello1',videoimage[0])
                    ServerUpdate = UpdateServer(videoimage[1],videoimage[2],videoimage[3],videoimage[4],videoimage[5],videoimage[6],videoimage[7],videoimage[8],videoimage[9],videoimage[10],videoimage[11],videoimage[12])
                    k = cv.waitKey(1) & 0xFF
                    # press 'q' to exit
                    if k == ord('q'):
                        break
                cv.destroyAllWindows()
