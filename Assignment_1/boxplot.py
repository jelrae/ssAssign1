import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    path = "data/resultsnightloop_jordanrandom.csv"
    nms = ["Type","Num of Itters", "Current Sample  Size", "Total Sample Size", "Number in the Mandel Set"]
    pandasdata = pd.read_csv(path, delimiter=',', names=nms)
    random_data = pandasdata[pandasdata.Type == 'random1']
    antithetic_data = pandasdata[pandasdata.Type == 'random2']
    del random_data['Type']
    del antithetic_data['Type']



    #print(random_data)
    #print(antithetic_data)


if __name__ == "__main__":
    main()
