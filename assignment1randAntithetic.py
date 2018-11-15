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
        su = 1-sx
        x = sx * 3. - 2.
        u = su * 3. - 2.
        random.seed()
        sy = random.random()
        sv = 1-sy
        y = sy * 1.5
        v = sv * 1.5
        if (x**2 + y**2 <= 4) and (u**2 + v**2 <= 4):
            return x, y, u, v
    
        
def hypercube(s):
    
    deltax = 3. / s
    deltay = 1.5 / s
    
    xs = []
    ys = []
    us = []
    vs = []

    for x in np.arange(-2., 1., deltax):

        xr = random.random()
        ur = 1- xr
        xs.append(xr*deltax + x)
        us.append(ur*deltax + x)

        
    for y in np.arange(0, 1.5+deltay, deltay):

        yr = random.random()
        vr = 1-yr
        ys.append(yr*deltay + y)
        vs.append(vr*deltay + y)

        
    random.shuffle(xs)
    random.shuffle(us)
    random.shuffle(ys)
    random.shuffle(vs)
    
    return xs,ys, us, vs

def orthogonal(s):
    
    deltax = 3. / s
    deltay = 1.5 / s
    
    xs = []
    ys = []
    us = []
    vs = []
    
    subspaces = 10
    
    if s % (subspaces**2) !=0:
        print("Error: s % subspaces^2 has to be 0.")

        sys.exit(1)
    
    perarea = s/subspaces
    
    for i in range(subspaces):
        xs.append([])
        ys.append([])
        us.append([])
        vs.append([])
            
    
    for x in np.arange(-2., 1., deltax):
        index = int((x+2)*subspaces/3.)
        
        # This if/else statement is necessary because the index is sometimes
        # incorrect due to rounding errors
        if len(xs[index]) < perarea:
            xr = random.random()
            ur = 1-xr
            xs[index].append(xr*deltax + x)
            us[index].append(ur * deltax + x)
        
        else:
            xr = random.random()
            ur = 1-xr
            xs[index+1].append(xr*deltax + x)
            us[index + 1].append(ur * deltax + x)
        
    for y in np.arange(0, 1.5, deltay):
        index = int((y+1.5)*subspaces/1.5)
        
        if len(ys[index]) < perarea:
            yr = random.random()
            ur = 1-yr
            ys[index].append(yr*deltay + y)
            vs[index].append(ur * deltay + y)
            
        else:
            yr = random.random()
            ur = 1-yr
            ys[index+1].append(yr*deltay + y)
            vs[index + 1].append(ur * deltay + y)
        
    for i in range(subspaces):
        random.shuffle(xs[i])
        random.shuffle(ys[i])
        random.shuffle(us[i])
        random.shuffle(vs[i])

    xfinal = []
    yfinal = []
    ufinal = []
    vfinal = []
        
    for i in range(subspaces):
        
        therange = int(perarea*i/subspaces)
        
        for k in range(subspaces):
            
            for l in range(therange,therange+int(perarea/subspaces)):
                
                xfinal.append(xs[k][l])
                ufinal.append(us[k][l])
        
        for j in range(int(perarea)):
            
            yfinal.append(ys[i][j])
            vfinal.append(vs[i][j])
            
    return xfinal, yfinal, ufinal, vfinal
        

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
    
    fraction1 = 0
    fraction2 = 0
    results = []

    for j in range(s):

        x,y,u,v = randPoint()

        check = checkMandelbrot(x,y,i)
        check2 = checkMandelbrot(u, v, i)

        if check == True:

            fraction1 += 1

        if check2 == True:

            fraction2 += 1
            
        if j % 1000 == 0:
            
            results.append(["random1",i,j,s,fraction1])
            results.append(["random2",i,j,s,fraction2])

    results.append(["random1",i,s,s,fraction1])
    results.append(["random2", i, s, s, fraction2])

    return fraction1, fraction2, results

def createHypercube(s,i):
    
    fraction1 = 0
    fraction2 = 0
    # hypercube(s) for hypercube, orthogonal(s) for orthogonal
    xs,ys, us, vs = orthogonal(s)
    results = []
    
    for j in range(s):


        check1 = checkMandelbrot(xs[j],ys[j],i)
        check2 = checkMandelbrot(us[j],vs[j],i)

        if check1 == True:

            fraction1 += 1

        if check2 == True:

            fraction2 += 1
            
        if j % 1000 == 0:
            
            results.append(["hypercube1",i,j,s,fraction1])
            results.append(["hypercube2", i, j, s, fraction2])

    results.append(["hypercube1",i,s,s,fraction1])
    results.append(["hypercube2", i, s, s, fraction2])
    return fraction1, fraction2, results

def save(results):
    """ Saves the results to a csv file. """
        
    filename = 'data/resultsnightloop_jordanorth.csv'
        
    with open(filename, 'a', newline = '') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        
        for row in results:
            writer.writerow(row)
               
    # List is reset for next set of results
    return []
 
def main():
    
    #randoms = [1000, 5000, 10000, 20000, 30000]
    hypers = [100, 500, 1000, 5000, 10000]
    
    # Set this very high to create a loop that runs all night
    for l in range(100):
        results = []

        # change to hypers if running hypers
        for j in hypers:
            print("Loop number: %i"%(l))
            for x in np.arange(3000, 6000, 500):
    
                s = j #Number of points
                i = x #Numbber of times through loop
                
                # createSet for random, createHypercube for hypercube
                fraction1, fraction2, results = createSet(s, i)
                #fraction1, fraction2, results = createHypercube(s, i)
                
                # argument 0 is "random" for random and "hypdercube" for hypercube
                #results.append(["random",i,s,fraction])
                print("With %i iterations, the number of points in the set is %i/%i and %i/%i" %(i,fraction1,s,fraction2,s))
        
                results = save(results)
        print("Done")
    
if __name__ == "__main__":
    main()
