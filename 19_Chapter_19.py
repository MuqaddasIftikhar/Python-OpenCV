# Coordinates of an image and videos

import cv2 as cv 
import numpy as np 
def find_coord(event, x, y, flags, params):
    if event == cv.EVENT_FLAG_LBUTTON:
        
        print(x, '',y)
    
        font=cv.FONT_HERSHEY_PLAIN
        cv.putText(img, str(x)+','+str(y), x, y, font, 1, (255, 0, 0), thickness=2)

        cv.imshow('Image', img)
        
if __name__=="__main__":
    img=cv.imread('resources/image.jpg', 1)
    cv.imshow('Image', img)
    cv.setMouseCallback('Image', find_coord)
cv.waitKey(0)
cv.destroyAllWindows()            