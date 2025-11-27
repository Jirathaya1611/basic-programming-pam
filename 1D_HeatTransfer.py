# 1-Dimensional Heat Transfer
# u_t = alpha * u_xx
# B.C. : u(0,t) = a , u(L,t) = b ; t>0 (ค่าขอบ)
# I.C. : u(x,0) = f(x) ; 0<x<L (อุณหภูมิเริ่มต้น)

import numpy as np
import matplotlib.pyplot as plt 

alpha = 3 #คือค่า c^2 ค่าการแพร่ความร้อน
L = 2*np.pi #ความยาวแท่งเหล็ก (length of domain)
n = 50 #แบ่งออกเป็นส่วนเท่าๆกัน (seperate the domain into 10 pieces equally)
t_final = 1 #เวลาสุดท้าย

dx = L/n #ส่วนย่อยๆ
dt = 0.5 * dx**2 / alpha
N = int(t_final/dt)

#Dirichlet Boundary Condition(ค่าขอบเป็นค่าคงที่):

#B.C. : u(0,t) = 0 , u(10,t) = 0 ; t>0
u_0t = 0
u_nt = 0

# I.C. : u(x,0) = 100 ; 0<x<10 (ค่าเริ่มต้น)
#u_x0 = 0
x = np.linspace(0, L, n+1) 
u = 100 * np.sin(x)

u[0] = u_0t
u[-1] = u_nt



for j in range(1,N+1):
    w = u.copy()
    for i in range(1,n):
        u[i] = w[i] + alpha * dt * ((w[i+1] - 2*w[i] + w[i-1])/dx**2)
    #print(u) #ถ้าต้องการให้แสดงค่ารอบสุดท้ายให้นำprintออกนอกloop แต่ถ้าprintอยู่ในloop จะแสดงค่าทุกรอบ
    #print(f'Round {j} : {u}')
    plt.clf() #เคลียร์เส้น
    plt.xlim(0,L)
    plt.ylim(-100,100)
    plt.plot(x,u)
    #plt.title(f'Distributions at round {j}')
    #plt.title(f'Distributions at round {j*dt}')
    plt.title('Distributions at time {:.4f}'.format(j*dt))
    #plt.title('Average Temperature {:.4f}'.format(np.average(u)))
    plt.pause(0.01)
    
plt.show()