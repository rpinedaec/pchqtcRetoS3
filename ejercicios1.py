# paises = []

# while (len(paises)<6):
#     pais = input("Ingrese un pais: ")
#     paises.append(pais)

# valor = input("Ingrese el valor a contar: ")
# print(paises)
# print(paises.count(valor))

# Uno al cien:
unoalcien = []

for i in range(100):
    unoalcien.append(i+1)

print(unoalcien)

# Meses

meses = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
mes = int(input("Ingrese un numero del 1 al 12 para ver que mes es: "))
print(meses[mes-1])


# Tabla de multiplicar

base = int(input("Ingresa un numero para devolver su tabla de multiplicar: "))
tablademult = []


for i in range(10):
    tablademult.append(base*(i+1))

print(tablademult)

# Pedir numeros

listaNumeros = []

while True:
    numero = int(input("Ingresa un numero para enlistarlo, ingresa 0 para terminar: "))
    if(numero==0):
        break
    else:
        listaNumeros.append(numero)

listaNumeros.sort()
print(listaNumeros)
listaNumeros.sort(reverse=True)
print(listaNumeros)

