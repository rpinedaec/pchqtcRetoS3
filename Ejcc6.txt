cadena = str(input("Escriba una cadena: "))

txt = cadena
lst=[]
for i in txt:
    if i!=' ':
        lst.append(i)
print(lst)