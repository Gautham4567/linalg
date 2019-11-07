import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
import intersection as INT

O1=np.array([1,0])
F=0
r=np.sqrt(np.linalg.norm(O1)**2+F)
n=np.array([1,1])
a1=3
m=omat@n
a2=m@O1

O=INT.intersection(n,m,a1,a2)

O2=2*O-O1
print(O2)
print(r)

A=np.array([5,-2])
B=np.array([-1,4])
AB=line_gen(A,B)

len=500
circle=np.zeros((2,len))
theta=np.linspace(0,2*np.pi,len)
circle[0,:]=r*np.cos(theta)
circle[1,:]=r*np.sin(theta)

C1=(circle.T+O1).T
C2=(circle.T+O2).T

plt.plot(O1[0],O1[1],'o')
plt.text(O1[0]*(1-0.1),O1[1]*(1-0.1),'O1')
plt.plot(O2[0],O2[1],'o')
plt.text(O2[0]*(1-0.1),O2[1]*(1-0.1),'O2')
plt.plot(AB[0,:],AB[1,:])
plt.plot(C1[0,:],C1[1,:],label='$circle1$')
plt.plot(C2[0,:],C2[1,:],label='$circle2$')

plt.grid()
plt.axis('equal')
plt.legend(loc='best')
plt.xlabel('$x$')
plt.ylabel('$y$')

plt.show()