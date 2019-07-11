'''
Created on Apr 23, 2019

@author: facebook
'''
#genrate febonacci series upto n number

a=0
b=1
fibo=[a,b]
n= int(input("Enter number: ")) 
while b<n:
    a,b = b,a+b
    fibo.append(b)
    print fibo
