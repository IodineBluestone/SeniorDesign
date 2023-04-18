import PySimpleGUI as sg
import cv2
import numpy as np
from screeninfo import get_monitors
from win32api import GetSystemMetrics
ScreenWidth = GetSystemMetrics(0)
ScreenHeight = GetSystemMetrics(1)
sg.theme('System Default ')
LIGHT_GRAY_BUTTON_COLOR = f'#212021 on #e0e0e0'
DARK_GRAY_BUTTON_COLOR = '#e0e0e0 on #212021'

image = cv2.imread(r'C:\Users\beaum\OneDrive\Desktop\Capstone2_Project_1\middle.png')
def updatewindowsize(image,ScreenWidth,ScreenHeight):
    newimagewidth = ScreenWidth/4
    newimageheight = ScreenHeight/4
    newxy = (newimagewidth,newimageheight)
    print(newxy)
    x = cv2.resize(image,(200,200))
    return x
hello = updatewindowsize(image,ScreenWidth,ScreenHeight)
#cv2.imshow('new image',hello)
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

   [sg.Image(filename= 'middle.png',size = (300,300))],

   [sg.Table([['Spot 1 Status','Spot 2 Status','Spot 3 Status','Spot 4 Status','Spot 5 Status','Spot 6 Status'], ['Spot 7 Status','Spot 8 Status','Spot 9 Status','Spot 10 Status','Spot 11 Status','Spot 12 Status']], ['Col 1','Col 2','Col 3','Col 4','Col 5','Col 6',], num_rows=2,expand_x=True,enable_events=True,key='Table')],

    [sg.Button('Filter Settings', size=(10,2), button_color=DARK_GRAY_BUTTON_COLOR),sg.Button('Lot Settings', size=(10,2), button_color=DARK_GRAY_BUTTON_COLOR),sg.Button('Quit', size=(10,2), button_color='red'),]

]

