#lista Ordenada Ascendiente ingresando numeros con finalizacion con 0.
bandera=1
lista=[]
print('')
print('---Digita los numeros que quieras para crear una lista.')
print('---Con la condicion que ingresando el numero 0, finalizas la lista.')
print('')
while bandera==1:
    numero=int(input('Ingresa un numero: '))
    if numero!= 0:
        lista.append(numero)
        lista.sort()           
    else:
        print('........... Fin del ejercicio - Lista Ordenada Ascendente........!!!!')
        bandera=2
        
print(lista)