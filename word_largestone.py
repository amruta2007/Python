'''
Created on Apr 23, 2019

@author: facebook
'''
def f(x):
    a = []
    for i in x:
        a.append((len(i), i))
    a.sort()
    return a[-1][1]
print(f(["facebook", "shrikant", "patil"]))