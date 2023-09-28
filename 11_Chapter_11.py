# import Libraries
import cv2 as cv 
import numpy as np 
from matplotlib.colors import is_color_like

# Capture the Video
cap=cv.VideoCapture(0)
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
        cv.imshow('Gray', gray)
        cv.imshow('Black and White', binary)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break 
cv.release()
out.release()
cv.destroyAllWindows()  
