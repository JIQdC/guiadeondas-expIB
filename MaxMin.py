import numpy as np
import csv
from scipy.signal import hilbert
from matplotlib import pyplot as plt

class waveform:
    def __init__(self):
        self.r=np.arange
        self.v=np.arange
        
def leerArchivo(path):
    with open(str(path)) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        R = []
        V = []

        for row in readCSV:
            if(row[0][0]!="R"):
                
                r = float(row[0])
                v = float(row[1])

                R.append(r)
                V.append(v)
        
    data=waveform()
    
    data.v=V
    data.r=R
    
    return data

def MaxMin(data):
    aux=data.v[0]
    #for i in range(0,np.size(data.v)):
        