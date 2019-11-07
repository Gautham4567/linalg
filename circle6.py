import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

P=np.array([-2,4])
Q=np.array([0,2])

R=(P+Q)*0.5

n1=dir_vec(P,Q)
c1=n1@R
n2=np.array([0,1])
c2=n2@Q

n=np.vstack((n1,n2))
c=np.array((c1,c2))
O = np.linalg.inv(n)@c
print (O)
r=np.linalg.norm(O-P)
N=np.array([2,-3])
m=omat@N/np.linalg.norm(omat@N)
A=O+m*r
B=O-m*r
AB=line_gen(A,B)

len=1000
theta=np.linspace(0,2*np.pi,len)
circle=np.zeros((2,len))
circle[0,:]=r*np.cos(theta)
circle[1,:]=r*np.sin(theta)
circle=(circle.T+O).T

plt.plot(circle[0,:],circle[1,:])
plt.plot(O[0],O[1],'o')
plt.text(O[0]*(1-0.1),O[1]*(1-0.1),'O')
plt.plot(AB[0,:],AB[1,:])

plt.grid()
plt.axis('equal')
plt.show()
