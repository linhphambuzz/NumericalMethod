#this program implement the projectile motion 

import math  
import myconst as co


v0= float(input('enter initial velocity:')) 
theta=float(input('enter initial angle:')) 

#angle conversion 
angle = theta* math.pi/180 

#calculate maximum heigh 
max_H = v0**2 * (math.sin(angle))**2/ (2*co.G) 
print('maximum height={} m'.format(max_H))

#calculate maximum range 
max_R= v0**2 * math.sin(2*angle)/ co.G 
print('maximum range={} m'.format(max_R))

#calculate flight time 
t= 2*v0*math.sin(angle)/co.G 
print('flight time={} sec'.format(t)) 
delta_t= t/1000

#create a file name result.txt to write into 
f= open("result.txt","w") 

x0=0
y0=0  
t_update = 0; 
#the loop to print 1000 point of coordinate 
for i in range(1000):
    f= open("result.txt","a")
    t_update= t_update + delta_t
    
    x= x0 + v0*math.cos(angle)* t_update
    f.write('{0}\t'.format(x))
    
    y= y0 + v0*math.sin(angle)* t_update - 0.5*co.G*(t_update**2) 
    f.write ('{0}\n'.format(y))
    
   # print('t={}'.format(t_update)) for debug purpose
 #  print('x{0}={1}'.format(i+1,x))  
  #  print('y{0}={1}'.format(i+1,y)) 

    

