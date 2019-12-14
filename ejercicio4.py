lista = []
 
flag = True
while flag == True:
    numero = int(input("Ingrese un numero: "))
    if(numero == 0):
        flag = False  
    else:
        lista.append(numero)
print(lista)