# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 11:23:17 2019

@author: PS43708
"""

def scold(narg):
    def scoldhim(arg):
        if 'praneeth' in arg:
            print("%s Anna Nuvv Thoppu"%arg)
        else:
            print("Bichara %s"%arg)
            narg(arg)
    return scoldhim

@scold
def hello(name):
    print('Namaste %s Anna'%name)
hello('praneeth')