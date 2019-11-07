import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

len=1000

y1=np.zeros((2,len))
y1[0]=np.linspace(-5,5,len)
y1[1]=(y1[0]**2)/3

y2=np.zeros((2,len))
y2[1]=np.linspace(-5,5,len)
y2[0]=(y2[1]**2)/3

A=np.array([-4,13/4])
B=np.array([13/4,-4])
x_AB=line_gen(A,B)

plt.plot(x_AB[0,:],x_AB[1,:])
plt.plot(y1[0,:],y1[1,:])
plt.plot(y2[0,:],y2[1,:])

plt.grid()
plt.show()

plt.axis('equal')