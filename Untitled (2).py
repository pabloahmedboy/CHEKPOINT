#!/usr/bin/env python
# coding: utf-8

# In[1]:


from array import *
array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array: "+str(array_num))
num_list = array_num.tolist()
print("Convert the said array to an ordinary list with the same items:")


# In[4]:


import numpy as np
m = np.arange(6).reshape(2,3)
print("Original matrix:")
print(m)
result =  np.trace(m)
print("Condition number of the said matrix:")
print(result)


# In[5]:


import numpy as np
x = np.array([[0, 10, 20], [20, 30, 40]])
print("Original array: ")
print(x)
print("Values bigger than 10 =", x[x>10])
print("Their indices are ", np.nonzero(x > 10))


# In[6]:


import numpy as np
a = np.array([0, 1, 2])
b = np.array([5, 5, 5])
a + b


# In[10]:


import numpy as np
X = np.array([[4,5,6]])
y=x.mean()
y


# In[ ]:




