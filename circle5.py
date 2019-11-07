import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

O1=np.array([2,-3])
O2=np.array([-3,2])
c1=12

r1=np.sqrt(np.linalg.norm(O1)**2+c1)
d=np.linalg.norm(O1-O2)

r2=np.sqrt(r1**2+d**2)
print(r2)

O1O2=dir_vec(O1,O2)
n=norm_vec(O1,O2)
N=n/np.linalg.norm(n)
A=O1+r1*N
B=O1-r1*N
AB=line_gen(A,B)

len=500
circle1=np.zeros((2,len))
theta=np.linspace(0,2*np.pi,len)
circle1[0,:]=r1*np.cos(theta)
circle1[1,:]=r1*np.sin(theta)
circle1=(circle1.T+O1).T

len=500
circle2=np.zeros((2,len))
theta=np.linspace(0,2*np.pi,len)
circle2[0,:]=r2*np.cos(theta)
circle2[1,:]=r2*np.sin(theta)
circle2=(circle2.T+O2).T

plt.plot(circle1[0,:],circle1[1,:],label='$circle1$')
plt.plot(circle2[0,:],circle2[1,:],label='$circle2$')
plt.plot(AB[0,:],AB[1,:])

plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.show()