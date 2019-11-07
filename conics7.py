import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
import intersection as INT

n1=np.array([4,3])
n2=np.array([3,4])
c1=12
c2=12

O=INT.intersection(n1,n2,c1,c2)
print(O)
len=1001
y1=np.zeros((2,len))
y1[0]=np.linspace(6/7-25,6/7,len)
y1[1]=((36/49)/(y1[0]-6/7))+6/7

len=1001
y2=np.zeros((2,len))
y2[0]=np.linspace(6/7,6/7+25,len)
y2[1]=((36/49)/(y2[0]-6/7))+6/7

plt.plot(y1[0,:],y1[1,:],color='r')
plt.plot(y2[0,:],y2[1,:],color='r')


plt.grid()
plt.axis('equal')
plt.show()