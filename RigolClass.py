import usbtmc

class RigolMult(object):
    def __init__(self):
        self.instr=None
    def ID(self):
        return(self.instr.ask("*IDN?"))
    def voltDC(self):
        return(float(self.instr.ask(":MEAS:VOLT:DC?")))
    def resist(self):
        return(float(self.instr.ask(":MEAS:RES?")))
    def reset(self):
        self.instr.write("*RST")
    def resistIntTime(self,t):
        self.instr.write(":SENS:RES:NPLC "+str(t))
    def voltIntTime(self,t):
        self.instr.write(":SENS:VOLT:DC:NPLC "+str(t))