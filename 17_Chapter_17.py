import cv2 as cv 
import numpy as np 
img=cv.imread('resources/image.jpg')
# Stacking same image
hor_img=np.h_stack((img, img))

ver_img=np.vstack((img, img))









cv.imshow('Horizontal', hor_img)
cv.imshow('Vertical', ver_img)
cv.waitKey(0)
cv.destroyAllWindows()