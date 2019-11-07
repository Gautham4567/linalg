import numpy as np
import matplotlib.pyplot as plt
from coeffs import *


A=np.array([2,3])
B=np.array([4,5])
n1=np.array([-1,4])
c1=3

C=(A+B)/2

n2=B-A
c2=n2@C

n=np.vstack([n1,n2])
c=np.array([c1,c2])

O=np.linalg.inv(n)@c
print(O)

r=np.linalg.norm(O-A)
print(r)

plt.plot(A[0],A[1],'o')
plt.text(A[0]*(1-0.1),A[1]*(1-0.1),'A')
plt.plot(B[0],B[1],'o')
plt.text(B[0]*(1-0.1),B[1]*(1-0.1),'B')
plt.plot(O[0],O[1],'o')
plt.text(O[0]*(1-0.1),O[1]*(1-0.1),'O')

C=np.array([0,3/4])
D=np.array([5,2])
CD=line_gen(C,D)
plt.plot(CD[0,:],CD[1,:])


len=1000
theta=np.linspace(0,2*np.pi,len)
circle=np.zeros((2,len))
circle[0,:]=r*np.cos(theta)
circle[1,:]=r*np.sin(theta)
circle=(circle.T+O).T

plt.plot(circle[0,:],circle[1,:])


plt.grid()
plt.axis('equal')
plt.show()
