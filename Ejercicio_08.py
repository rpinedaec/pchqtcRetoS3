#creacion de una lista informandonos cuantas veces se repite un numero de la lista.
numeros=[9,7,3,7,1,9,5,4,2,6,9,0,4,8,3,5,0,1,1,6,8,7]
print("")
print(numeros)
num_elegido=int(input("Elige un número de la lista para saber cuantas veces se repite en el registro..."))
print("")
print("Tu número elegido es : ")
print(num_elegido)
print("")
veces=(numeros.count(num_elegido))
print (("Y tu número elegido se repite : ")+str(veces)+" veces")
