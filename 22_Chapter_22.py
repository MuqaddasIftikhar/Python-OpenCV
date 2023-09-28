
# Face Detection in Images

import cv2 as cv 
import numpy as np 


face_cascade=cv.face_CascadeClassifier('resources/haarcascade_frontalface_default.xml')
img=cv.imread('resources/image.jpg')

img=cv.resize(img, (800, 600))

faces=face_cascade.detectMultiScale(img, 1.1, 4)

for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w), (y+h), (255, 0, 0), 2)
print(img.shape)
cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()
