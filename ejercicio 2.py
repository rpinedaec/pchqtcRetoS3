meses = ['enero', 'ferero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

band = True
while band == True:
    mes = int(input('Ingrese el numero de un mes: '))

    if mes> 12:
       
        print('Error, numero ingresado incorrecto')

    else:
        
        if mes == 0:
            band = False
            print ('finalizar')

        else:
            
            mesesfull = mes - 1
            print(meses[mesesfull])
            

    


