'''
Created on Apr 23, 2019

@author: facebook
'''

def f(x): 
    a= len(x) 
    x.sort() 
    print("Second Smallest element is:", x[1]) 
x=[12, 45, 2, 41, 31, 10, 8, 6, 4] 
print f(x) 