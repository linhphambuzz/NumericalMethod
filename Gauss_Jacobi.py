#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np 

a=np.array([[-1,2,3,-4],[2,5,-6,1],[4,1,3,-3],[-6,2,-2,-3]])
b=np.array([41,-16,28,13])

x_old=np.array([3,6,4,8])
x_new=np.array([0,0,0,0])
n=1000

for i in range (n): 
    x_new[0]=(b[0]-a[0][1]*x_old[1]-a[0][2]*x_old[2]-a[0][3]*x_old[3])/a[0][0]
    x_new[1]=(b[1]-a[1][0]*x_old[0]-a[1][2]*x_old[2]-a[1][3]*x_old[3])/a[1][1] 
    
    
    if sum(x_new)-sum(old) ==0: 
        print('Solution found at iteration{}'.format(i+1))
        print(x_new)
        sys.exit() 
    x_old=x_new 
        



