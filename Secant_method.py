#!/usr/bin/env python
# coding: utf-8

# In[6]:


import math
import matplotlib 

#define the function that need to find the root 
def eval_func(z):
    return pow(z,2)-4 
#pick 2 initial points 
x1=3
x2=5
tolerance=1.0e-10

for i in range(1000):
    x3=x2-eval_func(x2)*(x2-x1)/(eval_func(x2)-eval_func(x1))
    if eval_func(x3)<tolerance:
        print('Root{0} x={1} f(x)={2}'.format(i,x3,eval_func(x3)))
        break
    x1=x2
    x2=x3 
print(x3)   


    
        









# In[ ]:





# In[ ]:




