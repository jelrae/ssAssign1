# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:44:09 2018

@author: Jordan and Nathalie
"""

from random import random as rand

def randPoint():
    
    x = rand() * 3. - 2.
    y = rand() * 3. - 1.5
    
    return x,y

def checkMandelbrot(x,y):
    
    print("helloworld")
 
def main():
    
    x,y = randPoint()
    
if __name__ == "__main__":
    main()