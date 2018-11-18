# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:44:09 2018

@author: Jordan and Nathalie

area for random: 8.3765
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
        if x**2 + y**2 <= 4:
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
        
        # This if/else statement is necessary because the index is sometimes
        # incorrect due to rounding errors
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
        

def loopMandelbrot(x, y, xi, yi):


    xt = (x**2 - y**2) + xi
    yt = (2*x*y) + yi
    return xt, yt

def checkMandelbrot(x,y,numLoop):

    xi = x
    yi = y
    
    xn = (x**2 - y**2) + xi
    yn = (2*x*y) + yi

    for i in range(0,numLoop):
        xn, yn = loopMandelbrot(xn, yn, xi, yi)
        if xn**2 + yn**2 >=4:
            return False 

    return True
    
def createSet(s, i):
    
    fraction = 0
    results = []
    
    for j in range(s):

        x,y = randPoint()

        check = checkMandelbrot(x,y,i)

        if check == True:

            fraction += 1
            
        if j % 1000 == 0:
            
            results.append(["random",i,j,s,fraction])

    results.append(["random",i,s,s,fraction])

    return fraction, results

def createHypercube(s,i):
    
    fraction = 0
    # hypercube(s) for hypercube, orthogonal(s) for orthogonal
    xs,ys = hypercube(s)
    results = []
    
    for j in range(s):


        check = checkMandelbrot(xs[j],ys[j],i)

        if check == True:

            fraction += 1
            
        if j % 1000 == 0:
            
            results.append(["orthogonal",i,j,s,fraction])

    results.append(["orthogonal",i,s,s,fraction])
    return fraction, results

def save(results):
    """ Saves the results to a csv file. """
        
    filename = 'data/resultsnightloopOrthremain.csv'
        
    with open(filename, 'a', newline = '') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        
        for row in results:
            writer.writerow(row)
               
    # List is reset for next set of results
    return []
 
def main():
    
    randoms = [1000, 5000, 10000, 20000, 30000]
    hypers = [100, 500, 1000, 5000, 10000]
    leftover = [20000, 30000]
    
    # Set this very high to create a loop that runs all night
    for l in range(100):
        results = []
    
        for j in leftover:
            print("Loop number: %i"%(l))
            for x in np.arange(3000, 6000, 500):
    
                s = j #Number of points
                i = x #Numbber of times through loop
                
                # createSet for random, createHypercube for hypercube
                fraction, results = createHypercube(s, i)
                
                # argument 0 is "random" for random and "hypdercube" for hypercube
                #results.append(["random",i,s,fraction])
                print("With %i iterations, the number of points in the set is %i/%i" %(i,fraction,s))
        
                results = save(results)
        print("Done")
    
if __name__ == "__main__":
    main()
