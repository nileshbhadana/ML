#!/usr/bin/python3
import cv2
cam_cap=cv2.VideoCapture(0)
while cam_cap.isOpened():
	status,frame=cam_cap.read()
	#frame=frame+50
	gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)	
	cv2.circle(frame,(350,200),100,(0,0,255),5)
	cv2.imshow('live',frame)
	if cv2.waitKey(100) & 0xFF == ord('q'):		
		break
	elif cv2.waitKey(2) & 0xFF == ord('c'):
		cv2.imwrite('captured Image.jpg',frame)
		print('Image Captured')
		cv2.destroyAllWindows()
cv2.destroyAllWindows()
cam_cap.release()
