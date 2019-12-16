diccionario={}
respuesta=1
while respuesta==1:
    nombre=input("Ingrese nombre: ")
    numero = int(input("Ingrese numero: "))
    diccionario[nombre]=numero
    respuesta= int(input("Desea agregar otro contacto? ingrese 1 si la respuesta es si, caso contrario ingrese 0: "))
print(diccionario)