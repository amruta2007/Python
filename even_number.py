'''
Created on Apr 23, 2019

@author: facebook
'''
#generate even number upto n numbers

a= int(input("Enter the start of range: ")) 
b = int(input("Enter the end of range: ")) 
for i in range(a,b): 
    if i % 2 == 0: 
        print(i) 
        
        
        
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even")
else:
  print("{0} is Odd number".format(num))