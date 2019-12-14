Meses=['Enero',"Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

numMes=int(input('Ingrese nro del mes: '))

while numMes!=0:
        if numMes >=1 and numMes <=12:
            print(Meses[numMes-1])
            numMes=int(input('Ingrese nro del mes: '))
        else:
            print ("ERROR")
            numMes=int(input('Ingrese nro del mes: '))

        