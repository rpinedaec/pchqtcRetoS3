##Mete los valores del 1 al 100 en una lista.
"""num=[]
for i in range(100):
    num.append(i+1)

print(num)"""

##Crea una lista con los meses del año, pide números al usuario, si el numero esta entre 1 
# y la longitud máxima de la lista, muestra el contenido de esa posición sino muestra un mensaje de error.
#  El programa termina cuando el usuario introduce un cero
"""meses=['enero','febrero','marzo','abril','mayo','junio','julio','agosto','setiembre','octubre','noviembre','diciembre']

mes=int(input('ingrese el numero de un mes:\n'))


if mes!=0:
    if(mes>0 and mes<=len(meses)):
        print(meses[mes-1])
    else:
        print('error, vuelva intentarlo!!')
else:
    print("fin del programa")"""

##Pide un numero por teclado y guarda en una lista su tabla de multiplicar hasta el 10.
#  Por ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50
"""num1=input('ingrese un numero: \n')
mult=[]

for i in range(10):
    mult.append(int(num1)*(i+1))

print(mult)"""

##Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. 
# Por último, muestra los números ordenados de menor a mayor.

"""band=1
lista=[]

while(band==1):
    num=int(input('ingrese numeros: \n'))

    if (num!=0):        
        lista.append(num)
    else:
        band=0

menor=sorted(lista)
print(menor)"""
