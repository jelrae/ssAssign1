# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:44:09 2018

@author: Jordan and Nathalie
"""

import math
import random
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def randPoint():
    # The area searched by this is a rectangle trunchated by a radius, leaving an area of 8.3765 with the other side lost as well 7.753
    # Added antithetic variables
    incirc = False
    while not incirc:
        sx = random.random()
        ux = 1-sx
        x = sx * 3. - 2.
        u = ux * 3. - 2.
        sy = random.random()
        vy = 1-sy
        y = sy * 1.5
        v = vy * 1.5
        if x**2 + y**2 <= 4 and u**2 + v**2 <= 4:
            return x, y, u, v

def loopMadelbrot(x, y, xi, yi):
    xt = (x**2 - y**2) + xi
    yt = (2*x*y) + yi
    return xt, yt

def checkMandelbrot(x,y,numLoop):

    if 0 > x > -0.5 and math.fabs(y)<.4:
        return True

    xi = x
    yi = y
    
    xn = (x**2 - y**2) + xi
    yn = (2*x*y) + yi

    for i in range(0,numLoop):
        xn, yn = loopMadelbrot(xn, yn, xi, yi)
        if xn**2 + yn**2 >= 4:
            return False 

    return True

def checkMandelbrotout(x, y, numLoop):
    if 0 > x > -0.5 and math.fabs(y) < .4:
        return numLoop, True

    xi = x
    yi = y

    xn = (x ** 2 - y ** 2) + xi
    yn = (2 * x * y) + yi

    for i in range(0, numLoop+1):
        xn, yn = loopMadelbrot(xn, yn, xi, yi)
        if xn ** 2 + yn ** 2 >= 4:
            return i, False

    return i, True

def mandelbrotItters(s, itter):
    madeSet = []
    numIn = 0
    numPoints = s
    madeSet.append([])
    madeSet.append([])
    madeSet.append([])
    conCheck = False
    for i in range(0,s):
        check = False
        x,y, u, v= randPoint()

        newcheck = False

        while not newcheck:
            if (x in madeSet[0] and y in madeSet[1]) or (u in madeSet[0] and v in madeSet[1]):
                print("is this used?")
                x, y, u, v = randPoint()
            else:
                newcheck = True

        numloop, check = checkMandelbrotout(x,y,itter)

        if check:
            numIn += 1

        madeSet[0].append(x)
        madeSet[1].append(y)
        madeSet[2].append(numloop)

        numloop, check = checkMandelbrotout(u,v,itter)

        if check:
            numIn += 1

        madeSet[0].append(u)
        madeSet[1].append(v)
        madeSet[2].append(numloop)

    return madeSet, numIn, numPoints

def createSet(s, i):
    
    fraction = 0
    inSet = []
    outSet = []
    inSet.append([])
    inSet.append([])
    outSet.append([])
    outSet.append([])
    for j in range(s):

        x,y= randPoint()

        newcheck = False

        while not newcheck:
            if x in inSet[0] and y in inSet[1]:
                x, y = randPoint()
            else:
                newcheck = True

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
    s = 100000 #Number of points
    iloop = 2500 #Number of itterations through check

    areaCirc = math.pi * 4

    mandSet, pntsIn, pntsTot = mandelbrotItters(s, iloop)
    print(pntsIn)
    print(pntsTot)
    frac = pntsIn/(pntsTot*2)
    print(frac*8.3765)


    #fraction, inSet, outSet = createSet(s, i)
    norm = mpl.colors.Normalize(vmin=-1, vmax=iloop)
    cmap = mpl.cm.hot
    color = cmap(norm(mandSet[2]))
    plt.scatter(mandSet[0], mandSet[1], c=color, s=1)
    mirrormandel = -1 * np.array(mandSet[1])
    plt.scatter(mandSet[0], mirrormandel, c = color, s = 1)
    plt.title("Mandelbrot Set")
    plt.xlabel("Real")
    plt.ylabel("Imaginary")
    #plt.colorbar()
    plt.show()

    print("With %i itterations, the number of points in the set is %i" %(iloop,frac))


    print("Done")
    
if __name__ == "__main__":
    main()