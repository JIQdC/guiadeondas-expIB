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

def LockIn(ref,data):

    #antes de procesar, para quitar el offset de los datos, les resto su promedio
    data.v=data.v-np.average(data.v)
    ref.v=ref.v-np.average(ref.v)
    plt.plot(data.r,data.v,"g")
    plt.show()

    #defino Vs como el maximo valor de la señal de referencia
    Vs=np.amax(ref.v)

    #genero la referencia normalizando la señal de excitacion con su amplitud
    reff=ref.v/Vs
    plt.plot(ref.r,reff,"r")
    plt.show()
    #para la referencia en cuadratura, uso transformada de Hilbert
    refq=-np.imag(hilbert(reff))
    plt.plot(ref.r,refq,"r")
    plt.show()

    #proceso de lock-in: multiplico la señal de salida por las referencias...
    y1=data.v*reff
    y2=data.v*refq
    #... y filtro pasabajo con un promediador
    y3=np.average(y1)
    y4=np.average(y2)
    
    fase=np.arctan(y4/y3)

    return fase

print(LockIn(leerArchivo("CCAdapt.csv"),leerArchivo("Ag4.csv")))