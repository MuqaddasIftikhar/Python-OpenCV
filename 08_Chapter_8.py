# To write a Video

import cv2 as cv 
from matplotlib.colors import is_color_like
cap=cv.VideoCapture('resources/video.mp4')
frame_width=int(cap.get(3))
frame_height=int(cap.get(4))

# Conversion of video .mp4 into .avi extension
out=cv.VideoWriter('resources/video.avi', cv.VideoWriter_fourcc('M', 'J', 'p', 'G'), 10, (frame_width, frame_height), isColor=False)
while(True):
    (ret, frame)=cap.read()
    if ret==True:
        out.write(frame)
        grayFrame=cv.cvtColor(cap, cv.COLOR_BGR2GRAY)
        cv.imshow('Video', grayFrame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break 
cv.release()
out.release()
cv.destroyAllWindows()  

# import Libraries
import cv2 as cv 
cap=cv.VideoCapture('resources/video.mp4')
frame_width=int(cap.get(3))
frame_height=int(cap.get(4))
out=cv.VideoWriter('resources/video.avi', cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10 (frame_width, frame_height)) 
while(True):
    (ret, frame)=cap.read()
    if ret==True:
        out.write(frame)
        grayFrame=cv.cvtColor(cap, cv.COLOR_BGR2GRAY)
        cv.imshow('Video', grayFrame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break 
        else:
            break 
cv.release()
cv.destroyAllWindows()           