#x**3 กราฟสี
import numpy as np
import matplotlib.pyplot as plt 
from sympy import *
import math

alpha = 3

L = 2*np.pi
n = 50
dx = L/n
dt = 0.5 * dx**2 / alpha
t_final = 1

u_0t = 0
u_nt = 0

x = np.linspace(-L, L, n+1)
u = x**3
u[0] = u_0t
u[-1] = u_nt


fig, axis = plt.subplots()
pcm = axis.pcolormesh([u], cmap=plt.cm.jet, vmin=-100, vmax=100)
plt.colorbar(pcm, ax=axis) 
axis.set_ylim(-10,11)


counter = 0 
while counter < t_final:
    w = u.copy()
    for i in range(1,n):
        u[i] = w[i] + alpha * dt * ((w[i+1] - 2*w[i] + w[i-1])/dx**2)
    counter += dt
    #print(f'time = {counter} and average temperature = {np.average(u)}')
    pcm.set_array([u])
    axis.set_title('Distributions at time {:.3f}'.format(counter))
    
    plt.pause(0.01) #ปรับความไวของการแสดงผลกราฟ
plt.show()