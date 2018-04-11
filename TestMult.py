from RigolClass import RigolMult
import usbtmc
import time
import numpy as np 

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
    pos=instr2
else:
    volt=instr2
    pos=instr1

print(pos.resist())
pos.instr.write("SENS:RES:NPLC 2")
time.sleep(3)
pos.reset()