
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
         'Julio', 'Agosto', 'Setiembre', 'Ocutubre', 'Noviembre', 'Diciembre']
print(meses)
flag = True

while flag == True:
    mes = int(input('ingresa un numero que represente mes del anio'))

    if mes > 12:
        print('Error')
    else:
        if mes == 0:
            flag = False
        else:
            index = mes-1
    print(meses[index])
