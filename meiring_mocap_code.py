#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:53:38 2019

@author: meiringhe

This code will record continuous video of the joint of interest from a webcam.
"""

# import needed libraries - OpenCV (cv2), others?
import cv2

# Create a VideoCapture object to store camera image data; 0 = built-in webcam, 1 = external webcam
cap = cv2.VideoCapture(0)

# create window to display frame image
cv2.namedWindow('Frame Video')

# initialize a while loop to show continuous video until user presses Esc
keypressed = 1
while (keypressed != 27):
    
    # capture an image from the webcam in frame
    ret, frame = cap.read()
    
    # display the image in the window
    cv2.imshow('Frame Video',frame)
    
    # wait for button press
    keypressed = cv2.waitKey(1)

# save the image and/or destroy windows 
cv2.destroyAllWindows()