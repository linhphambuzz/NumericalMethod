#!/usr/bin/env python
# coding: utf-8

# In[4]:
#program to implement Gauss_seidel method of solving system of equation 

import numpy as np 

a=np.array([[4,2,3],[3,-5,2],[-2,3,8]])
b=np.array([8,-14,27])


x_old=np.array([0,0,0])
x_new=np.array([0,0,0])
n=1000 

for i in range (n): 
    x_new[0]=(b[0]-a[0][1]*x_old[1]-a[0][2]*x_old[2])/a[0][0] 
    x_new[1]=(b[1]-a[1][0]*x_new[0]-a[1][2]*x_old[2])/a[1][1] 
    x_new[2]=(b[2]-a[2][0]*x_new[0]-a[2][1]*x_new[1])/a[2][2]
    if sum(x_new)-sum(x_old)==0:
        print(x_new)
        break
    x_old=x_new
    
        
    
    
    




# In[ ]:




