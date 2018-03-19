
# coding: utf-8

# In[28]:


from numpy import *


# In[29]:


import os


# In[30]:


os.chdir(r'H:\自学项目\机器学习\机器学习实战\logistic regression')


# In[31]:


import lr


# In[32]:


dataArr ,labelMat =lr .loadDataSet()


# In[8]:


import importlib


# In[46]:


importlib.reload(lr)


# In[47]:


dataArr ,labelMat =lr .loadDataSet()


# In[48]:


dataArr[:10]


# In[49]:


labelMat[:10]


# In[234]:


lr.gradAscent(dataArr,labelMat)


# In[45]:


from numpy import *


# In[51]:


from importlib import *


# In[212]:


reload(lr)


# In[254]:


reload(lr)


# In[34]:


dataMat,labelMat=lr.loadDataSet()


# In[312]:


weights=lr.gradAscent(dataMat,labelMat)


# In[313]:


weights


# In[250]:


lr.plotBestFit(weights)


# In[265]:


weights =lr.stocGradAscent(array(dataMat),labelMat)


# In[266]:


weights


# In[239]:


weights[1]


# In[210]:


weights[1]


# In[47]:


reload(lr)


# In[304]:


dataArr ,labelMat =lr.loadDataSet()


# In[305]:


weights=lr.stocGradAscent(array(dataMat),labelMat)


# In[306]:


weights


# In[307]:


lr.plotBestFit(weights)


# In[308]:


reload(lr)


# In[315]:


lr.plotBestFit(weights.getA())


# In[354]:


reload(lr)


# In[39]:


weights=lr.stocGradAscent1(array(dataMat),labelMat)


# In[356]:


dataArr ,labelMat =lr.loadDataSet()


# In[357]:


lr.plotBestFit(weights)


# In[40]:


weights


# In[11]:


import os


# In[52]:


os.chdir(r'H:\自学项目\机器学习\machinelearninginaction\Ch05')


# In[21]:


from importlib import *


# In[24]:


import lr


# In[48]:


os.chdir(r'H:\自学项目\机器学习\机器学习实战\logistic regression')


# In[53]:


lr.multTest()


# In[50]:


importlib.reload(lr)


# In[45]:


import importlib

