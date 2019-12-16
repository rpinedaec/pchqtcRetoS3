# 6) Pide una cadena por teclado, mete los caracteres en una lista sin espacios.

cadena = input('Escriba una palabra u oracion (no olvides las comillas): ')

lista = []

for i in range(len(cadena)):
    if(cadena[i]==' '):
        continue
    else:
        lista.append(cadena[i])

print(lista)