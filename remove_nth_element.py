'''
Created on Apr 23, 2019

@author: facebook
'''
def f(string, i):  
    a = string[ : i] 
    b = string[i + 1: ] 
    return a + b

if __name__ == '__main__': 
      
    string = "amrutapatil"
    i = 5
    print(f(string, i)) 





s = 'facebook'
s = s[:3]+s[4:]
print(s)