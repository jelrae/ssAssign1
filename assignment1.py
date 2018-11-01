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

def loopMadelbrot(x, y, xi, yi):
    xt = (x**2 - y**2) + xi
    yt = (2*x*y) + yi
    return xt, yt

def checkMandelbrot(x,y,numLoop):

    xi = x
    yi = y
    
    xn = (x**2 + y**2) + xi
    yn = (2*x*y) + yi

    for i in range(0,numLoop):
        xn, yn = loopMadelbrot(xn, yn, xi, yi)
        if abs(xn) > 2 or abs(yn) > 2:
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

def accuracy(smin,smax,sstep,imin,imax,istep):
    
    for s in range(smin,smax+1,sstep):
        for i in range(imin,imax+1,istep):
            print(i,s)
            
            fraction, inSet, outSet = createSet(s, i)
    
            print("The number of points in the set is %i/%i" %(fraction,s))
            plt.figure()
            plt.plot(inSet[0], inSet[1], 'b.')
            #plt.plot(outSet[0], outSet[1], 'ro')
            plt.show()
 
def main():
    
    smin = 100000
    smax = 600000
    sstep = 100000
    
    imin = 700
    imax = 1500
    istep = 100
    
    accuracy(smin,smax,sstep,imin,imax,istep)
    
    
    
    
    
if __name__ == "__main__":
    main()
