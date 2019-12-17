#Ingresano cadenas sin espacios

cadena = str(input("Escriba una texto: "))

txt = cadena
lst=[]
for i in txt:
    if i!=' ':
        lst.append(i)
print(lst)