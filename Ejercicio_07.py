#Eliminacion de caracteres duplicados en una cadena.
palabra=input ('Escribe una palabra: ')
print("")
print ('---->Eliminacion de carácteres duplicados<----')
print("")
#Esta función se encarga de quitar los caracteres duplicados pero no los ordena.
print('**Cadena Desordenada sin caracter duplicado')
print("")
print( "".join(set(palabra)) )
print("")

print('**Cadena Ordenada sin caracter duplicado')
print("")
#Este Modolu hace quitar caracteres duolicados pero si los ordena.
from collections import OrderedDict 
palabra = palabra 
print("".join(OrderedDict.fromkeys(palabra)) )
