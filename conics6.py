import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

c=9
d=-18
f=5

e1=(-d+np.sqrt(d**2-4*c*f))/(2*c)
e2=(-d-np.sqrt(d**2-4*c*f))/(2*c)


if e1>1:
    e=e1
    print(e1)
else:
    e=e2
    print(e2)

F1=np.array([5,0])
a=F1[0]/e
b=a*np.sqrt((e**2)-1)
f=a/e
A=np.array([f,5])
B=np.array([f,-5])
AB=line_gen(A,B)

len=1004
theta=np.linspace(0,2*np.pi,len)
hyp=np.zeros((2,len))
hyp[0,:]=a/np.cos(theta)
hyp[1,:]=b*np.sin(theta)/np.cos(theta)

plt.plot(hyp[0,:],hyp[1,:])
print(a**2-b**2)
plt.plot(AB[0,:],AB[1,:])

plt.grid()
plt.axis('equal')
plt.show()