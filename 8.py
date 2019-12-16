lista = [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,2,4,6,8,0,2,4,6,8,0,2,4,6,8,0,4,8]

numeroIngresado=int(input("Ingresa un numero del 0 al 9:"))

if lista.count(numeroIngresado) != 0: 
    print("El numero {} se repite {} veces en la lista interna").format(numeroIngresado, lista.count(numeroIngresado))
else:
    print("El numero no existe")

