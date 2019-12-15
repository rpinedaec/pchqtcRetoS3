cadena = input("Ingrese dato: ")
 
print(cadena)
 
lista = []
 
for c in cadena:
    if(c != ' '):
        lista.append(c)
 
print(lista)