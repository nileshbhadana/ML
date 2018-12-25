#!/usr/bin/python3
import cv2
font=cv2.FONT_HERSHEY_SIMPLEX
# opening camera
cam_cap=cv2.VideoCapture(0)
# starting counter
counter=0

#cascading
cascade=cv2.CascadeClassifier('face.xml')
while cam_cap.isOpened():
    # reading frame
    frame=cam_cap.read()[1]
    #converting frame to gray 
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)	
    faces=cascade.detectMultiScale(gray_frame,1.5,5)
    
    #counting faces in the frame
    counter=len(faces)
    print(len(faces))
    for (x,y,w,h) in faces:
        #drawing rectangle on the faces
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
    msg="Face Detected="+str(counter)

    #displaying number of face detected 
    cv2.putText(frame,msg,(10,50),font,1,(255,255,255),3,cv2.LINE_AA)
    cv2.imshow('live',frame)

    #handler
    if cv2.waitKey(2) & 0xFF == ord('q'):		
    	break
cv2.destroyAllWindows()
cam_cap.release()

