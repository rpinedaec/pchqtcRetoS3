cadena = input("Ingrese una cadena de caracteres: ")

lista = []

for caracter in cadena:
    if caracter not in ' ':
     lista.append(caracter)

print(lista)