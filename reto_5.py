numeros = []

salir = False

while(not salir):
    Number = int(input("Numero: "))
    if(Number == 0):
        salir=True
    else:
        numeros.append(Number)
numeros.sort(reverse=True)
print(numeros)