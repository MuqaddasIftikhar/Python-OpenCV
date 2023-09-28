# Basic Functions or Manipulations in openCV 
import cv2 as cv 
import numpy as np 
img=cv.imread('resources/image.jpg')
resized_image=cv.resize(img, (150, 250))
gray_image=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
(thresh, binary)=cv.threshold(img, 125, 255, cv.THRESH_BINARY)
blurr_image=cv.GaussianBlur(img, (7, 7), 0)
edge_image=cv.Canny(img, 53, 53)
mat_kernal=np.ones((7, 7), np.uint8)
dilated_image=cv.dilate(edge_image,(mat_kernal), (23, 23), iterations=2)
ero_image=cv.erode(dilated_image, (mat_kernal), iterations=1)
# Croping the Image
print('The size of our image is ', img.shape)
crop_image=resized_image[0:200, 200:300]
cv.imshow('Original Image', img)
cv.imshow('Resize', resized_image)
cv.imshow('Gray Image', gray_image)
cv.imshow('Black and White', binary)
cv.imshow("Blurr Image", blurr_image)
cv.imshow("Edge Image", edge_image)
cv.imshow("Dilated Image", dilated_image)
cv.imshow('Erosion image', ero_image)
cv.imshow('Croped Image', crop_image)
cv.waitKey(0) 
cv.destroyAllWindows()