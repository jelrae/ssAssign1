# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 17:48:47 2018

@author: Gebruiker
"""

import csv
import matplotlib.pyplot as plt
import numpy as np

truearea = 1.50659

def makePlots(alist, rangelist, area,typeof):
    
    islist = []
    ilist = [3000,3500,4000,4500,5000,5500]
    variancelist = []
    
    for i in ilist:
        
        ys = []
        yerror = []
        
        for s in rangelist:
            
            y = 0
            error = 0
            n = 0
            
            for row in alist:
                if int(row[1]) == i and int(row[3]) == s:
                    y += int(row[4])
                    n += 1
                    
            y = float(y) / (n*s) * area
            ys.append(y)
            
            for row in alist:
                if int(row[1]) == i and int(row[3]) == s:
                    error += (float(row[4]) / (s) * area - y) ** 2
                    
            error = (error / n) ** 0.5
            yerror.append(error)
            
        
        for p in range(len(ys)):
            
            ys[p] = abs(ys[p] - truearea)
        
        islist.append(ys)
        variancelist.append(yerror)
        
        plt.figure()
        plt.errorbar(rangelist,ys,yerr = yerror,fmt='o')
        plt.xlabel("samples")
        plt.ylabel("area")
        plt.title("The area as a function of the number of samples using %s sampling with %i iterations."%(typeof,i))
    
    fig, ax = plt.subplots()
    im = ax.imshow(islist)#,extent=[rangelist[0],rangelist[len(rangelist)-1],ilist[0],ilist[len(ilist)-1]])
    
    # We want to show all ticks...
    ax.set_xticks(np.arange(len(rangelist)))
    ax.set_yticks(np.arange(len(ilist)))
    # ... and label them with the respective list entries
    ax.set_xticklabels(rangelist)
    ax.set_yticklabels(ilist)
    
    plt.title("The absolute difference between the outcome of the simulation \n and the literature value using %s sampling."%(typeof))
    plt.xlabel("samples")
    plt.ylabel("iterations")
    fig.colorbar(im, orientation = 'vertical', label = "Absolute difference in area")
    
    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")
    
    plt.show()
    
    fig, ax = plt.subplots()
    
    im = ax.imshow(variancelist)
    
    # We want to show all ticks...
    ax.set_xticks(np.arange(len(rangelist)))
    ax.set_yticks(np.arange(len(ilist)))
    # ... and label them with the respective list entries
    ax.set_xticklabels(rangelist)
    ax.set_yticklabels(ilist)
    
    plt.title("The variance in all point of the simulation using %s sampling."%(typeof))
    plt.xlabel("samples")
    plt.ylabel("iterations")
    fig.colorbar(im, orientation = 'vertical', label = "Variance")
    
    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")
    
    plt.show()

def nonantithetic():
    # The path length distribution is taken from the file
    
    randoms = []
    randoms2 = []
    hypers = []
    orthogonals = []
    
    randomlist = [1000,5000,10000,20000,30000]
    hyperlist = [100,500,1000,5000,10000]
    
    area1 = 9
    area2 = 8.3765
    
    with open("data/resultsnotantithetic.csv", 'r') as csvfile:
    
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        
        for row in reader:
            
            if row[0] == "random":
                randoms.append(row)
            if row[0] == "random2":
                randoms2.append(row)
            if row[0] == "hypercube":
                hypers.append(row)
            if row[0] == "orthogonal":
                orthogonals.append(row)
            
    makePlots(randoms,randomlist,area2,"random")
    makePlots(randoms2,hyperlist,area2,"random")
    makePlots(hypers,hyperlist,area1,"latin hypercube")
    makePlots(orthogonals,hyperlist,area1,"orthogonal")
    
def makeAntiPlots(alist, blist, rangelist, area,typeof):
    
    islist = []
    ilist = [3000,3500,4000,4500,5000,5500]
    variancelist = []
    
    for i in ilist:
        
        gem = []
        variance = []
        
        for s in rangelist:
            
            x = 0
            y = 0
            cov = 0
            xerror = 0
            yerror = 0
            n = 0
            
            for m in range(len(alist)):
                if int(alist[m][1]) == i and int(alist[m][3]) == s:
                    x += int(alist[m][4])
                    y += int(blist[m][4])
                    cov += float(alist[m][4]) / s *area * float(blist[m][4]) / s * area
                    n += 1
            
            x = float(x) / (n*s) * area
            y = float(y) / (n*s) * area
            gem.append((x+y)/2)
            cov = cov / n - x*y
            
            for m in range(len(alist)):
                if int(alist[m][1]) == i and int(alist[m][3]) == s:
                    xerror += (float(alist[m][4]) / (s) * area - y) ** 2
                    yerror += (float(blist[m][4]) / (s) * area - y) ** 2
                    
            xerror = (xerror / n) ** 0.5
            yerror = (yerror / n) ** 0.5
            var = (xerror + yerror + 2 * cov) / 4.
            variance.append(var)
            
        for p in range(len(gem)):
            
            gem[p] = abs(gem[p] - truearea)
        
        islist.append(gem)
        variancelist.append(variance)
        
        plt.figure()
        plt.errorbar(rangelist,gem,yerr = variance,fmt='o')
        plt.xlabel("samples")
        plt.ylabel("area")
        plt.title("The area as a function of the number of samples using %s sampling with %i iterations."%(typeof,i))
    
    fig, ax = plt.subplots()
    im = ax.imshow(islist)#,extent=[rangelist[0],rangelist[len(rangelist)-1],ilist[0],ilist[len(ilist)-1]])
    
    # We want to show all ticks...
    ax.set_xticks(np.arange(len(rangelist)))
    ax.set_yticks(np.arange(len(ilist)))
    # ... and label them with the respective list entries
    ax.set_xticklabels(rangelist)
    ax.set_yticklabels(ilist)
    
    plt.title("The absolute difference between the outcome of the simulation \n and the literature value using %s sampling."%(typeof))
    plt.xlabel("samples")
    plt.ylabel("iterations")
    fig.colorbar(im, orientation = 'vertical', label = "Absolute difference in area")
    
    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")
    
    plt.show()
    
    fig, ax = plt.subplots()
    
    im = ax.imshow(variancelist)
    
    # We want to show all ticks...
    ax.set_xticks(np.arange(len(rangelist)))
    ax.set_yticks(np.arange(len(ilist)))
    # ... and label them with the respective list entries
    ax.set_xticklabels(rangelist)
    ax.set_yticklabels(ilist)
    
    plt.title("The variance in all point of the simulation using %s sampling."%(typeof))
    plt.xlabel("samples")
    plt.ylabel("iterations")
    fig.colorbar(im, orientation = 'vertical', label = "Variance")
    
    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")
    
    plt.show()
    
def antithetic():
    # The path length distribution is taken from the file
    
    randoms1 = []
    randoms2 = []
    randoms3 = []
    randoms4 = []
    hypers1 = []
    hypers2 = []
    orthogonals1 = []
    orthogonals2 = []
    
    randomlist = [1000,5000,10000,20000,30000]
    hyperlist = [100,500,1000,5000,10000]
    
    area1 = 9
    area2 = 8.3765
    
    with open("data/resultsantithetic.csv", 'r') as csvfile:
    
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        
        for row in reader:
            
            if row[0] == "random1":
                randoms1.append(row)
            if row[0] == "random2":
                randoms2.append(row)
            if row[0] == "random3":
                randoms3.append(row)
            if row[0] == "random4":
                randoms4.append(row)
            if row[0] == "hypercube1":
                hypers1.append(row)
            if row[0] == "hypercube2":
                hypers2.append(row)
            if row[0] == "orthoginal1":
                orthogonals1.append(row)
            if row[0] == "orthoginal2":
                orthogonals2.append(row)
            
    makeAntiPlots(randoms1,randoms3,randomlist,area2,"random")
    makeAntiPlots(randoms2,randoms4,hyperlist,area2,"random")
    makeAntiPlots(hypers1,hypers2,hyperlist,area1,"latin hypercube")
    makeAntiPlots(orthogonals1,orthogonals2,hyperlist,area1,"orthogonal")
    
    
def merge():
    
    thelist = []
    
    with open("data/resultsnightloop_jordanrandom.csv", 'r') as csvfile:
    
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        
        for row in reader:
            
            
            if row[2] == row[3]:
                
                if row[0] == "random2":
                    row[0] = "random3"
                thelist.append(row)
                
    with open("data/resultsnightloop_jordanrandom2.csv", 'r') as csvfile:
    
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        
        for row in reader:
            
            if row[2] == row[3]:
                
                if row[0] == "random1":
                    row[0] = "random2"
                        
                elif row[0] == "random2":
                    row[0] = "random4"
                thelist.append(row)
                
    with open("data/resultsnightloop_jordanhyper.csv", 'r') as csvfile:
    
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        
        for row in reader:
            
            if row[2] == row[3]:
                
                thelist.append(row)
                
    with open("data/resultsnightloop_jordanorth.csv", 'r') as csvfile:
    
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        
        for row in reader:
            
            if row[2] == row[3]:
                thelist.append(row)
                
    with open("data/resultsantithetic.csv", 'a', newline = '') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        
            for row in thelist:
                writer.writerow(row)
                
nonantithetic()

antithetic()
                
#merge()
