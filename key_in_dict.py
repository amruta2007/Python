'''
Created on Apr 24, 2019

@author: facebook
'''

def checkKey(dict, key):   
    if key in dict.keys(): 
        print("Present") 
        print("value =", dict[key]) 
    else: 
        print("Not present") 
dict = {'a': 100, 'b':200, 'c':300} 
  
key = 'b'
checkKey(dict, key) 
  
key = 'z'
checkKey(dict, key) 