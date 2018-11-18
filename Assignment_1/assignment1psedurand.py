# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:44:09 2018

@author: Jordan and Nathalie
"""

import math
import random
import numpy as np
import matplotlib.pyplot as plt
import csv


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
    
def createSet(s, i,sx,sy):
    
    fraction = 0
    inSet = []
    outSet = []
    inSet.append([])
    inSet.append([])
    outSet.append([])
    outSet.append([])
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

def save(results):
    """ Saves the results to a csv file. """
        
    filename = 'data/results.csv'
        
    with open(filename, 'a', newline = '') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        
        for row in results:
            writer.writerow(row)
               
    # List is reset for next set of reflections
    return []
 
def main():
    sxarry = [7536, 4321, 6843, 5769]
    syarry = [8354, 4682, 6779, 3567]
    #sxarry = [7536]
    #syarry = [8354]
    
    results = []

    for k in range(0, len(sxarry)):
        rx = sxarry[k]
        ry = syarry[k]
        print("Seed: %i"%(k))
        for x in np.arange(500, 5000, 500):

            s = 100000 #Number of points
            i = x #Numbber of times through loop

            fraction, inSet, outSet = createSet(s, i, rx, ry)

            results.append([i,s,fraction,rx,ry])
            print("With %i iterations, the number of points in the set is %i/%i" %(i,fraction,s))
            #plt.figure(x/500)
            #plt.title("Madolbrot Set with {} points and {} loops".format(s, i))
            #plt.plot(inSet[0], inSet[1], 'b.')
            #plt.show()
    
    results = save(results)
    print("Done")
    
if __name__ == "__main__":
    main()
