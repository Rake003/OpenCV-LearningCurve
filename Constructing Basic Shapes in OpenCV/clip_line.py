# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 00:42:53 2021

@author: Rakesh Kumar
"""

import numpy as np

import cv2

import matplotlib.pyplot as plt

# Dictionary containing some colors:
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

def show_with_matplotlib(img, title):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB:
    img_RGB = img[:, :, ::-1]

    # Show the image using matplotlib:
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()

image=np.zeros((400,400,3),dtype="uint8")

image[:]=colors['light_gray']

cv2.line(image, (0, 0), (300, 300), colors['green'], 3) 
cv2.rectangle(image, (0, 0), (100, 100), colors['blue'], 3) 
ret, p1, p2 = cv2.clipLine((0, 0, 100, 100), (0, 0), (300, 300)) 
if ret:
    cv2.line(image, p1, p2, colors['yellow'], 3)


show_with_matplotlib(image, 'Clip_Line')