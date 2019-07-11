'''
Created on Apr 24, 2019

@author: facebook
'''
#def f(str): 
 ##   str = str.split()          
 #   str2 = [] 
##    for i in str:               
 #       if i not in str2: 
#            str2.append(i)     
#    for i in range(0, len(str2)): 
 #       print('Frequency of', str2[i], 'is :', str.count(str2[i]))     
  
#def main(): 
 #   str ='apple mango apple orange orange apple guava mango mango'
#f(str)                     
  
#if __name__=="__main__": 
#    main()             

from collections import Counter
t = 'i i am facebook patil'
print(Counter(t.split()))