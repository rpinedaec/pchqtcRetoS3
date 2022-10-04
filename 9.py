lista = []
i = 1
while i <= 3:
  numIngresado=int(input("Ingresa un numero"))
  lista.append(numIngresado)
  i += 1

print("El numero mayor de la lista es {}, el menor de la lista es {} )").format(max(lista),min(lista))

