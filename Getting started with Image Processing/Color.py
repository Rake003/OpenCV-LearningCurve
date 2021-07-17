# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 14:26:39 2021

@author: Rakesh Kumar
"""

import cv2 as cv
#import matplotlib.pyplot as plt

img_OpenCV=cv.imread('F:\Mastering_OpenCV_from_basics\OpenCV-LearningCurve\images/logo.png')
# Split the loaded image into its three channels (b, g, r):
b ,g ,r=cv.split(img_OpenCV)

# Merge again the three channels but in the RGB format: 
img_matplotlib = cv.merge([r, g, b])



cv.imshow("openCV_Image",img_OpenCV)
cv.imshow("Matplotlib_Image",img_matplotlib)

'''For showing output in one screen
# Show both images (img_OpenCV and img_matplotlib) using matplotlib
 # This will show the image in wrong color: 
plt.subplot(121) 
plt.imshow(img_OpenCV)
     # This will show the image in true color: 
plt.subplot(122)
plt.imshow(img_matplotlib)
plt.show()   '''

cv.waitKey(0)
cv.destroyAllWindows()