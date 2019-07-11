'''
Created on Apr 23, 2019

@author: facebook
'''
def f(list): 
    l = []  
    for i in list: 
        if i not in l: 
            l.append(i)
    for i in l: 
        print i, 
list = ['pink','pink','blue'] 
print("the unique values from list is") 
f(list) 




'''
x = input("Please enter a sentence: ")

print("The words in that sentence are: ", x.split())

unique = set(x)
print("Here are the unique words in that sentence: ",unique)'''
