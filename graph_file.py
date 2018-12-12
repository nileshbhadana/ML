#!/usr/bin/env python
# coding: utf-8

# In[1]:


names=[]
runs=[]


# In[2]:


with open("data.txt","r") as file_data:
     for line in file_data:
             name,run=line.split(",")
             names.append(name)
             runs.append(int(run))


# In[3]:


import matplotlib.pyplot as plt


# In[ ]:


print("1. Simple Graph\n2. Bar Graph\n3. Scatter Graph")
choice=input("Enter any one:")


# In[ ]:


if choice=='1':
    plt.plot(names,runs)
elif choice=='2':
    plt.bar(names,runs)
elif choice=='3':
    plt.scatter(names,runs)
else:
    print("Invalid Option.")


# In[ ]:


plt.grid()
plt.xlabel('Player')
plt.ylabel('Runs')
plt.show()


# In[ ]:





# In[ ]:




