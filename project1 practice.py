
import random
import numpy as np
import math
a=int(input("enter lower number="))
b=int(input("enter upper number="))
x=random.randint(a,b)
k=round(math.log(b-a+1,2))
print("you have",round(math.log(b-a+1,2)),"chance only")     
count=0
while(count<k):
    count+=1
    g=int(input("guess ur number="))
    if(x==g):
        print("congratulation  u guess correct in count =",count)
        break
    elif(x>g):
        print("u guessed small num")
    else:
        print("u guessed big number")
    if(count>=k):
        print("better luck next time")
    
    
    