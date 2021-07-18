# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 01:11:29 2021

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

image=np.zeros((400,500,3),dtype="uint8")

image[:]=colors['light_gray']


def draw_float_circle(img, center, radius, color, thickness=1, lineType=8, shift=4):
    """Wrapper function to draw float-coordinate circles"""

    factor = 2 ** shift
    center = (int(round(center[0] * factor)), int(round(center[1] * factor)))
    radius = int(round(radius * factor))
    cv2.circle(img, center, radius, color, thickness, lineType, shift)


# We draw some text on the image: 
cv2.putText(image, 'Mastering OpenCV4 with Python', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, colors['red'], 2, cv2.LINE_4) 
cv2.putText(image, 'Mastering OpenCV4 with Python', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.9, colors['red'], 2, cv2.LINE_8) 
cv2.putText(image, 'Mastering OpenCV4 with Python', (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.9, colors['red'], 2, cv2.LINE_AA) 



show_with_matplotlib(image, 'cv2.putText()')
