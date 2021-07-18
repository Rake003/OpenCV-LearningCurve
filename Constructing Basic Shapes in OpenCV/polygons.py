# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 00:56:29 2021

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

# These points define a triangle 
pts = np.array([[250, 5], [220, 80], [280, 80]], np.int32) 
# Reshape to shape (number_vertex, 1, 2) 
pts = pts.reshape((-1, 1, 2)) 
# Print the shapes: this line is not necessary, only for visualization 
print("shape of pts '{}'".format(pts.shape)) 
# Draw this poligon with True option 
cv2.polylines(image, [pts], True, colors['green'], 3)


show_with_matplotlib(image, 'Polygons')