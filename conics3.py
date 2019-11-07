import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
import intersection as INT

a=3
b=5
V=np.vstack([[25,0],[0,9]])
c=225
P=np.array([1.5,2.5*np.sqrt(3)])
O=np.array([0,0])

n1=P@V

e=np.sqrt(1-(a**2/b**2))
F1=np.array([0,b*e])
F2=np.array([0,-b*e])

n2=omat@n1
c1=n2@F1
c2=n2@F2

A1=INT.intersection(n1,n2,c,c1)
A2=INT.intersection(n1,n2,c,c2)

d1=np.linalg.norm(A1-F1)
d2=np.linalg.norm(A2-F2)

S=d1*d2
print(S)

len=1000
theta=np.linspace(0,2*np.pi,len)
ell=np.zeros((2,len))
ell[0,:]=a*np.cos(theta)
ell[1,:]=b*np.sin(theta)
ell=(ell.T+O).T

A1F1=line_gen(A1,F1)
A2F2=line_gen(A2,F2)
A1A2=line_gen(A1,A2)

plt.plot(ell[0,:],ell[1,:])
plt.plot(A1F1[0,:],A1F1[1,:])
plt.plot(A2F2[0,:],A2F2[1,:])
plt.plot(A1A2[0,:],A1A2[1,:])

plt.grid()
plt.axis('equal')
plt.show()