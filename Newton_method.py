#!/usr/bin/env python
# coding: utf-8

# In[7]:


from matplotlib import pyplot as plt  
import numpy as np 
import os 

def eval_func(z):
    return pow(z,3)-z+2 

def deriv(z): 
    return 3*pow(z,2)-1 

a=-6.0
b=6.0
n=100 
x0=-20000.0 
tol=1.0e-06
for i in range(n): 
    if abs(eval_func(x0))<= tol:
        print('root {0} is {1}'.format(i,x0))
        break 
    xn=x0 -(eval_func(x0)/deriv(x0))
    x0=xn






# In[ ]:





# In[ ]:




