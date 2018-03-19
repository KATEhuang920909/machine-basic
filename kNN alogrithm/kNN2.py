
# coding: utf-8


import numpy as np
import operator


# In[2]:


import kNN1


# In[3]:


group,labels=kNN.createDataSet()


# In[4]:


group


# In[5]:


labels


# In[67]:


inX=[1,1]


# In[7]:


dataset=group

print(group)
print(labels)
# In[8]:


k=3


# In[35]:


dataSetSize= dataset.shape[0]#0表示行数，1表示列数


# In[66]:


diffMat=np.tile(inX,(dataSetSize,1))-dataset


# In[29]:


diffMat


# In[31]:


sqdiffMat=diffMat**2



# In[32]:


sqDistances =sqdiffMat.sum(axis=1)#axis=0,按列相加，axis=1按行相加


# In[37]:


distances=sqDistances**0.5


# In[41]:


sortedDistIndicies = distances.argsort()#从小到大排列，输出索引
print(sortedDistIndicies)

# In[38]:


classCount={}


# In[50]:


for i in range(k):
    voteIlabel =labels[sortedDistIndicies[i]]
    print(voteIlabel)
    classCount[voteIlabel]= classCount.get(voteIlabel,0) +1
print(classCount)
keys = classCount.keys()
vals = classCount.values()
lst = [(key, val) for key, val in zip(keys, vals)]
print(lst)
l=sorted(lst, key=operator.itemgetter(1), reverse=True)
print(l[0][0])