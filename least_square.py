#!/usr/bin/env python
# coding: utf-8

# In[29]:

#program to demonstrate least_square method of a system of 4 equations
import numpy as np 
from matplotlib import pyplot as plt

n=0 
x=[]
y=[]




def square(x):
    return x*x 
def tri(x): 
    return x*x*x 
def fourth(x):
    return x**4
def fifth(x):
    return x**5
def sixth(x): 
    return x**6 


sum_x=0
sum_square=0 
sum_tri=0
sum_fourth=0 
sum_fifth=0 
sum_sixth=0

with open('data.txt') as f: 
    for line in f.readlines():
        n=n+1 #n counts the line
        arr=line.split() #split column 
        x.append(float(arr[0]))
        y.append(float(arr[1]))
        

        

        
    


# In[30]:


#for testing reference 
print(x)
print("\n")
print(y)


# In[31]:


for i in range(n): 
    sum_x+=x[i]
    sum_square+=square(x[i])
    sum_tri+=tri(x[i])
    sum_fourth+=fourth(x[i])
    sum_fifth+=fifth(x[i])


# In[32]:


#construct the matrix r
r=[]
r1=[n,sum_x,sum_square,sum_tri]
r2=[sum_x,sum_square,sum_tri,sum_fourth]
r3=[sum_square,sum_tri,sum_fourth,sum_fifth]
r4=[sum_tri,sum_fourth,sum_fifth,sum_sixth]
r=np.array([r1,r2,r3,r4])

print(r)


# In[33]:


#construct y array
y_arr=np.zeros(4)
y_arr[0]=np.sum(y)
for i in range(n):
    y_arr[1]+=x[i]*y[i]
    y_arr[2]+=x[i]**2*y[i]
    y_arr[3]+=x[i]**3*y[i]
print(y_arr)



# In[28]:


#solve for a0,a1,a2,a3
a=np.linalg.solve(r,y_arr)
print(a)


# In[42]:


#plot the result function
y_result=np.zeros(n)
for i in range(n): 
    y_result[i]=a[3]*x[i]**3 + a[2]*x[i]**2 + a[1]*x[i] +a[0]

#plt.plot(x,y_result,"o")
#plt.legend(['result func'])
#plt.show()



# In[34]:


#plot the original function 
y_or=np.zeros(n) 

for i in range(n):
    y_or[i]= -2*x[i]**3+10*x[i]*x_or[i]+3*x[i]-7
print(y_or)


# In[41]:


plt.plot(y_result,"-o")
plt.plot(y_or,"-o")
plt.legend(["result func","original func"])
plt.show()


# In[ ]:




