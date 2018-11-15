# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 17:09:22 2018

@author: Gebruiker
"""

import csv
import matplotlib.pyplot as plt

def retrieveDataNot():
    
    random1 = []
    random2 = []
    hypercube = []
    orthogonal = []
    
    with open("data/resultsnotantithetic.csv", 'r') as csvfile:
    
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        
        for row in reader:
            
            if int(row[1]) == 5500 and int(row[3]) == 10000:
                
                if row[0] == "random":
                    random1.append(row)
                    
                elif row[0] == "random2":
                    random2.append(row)
                    
                elif row[0] =="hypercube":
                    hypercube.append(row)
                    
                elif row[0] == "orthogonal":
                    orthogonal.append(row)
                    

    random = []
    otherrandom = []
    hypercube1 = []
    orthogonal1 = []
    
    for i in range(len(random1)):
        
        random.append(computeLists(random1,18.3765,i))
        otherrandom.append(computeLists(random2,8.3765,i))
        hypercube1.append(computeLists(hypercube,9.,i))
        orthogonal1.append(computeLists(orthogonal,9.,i))
    
    return random,otherrandom,hypercube1,orthogonal1

def computeLists(list1,area,i):
    
    return float(list1[i][4])/ (10000) * area

def retrieveDataAnti():
    
    random1 = []
    random2 = []
    random3 = []
    random4 = []
    hypercube1 = []
    hypercube2 = []
    orthogonal1 = []
    orthogonal2 = []
    
    with open("data/resultsantithetic.csv", 'r') as csvfile:
    
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        
        for row in reader:
            
            if int(row[1]) == 5500 and int(row[3]) == 10000:
                
                if row[0] == "random1":
                    random1.append(row)
                    
                elif row[0] == "random2":
                    random2.append(row)
                
                if row[0] == "random3":
                    random3.append(row)
                    
                if row[0] == "random4":
                    random4.append(row)
                    
                elif row[0] =="hypercube1":
                    hypercube1.append(row)
                    
                elif row[0] =="hypercube2":
                    hypercube2.append(row)
                    
                elif row[0] == "orthoginal1":
                    orthogonal1.append(row)
                    
                elif row[0] == "orthoginal2":
                    orthogonal2.append(row)
    
    random = []
    otherrandom = []
    hypercube = []
    orthogonal = []
    
    for i in range(len(random1)):
        
        random.append(computeList(random1,random3,8.3765,i))
        otherrandom.append(computeList(random2,random4,8.3765,i))
        hypercube.append(computeList(hypercube1,hypercube2,9.,i))
        orthogonal.append(computeList(orthogonal1,orthogonal2,9.,i))
    
    return random,otherrandom,hypercube,orthogonal

def computeList(list1,list2,area,i):
    return (float(list1[i][4]) + float(list2[i][4]))/ (2*10000) * area

def makePlot(random1,random2,hypercube,orthogonal):
    
    plt.figure()
    plt.hist(random1)
    plt.title("A histogram of the spread of found areas for s=10000 and i=5500 using random sampling")
    plt.xlabel("Area")
    
    
    plt.figure()
    plt.hist(random2)
    plt.title("A histogram of the spread of found areas for s=10000 and i=5500 using random sampling")
    plt.xlabel("Area")
    
    plt.figure()
    plt.hist(hypercube)
    plt.title("A histogram of the spread of found areas for s=10000 and i=5500 using latin hypercube sampling")
    plt.xlabel("Area")
    
    plt.figure()
    plt.hist(orthogonal)
    plt.title("A histogram of the spread of found areas for s=10000 and i=5500 using latin hypercube sampling")
    plt.xlabel("Area")
    
    plt.show()
    
random,otherrandom,hypercube,orthogonal = retrieveDataNot()
#print(random,otherrandom,hypercube,orthogonal)
    
makePlot(random,otherrandom,hypercube,orthogonal)

random,otherrandom,hypercube,orthogonal = retrieveDataAnti()
#print(random,otherrandom,hypercube,orthogonal)

makePlot(random,otherrandom,hypercube,orthogonal)