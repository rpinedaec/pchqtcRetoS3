meses = []
while len(meses)<12:
    nombreMes = input('Ingrese el nombre de un mes: ')
    meses.append(nombreMes)

value = True
while value==True:
    mes = int(input("Ingrese un número del [1 - 12]: "))
    if mes == 0:
        print('Programa finalizado')
        value = False
    else:
        if (mes >=1 and mes <= 12):
            print('El mes es '+ meses[mes-1])    
        else:
            print('ERROR')
                                                  
