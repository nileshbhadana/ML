#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 02:22:04 2019

@author: nilesh
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
#import csv  
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import linear_model


def prepare_data(df,forecast_col,forecast_out,test_size):
    label = df[forecast_col].shift(-forecast_out)#creating new column called label with the last 5 rows are nan
    X = np.array(df[[forecast_col]]); #creating the feature array
    print(X)
    X = preprocessing.scale(X) #processing the feature array
    print(X)
    X_lately = X[-forecast_out:] #creating the column i want to use later in the predicting method
    X = X[:-forecast_out] # X that will contain the training and testing
    label.dropna(inplace=True) #dropping na values
    y = np.array(label)  # assigning Y
    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.3) #cross validation 

    response = [X_train,X_test , Y_train, Y_test , X_lately]
    return response;





df = pd.read_csv("/home/nilesh/Desktop/ML/stock_data_5Y.csv") #loading the csv file
'''
dates=[]
prices=[]
with open('/home/nilesh/Desktop/stock_data.csv', 'r') as csvfile:
    csvFileReader = csv.reader(csvfile)
    next(csvFileReader) # skipping column names
    for row in csvFileReader:
        dates.append(row[0])
        prices.append(float(row[3]))
print(dates)
print(prices)'''

forecast_col = 'Close' #choosing which column to forecast
forecast_out = 5 #how far to forecast 
test_size = 0.2 #the size of my test set

X_train, X_test, Y_train, Y_test , X_lately =prepare_data(df,forecast_col,forecast_out,test_size) #calling the method were the cross validation and data preperation is in

learner = linear_model.LinearRegression(); #initializing linear regression model

learner.fit(X_train,Y_train) #training the linear regression model
score=learner.score(X_test,Y_test)#testing the linear regression model

forecast= learner.predict(X_lately) #set that will contain the forecasted data

#print(len(X_train),len(df['Date']),len(Y_train),len(X_test),len(Y_test))
#print(X_train)
#print(Y_train)
print(forecast)
print(score)



#creating new column called label with the last 5 rows are nan
    
