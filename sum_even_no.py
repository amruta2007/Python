'''
Created on May 9, 2019

@author: facebook
'''
n=int(input('Enter the limit '))
i=1
sum=0
while i<n:
    if i%2==0:
        sum=sum+i
    i=i+1
print 'Sum of even numbers',sum