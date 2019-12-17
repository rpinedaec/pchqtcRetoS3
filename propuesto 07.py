# Ingresando cadenas sin repetir y sin espacio

cadena = []

cadenafinal = input("Escriba un texto: ")

for c in cadenafinal:
    if(c not in cadena):
        cadena.append(c)

print(cadena)