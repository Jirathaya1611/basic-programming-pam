from sympy import *
from math import factorial

#หาอนุพันธ์อนดับที่ 5 ของสมการyข้างล่าง
x = Symbol('x')
y = ((sin(5*x))**2) + exp(5*x)
y_i = y.diff(x, 5)
print(y_i)

