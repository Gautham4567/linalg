import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

e=3/5
f=6
O=np.array([0,0])
a=f/(2*e)
b=np.sqrt((a**2)*(1-(e**2)))

A=np.array([a,0])
B=np.array([0,b])
C=np.array([-a,0])
D=np.array([0,-b])

AC=np.linalg.norm(A-C)
BD=np.linalg.norm(B-D)
Area=0.5*AC*BD
print(Area)

len=1000
theta=np.linspace(0,2*np.pi,len)
ell=np.zeros((2,len))
ell[0,:]=a*np.cos(theta)
ell[1,:]=b*np.sin(theta)
ell=(ell.T+O).T

x_AB=line_gen(A,B)
x_BC=line_gen(B,C)
x_CD=line_gen(C,D)
x_DA=line_gen(D,A)

plt.plot(A[0],A[1],'o')
plt.text(A[0]*(1-0.1),A[1]*(1-0.1),'A')
plt.plot(B[0],B[1],'o')
plt.text(B[0]*(1-0.1),B[1]*(1-0.1),'B')
plt.plot(C[0],C[1],'o')
plt.text(C[0]*(1-0.1),C[1]*(1-0.1),'C')
plt.plot(D[0],D[1],'o')
plt.text(D[0]*(1-0.1),D[1]*(1-0.1),'D')

plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(x_DA[0,:],x_DA[1,:],label='$DA$')

plt.plot(ell[0,:],ell[1,:])

plt.axis('equal')
plt.grid()
plt.show()