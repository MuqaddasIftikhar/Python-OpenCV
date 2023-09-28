# Capturing, Reading the video and display as output on the screen

import cv2 as cv 
cap=cv.VideoCapture('resources/video.mp4')
if(cap.isOpened()==False):
    print('Error in Reading Video')
while(cap.isOpened()):
    ret, frame=cv.read()
    if ret==True:
        cv.imshow('My First Video', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break 
cv.release()
cv.destroyAllWindows()            