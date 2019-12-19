stop=0
agenda={}
print('A continuacion registre sus contactos con sus respectivos numeros, por favor: ')
print('')
print('Para detener el registro debera informar con 0 para continuar o sino un 1 para detener.')
if stop==0:
    nombre=str(input('Ingrese el nombre del contacto a registrar: ') )
    celular=int(input('Ingrese el celular del contacto a registrar: ') )
    stop=int(input('ingrese 0 para seguir registrando o 1 para detener el registro: '))
    #agenda.append({nombre,celular})
else:
    print('Fin del registro.')

agenda={nombre:celular}
print(agenda)