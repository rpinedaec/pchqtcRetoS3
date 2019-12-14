##Mete los valores del 1 al 100 en una lista.
#num=[]
#for i in range(100):
#    num.append(i+1)

#print(num)

##Crea una lista con los meses del año, pide números al usuario, si el numero esta entre 1 
# y la longitud máxima de la lista, muestra el contenido de esa posición sino muestra un mensaje de error.
#  El programa termina cuando el usuario introduce un cero
meses=['enero','febrero','marzo','abril','mayo','junio','julio','agosto','setiembre','octubre','noviembre','diciembre']

mes=int(input('ingrese el numero de un mes:\n'))
#print(len(meses))

if mes!=0:
    if(mes>0 and mes<=len(meses)):
        print(meses[mes-1])
    else:
        print('error, vuelva intentarlo!!')
else:
    print("fin del programa")


