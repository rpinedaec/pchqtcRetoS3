cadena = input("ingrese dato: ")

print (cadena)

lista =[]

for a in cadena:
    if(a not in lista) :
        lista.append (a)

        print (lista)