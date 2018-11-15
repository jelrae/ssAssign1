# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 17:48:47 2018

@author: Gebruiker
"""

import csv
import matplotlib.pyplot as plt

def makePlots(alist, rangelist, area,typeof):
    
    
    
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
                    error += (float(row[4]) / (s) * area - y) ** 2
                    
            error = (error / n) ** 0.5
            yerror.append(error)
            
        
        plt.figure()
        plt.errorbar(ss,ys,yerr = yerror,fmt='o')
        plt.xlabel("samples")
        plt.ylabel("area")
        plt.title("The area as a function of the number of samples using %s sampling with %i iterations."%(typeof,i))
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
    
    for i in range(3000,6000,500):
        
        gem = []
        variance = []
        ss = []
        
        for s in rangelist:
            
            x = 0
            y = 0
            cov = 0
            xerror = 0
            yerror = 0
            n = 0
            ss .append(s)
            
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
            
        
        plt.figure()
        plt.errorbar(ss,gem,yerr = variance,fmt='o')
        plt.xlabel("samples")
        plt.ylabel("area")
        plt.title("The area as a function of the number of samples using %s sampling with %i iterations."%(typeof,i))
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
            if row[0] == "orthogonal1":
                orthogonals1.append(row)
            if row[0] == "orthogonal2":
                orthogonals2.append(row)
            
    print(len(randoms3))
    print(len(randoms4))
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
                print(row[0])
                
                if row[0] == "random1":
                    print("never")
                    row[0] = "random2"
                    print(row)
                        
                elif row[0] == "random2":
                    row[0] = "random4"
                    print(row)
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
                
                thelist.append
                
    with open("data/resultsantithetic.csv", 'a', newline = '') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        
            for row in thelist:
                writer.writerow(row)
                
#nonantithetic()

antithetic()
