# metodo 2
# 3) Pide un numero por teclado y guarda en una lista su tabla de multiplicar hasta el 10. Por ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50

lista = []

numero = int(input('Ingresa un numero y yo hallare hasta 10 multiplos: '))
for a in range(1, 11):
    resultado = numero*a
    lista.append(resultado)

print(lista)