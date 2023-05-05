#Aula dia 20/03

import math
x1 = math.sqrt(25)
print(int(x1))

from math import cos, pi
print(pi)
print(cos(pi))

import numpy as np

u = np.array([1, 0, 0])
M = np.array([[1, 2, 3], [4 , 5, 6], [7 , 8, 9]])
print(M)

type(M), type(u)

u[0]
M[2,1]

np.eye(3)
np.eye(3, dtype = np.int64)
np.zeros((2,3))
np.ones((2,3))
np.full((2,3), 5)
x = np.random.random((4, 4))

x
x + 11
x - 11
x * 3
x / 2
y = np.array([1, 2, 3, 4])
x + y



matéria1 = 7
matéria2 = 7
matéria3 = 9

soma= matéria1 + matéria2 + matéria3
print(soma)
media = soma/3
print(media)
aprovado = media >=7
print(aprovado)



s = "ABC"
print(s + 'C')

print(s + "D" * 4)
print("X" + "-" * 10 + "X")
print (s+"x4 = "+s*4)



# %d = inteiros
# %s = string
# %f = decimal

idade= 22
print("%d"%idade)
print("%03d"%idade)
print("%3d"%idade)
print("%-3d"%idade)
print("%04d"%idade)
print("%010d"%idade)
print("%5.4f"%idade)

print("%5f"%5)
print("%5.2f"%5)
print("%10.5f"%5)


"""
nome = "David"
idade= 18
grana= 1347.43

print("%s tem %d anos e apenas R$%f no bolso"%(nome, idade, grana))
print("%s tem %d anos e apenas R$%5.2f no bolso"%(nome, idade, grana))

s= "ABCDEFGHI"
print (s[0:2])
print(s[1:2])
print(s[2:4])
print(s[0:6])
print(s[3:6])

print(s[-1:])
print(s[-5:7])
"""