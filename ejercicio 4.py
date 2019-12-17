listaasendente=[]
band=1
while band==1 :
    numero = int(input("Escriba un numero positivo: "))
    if numero==0 :
        band=0
    else:
        listaasendente.append(numero)

menoramayor=sorted(listaasendente)

print(menoramayor)