'''
Created on Apr 23, 2019

@author: facebook
'''


#PRINT LOWERCASE+UPPERCASE_SPASE  LATTER IN STRING

string ='GeeksforGeeks is a computer Science portal for Geeks'
newstring ='' 
count1 = 0
count2 = 0
  
for a in string:  
    if (a.isupper()) == True: 
        count1+= 1
        newstring+=(a.lower()) 
    else:
        (a.islower()) == True
        count2+= 1
        newstring+=(a.upper()) 
print("In original String : ") 
print("Uppercase -", count1) 
print("Lowercase -", count2)  
print(newstring) 




str1 = 'AMRUTASSS'
print(any(c.islower() for c in str1))




word = "Programming is fun!"

for letter in word:
        if letter.lower():
            print(letter)