
meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Setiembre','Ocutubre','Noviembre','Diciembre']
print (meses)
flag = 1

while flag == 1:
    mes = int (input('ingresa un numero que represente mes del anio'))
    if (mes > 12):
        print ('Dato errado, ingrese datos del 1 - 12')
    else:
        if (mes == 0): 
            flag = 99
print(meses(mes-1))
        
    
    
 


