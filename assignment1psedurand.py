# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:44:09 2018

@author: Jordan and Nathalie
"""

import math
import random
import numpy as np
import matplotlib.pyplot as plt


def randPoint(sx, sy):
    incirc = False
    while not incirc:
        random.seed(sx)
        sx = random.random()
        x = sx * 3. - 2.
        random.seed(sy)
        sy = random.random()
        y = sy * 3. - 1.5
        if math.sqrt(x**2 + y**2) <= 2:
            return x, y, sx, sy

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
    sx = 7536
    sy = 8354
    for j in range(s):

        x,y,sx,sy = randPoint(sx, sy)
        
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

    for x in np.arange(500, 10000, 500):

        s = 100000 #Number of points
        i = x #Numbber of times through loop

        fraction, inSet, outSet = createSet(s, i)

        print("The number of points in the set is %i/%i" %(fraction,s))
        plt.figure(x/500)
        plt.title("Madolbrot Set with {} points and {} loops".format(s, i))
        plt.plot(inSet[0], inSet[1], 'b.')
        plt.show()
    
    print("Done")
    
if __name__ == "__main__":
    main()
