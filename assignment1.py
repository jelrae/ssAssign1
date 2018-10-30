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

def loopMadelbrot(xi, yi, x, y):
    xt = (x**2 + y**2) + xi
    yt = (2*x*y) + yi
    return xt, yt

def checkMandelbrot(x,y,numLoop):

    ix = x
    iy = y
    
    xn = (x**2 + y**2) + xi
    yn = (2*x*y) + yi

    for i in range(0,numLoop):
        xn, yn = loopMadelbrot(xn, yn, xi, yi)
        if xn > 2 or yn > 2:
            return False 

    return True

def main():
    
    x,y = randPoint()
    
if __name__ == "__main__":
    main()
