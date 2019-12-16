# coding=utf-8

# 7) Pide una cadena por teclado, mete los caracteres en una lista sin repetir caracteres.

def sinRepetidos(iterable):

    a = set()

    lista = []

    for i in iterable:
        if i not in a:
            a.add(i)
            lista.append(i)
    return lista

a = input('Ingrese una palabra u oracion: ')

print(sinRepetidos(a))
