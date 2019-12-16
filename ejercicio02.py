# 2) Crea una lista con los meses del año, pide números al usuario, si el numero esta entre 1 y la longitud máxima de la lista, muestra el contenido de esa posición sino muestra un mensaje de error.

meses = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","setiembre","octubre","noviembre","diciembre"]

bandera = True

while bandera == True:
    mes = int(input('Ingresa un numero de mes del 1 al 12: '))
    if mes > 12:
        print('Error. Tipea un numero correcto')
    else:
        if mes == 0:
            print('Error! No es un numero de mes')
            bandera = False
        else:
            mesreal = mes - 1
            print(meses[mesreal])