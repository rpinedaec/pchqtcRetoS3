# 3) Pide un numero por teclado y guarda en una lista su tabla de multiplicar hasta el 10. Por ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50
lista = []

numero = int(input('Ingresa un numero y hallare hasta 10 multiplos: '))

limite = numero*1

while limite <= numero*10:
    lista.append(limite)
    limite=limite+numero
print(lista)

