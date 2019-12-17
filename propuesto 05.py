listaasendente=[]
band=1
while band==1 :
    num = int(input("Ingrese un numero: "))
    if num==0 :
        band=0
    else:
        listaasendente.append(num)

menoramayor=sorted(listaasendente)


listadesendente=[]

for i in range(0,len(menoramayor),1):
    listadesendente.append(menoramayor[len(menoramayor)-1-i])

print(listadesendente)