'''
Created on Apr 23, 2019

@author: facebook
'''
def f(x): 
    a = len(x) 
    b = [] 
    for i in range(a): 
        k = i + 1
        for j in range(k, a): 
            if x[i] == x[j] and x[i] not in b:
                  b.append(x[i]) 
    return b 
l = [10,20,10,30,30,40,50,60,50] 
print (f(l)) 

