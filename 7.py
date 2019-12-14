
lista=[]
bandera = True
while bandera:
 valor = input('Ingresa una palabra:')
 x = lista.count(valor)
 if x != 0:
  print("Ingresa otra palabra")
 else:
  lista.append(valor)
  for x in lista:
    print(x)

 if valor == 'salir' or valor == 'exit':
  bandera = False
  break