window = sg.Window('Parkwise',layout,size = (800,800))
def changefitersettings():
    ViewParkinglayout = [
    [sg.Text(text='Change Filter Settings:',
   font=('Arial Bold', 20),
   size=20,
   expand_x=True,
   justification='center')],

    [sg.Text(text='This will be the area where you can change the image filters of each spot.',font=('Arial', 10),size=10,expand_x=True,justification='center')],

    [sg.Text(text='Filter Setting 1:',font=('Arial Bold', 15),size=10,expand_x=True,expand_y=True),sg.Slider(range=(10, 30), default_value=12,expand_x=False,expand_y=True, enable_events=True,orientation='horizontal', key='-F1-')],

    [sg.Text(text='Filter Setting 2:',font=('Arial Bold', 15),size=10,expand_x=True,expand_y=True),sg.Slider(range=(10, 30), default_value=12,expand_x=False,expand_y=True, enable_events=True,orientation='horizontal', key='-F2-')],

    [sg.Text(text='Filter Setting 3:',font=('Arial Bold', 15),size=10,expand_x=True,expand_y=True),sg.Slider(range=(10, 30), default_value=12,expand_x=False,expand_y=True, enable_events=True,orientation='horizontal', key='-F3-')],


[sg.Button('Quit', size=(10,2), button_color='red')],


]
    areawindow = sg.Window('Filter Settings',ViewParkinglayout,size = (800,800))
    while True: 
        event,values = areawindow.read()
        if event in (None,'Quit'):
            break
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
    ## Pixel Count, to be gathered from count variable and inserted into this table for easier threshold changing.
    [sg.Table([['Spot 1 Count','Spot 2 Count','Spot 3 Count','Spot 4 Count','Spot 5 Count','Spot 6 Count'], ['Spot 7 Count','Spot 8 Count','Spot 9 Count','Spot 10 Count','Spot 11 Count','Spot 12 Count']], ['Col 1','Col 2','Col 3','Col 4','Col 5','Col 6',], num_rows=2,expand_x=True,enable_events=True,key='Table')],
    ## Spot 1&2 pixel threshold control
   [sg.Text(text='Spot 1:',font=('Arial Bold', 15),size=10,expand_x=False,expand_y=True),sg.Slider(range=(10, 30), default_value=12,expand_x=False,expand_y=True, enable_events=True,orientation='horizontal', key='-SP1-')
    ,sg.Text(text='Spot 2:',font=('Arial Bold', 15),size=10,expand_x=False,expand_y=True),sg.Slider(range=(10, 30), default_value=12,expand_x=False,expand_y=True, enable_events=True,orientation='horizontal', key='-SP2-')],
    ## Spot 3&4 pixel threshold control
    [sg.Text(text='Spot 3:',font=('Arial Bold', 15),size=10,expand_x=False,expand_y=True),sg.Slider(range=(10, 30), default_value=12,expand_x=False,expand_y=True, enable_events=True,orientation='horizontal', key='-SP3-')
    ,sg.Text(text='Spot 4:',font=('Arial Bold', 15),size=10,expand_x=False,expand_y=True),sg.Slider(range=(10, 30), default_value=12,expand_x=False,expand_y=True, enable_events=True,orientation='horizontal', key='-SP4-')],
    ## Spot 5&6 pixel threshold control
    [sg.Text(text='Spot 5:',font=('Arial Bold', 15),size=10,expand_x=False,expand_y=True),sg.Slider(range=(10, 30), default_value=12,expand_x=False,expand_y=True, enable_events=True,orientation='horizontal', key='-SP5-')
    ,sg.Text(text='Spot 6:',font=('Arial Bold', 15),size=10,expand_x=False,expand_y=True),sg.Slider(range=(10, 30), default_value=12,expand_x=False,expand_y=True, enable_events=True,orientation='horizontal', key='-SP6-')],
    ## Spot 7&8 pixel threshold control
    [sg.Text(text='Spot 7:',font=('Arial Bold', 15),size=10,expand_x=False,expand_y=True),sg.Slider(range=(10, 30), default_value=12,expand_x=False,expand_y=True, enable_events=True,orientation='horizontal', key='-SP7-')
    ,sg.Text(text='Spot 8:',font=('Arial Bold', 15),size=10,expand_x=False,expand_y=True),sg.Slider(range=(10, 30), default_value=12,expand_x=False,expand_y=True, enable_events=True,orientation='horizontal', key='-SP8-')],
    ## Spot 9&10 pixel threshold control
    [sg.Text(text='Spot 9:',font=('Arial Bold', 15),size=10,expand_x=False,expand_y=True),sg.Slider(range=(10, 30), default_value=12,expand_x=False,expand_y=True, enable_events=True,orientation='horizontal', key='-SP9-')
    ,sg.Text(text='Spot 10:',font=('Arial Bold', 15),size=10,expand_x=False,expand_y=True),sg.Slider(range=(10, 30), default_value=12,expand_x=False,expand_y=True, enable_events=True,orientation='horizontal', key='-SP10-')],
    ## Spot 11&12 pixel threshold control
    [sg.Text(text='Spot 11:',font=('Arial Bold', 15),size=10,expand_x=False,expand_y=True),sg.Slider(range=(10, 30), default_value=12,expand_x=False,expand_y=True, enable_events=True,orientation='horizontal', key='-SP11-')
    ,sg.Text(text='Spot 12:',font=('Arial Bold', 15),size=10,expand_x=False,expand_y=True,),sg.Slider(range=(10, 30), default_value=12,expand_x=False,expand_y=True, enable_events=True,orientation='horizontal', key='-SP12-')],
    ##Apply Settings Button, restart program and apply desired detection values
    [[sg.Button('Apply Settings', size=(200,2), button_color=DARK_GRAY_BUTTON_COLOR)]],
    ##Display Current detection positions, Will show the current coordinates of desired spot coordinates
    [[sg.Button('View Current Detection Coordinates', size=(200,2), button_color=DARK_GRAY_BUTTON_COLOR)]],
    ##Remap Spots button, Will change the detection coordinates of each current spot
    [sg.Button('Remap Spot Locations', size=(200,2), button_color='green')],
    ##Quit button, exits the current page
    [sg.Button('Quit', size=(200,2), button_color='red',)],



]
    settingswindow = sg.Window('Change Detection Parameters',Settingslayout,size = (800,800))
    while True: 
        event,values = settingswindow.read()
        if event in (None,'Quit'):
            break
    settingswindow.close

while True: 
    event,values = window.read()
    if event in (None,'Quit'):
        break
    elif event == 'Filter Settings':
        changefitersettings()
    ## Put in an image for the item detection in here
        print('View the Parking Lot')
    elif event == 'Lot Settings': 
        Settings()
        print('Lot Settings has been pressed')
window.close
