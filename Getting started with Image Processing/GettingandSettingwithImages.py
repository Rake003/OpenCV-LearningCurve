# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 13:45:35 2021

@author: crazy
"""

import cv2 as cv

img=cv.imread('F:\Mastering_OpenCV_from_basics\OpenCV-LearningCurve\images/logo.png')

dimentions=img.shape  #shows the dimention of the image
print(dimentions)

sizeofImage=img.size #shows the whole size if the image
print(sizeofImage)

image_dtype=img.dtype  #shows the data type of the image
print(image_dtype)


# A pixel value can be accessed by row and column coordinates. # In case of BGR image, it returns an array of (Blue, Green, Red) values.
# Get the value of the pixel (x=40, y=6):
(b, g, r) = img[6, 40]


# We can only access one channel at a time.
 # In this case, we will use row, column and the index of the desired channel for indexing.
 # Get only blue value of the pixel (x=40, y=6): 
b = img[6, 40, 0]


# The pixel values can be also modified in the same way - (b, g, r) format: 
img[6, 40] = (0, 0, 255)

# In this case, we get the top left corner of the image: 
top_left_corner = img[0:50, 0:50]


cv.imshow("original image",img)




cv.waitKey(0)
cv.destroyAllWindows()

