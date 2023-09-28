# Saving HD recodring of Cam

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
    # Capture the Video
frame_width=int(cap.get(3))
frame_height=int(cap.get(4))

# Conversion of video .mp4 into .avi extension
out=cv.VideoWriter('resources/Cam_Video.avi', cv.VideoWriter_fourcc('M', 'J', 'p', 'G'), 10, (frame_width, frame_height))
while(True):
    (ret, frame)=cap.read()
    if ret==True:
        gray=cv.cvtColor(cv.COLOR_BGR2GRAY)
        (thresh_binary)=cv.threshold(frame, 127, 255, cv.THRESH_BINARY)
        out.write(frame)
        cv.imshow('Video', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break    
cv.release()
cv.destroyAllWindows()   
