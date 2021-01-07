#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math 
import matplotlib.pyplot as plt 


#define the function that need to find the root 
def eval_func(z):
    return pow(z,3)-4*z+4 

tolerance=1.0e-6 
a=0
b=4

#plotting
h=0.1
n=(b-a)/h
x=[] 
y=[]

#f=open("bisection_method.txt","a")
for i in range(100): 
    x.append(a+i*h) 
    x0=a+i*h
    y.append(eval_func(x0))
   # f.write('{0},{1}'.format(x,y))
plt.plot(x,y) 
plt.show()



for i in range(1,101):
    fa=eval_func(a)
    fb=eval_func(b)
    c=(a+b)/2 
    fc=eval_func(c)
    if abs(fc) <= tolerance or abs((b-a)/2) <= tolerance: 
        print('Root{0}\t{1}\t{2}'.format(i,c,fc))
        break 
    else: 
        if fa*fc<=0: 
            b=c 
        else:
            a=c
            

            






# In[ ]:





# In[ ]:




