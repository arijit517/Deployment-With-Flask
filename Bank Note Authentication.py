#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.read_csv('C:/Users/Arijit Raha/Desktop/Sample/DEPLOYMENT/FLASK/BankNote_Authentication.csv')


# In[3]:


df.head(3)


# In[4]:


X=df.iloc[:,:-1]
y=df.iloc[:,-1]


# In[5]:


X.head(1)


# In[7]:


y.head(3)


# In[8]:


from sklearn.model_selection import train_test_split


# In[9]:


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)


# In[10]:


from sklearn.ensemble import RandomForestClassifier
classifier=RandomForestClassifier()
classifier.fit(X_train,y_train)


# In[11]:


y_pred=classifier.predict(X_test)


# In[12]:


from sklearn.metrics import accuracy_score
score=accuracy_score(y_test,y_pred)


# In[13]:


score


# In[14]:


import pickle
pickle_out = open("classifier.pkl","wb")
pickle.dump(classifier, pickle_out)
pickle_out.close()


# In[15]:


classifier.predict([[2,3,4,1]])


# In[ ]:




