# Hoe to Draw Lines and Shapes inside Python in openCV

import cv2 as cv 
import numpy as np 
# Draw a canvas
img=np.zeros((600, 600)) # zeros=Black
img1=np.ones((600, 600)) # ones=White
# Print Size
print('The size of out canvas is ', img.shape)
print(img)
# Adding Colors to Canvas
color_img=np.zeros((600, 600, 3), np.uint8)
color_img[:]=550, 0, 450
color_img[150:230,100:207]=255, 0, 155
# Adding  line
# cv.line(color_img, (0, 0), (230, 230), (255, 0, 0), 3)

# cv.line(color_img,(0, 0),(color_img.shape[0], (color_img.shape[1]), (255, 0, 0), 3))
cv.rectangle(color_img, (50, 100), (300, 400), (255, 240, 0), 3)
cv.rectangle(color_img, (50, 100), (300, 400), (255, 240, 0), cv.FILLED)
cv.circle(color_img, (400, 300), 100, (255, 100, 0))

# Adding Text 
cv.putText(color_img, ('Codanics'), (200, 500), cv.FONT_HERSHEY_DUPLEX, 1, (255, 255, 0), 2)

# cv.imshow('Black Image', img)
#cv.imshow('White Image', img1)
cv.imshow('Colored Image', color_img)
cv.waitKey(0)
cv.destroyAllWindows()