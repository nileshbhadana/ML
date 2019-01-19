#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 02:22:04 2019

@author: nilesh
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn import svm
from sklearn import linear_model
import matplotlib.pyplot as plt

df=pd.read_csv("/home/nilesh/Desktop/ML/stock_data.csv")

price_data_obj=df['Close']
price_data=price_data_obj.values
price_df=price_data.reshape(-1,1)

day=[]
for i in range(len(price_df)):
    day.append(i)

day_count=np.array(day).reshape(-1,1)
print(type(day),len(day))



price_data_train=price_df[:-50]
price_data_test=price_df[-50:]

print(len(price_data_train),len(price_data_test))

day_target_train=day_count[:-50]
day_target_test=day_count[-50:]

regr=linear_model.LinearRegression()
regr_svm=svm.SVR()

regr.fit(day_target_train,price_data_train)
regr_svm.fit(day_target_train,price_data_train)

prediction=regr.predict(day_target_test)
prediction_svm=regr_svm.predict(day_target_test)


print(prediction)
print(prediction_svm)
print(price_data_test)

plt.plot(day_target_train,price_data_train,'r')
plt.plot(day_target_test,price_data_test,'g')
plt.plot(day_target_test,prediction_svm,'b')
plt.show()
