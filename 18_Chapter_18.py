# How to change perspective
import cv2 as cv 
import numpy as np

img=cv.imread('resources/image.jpg')
print(img.print())
point1=np.float32([[233, 196], [82, 471], [522, 169], [715, 482]])
width=800
height=900
point2=np.float32([[0, 0], [800, 0], [0, 900], [800, 900]])

matrix=cv.getPerspectiveTransform(point1, point2)
out_img=cv.imgperpective(img, matrix, (width, height))
out_img=cv.resize(out_img, (800, 600))
cv.imwrite('resources/img.jpg', img)
cv.imshow('Original', img)
cv.imshow('Transformed', out_img)
cv.waitKey(0)
cv.destroyAllWindows()