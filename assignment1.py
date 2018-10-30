# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:44:09 2018

@author: Jordan and Nathalie
"""

from random import random as rand
import matplotlib.pyplot as plt

def randPoint():
    
    x = rand() * 3. - 2.
    y = rand() * 3. - 1.5
    
    return x,y

def loopMadelbrot(xi, yi, x, y):
    xt = (x**2 + y**2) + xi
    yt = (2*x*y) + yi
    return xt, yt

def checkMandelbrot(x,y,numLoop):

    xi = x
    yi = y
    
    xn = (x**2 + y**2) + xi
    yn = (2*x*y) + yi

    for i in range(0,numLoop):
        xn, yn = loopMadelbrot(xn, yn, xi, yi)
        if xn > 2 or yn > 2:
            return False 

    return True
    
def createSet(s, i):
    
    fraction = 0
    inSet = []
    outSet = []
    inSet.append([])
    inSet.append([])
    outSet.append([])
    outSet.append([])
    
    for j in range(s):
    
        x,y = randPoint()
        
        check = checkMandelbrot(x,y,i)
        
        if check == True:
            
            fraction += 1
            inSet[0].append(x)
            inSet[1].append(y)
        
        else:
            outSet[0].append(x)
            outSet[1].append(y)
            
    return fraction, inSet, outSet
 
def main():
    
    
    s = 1000
    i = 1000
    
    fraction, inSet, outSet = createSet(s, i)
    
    print("The number of points in the set is %i/%i" %(fraction,s))
    plt.figure()
    plt.plot(inSet[0], inSet[1], 'bo')
    plt.plot(outSet[0], outSet[1], 'ro')
    plt.show()
    
    
    
if __name__ == "__main__":
    main()
