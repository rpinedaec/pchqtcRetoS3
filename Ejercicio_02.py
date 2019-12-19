# Creacion de la lista con los meses del año
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

#Creacion de una vaariable bandera para ejecutar el while.
bandera = True

# Mientras la bandera sea True, se ejecutara el while.
while bandera == True:
    # Solicitamos el ingreso de un numero y convertirmos el dato en entero
    numeroMes = int(input('Ingrese el numero de un mes: '))

    # Validamos que el numero se encuentre dentro del rango del 1 a 12
    if numeroMes > 12:
        # En caso se mayor que 12, saldra un Error
        print('Error.....!!!')
    else:
        # Regla de Negocio: Si ingresas el valor cero, se termina el programa
        if numeroMes == 0:
            bandera = False
        else:
            # Al numero ingesado por el usuario le restamos uno para que coincida
            # con el indice verdadero del mes.
            index = numeroMes - 1
            print(meses[index])