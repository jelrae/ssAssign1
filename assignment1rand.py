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
import sys


def randPoint():
    incirc = False
    while not incirc:
        random.seed()
        sx = random.random()
        x = sx * 3. - 2.
        random.seed()
        sy = random.random()
        y = sy * 3. - 1.5
        if math.sqrt(x**2 + y**2) <= 2:
            return x, y
    
        
def hypercube(s):
    
    deltax = 3. / s
    deltay = 3. / s
    
    xs = []
    ys = []
    
    for x in np.arange(-2., 1., deltax):
        
        xs.append(random.random()*deltax + x)
        
    for y in np.arange(-1.5, 1.5+deltay, deltay):
        
        ys.append(random.random()*deltay + y)
        
    random.shuffle(xs)
    random.shuffle(ys)
    
    return xs,ys

def orthogonal(s):
    
    deltax = 3. / s
    deltay = 3. / s
    
    xs = []
    ys = []
    
    subspaces = 10
    
    if s % (subspaces**2) !=0:
        print("Error: s % subspaces^2 has to be 0.")

        sys.exit(1)
    
    perarea = s/subspaces
    
    for i in range(subspaces):
        xs.append([])
        ys.append([])
            
    
    for x in np.arange(-2., 1., deltax):
        index = int((x+2)*subspaces/3.)
        
        if len(xs[index]) < perarea:
            xs[index].append(random.random()*deltax + x)
        
        else:
            xs[index+1].append(random.random()*deltax + x)
        
    for y in np.arange(-1.5, 1.5, deltay):
        index = int((y+1.5)*subspaces/3.)
        
        if len(ys[index]) < perarea:
            ys[index].append(random.random()*deltay + y)
            
        else:
            ys[index+1].append(random.random()*deltay + y)
        
    for i in range(subspaces):
        random.shuffle(xs[i])
        random.shuffle(ys[i])
        
    xfinal = []
    yfinal = []
        
    for i in range(subspaces):
        
        therange = int(perarea*i/subspaces)
        
        for k in range(subspaces):
            
            for l in range(therange,therange+int(perarea/subspaces)):
                
                xfinal.append(xs[k][l])
        
        for j in range(int(perarea)):
            
            yfinal.append(ys[i][j])
            
    return xfinal, yfinal
        

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
    
    for j in range(s):

        x,y = randPoint()

        check = checkMandelbrot(x,y,i)

        if check == True:

            fraction += 1

    return fraction

def createHypercube(s,i):
    
    fraction = 0
    xs,ys = orthogonal(s)
    
    for j in range(s):


        check = checkMandelbrot(xs[j],ys[j],i)

        if check == True:

            fraction += 1

    return fraction

def save(results):
    """ Saves the results to a csv file. """
        
    filename = 'data/resultsnightloop.csv'
        
    with open(filename, 'a', newline = '') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        
        for row in results:
            writer.writerow(row)
               
    # List is reset for next set of results
    return []
 
def main():
    
    # Set this very high to create a loop that runs all night
    for l in range(1):
        results = []
    
        for j in range(3,6):
            print("Loop number: %i"%(l))
            for x in np.arange(2000, 7000, 500):
    
                s = 10**j #Number of points
                i = x #Numbber of times through loop
                
                # createSet for random, createHypercube for hypercube
                fraction = createHypercube(s, i)
                
                # argument 0 is "random" for random and "hypdercube" for hypercube
                results.append(["orthogonal",i,s,fraction])
                print("With %i iterations, the number of points in the set is %i/%i" %(i,fraction,s))
        
        results = save(results)
        print("Done")
    
if __name__ == "__main__":
    main()
