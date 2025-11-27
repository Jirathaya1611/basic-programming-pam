import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

print("Start : . . .")
print("........................")
print("Solution of 2D Heat Equation")
print("........................")

#w, h = input("Define your domain's width and height").split()
#print(f"Width = {w} x Height = {h}")
'''
plate_width = int(w)
plate_height = int(h) 
'''
plate_width = 5
plate_height = 8

#it = input("Define number of iterations : ")
#max_iter_time = int(it) 
max_iter_time = 500

nx = 51
ny = 81

alpha = 2
delta_x = plate_width/(nx-1)
delta_y = plate_height/(ny-1)

delta_t = (delta_x ** 2)/(4 * alpha)
gamma = (alpha *delta_t)/(delta_x ** 2)


u = np.empty((max_iter_time,ny,nx ))

u_initial = 0
u_top = 0
u_bottom = 0
u_left = 100
u_right = 0


u.fill(u_initial)


def calculate(u): 
    for k in range(0, max_iter_time -1, 1): 
        for i in range(1, ny -1, 1): 
            for j in range(1, nx -1 , 1): 
                u[k + 1, i, j] = u[k][i][j] + gamma * (u[k][i+1][j] + u[k][i-1][j] + u[k][i][j+1] + u[k][i][j-1] - 4*u[k][i][j])
        u[ k:, -1,  : ] = u[k:, -2, : ] 
        u[ k:,  1,  : ] = u[k:, 2, : ] 
        u[ k:,  :,  1 ] = u[k:, :, 2 ] 
        u[ k:,  :, -1 ] = u[k:, :, -2 ] 
        u[ k:, 40,25 ] = 45*k
        u[ k:, 70, 5 ] = 20*k
        u[ k:,  65, 35 ] = 10*k
        u[ k:,  15, 10 ] = 2*k                      
          
    return u


def plot_haet_map(u_k, k): 
    plt.clf()
    
    plt.title(f'Temperature at t = {k * delta_t:.3f} unit time')
    plt.xlabel("x")
    plt.ylabel("y")
    
   
    plt.pcolormesh(u_k, cmap=plt.cm.jet, vmin=0, vmax=100)
    plt.colorbar
    
    return plt

u = calculate(u)

def animate(k):
    plot_haet_map(u[k], k)
    
anim = FuncAnimation(plt.figure(), animate, interval=1, frames=max_iter_time, repeat=False)
anim.save("solution_of_2d_haet_eq.gif")

animate(300)

plt.show()

print("Done !!")
