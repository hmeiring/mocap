#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:53:38 2019

@author: meiringhe

This code will record continuous video of the joint of interest from a webcam.
It will filter the video frames for one color of the user's choice specified by a trackbar.
"""

# import needed libraries - OpenCV (cv2), others?
import cv2
import numpy

# Create a VideoCapture object to store camera image data; 0 = built-in webcam, 1 = external webcam
cap = cv2.VideoCapture(0)

# create windows for trackbars, frame video and filtered video
cv2.namedWindow('First Video')
cv2.namedWindow('Filtered Video')
cv2.namedWindow('Filter Trackbars')

# save frame size data into variables for use when displaying filter
image_height = frame.shape[0]
image_width = frame.shape[1]
image_channels = frame.shape[2]

# create color trackbars for color filter settings
# cv2.createTrackbar('','Filter Trackbars', 85, 255, lambda x:None)

# initialize a while loop to show continuous video until user presses Esc
keypressed = 1
while (keypressed != 27):
    
    # capture an image from the webcam in frame
    ret, frame = cap.read()
    
    # display the image in the window
    cv2.imshow('First Video',frame)
    
    # wait for button press
    keypressed = cv2.waitKey(1)

# release image and destroy windows 
cap.release()
cv2.destroyAllWindows()