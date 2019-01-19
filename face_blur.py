#!/usr/bin/python3
import cv2
import numpy as np
cam_cap=cv2.VideoCapture(0)
cascade=cv2.CascadeClassifier('face.xml')
while cam_cap.isOpened():
    status,frame=cam_cap.read()
    #converting to hsv frame
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_green=np.array([0,0,9])
    upper_green=np.array([133,250,250])
    
    #creating mask
    mask=cv2.inRange(hsv,lower_green,upper_green)
    
    #blurring the frame
    blur_frame=cv2.GaussianBlur(frame,(15,15),30)
    '''
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)	
    #mask_inv = cv2.bitwise_not(mask)
    faces=cascade.detectMultiScale(gray_frame,1.5,5)
    #cv2.medianBlur(frame,15,new_img)
    #kernal = np.ones((480 ,640), "uint8")
    for (x,y,w,h) in faces:
        hsv=cv2.cvtColor(frame[y:y+h,x:x+w],cv2.COLOR_BGR2HSV)
        lower_green=np.array([0,0,9])
        upper_green=np.array([133,250,250])
        mask=cv2.inRange(hsv,lower_green,upper_green)
        blur_frame=cv2.GaussianBlur(frame[y:y+h,x:x+w],(15,15),30)'''
        
    final1=cv2.bitwise_and(blur_frame,frame,mask=mask)
    #final2=cv2.bitwise_and(frame,blur_frame,mask=mask_inv)
    '''
        width, height, channels = frame.shape
        center = (int(height/2), int(width/2))
        output = cv2.seamlessClone(blur_frame, frame, mask, center, cv2.MIXED_CLONE)
    '''
    
    cv2.imshow('live',blur_frame)
    cv2.imshow('live2',final1)
    #cv2.imshow('live3',final2)
    #cv2.imshow('live4',mask_inv)
    #cv2.imshow('live5',hsv)
    #cv2.imshow('live6',output)
    #cv2.imshow('live7',lower_green)
    #cv2.imshow('live8',upper_green)
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
cam_cap.release()