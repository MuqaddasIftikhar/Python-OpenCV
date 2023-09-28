# How to capture a webam inside python in openCV
import cv2 as cv 
import numpy as np 
cap=cv.VideoCapture(0) # Webcam number will be 1
# read until the end
while(cap.isOpened()):
    ret, frame=cap.read()
    if ret==True:
        cv.imshow('Video', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break 
    else:
        break     
cap.release()
cv.destroyAllWindows()    