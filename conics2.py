import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

P=np.array([np.sqrt(2),np.sqrt(3)])
V=np.vstack([[1,0],[0,-1/3]])
c1=1

n1=P@V
A=np.array([2*np.sqrt(2),3*np.sqrt(3)])
B=np.array([0,-np.sqrt(3)])
AB=line_gen(A,B)

len=1000

theta=np.linspace(0,2*np.pi,len)
y=np.zeros((2,len))
y[0,:]=1/np.cos(theta)
y[1,:]=np.sqrt(3)*np.tan(theta)

plt.plot(P[0],P[1],'o')
plt.text(P[0]*(1-0.1),P[1]*(1-0.1),'P')
plt.plot(AB[0,:],AB[1,:],label='$AB$')
plt.plot(y[0,:],y[1,:],label='$hyperbola$')

plt.grid()
plt.axis('equal')
plt.legend(loc='best')
plt.show()
