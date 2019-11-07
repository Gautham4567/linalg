import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

def rot_vec(n,theta):
    M1=np.array([np.cos(theta),-np.sin(theta)])
    M2=np.array([np.sin(theta), np.cos(theta)])
    M=np.vstack([M1,M2])
    N=M@n
    return N

