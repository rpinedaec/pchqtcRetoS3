lista=[]
bandera = True
while bandera:
  valor = int(input('Ingresa un numero:'))
  lista.append(valor)
  lista.sort()
  for x in lista:
   print(x) 

  if valor == 0:
   bandera = False
   break


