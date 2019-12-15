cadena = input("Dame una cadena: ")

print(cadena)

lista = []

for c in cadena:
    if(c != ' '):
        lista.append(c)

print(lista)