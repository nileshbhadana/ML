#!/usr/bin/python3
import cv2
import numpy as np
cam_cap=cv2.VideoCapture(0)
counter=0
cascade=cv2.CascadeClassifier('face.xml')
while cam_cap.isOpened():
    status,frame=cam_cap.read()
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)	
    faces=cascade.detectMultiScale(gray_frame,1.5,5)
    for (x,y,w,h) in faces:
        #new_frame=frame[x:x+w,y:y+h]
        print(x,w)
    new_frame1=frame[0:232,0:377]
        #print(new_frame1.shape)
    mask = 255 * np.ones((232,377,3),"uint8")
    #width, height, channels = frame.shape
    #print(frame.shape)
    center=(380,240)
    #print(center)
   # print(mask.shape)
    
    mixed_clone = cv2.seamlessClone(new_frame1, frame, mask, center, cv2.MIXED_CLONE)

    #mixed_clone=np.concatenate((frame,frame),axis=0.5)
    
    cv2.imshow('live',mixed_clone)
    if cv2.waitKey(1) & 0xFF == ord('q'):		
    	break
cv2.destroyAllWindows()
cam_cap.release()
