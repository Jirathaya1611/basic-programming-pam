#x**3 กราฟแบบเส้น
import numpy as np
import matplotlib.pyplot as plt 

alpha = 3
L = 2*np.pi 
n = 50 
t_final = 1

dx = L/n
dt = 0.5 * dx**2 / alpha
N = int(t_final/dt)

u_0t = 0
u_nt = 0

x = np.linspace(-L, L, n+1) 
u = x**3

u[0] = u_0t
u[-1] = u_nt



for j in range(1,N+1):
    w = u.copy()
    for i in range(1,n):
        u[i] = w[i] + alpha * dt * ((w[i+1] - 2*w[i] + w[i-1])/dx**2)
    plt.clf()
    plt.xlim(-L,L)
    plt.ylim(-100,100)
    plt.plot(x,u)
    #plt.title(f'Distributions at round {j}')
    #plt.title(f'Distributions at round {j*dt}')
    plt.title('Distributions at time {:.4f}'.format(j*dt))
    #plt.title('Average Temperature {:.4f}'.format(np.average(u)))
    plt.pause(0.01)
    
plt.show()