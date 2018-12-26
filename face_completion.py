#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 04:56:10 2018

@author: nilesh
"""

#importing libraries,dataset,etc
from sklearn.datasets import fetch_olivetti_faces
from sklearn.ensemble import ExtraTreesRegressor
import matplotlib.pyplot as plt
import numpy as np

data=fetch_olivetti_faces()
print(dir(data))
targets=data.target

#reshaping image data to 2D array
data=data.images.reshape((data.images.shape[0]),-1)
print(data.shape)

#dividing training and testing data
train_data=data[targets<30]
test_data=data[targets>=30]

#counting number of total rows in a image 
pixels=data.shape[1]   

#dividing train and test face data in upper and lower half
x_train=train_data[:,:int(0.5*pixels)]  #upper half of face
y_train=train_data[:,int(0.5*pixels):]  #lower half of face
x_test=test_data[:,:int(0.5*pixels)]  
y_test=test_data[:,int(0.5*pixels):]  

#calling regressor
regres=ExtraTreesRegressor(n_estimators=10,max_features=32,random_state=0)

#training the data 
#training upper half for lower half
regres.fit(x_train,y_train)

#now predicting the output Y from x 
predicted_y_output=regres.predict(x_test)

#giving the number of faces to plot
faces_to_plot=6
#defining shape of image to plot
image_shape=(64,64)

#setting the size of image
plt.figure(figsize=(3. *faces_to_plot,6))

#now plotting the predicted face
for i in range(1,1+faces_to_plot):
    #generating a random face id 
    face_id=np.random.randint(x_test.shape[0])
    
    #joining the upper and lower face arrays
    original_face=np.hstack((x_test[face_id],y_test[face_id]))    #original face from test data
    completed_face=np.hstack((x_test[face_id],predicted_y_output[face_id]))  #completed face with original upper half and predicted lower half
    
    #creating subplots to plot all the required images
    plt.subplot(2,faces_to_plot,i)      # 2 rows, n columns and index of every position
    plt.axis("off")     #keeping axis off
    plt.imshow(original_face.reshape(image_shape))   #showing the original face
    
    plt.subplot(2,faces_to_plot,i+faces_to_plot)    #2 rows, n coloumns and i+number as position index
    plt.axis("off")
    plt.imshow(completed_face.reshape(image_shape))     #showing the completed face
    
plt.show()

