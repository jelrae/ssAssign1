import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def openCSVfile(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        return reader

def main():
    path = "data/resultsnightloop_jordanrandom.csv"
    nms = ["Type","Num of Itters", "Current Sample  Size", "Total Sample Size", "Number in the Mandel Set"]
    pandasdata = pd.read_csv(path, delimiter=',', names=nms)
    random_data = pandasdata[pandasdata.Type == 'random1']
    antithetic_data = pandasdata[pandasdata.Type == 'random2']
    del random_data['Type']
    del antithetic_data['Type']

    #print(random_data)
    #mydata = np.genfromtxt(path, delimiter=',')
    #mydata = np.delete(mydata, 0,axis =1)

    #randomdata = mydata
    #antitheticdata = mydata
    #print(randomdata)
    #print(mydata[0,:])
    # for i in range(mydata.shape[0], 0, -1):
    #     if i%2 == 0:
    #         randomdata = np.delete(randomdata, i, axis=0)
    #     else:
    #         antitheticdata = np.delete(antitheticdata, i, axis=0)

    #np.savetxt("randomsampleR.csv", randomdata, delimiter=",")
    #np.savetxt("randomsampleA.csv", antitheticdata, delimiter=",")
    #print(randomdata)
    #print(antitheticdata)

    #print(randomdata)

if __name__ == "__main__":
    main()
