# reolution of cam 

import cv2 as cv 
import numpy as np 
cap=cv.VideoCapture(0)

def hd_resolution():
    cap.set(3, 1280)
    cap.set(4, 720) # HD Resolution(1280x720)
def sd_resolution():
    cap.set(3, 1280)
    cap.set(4, 720) # HD Resolution(640x480)
hd_resolution()   
sd_resolution() 
while(True):
    ret, frame=cap.read()
    if ret==True:
        cv.imshow('Camera', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break 
    else:
        break    
cv.release()
cv.destroyAllWindows()     