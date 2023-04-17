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
cv2.imshow('new image',hello)
layout = [
    [sg.Text(text='Welcome to Parkwise Control Panel',
   font=('Arial Bold', 20),
   size=20,
   expand_x=True,
   justification='center')],

   [sg.Text(text='Current Lot View:',
   font=('Arial Bold', 10),
   size=10,
   expand_x=True,
   justification='center')],

   [sg.Image(filename= 'middle.png',size = (300,300))],
   
    

    [sg.Button('View Parking Lot', size=(10,2), button_color=DARK_GRAY_BUTTON_COLOR),sg.Button('Lot Settings', size=(10,2), button_color=DARK_GRAY_BUTTON_COLOR),sg.Button('Quit', size=(10,2), button_color='red'),]

]

window = sg.Window('Parkwise',layout,size = (1000,500))
def viewParkingwindow():
    ViewParkinglayout = [
    [sg.Text(text='Current Parking Lot View:',
   font=('Arial Bold', 20),
   size=20,
   expand_x=True,
   justification='center')],
    [sg.Button('Quit', size=(10,2), button_color='red')]
]
    areawindow = sg.Window('View The Current Parking Lot',ViewParkinglayout,size = (500,100))
    while True: 
        event,values = areawindow.read()
        if event in (None,'Quit'):
            break
    areawindow.close

def Settings():
    Settingslayout = [
    [sg.Text(text='Settings:',
   font=('Arial Bold', 20),
   size=20,
   expand_x=True,
   justification='center')],
    [sg.Button('Quit', size=(10,2), button_color='red')]
]
    settingswindow = sg.Window('Change Detection Parameters',Settingslayout,size = (500,100))
    while True: 
        event,values = settingswindow.read()
        if event in (None,'Quit'):
            break
    settingswindow.close

while True: 
    event,values = window.read()
    if event in (None,'Quit'):
        break
    elif event == 'View Parking Lot':
        viewParkingwindow()
    ## Put in an image for the item detection in here
        print('View the Parking Lot')
    elif event == 'Lot Settings': 
        Settings()
        print('Lot Settings has been pressed')
window.close