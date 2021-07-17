# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 10:46:14 2021

@author: crazy
"""

import numpy as np
import matplotlib.pylab as plt
import matplotlib.image as mpimg

im1 = mpimg.imread("F:/Mastering_OpenCV_from_basics/OpenCV-LearningCurve/images/messi.jpg") / 255 # scale RGB values in [0,1]
im2 = mpimg.imread("F:/Mastering_OpenCV_from_basics/OpenCV-LearningCurve/images/ronaldo.jpg") / 255
i = 1
plt.figure(figsize=(18,15))
for alpha in np.linspace(0,1,20):
    plt.subplot(4,5,i)
    plt.imshow((1-alpha)*im1 + alpha*im2)
    plt.axis('off')
    i += 1
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.show()