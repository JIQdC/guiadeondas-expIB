from RigolClass import RigolMult
import usbtmc
import time
import numpy as np 

dev=usbtmc.list_devices()

instr1=RigolMult()
instr2=RigolMult()

instr1.instr=usbtmc.Instrument(dev[0])
instr2.instr=usbtmc.Instrument(dev[1])

str1=instr1.ID()
alfa=str1[38]
if(str1[38]=="9"):
    volt=instr1
    pos=instr2
else:
    volt=instr2
    pos=instr1

path1 = "MedicionManual1.csv"
output = open(path1,'w')

p=np.zeros(360)
v=np.zeros(360)

output.write("resist\tvolt\n")
for i in range (0,360):
    p[i]=pos.resist()
    v[i]=volt.voltDC()
    time.sleep(1/15)
    output.write("%.5f\t%.5f\n" % (p[i],v[i]))

output.close()