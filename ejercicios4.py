value = True
lista = []

while value == True:
    numero = int(input("Ingrese un número: "))
    if numero == 0:
        value = False
    else:
        lista.append(numero)

print(lista)

lista.sort()  

print(lista)