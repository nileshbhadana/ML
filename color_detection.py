#!/usr/bin/python3

import cv2
import numpy as np

# start camera
cap=cv2.VideoCapture(0)

while True:

	status,frame=cap.read()
	# capture only color frames
	red_img=cv2.inRange(frame,(0,0,50),(20,20,255))
	blue_img=cv2.inRange(frame,(60,0,0),(255,20,20))
	green_img=cv2.inRange(frame,(0,80,0),(20,255,20))
	yellow_img=cv2.inRange(frame,(0,180,210),(60,255,255))	
	
	kernal = np.ones((5 ,5), "uint8")

	red=cv2.dilate(red_img, kernal)
	blue=cv2.dilate(blue_img, kernal)
	green=cv2.dilate(green_img, kernal)
	yellow=cv2.dilate(yellow_img, kernal)

	split_data=train_test_split(diabetes_data,diabetes_target,test_size=0.1)

	train_data,test_data,train_target,test_target=split_data

	#implementing decision tree classifier
	dsc_algo=DecisionTreeClassifier()
	# taking bitwise and of the frames	
	res_red = cv2.bitwise_and(frame,frame, mask= red_img)	
	res_green = cv2.bitwise_and(frame,frame, mask= green_img)	
	res_blue = cv2.bitwise_and(frame,frame, mask= blue_img)	
	res_yellow = cv2.bitwise_and(frame,frame, mask= yellow_img)
	total=res_red+res_blue+res_green+res_yellow
	
	#tracking the red Color	
	(_,contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>200):
			x,y,w,h = cv2.boundingRect(contour)	
			frame = cv2.rectangle(total,(x,y),(x+w,y+h),(255,0,0),2)
			cv2.putText(total,"Red color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
			
	#Tracking the Blue Color
	(_,contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>200):
			x,y,w,h = cv2.boundingRect(contour)	
			frame = cv2.rectangle(total,(x,y),(x+w,y+h),(255,0,0),2)
			cv2.putText(total,"Blue color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))

	#Tracking the green Color
	(_,contours,hierarchy)=cv2.findContours(green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>200):
			x,y,w,h = cv2.boundingRect(contour)	
			frame = cv2.rectangle(total,(x,y),(x+w,y+h),(0,255,0),2)
			cv2.putText(total,"Green  color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0))  
        
	#Tracking the yellow Color
	(_,contours,hierarchy)=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>200):
			x,y,w,h = cv2.boundingRect(contour)	
			frame = cv2.rectangle(total,(x,y),(x+w,y+h),(0,255,0),2)
			cv2.putText(total,"Yellow  color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0))  
            
           	
		
	#adding all the frames	
	
	cv2.imshow('window',total)
	if cv2.waitKey(2) & 0xFF == ord('q'):
		break


cv2.destroyAllWindows()
cap.release()
