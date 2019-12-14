lista = []
 
salir = False
 
while(not salir):
    numero = int(input("Dame un numero: "))
    if(numero == 0):
        salir=True
    else:
        lista.append(numero)
 
lista.sort()

print (lista) 