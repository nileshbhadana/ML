#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 03:44:34 2018

@author: nilesh
"""
#importing libraries
import cv2,os

#casecading xml file
cascade=cv2.CascadeClassifier("face.xml")

#setting up counter
counter=0

#startiing the camera
cam=cv2.VideoCapture(0)

#defining directory name where images will be stored
dir_name="/home/nilesh/Desktop/ML/dataset_images"

#using try to avoid error when directory is already present
try:
    os.mkdir(dir_name)
except:
    print()
    
#startin the loop
while cam.isOpened():
    
    #readin the frame
    frame=cam.read()[1]
    #converting frame to gray
    gray_image=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    #reading and detecting faces in the frame
    faces=cascade.detectMultiScale(gray_image,1.5,5)
    
    for (x,y,w,h) in faces:
        #drawing around the face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
        counter=counter+1
        print(counter)
        
        #saving the face images
        cv2.imwrite(dir_name+"/image"+str(counter)+".jpg",gray_image)
    
    #showing the frame
    cv2.imshow('capturing images',frame)
    
    #handler
    if cv2.waitKey(100) & 0xFF==ord('q'):
        break
    elif cv2.waitKey(100) & counter==20:
        break
    
#releasing the camera
cam.release()
#destroying all windows
cv2.destroyAllWindows()
