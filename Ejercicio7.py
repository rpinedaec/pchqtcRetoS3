texto=input("Ingresa el texto: ")
lista_caracteres=[]
for i in texto:
    if texto.count(i)==1:
        lista_caracteres.append(i)
        
print(lista_caracteres)