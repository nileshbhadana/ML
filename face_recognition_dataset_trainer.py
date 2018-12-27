#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 04:26:08 2018

@author: nilesh
"""
#importing libraries
import cv2,os
import numpy as np

#casecading the xml file
cascade=cv2.CascadeClassifier("face.xml")

#definig directory name where image data is stored
dir_name="/home/nilesh/Desktop/ML/dataset_images"
face_names=os.listdir(dir_name)

#creating blank list to save face_data and label
face_datas=[]
labels=[]
label=0

for image_name in face_names:
    
    #creating image path
    image_path=dir_name+"/"+image_name
    print(image_path)
    
    #reading image data in gray fromat
    face_data=cv2.imread(image_path,0)
    faces=cascade.detectMultiScale(face_data,1.5,5)
    print(faces)
    for (x,y,w,h) in faces:
        
        #appending data in lists
        face_datas.append(face_data[y:y+h,x:x+w])
        labels.append(label)

np.save('training_faces', face_datas)
np.save('training_labels', labels)