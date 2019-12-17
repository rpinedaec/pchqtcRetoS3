
lista = []

flag = True
while flag == True:
    num = int(input("Ingrese un numero: "))
    if(num == 0):
        flag = False  
    else:
        lista.append(num)

print(lista)