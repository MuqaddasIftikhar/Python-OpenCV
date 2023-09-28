
# Converting Video to GrayScale and black and White

import cv2 as cv 
cap=cv.VideoCapture('resources/video.mp4')
while(True):
    (ret, frame)=cap.read()
    grayFrame=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (thresh, binary)=cv.threshold(grayFrame, 127, 255, cv.THRESH_BINARY)
    if ret==True:
        cv.imshow('Video', grayFrame) # For GrayScale
        cv.imshow('Video', binary) # For Black and White
        # To quit with 'q' key
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break 
cv.release()
cv.destroyAllWindows()        