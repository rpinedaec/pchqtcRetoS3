cadena = []

cadenafinal = input("escriba numero,sin repetir y sin espacio: ")

for c in cadenafinal:
    if(c not in cadena):
        cadena.append(c)

print(cadena)