# 5) Lo mismo que el anterior pero ordenando de mayor a menor.

lista = []

while True:
    numeros = input('Ingresa un numero: ')
    if numeros != 0:
        lista.append(numeros)
        print('Ingresa un numero mas. Cuando no desees agregar mas numeros, presiona 0.')
    else:
        lista.sort(reverse=True)
        print('La lista de mayor a menor es', lista)
        break
