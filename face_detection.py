#!/usr/bin/python3
import cv2
cam_cap=cv2.VideoCapture(0)
counter=0
cascade=cv2.CascadeClassifier('face.xml')
while cam_cap.isOpened():
	status,frame=cam_cap.read()
	gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)	
	faces=cascade.detectMultiScale(gray_frame,1.5,5)
	cv2.imshow('live',frame)
	if cv2.waitKey(2) & 0xFF == ord('q'):		
		break
	elif cv2.waitKey(2) & len(faces)!=0:
		counter=counter+1
		print (counter)
		name="image"+str(counter)+".jpg"
		cv2.imwrite(name,frame)
		print('Image Captured')
		cv2.destroyAllWindows()
		if counter==5:
			break
cv2.destroyAllWindows()
cam_cap.release()

