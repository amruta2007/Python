'''
Created on Apr 23, 2019

@author: amruta
'''
import random
def random_line():
    lines = open().read().splitlines()
    return random.choice(lines)
print(random_line(‘test.txt’))