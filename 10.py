dictionary = {}
bandera = 1
while True:
    try:
        while bandera <= 5:
          ingresaNombre = input("Ingresa un nombre: ")
          if ingresaNombre in dictionary:
            print("Ingresa otro nombre")
          else:
            ingresaTelefono = input("Ingresa un numero telefonico: ")
          dictionary.update({ingresaNombre:ingresaTelefono})
          bandera += 1
          
          
        for k, v in dictionary.items():
          
          print("Los datos ingresados son: " + k,v)

        break
    except ValueError:
        print("Oops! No era válido. Intente nuevamente...")