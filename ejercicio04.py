
lista = []

while True:
    numeros = input('Ingresa un numero')
    if numeros != 0:
        lista.append(numeros)
    else:
        lista.sort()
        print(lista)
        break
