#!/usr/bin/env python
# coding: utf-8

# # Cars Dataset

# In[1]:


import pandas as pd


# In[2]:


cars = pd.read_csv(r"C:\Users\natth\Documents\py_dataset\project2_car.csv")
cars


# # EDA

# In[7]:


## checking null 
cars.isnull().sum()


# In[8]:


cars.info()


# In[11]:


#manage with 'Cylinders' column which have null 
cars['Cylinders'].fillna(cars['Cylinders'].mean(), inplace=True)


# In[13]:


#check again
cars.isnull().sum()


# #### Q2. Check what are the different type of 'Make' and the count for each 'Make' in DF

# In[16]:


cars['Make'].value_counts()


# #### Q3. Show the records where Origin is Asia and Europe

# In[23]:


cars[cars['Origin'].isin(['Asia','Europe'])]
# the answer is 281 rows


# #### Remove all the records where weight is above 4000

# In[27]:


# cars[cars['Weight'] > 4000]
cars[~(cars['Weight'] > 4000)]


# #### Increase all the value of 'MPG_city' column by 3

# In[30]:


#write function to apply 
cars['MPG_City'] = cars['MPG_City'].apply(lambda x: x+3)


# In[31]:


cars


# In[32]:





# In[ ]:




