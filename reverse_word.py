'''
Created on Apr 23, 2019

@author: facebook
'''

x='i am facebook patil'
for i in x.split('\n'):
    print(' '.join(i.split()[::-1]))
    
    
x = 'i am facebook'
p = x.split()
print(''.join(x[::-1]))