meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Setiembre","Octubre","Noviembre","Diciembre"]

valorIngreso = int(input(" ingresa un numero: "))
if valorIngreso >= 13 or valorIngreso <= 0:
 print("el valor no es correcto")
else: 

 for x in range(len(meses)):
  
  if valorIngreso - 1 == x:
   print(meses[x])
   break
   
  








