meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Agosto","Setiembre",
       "Octubre","Noviembre","Diciembre"]
while True:
    num=int(input("Ingresa numero: "))
    if num>12 or num<1:
        break
    else:
        print(meses[num-1])