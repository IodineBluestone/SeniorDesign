import cv2
from imageResize import resize


img = cv2.imread(r'C:\Users\beaum\OneDrive\Desktop\Capstone2_Project_1\left.jpeg')
img2 =  resize(img,40)


while True:
    cv2.rectangle(img2,(150,400),(350,600),(0,0,255),2)
    cv2.rectangle(img2,(400,400),(600,600),(0,0,255),2)
    cv2.rectangle(img2,(620,400),(850,600),(0,0,255),2)
    cv2.imshow('image',img2)
    k = cv2.waitKey(1) & 0xFF
    # press 'q' to exit
    if k == ord('q'):
        break