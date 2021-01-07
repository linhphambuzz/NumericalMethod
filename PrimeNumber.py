#program to check how many prime number less than a given number
import math 

n=int(input('Enter a number:')) 
a=2
count=0 
#check if a is a prime number 
while (a<=n): 
    count=0                          # c is to count how many dividing are there with remainder  
    for i in range(1,a):
        if a%i == 0 and i!=1:     #check if a could be divided by any smaller number with remainder. 
            break 
        else:
            count=count+1                  #if there's remainder, c is increased by 1 
    if count == a-1:  
        count=count+1 
        print('{} is a prime number'.format(a))
    a=a+1 
          
print('there are {} prime number'.format(count)) 
        
