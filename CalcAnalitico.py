import numpy as np 

ROE=2.81468076453843
desfasaje=0.136755196896824

beta=.25+desfasaje

modGamma=(ROE-1)/(ROE+1)

Gamma=modGamma*(np.cos(-4*np.pi*beta)+1j*np.sin(-4*np.pi*beta))

#ZL=(1+Gamma)/(1-Gamma)
ZL=0.63+0.85j
print("ZL = "+str(ZL)+"\n")
YL=1/ZL
print("YL = "+str(YL)+"\n")

Z=(ROE+1j*np.tan(2*np.pi*beta))/(1+1j*ROE*np.tan(2*np.pi*beta))

Y1=1-1j*np.sqrt(((1-np.real(YL))**2+np.imag(YL)**2)/np.real(YL))

GammaYL=(1-YL)/(1+YL)
GammaY1=(1-Y1)/(1+Y1)

print("argGammaYL = "+str(180*np.angle(GammaYL)/np.pi)+"\n")
print("argGammaY1 = "+str(180*np.angle(GammaY1)/np.pi)+"\n")

d=(np.pi+np.angle(GammaYL)-np.angle(GammaY1))/(4*np.pi)

print("Y1 = "+str(Y1)+"\n")
print("d = "+str(d))




