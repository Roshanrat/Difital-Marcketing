#!/usr/bin/env python
# coding: utf-8

# # Introduction

# ### Import packages

# In[1]:


import pandas as pd
import numpy as np


# ### Import Data set as dm_data

# In[7]:


dm_data=pd.read_csv(r"C:\Users\HP\Desktop\digital marketing\Digital marcketing.csv")


# In[9]:


dm_data


# ### Get basic information about the data set

# #### 01)head  ( to show top 5 records of the data set )

# In[11]:


dm_data.head()


# #### 02)tail ( to show bottom 5 records of the data set )

# In[12]:


dm_data.tail()


# #### 03) shape (to get # of rows and # of columns)

# In[13]:


dm_data.shape


# #### 04) size(to show total number of elements)

# In[14]:


dm_data.size


# #### 05) column (to show each column name)

# In[15]:


dm_data.columns


# #### 06) dtypes (to show data type of each column)

# In[16]:


dm_data.dtypes


# #### 07) info()    (to show index,columns,data types of each column,memory at once)

# In[17]:


dm_data.info()


# ## Records the duplicate value and remove that values

# In[18]:


dm_data.duplicated()


# In[19]:


dm_data[dm_data.duplicated()]


# #### So in this data set no any duplicate values 

# ## Null value remove and replace

# In[20]:


dm_data.isnull()


# In[21]:


dm_data.isnull().sum()


# #### In here no any null values.
# #### Now the data set is cleaned.

# In[ ]:




