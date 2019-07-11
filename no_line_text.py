'''
Created on May 15, 2019

@author: amruta
'''
def f(x):
with open(x) as f:
for i, l in enumerate(f):
pass
return i + 1
print(“Number of lines in the file: “,f(“test.txt”))