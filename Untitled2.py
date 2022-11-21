#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[3]:


import pandas as pd
df = pd.read_csv('FoodBalanceSheets_E_Africa_NOFLAG.csv', encoding ='latin-1')


# In[4]:


df.head()
print(df.head())


# In[5]:


df.info()


# In[7]:


df.groupby('Item').sum()


# In[9]:


df['Area'].nunique


# In[11]:


print(df['Area'].unique)


# In[12]:


df.nunique()


# In[14]:


df.groupby('Element').sum()


# In[21]:


New= df[['Y2017','Area']]


# In[32]:


New.groupby('Area').sum().sort_values('Y2017')


# In[30]:


New.sort_values('Area')


# In[31]:


New.sort_values('Y2017')


# In[ ]:




