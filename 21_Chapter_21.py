
# How to detect specfic colors in python 

import cv2 as cv 
import numpy as np 

img=cv.imread('resources/image.jpg')

# Convert it into HSV (Hue, Saturation, Value)

# hsv_img=cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Sldiers

def Slider():
    pass
path='resources/image.jpg'
cv.namedWindow('Bars')
cv.resize("Bars", (640, 300))

cv.createTrackers('Hue Minimum', 'Bars', (0, 179, Slider))
cv.createTrackers('Hue Maximum', 'Bars', (179, 179, Slider))
cv.createTrackers('Saturation Minimum', 'Bars', (0, 255, Slider))
cv.createTrackers('Saturatin Maximum', 'Bars', (255, 255, Slider))
cv.createTrackers('Value Minimum', 'Bars', (0, 179, Slider))
cv.createTrackers('Value Maximum', 'Bars', (179, 179, Slider))
img=cv.imread(path)
hsv_img=cv.cvtColor(img, cv.COLOR_BGR2HSV)

#hue_min=cv.getTrackbarPos('Hue Min', 'bars')
# print(hue_min)

while (True):
    img=cv.imread(path)
    hsv_img=cv.cvtColor(img, cv.COLOR_BGR2HSV)
    hue_min=cv.getTrackbarPos('Hue Minimum', 'Bars')
    hue_max=cv.getTrackbarPos('Hue Maximum', 'Bars')
    Saturation_min=cv.getTrackbarPos('Hue Minimum', 'Bars')
    Saturation_max=cv.getTrackbarPos('Hue Minimum', 'Bars')
    Value_min=cv.getTrackbarPos('Hue Minimum', 'Bars')
    Value_max=cv.getTrackbarPos('Hue Minimum', 'Bars')
    print(hue_min, hue_max, Saturation_min, Saturation_max, Value_min, Value_max)
    cv.imshow('Original', img)
    
    cv.imshow('HSV', hsv_img)
    
    lower=np.array(hue_min, Saturation_min, Value_min)
    upper=np.array(hue_max, Saturation_max, Value_max)
    mask_img=cv.inRange(hsv_img, lower, upper)
    out_img=cv.bitwise_and(img, mask=mask_img)
    if cv.waitKey(0) & 0xFF == ord('q'):
        break



cv.imshow('Original', img)
cv.imshow('HSV', hsv_img)
cv.imshow("Mask", mask_img)
cv.waitKey(0)
cv.destroyAllWindows()