#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 05:19:44 2018

@author: nilesh
"""
#importing libraries
import cv2,time
import numpy as np

#setting font for puttext
font=cv2.FONT_HERSHEY_SIMPLEX

#loading and reading data from the saved training files
face_data=np.load('training_faces.npy')
labels=np.load('training_labels.npy')

#creating recognizer
recognizer=cv2.face.LBPHFaceRecognizer_create()

#training the recognizer
recognizer.train(face_data,np.array(labels))

#flag for the detected face
detected=0
#cascading
cascade=cv2.CascadeClassifier('face.xml')
# opening camera
cam=cv2.VideoCapture(0)
while cam.isOpened():
    # reading frame
    frame=cam.read()[1]
    #converting frame to gray 
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)	
    faces=cascade.detectMultiScale(gray_frame,1.5,5)
    
    for (x,y,w,h) in faces:
        #drawing rectangle on the faces
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
        
        #predicting the label and confidence
        label,confidence=recognizer.predict(gray_frame[y:y+h,x:x+w])
        
        #checking for confidence (the lower the confidence the more accurate the prediction is)
        if confidence<50:
            msg="Face Detected"
            
            #printing the message 
            cv2.putText(frame,msg,(20,50),font,1,(255,255,255),3,cv2.LINE_AA)
            
            #changing flag to 1
            detected=1
    cv2.imshow('live',frame)

    #handler
    if cv2.waitKey(2) & 0xFF == ord('q'):		
        break
    elif cv2.waitKey(2) & detected==1:
        time.sleep(0.5)
        break
cv2.destroyAllWindows()
cam.release()


#checking whether face is detected or not
if detected==1:
    
    #importing selenium library 
    from selenium import webdriver
    
    #creating driver instance
    driver = webdriver.Firefox()
    
    #username for facebook
    user="nileshbhadana"
    #password for facebook
    passwd="esehithodebtadunga"
    
    #opening window and fetching the facebook
    driver.get('https://www.facebook.com')
    
    #finding elements by id on the webpage
    username_box=driver.find_element_by_id('email')
    password_box=driver.find_element_by_id('pass')
    login_button=driver.find_element_by_id('loginbutton')
    
    #filling the username and password
    username_box.send_keys(user)
    password_box.send_keys(passwd)
    
    #clicking the login button
    login_button.click()
