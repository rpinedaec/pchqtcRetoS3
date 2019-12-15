# coding=utf-8

# 9) Crea una lista con números e indica el numero con mayor valor y el que menor tenga.

import random

lista = []

for i in range(100):
    lista.append(random.randrange(100))

mayor=max(lista)
menor=min(lista)
print('Mi lista es', lista)
print('El numero mayor es {} y el menor es {}'.format(mayor, menor))
