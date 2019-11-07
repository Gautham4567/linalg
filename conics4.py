import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

len=1000

y1=np.zeros((2,len))
y1[1]=np.linspace(-10,10,len)
y1[0]=(y1[1]**2)/8

O=np.array([0,-6])
r=np.sqrt(37)

P=np.array([2,-4])
r1=np.linalg.norm(O-P)

len=1000
theta=np.linspace(0,2*np.pi,len)
circle=np.zeros((2,len))
circle[0,:]=r*np.cos(theta)
circle[1,:]=r*np.sin(theta)
circle=(circle.T+O).T


len=1000
theta=np.linspace(0,2*np.pi,len)
circle1=np.zeros((2,len))
circle1[0,:]=r1*np.cos(theta)
circle1[1,:]=r1*np.sin(theta)
circle1=(circle1.T+P).T

plt.plot(circle[0,:],circle[1,:])
plt.plot(O[0],O[1],'o')
plt.plot(circle1[0,:],circle1[1,:])
plt.text(O[0]*(1+0.1),O[1]*(1+0.1),'O')
plt.plot(y1[0,:],y1[1,:])
plt.plot(P[0],P[1],'o')
plt.text(P[0]*(1+0.1),P[1]*(1+0.1),'P')

plt.grid()
plt.axis('equal')
plt.show()
