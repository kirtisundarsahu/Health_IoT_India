#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('calgary_edmonton.csv')
df.head()


# In[2]:


#shape of our data
df.shape


# In[3]:


df['Temperature_ctrl'].value_counts()
sns.countplot(x='Datetime', data=df, palette='hls')


# In[6]:


sns.relplot(x="Datetime", y="Temperature_ctrl", kind="line", data=df)


# In[7]:


plt.xticks(fontsize=8, rotation=90)


# In[ ]:




