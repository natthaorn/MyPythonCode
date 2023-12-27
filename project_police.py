#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import library# 
import pandas as pd


# In[2]:


police = pd.read_csv(r"C:\Users\natth\Documents\py_dataset\police.csv")


# In[3]:


police


# In[4]:


police.info()


# In[5]:


## Remove the column that only contains missing values.##
# police.isnull().sum()


# In[8]:


police.drop(columns='country_name',inplace=True)


# In[9]:


police


# In[15]:


## For Speeding , were Men or Women stopped more often ? ##
# police[police['violation'] == 'Speeding']['driver_gender'].value_counts()
# or # 
police[police.violation == 'Speeding'].driver_gender.value_counts()


# In[16]:


## Does gender affect who gets searched during a stop ? Question ( mapping + data-type casting ) ##  
# df.groupby('Column_1').Column_2.sum()
police.groupby('driver_gender').search_conducted.sum()


# In[19]:


##  What is the mean stop_duration ? ##
#df['Column_name'].mean()
police['stop_duration'].value_counts()


# In[20]:


# use map function to map string with key value pairs
police['stop_duration'] = police['stop_duration'].map({'0-15 Min': 7.5,'16-30 Min': 24,'30+ Min': 45})
police


# In[21]:


police['stop_duration'].mean()


# In[22]:


##  Compare the age distributions for each violation ## 
#df.groupby('Column_1').column_2.describe()
police.groupby('violation').driver_age.describe()


# In[ ]:




