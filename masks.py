#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 04:32:46 2019

@author: nilesh
"""

import cv2
import numpy as np
cam_cap=cv2.VideoCapture(0)
cascade=cv2.CascadeClassifier('face.xml')

while cam_cap.isOpened():
    status,frame=cam_cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_green=np.array([0,0,9])
    upper_green=np.array([133,250,250])
    #creating mask
    mask=cv2.inRange(hsv,lower_green,upper_green)
    ret, mask2 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    mask3 = cv2.createBackgroundSubtractorMOG2().apply(frame)
    mask3_inv=cv2.bitwise_not(mask3)
    
    cv2.imshow('hsv',mask)
    cv2.imshow('thresh',mask2)
    cv2.imshow('sub',mask3)
    cv2.imshow('sub2',mask3_inv)
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
cam_cap.release()