x = 13
meses = (0, 'Enero', 'Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')
while x != 0:
    x = int(input("Ingreso numero relacionado con el mes: "))
    if x >= len(meses):
        print("Intentar de nuevo ")
        continue
    elif x < 0:
        print("Intentar de nuevo")
        continue
    elif x == 0:
        break
    print(meses[x])
print("Fin de programa")