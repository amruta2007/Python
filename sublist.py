'''
Created on Apr 23, 2019

@author: facebook
'''
def isSubset(list_, sub_list):
    for item in sub_list:
        if sub_list.count(item) > list_.count(item):
            return False
    return True