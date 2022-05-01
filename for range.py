"""
 what is range?
 	range is list generator,but its result is not list
 where use range?
	usually comes with for loop
 why range?
 	do something in fixed times
"""
import random

range(5) # [0,1,2,3]
range(2,5) # [2,3,4]
range(3,8,2) # [3,5,7]
range(10,3,-2) # [10,8,6,4]
print("range(5)= [0,1,2,3] = ", range(5),"\nrange(2,5)= [2,3,4]= ",range(2,5),"\nrange(3,8,2)= [3,5,7]= ",range(3,8,2),"\nrange(10,3,-2)=  [10,8,6,4]= ",range(10,3,-2))

for i in range(100):
	print("This is ",i+1," times, random=",random.randint(1,50)," .")