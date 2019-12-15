# coding=utf-8

# 4) Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. Por último, muestra los números ordenados de menor a mayor.

lista = []

while True:
    numeros = input('Ingresa un numero. ')
    if numeros != 0:
        lista.append(numeros)
        print('Ingresa un numero mas. Cuando no desees agregar mas numeros, presiona 0.')
    else:
        lista.sort()
        print('La lista de menor a mayor es', lista)
        break
