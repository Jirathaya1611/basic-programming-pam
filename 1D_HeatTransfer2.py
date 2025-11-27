# 1-Dimensional Heat Transfer
# u_t = alpha * u_xx
# B.C. : u(0,t) = a , u(n,t) = b ; t>0 (ค่าขอบ)
# I.C. : u(x,0) = f(x) ; 0<x<n (อุณหภูมิเริ่มต้น)

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

#(ค่าเริ่มต้น)
#u_x0 = 0
#u = np.ones(n+1) * u_x0    #(ones การสร้างarray)(ค่าเริ่มต้นตั้งแต่ 1 ถึง 51 หลัก)
#B.C. : u(0,t) = 0 , u(10,t) = 0 ; t>0
u_0t = 0
u_nt = 0

#B.C. : u(0,t) = 0 , u(10,t) = 0 ; t>0
x = np.linspace(0, L, n+1)
u = 100 * np.sin(x)
u[0] = u_0t
u[-1] = u_nt

#Visualizing eith a plot
fig, axis = plt.subplots()
pcm = axis.pcolormesh([u], cmap=plt.cm.jet, vmin=-100, vmax=100)
plt.colorbar(pcm, ax=axis) 
axis.set_ylim(-10,11)

#Simulating 
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