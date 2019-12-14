lista=[]
while True:
    num=int(input("Ingresa numero: "))
    if num==0:
        break
    else:
        lista.append(num)
lista.sort()
print(lista)    
