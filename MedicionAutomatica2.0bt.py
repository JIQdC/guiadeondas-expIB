from RigolClass import RigolMult
import usbtmc
import time
import numpy as np 
import serial

port="/dev/ttyUSB0"
arduino=serial.Serial(port,9600)

#deteccion de multimetros
dev=usbtmc.list_devices()
instr1=RigolMult()
instr2=RigolMult()
instr1.instr=usbtmc.Instrument(dev[0])
instr2.instr=usbtmc.Instrument(dev[1])
str1=instr1.ID()
alfa=str1[38]
if(str1[38]=="9"):
    volt=instr1
    res=instr2
else:
    volt=instr2
    res=instr1

def paso(t):
    #funcion que deja correr el carrito por un tiempo t
    arduino.write(b"a")
    time.sleep(t)
    arduino.write(b"s")

path="MedicionAutomatica1.0.csv"
out=open(path,'w')

n=450 #nro de puntos a medir
prom=4 #promedios 

#inicializo vectores de resistencia y voltaje
r=np.zeros(n)
v=np.zeros(n)

volt.voltDCIntTime(2)
res.resistIntTime(2)

out.write("R,V\n")
print("i\tR\tV\n")
for i in range(0,n):
    #tomo prom mediciones de resistencia y voltaje
    for j in range(0,prom):
        r[i]=r[i]+res.resist()
        v[i]=v[i]+volt.voltDC()
    #tomo los promedios de las mediciones
    r[i]=r[i]/prom
    v[i]=v[i]/prom
    #imprimo en pantalla y en el archivo
    print("%d\t%.6f\t%.6f\n" % (i,r[i],v[i]))
    out.write("%.6f,%.6f\n" % (r[i],v[i]))
    paso(0.5)
    time.sleep(0.7)

out.close()
volt.reset()
res.reset()