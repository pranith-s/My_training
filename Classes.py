# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 14:51:19 2019

@author: PS43708
"""

class Bird:
    '''This is my first class'''
    
    color='white'
    
    def __init__(self,name):
        self.name = name
        print('%s have born in this world'%self.name)
    
    def fly(self,d):
        self.distance = d
        print('Bird is flying for a distance of %s km'%self.distance)
        
    @classmethod
    def shout(cls):
        print('ko ko ko')
        
        
b1=Bird('pink')
b1.fly('5')
b1.shout()