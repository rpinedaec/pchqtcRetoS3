# coding=utf-8

# 8) Crea una lista con números, pide un numero por teclado e indica cuantas veces se repite.

import random

lista = []

for i in range(100):
    lista.append(random.randrange(100))

numero = int(input('Ingrese un numero para saber cuantas veces se repite en mi lista: '))

repetida = lista.count(numero)
print('Mi lista es', lista)
print('Tu numero se repite: ', repetida, 'veces.')