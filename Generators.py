# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 15:56:10 2019

@author: PS43708
"""

def hekk(no):
    count = 0
    
    while count<no:
        yield count
        count +=1
        
ret = hekk(10)
print(ret)
for i in ret:
    print(i)