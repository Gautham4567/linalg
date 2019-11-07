import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
import rotation as ROT

P=np.array([4,7])
c=9
O=np.array([0,0])

r=np.sqrt(c+np.linalg.norm(O)**2)

d=np.linalg.norm(P-O)
T=np.sqrt(d**2-r**2)
print(r)
print(T)

m=(P-O)/np.linalg.norm(P-O)
OP=line_gen(O,P)

tanL=T/r
L=np.arctan(tanL)

n1=ROT.rot_vec(m,L)
n2=ROT.rot_vec(m,-L)

A=O+r*n1
B=O+r*n2
AB=line_gen(A,B)
AP=line_gen(A,P)
BP=line_gen(B,P)

len=1000
theta=np.linspace(0,2*np.pi,len)
circle=np.zeros((2,len))
circle[0,:]=r*np.cos(theta)
circle[1,:]=r*np.sin(theta)
circle=(circle.T+O).T

plt.plot(circle[0,:],circle[1,:])
plt.plot(AB[0,:],AB[1,:])
plt.plot(OP[0,:],OP[1,:])
plt.plot(AP[0,:],AP[1,:])
plt.plot(BP[0,:],BP[1,:])
plt.plot(O[0],O[1],'o')
plt.text(O[0]*(1+0.2),O[1]*(1+0.2),'O')
plt.plot(P[0],P[1],'o')
plt.text(P[0]*(1+0.1),P[1]*(1+0.1),'P')
plt.plot(A[0],A[1],'o')
plt.text(A[0]*(1-0.1),A[1]*(1-0.1),'A')
plt.plot(B[0],B[1],'o')plt.text(B[0]*(1-0.1),B[1]*(1-0.1),'B')


plt.grid()
plt.axis('equal')
plt.show()
