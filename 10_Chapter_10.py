# Convert into different shades i.e GrayScale, Black and White
import cv2 as cv 
import numpy as np 
cap=cv.VideoCapture(0)
while(True):
    (ret, frame)=cap.read()
    gray_frame=cv.cvtColor(frame, cv.COLOR_BG2GRAY)
    (thresh, binary)=cv.threshold(frame, 127, 255, cv.THRESH_BINARY)
    cv.imshow('Original Camera', frame) # Original WebCam
    cv.imshow('Gray Camera', gray_frame) # GrayScale WebCam
    cv.imshow('Black and White Camera', binary) # Black and White/Binary WebCam
    if cv.waitKey(1) & 0xFF == ord('q'):
        break 
cv.release()
cv.destroyAllWindows()    