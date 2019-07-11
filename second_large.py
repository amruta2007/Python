'''
Created on Apr 23, 2019

@author: facebook
'''
def f(x): 
    a= len(x) 
    x.sort() 
    print("Second largest element is:", x[a-2]) 
x=[12, 45, 2, 41, 31, 10, 8, 6, 4] 
print f(x) 