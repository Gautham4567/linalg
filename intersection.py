import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

def intersection(n1,n2,c1,c2):
    n=np.vstack([n1,n2])
    c=np.array([c1,c2])
    N=np.linalg.inv(n)@c
    return N

O=np.array([0,0])

n1=np.array([1,1])
c1=2
n2=omat@n1
c2=n2@O

N=intersection(n1,n2,c1,c2)

#print(N)