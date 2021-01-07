#!/usr/bin/env python
# coding: utf-8

# In[7]:


import math


def func(x): 
    return 3*pow(x,2)-6*x+3

a=2.0
b=5.5
n=10000 
dx=(b-a)/n #how many points? 

 
integral= (func(a)+func(b))/2 
for i in range(1,n): 
    x=a+i*dx 
    integral=integral+ func(x)
integral= integral*dx 
print(integral)
    
    


# In[ ]:





# In[ ]:




