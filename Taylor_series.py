import numpy as np
from sympy import *
import math
from matplotlib import pyplot as plt
#from math import pi


y = cos(x)
#y = sin(x)
#y = exp(x)
#y = math.pi**x # หรือ y= math.e**x
a = 0
#y_0 = cos(a)
#print( f'y_0 at a = 0 is {y_0}')


'''
y_1 = y.diff(x, 1)
y_1 = lambdify(x, y_1) #lmmdify สามารถทำให้ x แทนค่าได้
print(f'y_1 = {y_1(a)}')
'''
'''
y_2 = y.diff(x, 2)
y_2 = lambdify(x, y_2) #lmmdify สามารถทำให้ x แทนค่าได้
print(f'y_2 = {y_2(a)}')
'''
Tn = 0

for i in range(15):
    y_dif = y.diff(x, i)
    y_dif = lambdify(x, y_dif)
   # print(f'ครั้งที่ {i} = {y_dif(a)}') #หรือ print(f'{i} : y_dif at a = 0 is {y_dif}')
    Ti = y_dif(a)/math.factorial(i)  * (x - a)**i
    Tn_i = Ti
    Tn = Tn + Tn_i 
    print(f'{i} : = {Tn}')
    
Tnn = lambdify(x, Tn)
#print(f'Tnn = {Tnn(math.pi)}') 
x = np.linspace(-5, 5, 100)
plt.plot(x, Tnn(x)) #พล็อตกราฟ
plt.show() #แสดงกราฟ