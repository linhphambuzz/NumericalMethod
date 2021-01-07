import numpy as np
import matplotlib.pyplot as plt #libr to plot function 

#this program evaluate the derivative of a given function to obtain the slope of it. 

#range of number 
a=-10
b=10 
h=2 

#how many pts we're going to be evaluating 
n=int((b-a)/h)  
print(n) 

#function to evaluate 
def eva_func(c):
    return 3*c**2-2*c+6 

#linspace is a function in numpy 
x=np.linspace(a,b,n) 

#declare a list dl  
dl=[] 
for i in range(n-1):
    d1= eva_func(x[i]+h)
    d2= eva_func(x[i]-h)
    d=d1-d2/(2*h) 
    #append d  into dl     
    dl.append(d) 
#convert list into array 
dy=np.array(dl) 

#plot the function 
plt.plot(x,dy) 
plt.show() 
