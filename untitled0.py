# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 17:48:47 2018

@author: Gebruiker
"""

import csv
import matplotlib.pyplot as plt

def makePlots(alist, rangelist, area):
    
    
    
    for i in range(3000,6000,500):
        
        ys = []
        yerror = []
        ss = []
        
        for s in rangelist:
            
            y = 0
            error = 0
            n = 0
            ss .append(s)
            
            for row in alist:
                if int(row[1]) == i and int(row[3]) == s:
                    y += int(row[4])
                    n += 1
                    
            y = float(y) / (n*s) * area
            ys.append(y)
            
            for row in alist:
                if int(row[1]) == i and int(row[3]) == s:
                    error += (int(row[4]) - y) ** 2
                    
            error = error ** 0.5
            yerror.append(error)
            
        
        plt.figure()
        plt.plot(ss,ys,'bo',yerr = yerror)
    plt.show()

def thefunction():
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
            
    makePlots(randoms,randomlist,area2)
    makePlots(randoms2,hyperlist,area2)
    makePlots(hypers,hyperlist,area1)
    makePlots(orthogonals,hyperlist,area1)
                
thefunction()