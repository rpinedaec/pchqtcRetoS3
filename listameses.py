
meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Setiembre','Ocutubre','Noviembre','Diciembre']
print (meses)
mes = 0
flag = 1

while flag == 1:
    mes = input('ingresa un numero que represente mes del anio')
    if (mes>12):
        print ('Dato errado')
        
    else:
        if (mes == 0): 
            flag = 99
print(meses(mes-1))
        
    
    
 


