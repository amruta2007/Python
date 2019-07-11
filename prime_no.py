'''
Created on May 9, 2019

@author: facebook
'''

num = int(input("enter a number: "))
 
for i in range(2, num):
    if num % i  == 0:
        print("not prime number")
        break
else:
    print("prime number")