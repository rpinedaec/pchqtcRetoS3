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

##Lo mismo que el anterior pero ordenando de mayor a menor

"""band=1
lista=[]

while(band==1):
    num=int(input('ingrese numeros: \n'))

    if (num!=0):        
        lista.append(num)
    else:
        band=0

mayor=sorted(lista,reverse=True)
print(mayor)"""

##ejercicio 6 ::::
# Pide una cadena por teclado, mete los caracteres en una lista sin espacios.

"""cadena=input("ingrese una cadena: \n")
lis=[]

for i in range(len(cadena)):
    lis.append(cadena[i])

print(lis)"""

##ejercicio 7 ::::
#Pide una cadena por teclado, mete los caracteres en una lista sin repetir caracteres.
"""cadena=input("ingrese una cadena: \n")
lis=[]
for i in range(len(cadena)):
    lis.append(cadena[i])

print(lis)
lisNew=[]
for i in lis:
    if i not in lisNew:
        lisNew.append(i)
print(lisNew)"""

##ejercicio 8 ::::
#Crea una lista con números, pide un numero por teclado e indica cuantas veces se repite.
lisNum=[1,2,3,4,5,6,7,8,9,11,1,2,23,45,3,6,78,34,2,6,3,4,5,8,6,9,0,23,21,14,16,23,18,29,21,23,22,24,3] 

num=int(input('ingrese algun numero: \n'))
contador=0

for i in lisNum:
    if i==num:
        contador+=1
print("el numero "+str(num)+" se repite "+ str(contador)+ " veces")












