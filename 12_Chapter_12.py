import cv2 as cv 
import numpy as np 
cap=cv.VideoCapture(0)
cap.set(10, 100) # Brightness key=10
cap.set(3, 640) # Width key=3
cap.set(4, 480) # Height key=4
while(True):
    ret, frame=cap.read()
    if ret==True:
        cv.imshow('Frame', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break 
        else:
            break
cv.release()
cv.destroyAllWindows()        