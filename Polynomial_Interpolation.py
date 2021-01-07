#!/usr/bin/env python
# coding: utf-8

#program to demonstrate  polynomial interpolation


import numpy as np
import math

#ask user for x
x0= float(input("Enter xo: \t"))
x1= float(input("Enter x1: \t"))
x2= float(input("Enter x1: \t")) 
x3= float(input("Enter x2: \t")) 

#function to construct each row of the matrix 
def matrix_constr(x):
    arr=[]
    for i in range (3,-1,-1): 
        arr.append(x**i)
    return arr 

#trace in value of x  
r_0=matrix_constr(x0) 
r_1=matrix_constr(x1)
r_2=matrix_constr(x2)
r_3=matrix_constr(x3)

#matrix appending as 1d array list
big_arr=[]
big_arr=np.append(big_arr,r_0)
big_arr=np.append(big_arr,r_1)
big_arr=np.append(big_arr,r_2)
big_arr=np.append(big_arr,r_3)
print(big_arr)


# In[12]:


#reshape to matrix 4x4
matrix=np.reshape(big_arr,(4,4))
print(matrix)
print(len(matrix))
#obtain number of row and column
row=matrix.shape[0]
col=matrix.shape[1]
print('row={}'.format(row))
print('colums={}'.format(col))


# In[13]:


#construct y[]
y=[]
y0= float(input("Enter yo: \t"))
y1= float(input("Enter y1: \t"))
y2= float(input("Enter y1: \t"))
y3= float(input("Enter y2: \t")) 
y=np.append(y,[y0,y1,y2,y3])
print(y)


# In[14]:


#append a column of 0 at the end of matrix 
a=np.append(matrix,np.zeros([4,1]),axis=1)
print(a)


# In[15]:


for i in range(row): 
    a[i][-1]=y[i]
print(a)


# In[16]:


#Gauss elimination procedure 
#after this step we will get row echelon form 

for i in range (0,col-1): 
    for j in range(i+1,row):
        a[j,:]= -(a[j][i]/a[i][i]*a[i,:])+a[j,:]
print(a)


# In[28]:


#push the result into a matrix
#call matrix r to store result 
r=np.zeros(4)

for i in range (row-1,-1,-1): 
    r[i]= a[i,-1]- a[i,0:col]@r 

print (r)














