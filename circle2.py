import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

n=np.array([2,-4])
P=np.array([2,2])
c=4

O2=-1*n*0.5

r2=np.sqrt(c+(np.linalg.norm(O2)**2))
print(r2)

m=(P-O2)/np.linalg.norm(P-O2)
r1=3

O1=P+m*r1
print(O1)

a=1
b=-10
c=20

x1=(-b+np.sqrt(b**2-4*a*c))/(2*a)
x2=(-b-np.sqrt(b**2-4*a*c))/(2*a)

intercept=x1-x2
print(intercept)

A=np.array([-4,0])
B=np.array([8,0])
AB=line_gen(A,B)

len=1000
theta=np.linspace(0,2*np.pi,len)
circle1=np.zeros((2,len))
circle1[0,:]=r1*np.cos(theta)
circle1[1,:]=r1*np.sin(theta)
circle1=(circle1.T+O1).T


len=1000
theta=np.linspace(0,2*np.pi,len)
circle2=np.zeros((2,len))
circle2[0,:]=r2*np.cos(theta)
circle2[1,:]=r2*np.sin(theta)
circle2=(circle2.T+O2).T

plt.plot(circle1[0,:],circle1[1,:])
plt.plot(circle2[0,:],circle2[1,:])
plt.plot(O1[0],O1[1],'o')
plt.text(O1[0]*(1+0.1),O1[1]*(1+0.1),'O1')
plt.plot(O2[0],O2[1],'o')
plt.text(O2[0]*(1+0.1),O2[1]*(1+0.1),'O2')
plt.plot(AB[0,:],AB[1,:])


plt.grid()
plt.axis('equal')
plt.show()