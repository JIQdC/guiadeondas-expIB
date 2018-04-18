import usbtmc

class RigolMult(object):
    #funciones de control de multimetro
    #Rigol DM3068
    def __init__(self):
        self.instr=None
    def ID(self):
        #devuelve el ID del instrumento
        return(self.instr.ask("*IDN?"))
    def voltDC(self):
        #devuelve el voltaje DC medido
        return(float(self.instr.ask(":MEAS:VOLT:DC?")))
    def resist(self):
        #devuelve la resistencia medida
        return(float(self.instr.ask(":MEAS:RES?")))
    def reset(self):
        #resetea el multimetro
        self.instr.write("*RST")
    def resistIntTime(self,t):
        #setea el tiempo de integracion de la medicion de resistencia
        #el tiempo t debe pasarse en NPLC
        self.instr.write(":SENS:RES:NPLC "+str(t))
    def voltDCIntTime(self,t):
        #setea el tiempo de integracion de la medicion de voltaje DC
        #el tiempo t debe pasarse en NPLC
        self.instr.write(":SENS:VOLT:DC:NPLC "+str(t))
    def voltDCRange(self):
        #devuelve el rango de medicion de voltaje DC actual
        p=self.instr.ask(":MEAS:VOLT:DC:RANG?")
        if(p=="0"):
            return 0.2
        if(p=="1"):
            return 2
        if(p=="2"):
            return 20
        if(p=="3"):
            return 200
        if(p=="4"):
            return 1000
        else:
            return -1

    def resistRange(self):
        #devuelve el rango de medicion de resistencia actual
        p=self.instr.ask(":MEAS:RES:RANG?")
        if(p=="0"):
            return 200
        if(p=="1"):
            return 2E3
        if(p=="2"):
            return 20E3
        if(p=="3"):
            return 200E3
        if(p=="4"):
            return 1E6
        if(p=="5"):
            return 10E6
        if(p=="6"):
            return 100E6
        else:
            return -1
