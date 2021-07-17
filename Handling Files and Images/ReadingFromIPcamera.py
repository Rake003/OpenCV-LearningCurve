# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 17:17:34 2021

@author: Rakesh Kumar
"""

# Import the required packages
import cv2
#import argparse



# Create a VideoCapture object
# In this case, the argument is the URL connection of the IP camera
capture = cv2.VideoCapture("http://217.126.89.102:8010/axis-cgi/mjpg/video.cgi")


# Check if camera opened successfully
if capture.isOpened()is False:
    print("Error opening the camera")
 
# Read until the video is completed, or 'q' is pressed
while capture.isOpened():
    # Capture frame-by-frame from the camera
    ret, frame = capture.read()

    if ret is True:
        # Display the captured frame:
        cv2.imshow('Club Nàutic Port de la Selva (Girona - Spain)', frame)

        # Convert the frame captured from the camera to grayscale:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the grayscale frame
        cv2.imshow('Grayscale Club Nàutic Port de la Selva (Girona - Spain)', gray_frame)

        # Press q on keyboard to exit the program
        if cv2.waitKey(2000) & 0xFF == ord('q'):
            break
    # Break the loop
    else:
        break
 
# Release everything:
capture.release()
cv2.destroyAllWindows()