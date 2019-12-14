meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
 
salir = False
while(not salir):
     
    numero = int(input("Pon un numero: "))
 
    if(numero==0):
        salir= True
    else:
        if(numero>=1 and numero<=12):
            print(meses[numero-1])
        else:
            print("Error .....")
