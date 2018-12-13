#!/usr/bin/python3
import cv2
cv2.__version__
left_img=cv2.imread('left.jpg')
right_img=cv2.imread('right.jpg')
new_img=cv2.addWeighted(left_img,0.5,right_img,0.5,0)
cv2.imshow('new image',new_img)
cv2.waitKey(0)
