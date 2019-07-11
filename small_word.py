'''
Created on Jun 27, 2019

@author: facebook
'''
s = 'Happy day'
l = s.split()
print min(l, key=len)


s = 'Happy day'
l = s.split()
print max(l, key=len)
