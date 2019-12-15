lista = []
 
salir = False
 
while(not salir):
    numero = int(input("Ingrese numero: "))
    if(numero == 0):
        salir=True
    else:
        lista.append(numero)
 
lista.sort(reverse=True) 
 
print(lista)