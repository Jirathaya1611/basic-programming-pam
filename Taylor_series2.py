import numpy as np
from sympy import *
from math import factorial
from matplotlib import pyplot as plt


x = Symbol('x')

#เป็นฟังก์ชันสำหรับหาพจน์ที่ i ของ Taylor series
'''
def Taylor_i(y, n,  a): #nคือจำนวนครั้งที่diff
    # i เริ่มจาก 0 ถึง n
    for i in range(n+1):
         y_dif = y.diff(x, i) 
         y_dif = lambdify(x, y_dif)
         Ti = y_dif(a)/factorial(i) * (x-a)**i
    return Ti 
'''
def Taylor_i(y, n,  a):
    y_dif = y.diff(x, n) 
    y_dif = lambdify(x, y_dif)
    Ti = y_dif(a)/factorial(n) * (x-a)**n
    return Ti 

def Sum_Taylor(y, n, a):
    Tn = 0
    for i in range(n+1):
        Tn_i = Taylor_i(y, i, a)
        Tn = Tn + Tn_i
    return Tn


#main function
x = Symbol('x')
y = cos(x)
n = 100
a = 0
Tnn = Sum_Taylor(y, n, a)
Tnnx = lambdify(x, Tnn)

x = np.linspace(-10, 10, 1000)
plt.plot(x, Tnnx(x))
plt.show()