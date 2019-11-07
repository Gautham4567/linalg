import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

P=np.array([1,-1])
n1=np.array([2,1])
n2=np.array([1,-1])
c1=3
c2=1

n=np.vstack([n1,n2])
c=np.array([c1,c2])

O=np.linalg.inv(n)@c
print(O)

m=dir_vec(O,P)
k=m@P
r=np.linalg.norm(O-P)
print(m,k)

Q=np.array([-3,0])
R=np.array([5,-2])
QR=line_gen(R,Q)

len=1000
theta=np.linspace(0,2*np.pi,len)
circle=np.zeros((2,len))
circle[0,:]=r*np.cos(theta)
circle[1,:]=r*np.sin(theta)
circle=(circle.T+O).T

plt.plot(circle[0,:],circle[1,:])
plt.plot(O[0],O[1],'o')
plt.text(O[0]*(1-0.1),O[1]*(1-0.1),'O')
plt.plot(P[0],P[1],'o')
plt.text(P[0]*(1-0.1),P[1]*(1-0.1),'P')
plt.plot(QR[0,:],QR[1,:])
plt.grid()

plt.axis('equal')
plt.show()
