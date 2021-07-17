# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 14:12:26 2021

@author: crazy
"""

import cv2 as cv

img=cv.imread('F:\Mastering_OpenCV_from_basics\OpenCV-LearningCurve\images/logo.png',cv.IMREAD_GRAYSCALE)

dimentions=img.shape  #shows the dimention of the image
print(dimentions)

sizeofImage=img.size #shows the whole size if the image
print(sizeofImage)

image_dtype=img.dtype  #shows the data type of the image
print(image_dtype)


# You can modify the pixel values of the image in the same way. 
# Set the pixel to black: 
img[40, 40] = 0

cv.imshow("original image",img)

cv.waitKey(0)
cv.destroyAllWindows()